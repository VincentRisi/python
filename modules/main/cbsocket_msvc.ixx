export module cbsocket;
import obsocket;

import <windows.h>;
import <exception>;
import <iostream>;
import <format>;

using namespace std;

typedef int socklen_t;
typedef char* pchar;
typedef unsigned int uint;

enum ESocketErr
{
    errSockOK
  , errSockInit
  , errSockHost
  , errSockService
  , errSockSocket
  , errSockBind
  , errSockListen
  , errSockConnect
  , errSockClose
  , errSockRead
  , errSockWrite
  , errSockVersion
  , errSockIOCtl
  , errSockLinger
  , errSockKeepAlive
  , errSockTimeout
  , errSockDebug
  , errSockGetOpt
  , errSockSetOpt
  , errSockParse
#if defined(USE_OPENSSL)
  , errSockSSLContext
#endif    
};

export struct XSocketErr : public exception
{
  static const char* getText(int err)
  {
    switch (err)
    {
    case errSockOK:          return "No Error";         
    case errSockInit:        return "Socket Init";           
    case errSockHost:        return "Socket Host";           
    case errSockService:     return "Socket Service";              
    case errSockSocket:      return "Socket Socket";             
    case errSockBind:        return "Socket Bind";           
    case errSockListen:      return "Socket Listen";             
    case errSockConnect:     return "Socket Connect";              
    case errSockClose:       return "Socket Close";            
    case errSockRead:        return "Socket Read";           
    case errSockWrite:       return "Socket Write";            
    case errSockVersion:     return "Socket Version";              
    case errSockIOCtl:       return "Socket IOCtl";            
    case errSockLinger:      return "Socket Linger";             
    case errSockKeepAlive:   return "Socket KeepAlive";                
    case errSockTimeout:     return "Socket Timeout";              
    case errSockDebug:       return "Socket Debug";            
    case errSockGetOpt:      return "Socket GetOpt";             
    case errSockSetOpt:      return "Socket SetOpt";             
    case errSockParse:       return "Socket Parse";            
#if defined(USE_OPENSSL)
    case errSockSSLContext:  return "Socket SSL Context";
#endif    
    default:                 return "Unknown exception";
    }
  }
  XSocketErr(int error, const char* context = "")
  {
    string err = format("Socket {} {} : {}", context, error, getText(error));
    cout << err << endl;
  }
  XSocketErr(const XSocketErr& aX)
  {
  }
};

struct CBSockBuffer
{
   uint BytesToRead;
   uint BytesRead;
   uint BytesToWrite;
   uint BytesWritten;
   pchar p;
};

export class CBSockClient
{
protected:
  CBSockClient() {}
  static int ParseName(char* name, const char sep, char* names[])
  {
    // ---------------------------------------------------------
    // returns 0 if name does not start with a separator
    // else splits into substrings on the separator and returns
    // the number of parts - at least one
    // ---------------------------------------------------------
    int   i;
    char* seppos;
    // .skip the first separator
    if (*name++ != sep)
      return 0;
    for (i = 0; i < 3; i++)
    {
      seppos = strchr(name, sep);
      if (!seppos)
      {
        names[i++] = name;
        break;
      }
      *seppos = 0;
      names[i] = name;
      name = seppos + 1;
    }
    return i;
  }

public:
  tSockCB* fSockCB;
  // This form of the constructor will parse the Name and pull out the
  // Host and Service. This is present to cater for the older interfaces
  // like cliserv and cs. the form of this name is :socket:<host>:<service>
  CBSockClient(const char* aName)
  {
    char* names[3];
    char  temp[128];
    fSockCB = 0;
    strncpy(temp, aName, sizeof(temp));
    int parts = ParseName(temp, ':', names);
    if (parts != 3 || (strcmp(names[0], "socket")) != 0)
      throw XSocketErr(errSockParse, "");
    //SockError(fSockCB),
    //SockErrorMsg(fSockCB),
    //aHost, aService);
    int wError = SockClientInit(&fSockCB, names[1], names[2]);
    if (wError)
      throw XSocketErr(wError, "");
        //throw XSockError(xSockErr::eError(wError), fSockCB,
        //SockError(fSockCB),
        //SockErrorMsg(fSockCB),
        //names[1],
        //names[2]);
  }
  // This is the preferred form of constructor.
  // aHost is the name of the server providing the service, defined either in
  // the hosts file (/etc/hosts or \winnt\system32\drivers\etc\hosts) or
  // resolved by a domain name server.
  // aService is a service name defined in the services file // (/etc/services
  // or \winnt\system32\drivers\etc\services). This must resolve to the same
  // number on both the local and remote machines.
  CBSockClient(const char* aHost, const char* aService)
  {
    int wError = SockClientInit(&fSockCB, aHost, aService);
    if (wError)
      throw XSocketErr(wError, "");
        //SockError(fSockCB),
        //SockErrorMsg(fSockCB),
        //aHost, aService);
  }
  // Construct Client from an existing socket number

