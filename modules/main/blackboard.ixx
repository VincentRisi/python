export module blackboard;
import tbuffer;

import <windows.h>;
import <exception>;
import <iostream>;
import <format>;

using namespace std;

typedef char* pchar;

enum EXBlackBoard
{ eBBNoError = 0
, eBBMappingfailed
, eBBMutexfailed
, eBBCircled
};

export struct XBlackBoard : public exception
{
  static const char *getText(int err)
  {
    switch (err)
    {
    case eBBNoError:        return "No Error";
    case eBBMappingfailed:  return "Cannot Access Shared Memory Map Failure";
    case eBBMutexfailed:    return "Cannot Access Shared Memory Mutex Failure";
    case eBBCircled:        return "Circular Buffer Store Failed, size exceeded";
    default:                return "Unknown exception";
    }
  }
  XBlackBoard(int error, string context = "")
  {
    string err = std::format("Socket {} {} : {}", context, error, getText(error));
    cout << err << endl;
  }
  XBlackBoard(const XBlackBoard& aX)
  {
  }
};

template <class TE> struct BlackBoard
{
  struct Store
  {
    long long head;
    long long tail;
    long long size;
    long long count;
  };
  struct Wait
  {
    HANDLE mutex;
    Wait(HANDLE amutex)
    {
      mutex = amutex;
      DWORD Result = WaitForSingleObject(mutex, 5000);
      if (Result != WAIT_OBJECT_0)
        throw XBlackBoard(eBBMutexfailed, format("{} {}", __FILE__, __LINE__));
    }
    ~Wait()
    {
      ReleaseMutex(mutex);
    }
  };
  SECURITY_ATTRIBUTES sa;
  SECURITY_DESCRIPTOR sd;
  HANDLE fmh;
  HANDLE mutex;
  long long rollOver;
  pchar area;
  Store *store;
  TBChar name;
  BlackBoard(pchar inName, long long inCount=5000, long long inRollOver=0)
  {
    InitializeSecurityDescriptor(&sd, SECURITY_DESCRIPTOR_REVISION);
    SetSecurityDescriptorDacl(&sd, true, NULL, false);
    sa.nLength = sizeof(sa);
    sa.lpSecurityDescriptor = &sd;
    sa.bInheritHandle = 1;
    rollOver = inRollOver;
    name.set(inName);
    long long fileSize = sizeof(store)+sizeof(TE)*inCount;
    fmh = CreateFileMapping(HANDLE(0xFFFFFFFF), &sa, PAGE_READWRITE, 0, fileSize, name);
    area = (pchar)MapViewOfFile(fmh, FILE_MAP_ALL_ACCESS, 0, 0, fileSize);
    if (area == 0)
      throw XBlackBoard(eBBMappingfailed, format("{} {}", __FILE__, __LINE__));
    store = (Store*)area;
    if (store->size != sizeof(TE) || store->count != inCount)
    {
      store->size = sizeof(TE);
      store->count = inCount;
      store->head = 0;
      store->tail = 0;
    }
    TBChar mutexName;
    mutexName.set(name.data);
    mutexName.append("__Mutex");
    mutex = CreateMutex(&sa, FALSE, mutexName);
  }
  virtual ~BlackBoard()
  {
    UnmapViewOfFile(area);
    CloseHandle(fmh);
    CloseHandle(mutex);
  }
  void Insert(TE &element)
  {
    Wait here(mutex);
    TE *newItem = (TE*)(area+sizeof(Store)+store->size*store->tail);
    if (newItem == 0)
      throw XBlackBoard(eBBMappingfailed, format("{} {}", __FILE__, __LINE__));
    *newItem = element;
    long long newTail = store->tail+1;
    if (newTail >= store->count)
      newTail = 0;
    if (newTail == store->head)
    {
      if (rollOver == 0)
        throw XBlackBoard(eBBCircled, format("{} {}", __FILE__, __LINE__));
      else
      {
        long long newHead = store->head+1;
        if (newHead >= store->count)
          newHead = 0;
        store->head = newHead;
      }
    }
    store->tail = newTail;
  }
  bool Retrieve(TE &element)
  {
    Wait here(mutex);
    if (store->tail == store->head)
    {
      store->tail = store->head = 0;
      return false;
    }
    TE *newItem = (TE*)(area+sizeof(Store)+store->size*store->head);
    if (newItem == 0)
      throw XBlackBoard(eBBMappingfailed, format("{} {}", __FILE__, __LINE__));
    element = *newItem;
    store->head++;
    if (store->head >= store->count)
      store->head = 0;
    return true;
  }
  void Clear()
  {
    Wait here(mutex);
    store->tail = store->head = 0;
  }
};
