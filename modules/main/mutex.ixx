/**--------------------------------------------------------------------------
This is a rework of a number of semaphore classes, libti has tsem which
is the basis for the unix semaphore usage, libmain has autoSemaphore and
sharedSemaphore which are not based on a mutex principle but a post/wait
stategy - which allows for multiple instances depending on how many posts
are active. They also all do not do a windows implementation. The other
feature added is the semaphores are timed - and on the constructor seconds
and nanoseconds can be provided. If 0 seconds and nano seconds are specified
then the wait will block indefinitely.

Usage is quite simple:
1)
	import mutex;

2)
- construct a semaphore (int in unix and a HANDLE in windows) using either
	semaphore = Mutex::makePrivate();   // single process (or fork parent/child)
- or
	semaphore = Mutex::makeNamed(name); // In windows this may be just a unique name
																			// In unix this must be an existing file or
																			// a valid file that can be created.
3)
- where you want to set your critical section, use a stack created resource like
	Mutex wait(semaphore);              // When this goes out of scope the destructor
																			// will release. The constructor acquires.
----------------------------------------------------------------------------- */

export module mutex;
import machine;
#if defined(_MSC_VER)
import <windows.h>;
#endif
import <exception>;
import <iostream>;
import <format>;
import <print>;

using namespace std;
enum EMutex
{
	eMNoError = 0
	, eMutexAcquireFailed
	, eMutexFtokFailed
	, eMutexSemGetFailed
	, eMutexSemKeyFailed
	, eMutexReleaseFailed
};

export struct XMutex : public exception
{
	static const char* getText(int err)
	{
		switch (err)
		{
		case eMNoError:            return "No Error";
		case eMutexAcquireFailed:  return "Mutex Acquire Failure";
		case eMutexFtokFailed:     return "Mutex File does not exist or cannot be opened Failure";
		case eMutexSemGetFailed:   return "Mutex File semget Failure";
		case eMutexSemKeyFailed:   return "Mutex File construction of semkey Failure";
		case eMutexReleaseFailed:  return "Mutex File release of semkey Failure";
		default:                   return "Unknown exception";
		}
	}
	XMutex(int error, const char* context = "")
	{
		println("Mutex {} {} : {}", context, error, getText(error));
	}
	XMutex(const XMutex& aX)
	{
	}
};

static SECURITY_ATTRIBUTES sa;
static SECURITY_DESCRIPTOR sd;

static void _setup()
{
	if (sa.nLength == sizeof(sa))
		return;
	InitializeSecurityDescriptor(&sd, SECURITY_DESCRIPTOR_REVISION);
	SetSecurityDescriptorDacl(&sd, true, NULL, false);
	sa.nLength = sizeof(sa);
	sa.lpSecurityDescriptor = &sd;
	sa.bInheritHandle = 1;
}

#if defined(__GNUC__) || defined(__clang__)
import <sys/types.h>;
import <sys/ipc.h>;
import <sys/sem.h>;
import <errno.h>;
#endif

export struct Mutex
{
	int secs, nanosecs;
	bool failed;
#if defined(__GNUC__) || defined(__clang__)
  int semaphore;

  int makePrivate()
  {
    int semaphore = semget(IPC_PRIVATE, 1, 0666 | IPC_CREAT);
    return semaphore;
  }

  int makeNamed(const char* name)
  {
    FILE* temp = fopen(name, "rb");
    if (temp == 0)
    {
      temp = fopen(name, "wb");
      if (temp == 0)
        throw XMUTEX(eMutexFtokFailed);
    }
    fclose(temp);
    key_t semKey = ftok(name, 1);
    if (semKey == -1)
      throw XMUTEX(eMutexSemKeyFailed);
    int semaphore = semget(semKey, 1, 0666 | IPC_CREAT);
    if (semaphore == -1)
      throw XMUTEX(eMutexSemGetFailed);
    return semaphore;
  }

  void remove(int semaphore)
  {
    semctl(semaphore, 0, IPC_RMID);
  }

  void acquire()
  {
    struct timespec waitFor = {secs, nanosecs};
    static struct sembuf acquireOp[] =  // The possible semaphore
    { 0, 0, 0                           // Wait for semaphore == 0
    , 0, 1, SEM_UNDO                    // inc semaphore if crash undo
    };
    int rc = semtimedop(semaphore, acquireOp, 2, secs != 0 || nanosecs != 0 ? &waitFor : 0);
    if (rc == -1)
    {
      failed = true;
      if (errno == EINTR)
        return;
      throw XMUTEX(eMutexAcquireFailed);
    }
  }

  void release()
  {
    struct timespec waitFor = {secs, nanosecs};
    static struct sembuf releaseOp[] =
    { 0, -1, SEM_UNDO  // dec semaphore
    };
    int rc = semtimedop(semaphore, releaseOp, 1, secs != 0 || nanosecs != 0 ? &waitFor : 0);
    if (rc == -1)
    {
      failed = true;
      throw XMUTEX(eMutexReleaseFailed);
    }
  }

#elif defined(_MSC_VER)	
  HANDLE semaphore;

	HANDLE makePrivate()
	{
		_setup();
		srand((unsigned int)time(0));
		char mutexName[128];
		snprintf(mutexName, sizeof(mutexName), "MUTEX_%04d", rand() % 10000);
		HANDLE semaphore = CreateMutex(&sa, FALSE, mutexName);
		return semaphore;
	}

	HANDLE makeNamed(const char* name)
	{
		_setup();
		HANDLE semaphore = CreateMutex(&sa, FALSE, name);
		return semaphore;
	}

	void remove(HANDLE semaphore)
	{
		CloseHandle(semaphore);
	}

	void acquire()
	{
		DWORD waitFor = (DWORD)(secs * 1000 + nanosecs / 1000000);
		if (waitFor == 0)
			waitFor = INFINITE;
		DWORD result = WaitForSingleObject(semaphore, waitFor);
		if (result != WAIT_OBJECT_0)
		{
			failed = true;
			char context[256];
			snprintf(context, 256, "%s %d", __FILE__, __LINE__);
			throw XMutex(eMutexAcquireFailed, context);
		}
	}

	void release()
	{
		ReleaseMutex(semaphore);
	}
#endif

#if defined(__GNUC__) || defined(__clang__)
  Mutex(int semaphore, int secs=0, int nanosecs=0)
#elif defined(_MSC_VER)
  Mutex(HANDLE semaphore, int secs=0, int nanosecs=0)
#endif
  {
    this->semaphore = semaphore;
    this->secs = secs;
    this->nanosecs = nanosecs;
    this->failed = false;
    acquire();
  }
  ~Mutex()
  {
    release();
  }
};