  CBSockClient(const int iSocket, const int Retries = 5, const int TimeOut = 10000)
  {
    int wError = SockDuplicate(&fSockCB, aCommsPort, aRetries, aTimeOut);
    if (wError)
      throw XSOCKERR(xSockErr::eError(wError), fSockCB,
        SockError(fSockCB),
        SockErrorMsg(fSockCB));
  }

#if defined(USE_OPENSSL)
  // Construct SSL Client. CertFile and KeyFile can be passed in as null(0). If used the other 3 can be used or passed in as null(0).
  CBSockClient(const char* aHost, const char* aService, const char* CertFile, const char* CAfile, const char* CApath, const char* KeyFile, const char* KeyPassword);
#endif
  // Standard destructor
  virtual ~CBSockClient();

  // Open the socket for the client.
  void   Open();

  // Close the socket.
  void   Close();

  //Gets the client's IP Address
  //Changed to return a char *, as tString has been removed
  char* ClientIPAddress() const;

  // ReadLength is used to read an unsigned long as data and convert it
  // to host from network byte order. This is the counterpart for
  // WriteLength;
  unsigned int ReadLength();

  // Read data into aBuffer for the exact length aLength, else raise
  // an exception. This is used directly after ReadLength;
  void  Read(void* aBuffer, const unsigned int aLength);

  // Read data into aBuffer for the length aToRead throwing away
  // any excess and return the actual no read in aRead.
  // This is arguably a bad form and should be avoided.
  void   Read(void* aBuffer, const unsigned int aToRead, unsigned int& aRead);

  // Old form read that uses a tBuffer construct for the lengths and data.
  // Will resolve into new form.
  void   Read(tCBSockBuffer* aBuffer);

  // Read data into aBuffer up to the length aLength
  // returns the length read.
  unsigned int ReadStream(void* aBuffer, const unsigned int aLength);

  // WriteLength writes an unsigned int as data after converting it
  // to network byte order.
  void   WriteLength(const unsigned int aLength);

  // Write data for exactly the length of aLength. This is normally
  // used after WriteLength, but can also be used to write stream
  // data.
  void   Write(void* aBuffer, const unsigned int aLength);

  // Old form write that uses a tBuffer construct for the lengths and
  // data. Will resolve into the new form.
  void   Write(tCBSockBuffer* aBuffer);

  // ================================================================
  // A fix for the existing problem of multiple write resolved to one
  // ================================================================

  //void   Write(tCBSockBuffer **aBuffer, ulong aCount);

  // WaitRead will not read data, but will wait until there is data
  // to read or timeout. Returns true if there is data or returns
  // false if it times out.
  bool   WaitRead(const unsigned int aTimeout);

  // WaitWrite will not write data, but will wait until the
  // counterpart is ready to read or timeout. Returns true if the
  // counterpart is ready or returns false if it times out.
  bool   WaitWrite(const unsigned int aTimeout);

  // This only really makes sense from a client point of view
  // Will do an old style write followed by a read.
  void   Transact(tCBSockBuffer* bufOut, tCBSockBuffer* bufIn); // WR

  // This only really makes sense from a client point of view
  // Will do an open, old style write followed by a read, then a close.
  void   Call(tCBSockBuffer* bufOut, tCBSockBuffer* bufIn);     // OWRC

  // Sets the timeout parameter is millisecs
  void   SetTimeout(const unsigned int aTimeout) { fSockCB->TimeOut = aTimeout; }

  // gets the timeout value
  unsigned int GetTimeout() const { return fSockCB->TimeOut; }

  // Sets the number of times to retry
  void   SetRetries(const unsigned int aRetries) { fSockCB->Retries = (unsigned short)aRetries; }

  // Gets the number of retries
  unsigned short GetRetries() const { return fSockCB->Retries; }

  // Query the open status
  bool   IsOpen() const { return fSockCB->CommsPort == -1 ? false : true; }

  // Return the IP address
  sockaddr_in* SockAddr() const { return &fSockCB->Addr; }

  // Return the socket
  int Socket() const { return fSockCB->CommsPort; }

  unsigned short PortNo() const { return (unsigned short)htons(fSockCB->Addr.sin_port); }

  int CommsPort() const { return fSockCB->CommsPort; }
};


