export module cbsocket;
import obsocket;
import mutex;

import <windows.h>;
import <exception>;
import <iostream>;
import <format>;

using namespace std;

using socklen_t = int;
using pchar = char*;
using uint = unsigned int;
using ushort = unsigned short;	

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
	XSocketErr(int error, string context = "")
	{
		string err = std::format("Socket {} {} : {}", context, error, getText(error));
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
	static int ParseName(pchar name, const char sep, pchar names[])
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
	void throw_simple_error(int wError, string context)
	{
		string err = std::format("{} invalid {} {}",
			context,
			SockError(fSockCB), SockErrorMsg(fSockCB));
		throw XSocketErr(wError, err);
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
		{
			string err = std::format("{} {} coded:{} coding invalid {} {}",
				__FILE__, __LINE__,
				aName,
				SockError(fSockCB), SockErrorMsg(fSockCB));
			throw XSocketErr(errSockParse, err);
		}
		int wError = SockClientInit(&fSockCB, names[1], names[2]);
		if (wError)
		{
			string err = std::format("{} {} host:{} service:{} invalid {} {}",
				__FILE__, __LINE__,
				names[1], names[2],
				SockError(fSockCB), SockErrorMsg(fSockCB));
			throw XSocketErr(wError, err);
		}
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
		{
			string err = std::format("{} {} host:{} service:{} invalid {} {}",
				__FILE__, __LINE__,
				aHost, aService,
				SockError(fSockCB), SockErrorMsg(fSockCB));
			throw XSocketErr(wError, err);
		}
	}
	// Construct Client from an existing socket number
	CBSockClient(const int iSocket, const int Retries = 5, const int TimeOut = 10000)
	{
		int wError = SockDuplicate(&fSockCB, iSocket, Retries, TimeOut);
		if (wError)
		{
			string err = std::format("{} {} socket:{} retries:{} timeout:{} invalid {} {}",
				__FILE__, __LINE__,
				iSocket, Retries, TimeOut,
				SockError(fSockCB), SockErrorMsg(fSockCB));
			throw XSocketErr(wError, "");
		}
	}
#if defined(USE_OPENSSL)
	// Construct SSL Client. CertFile and KeyFile can be passed in as null(0). If used the other 3 can be used or passed in as null(0).
	CBSockClient(const char* aHost, const char* aService, const char* CertFile, const char* CAfile, const char* CApath, const char* KeyFile, const char* KeyPassword)
	{
		int wError = SockClientInit(&fSockCB, aHost, aService);
		if (wError)
		{
			fSockCB->CommsPort = -1;
			string err = std::format("{} {} host:{} service:{} invalid {} {}",
				__FILE__, __LINE__,
				aHost, aService,
				SockError(fSockCB), SockErrorMsg(fSockCB));
			throw XSocketErr(wError, err);
		}
		wError = SSLClientInit(fSockCB, CertFile, CAfile, CApath, KeyFile, KeyPassword);
		if (wError)
		{
			fSockCB->CommsPort = -1;
			string err = std::format("{} {} host:{} service:{} SSL invalid {} {}",
				__FILE__, __LINE__,
				aHost, aService,
				SockError(fSockCB), SockErrorMsg(fSockCB));
			throw XSocketErr(wError, err);
		}
	}
#endif
	// Standard destructor
	virtual ~CBSockClient()
	{
		if (fSockCB == 0)
			return;
		int wError = SockDone(fSockCB);
		if (wError != errSockInit)
			free(fSockCB);
	}
	// Open the socket for the client.
	void Open()
	{
		int wError = SockClientOpen(fSockCB);
		if (wError)
		{
			fSockCB->CommsPort = -1;
			throw_simple_error(wError, std::format("{} {} Open", __FILE__, __LINE__));
		}
	}
	// Close the socket.
	void  Close()
	{
#if defined(SD_BOTH)
		shutdown(fSockCB->CommsPort, SD_BOTH);
#elif defined(SHUT_RDWR)
		shutdown(fSockCB->CommsPort, SHUT_RDWR);
#endif
		int wError = SockClose(fSockCB);
		if (wError)
			throw_simple_error(wError, std::format("{} {} Close", __FILE__, __LINE__));
	}

	//Gets the client's IP Address
	//Changed to return a char *, as tString has been removed
	char* ClientIPAddress() const
	{
		return inet_ntoa(fSockCB->Addr.sin_addr);
	}

	// ReadLength is used to read an unsigned long as data and convert it
	// to host from network byte order. This is the counterpart for
	// WriteLength;
	unsigned int ReadLength()
	{
		uint wResult;
		int wError = SockReadLength(fSockCB, &wResult);
		if (wError)
			throw_simple_error(wError, std::format("{} {} ReadLength", __FILE__, __LINE__));
		return wResult;
	}

	// Read data into aBuffer for the exact length aLength, else raise
	// an exception. This is used directly after ReadLength;
	void  Read(void* aBuffer, const uint aLength)
	{
		int wError = SockRead(fSockCB, aBuffer, aLength);
		if (wError)
			throw_simple_error(wError, std::format("{} {} Read", __FILE__, __LINE__));
	}

	// Read data into aBuffer for the length aToRead throwing away
	// any excess and return the actual no read in aRead.
	// This is arguably a bad form and should be avoided.
	void   Read(void* aBuffer, const uint aToRead, uint& aRead)
	{
		aRead = ReadLength();
		if (aRead <= aToRead)
			Read(aBuffer, aRead);
		else
		{
			Read(aBuffer, aToRead);
			char soak[512];
			while (ReadStream((void*)soak, sizeof(soak)));
		}
	}

	// Old form read that uses a tBuffer construct for the lengths and data.
	// Will resolve into new form.
	void   Read(CBSockBuffer* aBuffer)
	{
		Read(aBuffer->p, aBuffer->BytesToRead, aBuffer->BytesRead);
	}

	// Read data into aBuffer up to the length aLength
	// returns the length read.
	uint ReadStream(void* aBuffer, const uint aLength)
	{
		uint wActual;
		int wError = SockStreamRead(fSockCB, aBuffer, aLength, &wActual);
		if (wError)
			throw_simple_error(wError, std::format("{} {} ReadStream", __FILE__, __LINE__));
		return wActual;
	}

	// WriteLength writes an uint as data after converting it
	// to network byte order.
	void   WriteLength(const uint aLength)
	{
		int wError = SockWriteLength(fSockCB, aLength);
		if (wError)
			throw_simple_error(wError, std::format("{} {} WriteLength", __FILE__, __LINE__));
	}

	// Write data for exactly the length of aLength. This is normally
	// used after WriteLength, but can also be used to write stream
	// data.
	void   Write(void* aBuffer, const uint aLength)
	{
		int wError = SockWrite(fSockCB, aBuffer, aLength);
		if (wError)
			throw_simple_error(wError, std::format("{} {} Write", __FILE__, __LINE__));
	}

	// Old form write that uses a tBuffer construct for the lengths and
	// data. Will resolve into the new form.
	void   Write(CBSockBuffer* aBuffer)
	{
		WriteLength(aBuffer->BytesToWrite);
		Write((void*)aBuffer->p, aBuffer->BytesToWrite);
		aBuffer->BytesWritten = aBuffer->BytesToWrite;
	}

	// ================================================================
	// A fix for the existing problem of multiple write resolved to one
	// ================================================================

	//void   Write(tCBSockBuffer **aBuffer, ulong aCount);

	// WaitRead will not read data, but will wait until there is data
	// to read or timeout. Returns true if there is data or returns
	// false if it times out.
	bool   WaitRead(const uint aTimeout)
	{
		bool wResult;
		int  wError = SockWaitRead(fSockCB, aTimeout, &wResult);

		if (wError == errSockTimeout && errno != EINTR)
			return false;

		if (wError)
			throw_simple_error(wError, std::format("{} {} WaitRead", __FILE__, __LINE__));
		return wResult;
	}

	// WaitWrite will not write data, but will wait until the
	// counterpart is ready to read or timeout. Returns true if the
	// counterpart is ready or returns false if it times out.
	bool   WaitWrite(const uint aTimeout)
	{
		bool wResult;
		int  wError = SockWaitWrite(fSockCB, aTimeout, &wResult);

		if (wError == errSockTimeout && errno != EINTR)
			return false;

		if (wError)
			throw_simple_error(wError, std::format("{} {} WaitWrite", __FILE__, __LINE__));
		return wResult;
	}

	// This only really makes sense from a client point of view
	// Will do an old style write followed by a read.
	void   Transact(CBSockBuffer* bufOut, CBSockBuffer* bufIn)
	{
		Write(bufOut);
		Read(bufIn);
	}

	// This only really makes sense from a client point of view
	// Will do an open, old style write followed by a read, then a close.
	void   Call(CBSockBuffer* bufOut, CBSockBuffer* bufIn)
	{
		Open();
		Transact(bufOut, bufIn);
		Close();
	}
	// Sets the timeout parameter is millisecs
	void   SetTimeout(const uint aTimeout) { fSockCB->TimeOut = aTimeout; }

	// gets the timeout value
	uint GetTimeout() const { return fSockCB->TimeOut; }

	// Sets the number of times to retry
	void   SetRetries(const uint aRetries) { fSockCB->Retries = (ushort)aRetries; }

	// Gets the number of retries
	ushort GetRetries() const { return fSockCB->Retries; }

	// Query the open status
	bool   IsOpen() const { return fSockCB->CommsPort == -1 ? false : true; }

	// Return the IP address
	sockaddr_in* SockAddr() const { return &fSockCB->Addr; }

	// Return the socket
	int Socket() const { return fSockCB->CommsPort; }

	ushort PortNo() const { return (ushort)htons(fSockCB->Addr.sin_port); }

	int CommsPort() const { return fSockCB->CommsPort; }
};

export class CBSockServer : public CBSockClient
{
private:
	// This form of constructor is illegal now.
	CBSockServer()
	{
	}
public:
	// This form of constructor expects a service defined in a services file.
	// see above. It will also honour the old form name :socket:<host>:<service>
	// and extract the service.
	CBSockServer(const char* aService)
	{
		char* names[3];
		char  temp[128];
		strncpy(temp, aService, sizeof(temp) - 1);
		int parts = ParseName(temp, ':', names);

		int wError = 0;
		if (parts == 0)
			wError = SockServerInit(&fSockCB, aService);
		else if (parts != 3 || (strcmp(names[0], "socket")) != 0)

			throw_simple_error(wError, std::format("{} {} :socket:<host>:<service> or <service> expected WaitWrite {}", __FILE__, __LINE__, aService));
		else
			wError = SockServerInit(&fSockCB, names[2]);
		if (wError)
			throw_simple_error(wError, std::format("{} {} Init", __FILE__, __LINE__));
	}
	// Construct a socket class from an existing socket number
	CBSockServer(const int iSocket, const int Retries = 5, const int TimeOut = 10000)
	{
		int wError = SockDupServer(&fSockCB, iSocket, Retries, TimeOut);
		if (wError)
			throw_simple_error(wError, std::format("{} {} Init", __FILE__, __LINE__));
	}
	// Construct a socket class from an existing socket number
	CBSockServer(const CBSockServer& Sock)
	{
		fSockCB = Sock.fSockCB;
	}
#if defined(USE_OPENSSL)
	// Construct an OpenSSL server - required CertFile and KeyFile - the others may be left as null(0) or used.
	CBSockServer(const char* aService, const char* CertFile, const char* CAfile, const char* CApath, const char* KeyFile, const char* KeyPassword)
	{
		int wError = SockServerInit(&fSockCB, aService);
		if (wError == 0)
			wError = SSLServerInit(fSockCB, CertFile, CAfile, CApath, KeyFile, KeyPassword);
		if (wError)
			throw XSOCKERR(xSockErr::eError(wError), fSockCB,
				SockError(fSockCB),
				SockErrorMsg(fSockCB));
	}
#endif
	// Open the socket for the server.
	void Open()
	{
		int wError = SockServerOpen(fSockCB);
		if (wError)
			throw_simple_error(wError, std::format("{} {} Open", __FILE__, __LINE__));
	}
	// Waits until a client is ready to connect or times out.
	// Does not do the Open. Returns true if a client is
	// present else false if times out.
	bool WaitConnect(const unsigned int aTimeout)
	{
		bool wResult;
		int wError = SockWaitServer(fSockCB, aTimeout, &wResult);
		if (wError == errSockTimeout && errno == EINTR)
			return false;
		if (errno == EINTR)
		{
			fprintf(stderr, "WaitConnect\n"
				"  wResult: %s\n"
				"  wError: %d\n"
				"  errno: %d\n"
				, wResult ? "TRUE" : "FALSE"
				, wError
				, errno);
			return false;
		}
		return wResult;
	}
	int ListenPort() const { return fSockCB->ListenPort; }
	Mutex *mutex;
};

