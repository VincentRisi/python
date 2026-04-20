#include <stdlib.h>
#include <malloc.h>
#include <winsock2.h>
#include <windows.h>

#include "openssl/ossl_typ.h"
#include <openssl/err.h>

#define  DESIRED_WINSOCK_VERSION 0x0101
#define  MINIMUM_WINSOCK_VERSION 1
#define  ioctl   ioctlsocket
#define  PROTOCOL "tcp"
#ifndef SOCKET_QSIZE
#  define SOCKET_QSIZE 1024
#endif
//#define USE_OPENSSL

export module obsocket;

typedef int socklen_t;
typedef char* pchar;
typedef unsigned int uint;

export struct tSockCB
{
	int ListenPort;            // TCP socket Descriptor for Server
	int CommsPort;             // TCP socket Descriptor for active connection
	struct sockaddr_in Addr;   // Socket address
	socklen_t AddrLen;
	unsigned short Retries;     // For Wait
	int TimeOut;                // For Wait
	int ErrorNo;                // Error Code
	SSL_CTX* ctx;
	SSL* ssl;
	char    SSL_Error[512];
	bool    hasCAFile;
	bool    hasCertFile;
};

export enum eSocketError
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

static const char* SockErrorText(int rc);
static int       _CloseComms(tSockCB* SockCB);
static int       _CloseListen(tSockCB* SockCB);
static void      _ForceClose(tSockCB* SockCB);
static bool      _InitForClient(tSockCB* SockCB, hostent*& ph, const char* aHost, int* rc, sockaddr_in& Addr);
static bool      _InitForServer(tSockCB* SockCB, sockaddr_in& Addr, int& ListenPort, int* rc);
static int       _Read(tSockCB* SockCB, char* buffer, int len);
static int       _ReadAll(tSockCB* SockCB, char* Buff, int Size);
static void      _SetError(tSockCB* SockCB);
static int       _Socket_ReadAll(tSockCB* SockCB, char* Buff, int Size);
static tSockCB*  _SockInit(const char* aHost, const char* aService, int* rc);
static int       _Wait(int aPort, uint aMSec, bool onRead, bool* aResult);
static int       _Write(tSockCB* SockCB, const char* buffer, int len);
#if defined(USE_OPENSSL)
static int       _LoadCertificates(tSockCB* SockCB, SSL_CTX* ctx, const char* CertFile, const char* CAfile, const char* CApath, const char* KeyFile, const char* KeyPassword);
static void      _Set_SSL_Error(tSockCB* SockCB);
static int       _SSL_ReadAll(tSockCB* SockCB, char* Buff, int Size);

export void _Set_SSL_Error(tSockCB* SockCB)
{
	int err = ERR_get_error();
	ERR_error_string_n(err, SockCB->SSL_Error, sizeof(SockCB->SSL_Error));
	printf("%s\n", SockCB->SSL_Error);
}

export int SSLServerInit(tSockCB* SockCB, const char* CertFile, const char* CAFile, const char* CAPath, const char* KeyFile, const char* KeyPassword)
{
	SSL_library_init();
	SSL_CTX*& ctx = SockCB->ctx;
	OpenSSL_add_all_algorithms();              /* Load cryptos, et.al. */
	SSL_load_error_strings();                  /* Bring in and register error messages */
	ctx = SSL_CTX_new(SSLv23_server_method()); /* Create new context */
	if (ctx == NULL)
	{
		_Set_SSL_Error(SockCB);
		return errSockSSLContext;
	}
	SockCB->hasCAFile = CAFile != 0;
	SockCB->hasCertFile = CertFile != 0;
	return _LoadCertificates(SockCB, ctx, CertFile, CAFile, CAPath, KeyFile, KeyPassword);
}

export int SSLClientInit(tSockCB* SockCB, const char* CertFile, const char* CAFile, const char* CAPath, const char* KeyFile, const char* KeyPassword)
{
	SSL_library_init();
	SSL_CTX*& ctx = SockCB->ctx;
	OpenSSL_add_all_algorithms();              /* Load cryptos, et.al. */
	SSL_load_error_strings();                  /* Bring in and register error messages */
	ctx = SSL_CTX_new(SSLv23_client_method()); /* Create new context */
	if (ctx == NULL)
	{
		_Set_SSL_Error(SockCB);
		return errSockSSLContext;
	}
	SockCB->hasCAFile = CAFile != 0;
	SockCB->hasCertFile = CertFile != 0;
	if (CertFile == 0 && KeyFile == 0)
		return 0;
	return _LoadCertificates(SockCB, ctx, CertFile, CAFile, CAPath, KeyFile, KeyPassword);
}

export int _LoadCertificates(tSockCB* SockCB, SSL_CTX* ctx, const char* CertFile, const char* CAFile, const char* CAPath, const char* KeyFile, const char* KeyPassword)
{
	if (SSL_CTX_use_certificate_file(ctx, CertFile, SSL_FILETYPE_PEM) <= 0)
	{
		_Set_SSL_Error(SockCB);
		return errSockSSLContext;
	}
	if (KeyPassword != 0)
		SSL_CTX_set_default_passwd_cb_userdata(ctx, (void*)KeyPassword);
	if (SSL_CTX_use_PrivateKey_file(ctx, KeyFile, SSL_FILETYPE_PEM) <= 0)
	{
		_Set_SSL_Error(SockCB);
		return errSockSSLContext;
	}
	if (!SSL_CTX_check_private_key(ctx))
	{
		int n = sizeof(SockCB->SSL_Error) - 1;
		strncpy(SockCB->SSL_Error, "Private key does not match the public certificate\n", n);
		SockCB->SSL_Error[n] = 0;
		return errSockSSLContext;
	}
	if (CAFile == 0 || CAPath == 0)
		return 0;
	if (SSL_CTX_load_verify_locations(ctx, CAFile, CAPath) <= 0)
	{
		_Set_SSL_Error(SockCB);
		return errSockSSLContext;
	}
	return 0;
}
#endif

export int SockDuplicate(tSockCB** SockCB,
	int     aCommsPort,
	int     aRetries,
	int     aTimeOut)
{
	*SockCB = (tSockCB*)malloc(sizeof(tSockCB));
	if (*SockCB)
	{
		(*SockCB)->ListenPort = -1;
		(*SockCB)->CommsPort = aCommsPort;
		(*SockCB)->Retries = (unsigned short)aRetries;
		(*SockCB)->TimeOut = aTimeOut;
		return 0;
	}
	return errSockInit;
}

export int SockDupServer(tSockCB** SockCB,
	int     aListenPort,
	int     aRetries,
	int     aTimeOut)
{
	*SockCB = (tSockCB*)malloc(sizeof(tSockCB));
	if (*SockCB)
	{
		(*SockCB)->ListenPort = aListenPort;
		(*SockCB)->CommsPort = -1;
		(*SockCB)->Retries = (unsigned short)aRetries;
		(*SockCB)->TimeOut = aTimeOut;
		return 0;
	}
	return errSockInit;
}

export int SockServerInit(tSockCB** SockCB, const char* aService)
{
	int rc;
	*SockCB = _SockInit(0, aService, &rc);
	return rc;
}

export int SockServerOpen(tSockCB* SockCB)
{
	SockCB->AddrLen = sizeof(SockCB->Addr);
	SockCB->CommsPort = accept(SockCB->ListenPort, (sockaddr*)&SockCB->Addr, &SockCB->AddrLen);
	if (SockCB->CommsPort == -1)
	{
		_SetError(SockCB);
		return errSockSocket;
	}
#if defined(TCP_NODELAY)
	int on = 1;
	setsockopt(SockCB->CommsPort, SOL_SOCKET, TCP_NODELAY, (char*)&on, sizeof(on));
#endif
#if defined(USE_OPENSSL)
	if (SockCB->ctx != 0)
	{
		SockCB->ssl = SSL_new(SockCB->ctx);
		int rc = SSL_set_fd(SockCB->ssl, SockCB->CommsPort);
		if (rc < 1)
		{
			_Set_SSL_Error(SockCB);
			return errSockSSLContext;
		}
		rc = SSL_accept(SockCB->ssl);
		if (rc < 1)
		{
			_Set_SSL_Error(SockCB);
			return errSockSSLContext;
		}
	}
#endif
	return 0;
}

export int SockClientInit(tSockCB** SockCB, const char* aHost, const char* aService)
{
	int rc;
	*SockCB = _SockInit(aHost, aService, &rc);
	return rc;
}

export int SockClientOpen(tSockCB* SockCB)
{
	int rc;
	SockCB->CommsPort = socket(AF_INET, SOCK_STREAM, 0);
	if (SockCB->CommsPort == -1)
	{
		_SetError(SockCB);
		return errSockSocket;
	}
	rc = connect(SockCB->CommsPort, (sockaddr*)&SockCB->Addr, sizeof(SockCB->Addr));
	if (rc)
	{
		_SetError(SockCB);
		_ForceClose(SockCB);
		return errSockConnect;
	}
#if defined(TCP_NODELAY)
	int delay_on = 1;
	setsockopt(SockCB->CommsPort, SOL_SOCKET, TCP_NODELAY, (char*)&delay_on, sizeof(delay_on));
#endif
#if defined(SO_USELOOPBACK)
	int loop_on = 1;
	setsockopt(SockCB->CommsPort, SOL_SOCKET, SO_USELOOPBACK, (char*)&loop_on, sizeof(loop_on));
#endif
#if defined(USE_OPENSSL)
	if (SockCB->ctx != 0)
	{
		SockCB->ssl = SSL_new(SockCB->ctx);
		rc = SSL_set_fd(SockCB->ssl, SockCB->CommsPort);
		if (rc < 1)
		{
			_Set_SSL_Error(SockCB);
			return errSockSSLContext;
		}
		if (SockCB->hasCertFile)
		{
			rc = SSL_connect(SockCB->ssl);
			if (rc < 1)
			{
				_Set_SSL_Error(SockCB);
				return errSockSSLContext;
			}
			if (SockCB->hasCertFile)
			{
				X509* peerCert = SSL_get_peer_certificate(SockCB->ssl);
				if (peerCert != 0)
				{
					int32 verify = SSL_get_verify_result(SockCB->ssl);
				}
			}
		}
		else
		{
			SSL_set_connect_state(SockCB->ssl);
		}
	}
#endif
	return 0;
}

export int SockSetTimeOut(tSockCB* SockCB, int aTimeOut)
{
	SockCB->TimeOut = aTimeOut;
	return 0;
}

export int SockSetRetries(tSockCB* SockCB, unsigned short aRetries)
{
	SockCB->Retries = aRetries;
	return 0;
}

export int SockDone(tSockCB* SockCB)
{
	if (SockCB->CommsPort != -1)
		_CloseComms(SockCB);
	if (SockCB->ListenPort != -1)
		_CloseListen(SockCB);
	SockCB->CommsPort = -1;
	SockCB->ListenPort = -1;
#if defined(USE_OPENSSL)
	SockCB->ctx = 0;
	SockCB->ssl = 0;
	memset(SockCB->SSL_Error, 0, sizeof(SockCB->SSL_Error));
#endif
	return 0;
}

export int SockClose(tSockCB* SockCB, bool both = true, bool rdrw = true)
{
#if defined(SO_LINGER)
	struct linger x = { 1, 5 };
	setsockopt(SockCB->CommsPort, SOL_SOCKET, SO_LINGER, (char*)&x, sizeof(x));
#endif
	if (SockCB->CommsPort != -1)
	{
#if defined(SD_BOTH)
		shutdown(SockCB->CommsPort, SD_BOTH);
#elif defined(SHUT_RDWR)
		shutdown(SockCB->CommsPort, SHUT_RDWR);
#endif
		_CloseComms(SockCB);
	}
	SockCB->CommsPort = -1;
	return 0;
}

export int SockReadLength(tSockCB* SockCB, uint* aSize)
{
	uint Size;
	int n = _ReadAll(SockCB, (char*)&Size, sizeof(Size));
	if (n != sizeof(uint))
		return errSockRead;
	*aSize = ntohl(Size);
	return 0;
}

export int SockRead(tSockCB* SockCB, void* aBuffer, uint  aBufferLen)
{
	int n = _ReadAll(SockCB, (char*)aBuffer, aBufferLen);
	if ((uint)n != aBufferLen)
		return errSockRead;
	return 0;
}

export int SockStreamRead(tSockCB* SockCB, void* aBuffer, uint aBufferLen, uint* aSize)
{
	*aSize = _Read(SockCB, (char*)aBuffer, aBufferLen);
	return 0;
}

export int SockWaitRead(tSockCB* SockCB, uint aTimeOut, bool* aResult)
{
	return _Wait(SockCB->CommsPort, aTimeOut, true, aResult);
}

export int SockWaitWrite(tSockCB* SockCB, uint aTimeOut, bool* aResult)
{
	return _Wait(SockCB->CommsPort, aTimeOut, false, aResult);
}

export int SockWaitServer(tSockCB* SockCB, uint aTimeOut, bool* aResult)
{
	return _Wait(SockCB->ListenPort, aTimeOut, true, aResult);
}

export int SockWriteLength(tSockCB* SockCB, uint aLength)
{
	uint writeLength = htonl(aLength);
	int n;
	n = _Write(SockCB, (char*)&writeLength, sizeof(writeLength));
	if (n != sizeof(writeLength))
	{
		_SetError(SockCB);
		return errSockWrite;
	}
	return 0;
}

export int SockWrite(tSockCB* SockCB, void* aBuffer, uint aBufferLen)
{
	int n;
	n = _Write(SockCB, (char*)aBuffer, aBufferLen);
	if ((uint)n != aBufferLen)
	{
		_SetError(SockCB);
		return errSockWrite;
	}
	return 0;
}

export int SockError(tSockCB* SockCB)
{
	return SockCB->ErrorNo;
}

export const char* SockErrorMsg(tSockCB* SockCB)
{
#if defined(USE_OPENSSL)
	if (SockCB->SSL_Error[0] != 0)
		return (pchar)SockCB->SSL_Error;
#endif
	return SockErrorText(SockCB->ErrorNo);
}

export int SockErrorMsgNet(tSockCB* SockCB, char* Buffer, uint BufferLen)
{
	int i;
	strncpy(Buffer, SockErrorMsg(SockCB), BufferLen - 1);
	Buffer[BufferLen - 1] = 0;
	for (i = strlen(Buffer); i < BufferLen; i++)
		Buffer[i] = ' ';
	return SockCB->ErrorNo;
}

static void _ForceClose(tSockCB* SockCB)
{
	if (SockCB->CommsPort != -1)
		_CloseComms(SockCB);
	SockCB->CommsPort = -1;
}

static tSockCB* _SockInit(const char* aHost, const char* aService, int* rc)
{
	tSockCB* SockCB = (tSockCB*)calloc(1, sizeof(tSockCB));
	if (aService == 0)
	{
		errno = WSAEADDRNOTAVAIL; // usurping errno
		*rc = errSockService;
		_SetError(SockCB);
		return SockCB;
	}
	servent* ps;
	hostent* ph;
	sockaddr_in      Addr;
	int ListenPort = -1;
	int isNo, i;
	WSADATA  wsadata;
	*rc = WSAStartup(DESIRED_WINSOCK_VERSION, &wsadata);
	if (*rc)
	{
		*rc = SockCB->ErrorNo = WSAGetLastError();
		return SockCB;
	}
	/* Check that the windows socket dll version is ok */
	if (wsadata.wVersion < MINIMUM_WINSOCK_VERSION)
	{
		*rc = errSockVersion;
		_SetError(SockCB);
		return SockCB;
	}
	*rc = 0;
	for (isNo = 1, i = 0; aService[i]; i++)
	{
		if (aService[i] < '0' || aService[i] > '9')
		{
			isNo = 0;
			break;
		}
	}
	if (isNo == 1)
		Addr.sin_port = htons((short)atoi(aService));
	else
	{
		ps = getservbyname(aService, PROTOCOL);
		if (ps == 0)
		{
			*rc = errSockService;
			_SetError(SockCB);
			return SockCB;
		}
		Addr.sin_port = ps->s_port;
	}
	if (aHost != 0)
	{
		if (_InitForClient(SockCB, ph, aHost, rc, Addr) == false)
			return SockCB;
	}
	else
	{
		if (_InitForServer(SockCB, Addr, ListenPort, rc) == false)
			return SockCB;
	}
	SockCB->ListenPort = ListenPort;
	SockCB->CommsPort = -1;
	SockCB->Retries = 5;
	SockCB->TimeOut = 10000;
	SockCB->Addr = Addr;
	if (aHost != 0)
		SockCB->Addr.sin_addr.s_addr = *((unsigned int*)ph->h_addr);
	else
		SockCB->Addr.sin_addr.s_addr = INADDR_ANY;
	SockCB->Addr.sin_family = AF_INET;
	return SockCB;
}


static bool _InitForServer(tSockCB* SockCB, sockaddr_in& Addr, int& ListenPort, int* rc)
{
	Addr.sin_addr.s_addr = INADDR_ANY;
	Addr.sin_family = AF_INET;
	ListenPort = socket(AF_INET, SOCK_STREAM, 0);
	if (ListenPort == -1)
	{
		*rc = errSockSocket;
		_SetError(SockCB);
		return false;
	}
	int on = 1;
#if defined(SO_REUSEADDR)
	if (setsockopt(ListenPort, SOL_SOCKET, SO_REUSEADDR, (char*)&on,
		sizeof(on)) < 0)
	{
		*rc = errSockSocket;
		_SetError(SockCB);
		return false;
	}
#endif
#if defined(NO_SO_REUSEPORT)
	if (setsockopt(ListenPort, SOL_SOCKET, SO_REUSEPORT, (char*)&on,
		sizeof(on)) < 0)
	{
		*rc = errSockSocket;
		_SetError(SockCB);
		return false;
	}
#endif
	* rc = bind(ListenPort, (struct sockaddr*)&Addr, sizeof(Addr));
	if (*rc == -1)
	{
		*rc = errSockBind;
		_SetError(SockCB);
		return false;
	}
	*rc = listen(ListenPort, SOCKET_QSIZE);
	if (*rc == -1)
	{
		*rc = errSockListen;
		_SetError(SockCB);
		return false;
	}
	if (Addr.sin_port == 0)
	{
		int len = sizeof(Addr);
		getsockname(ListenPort, (struct sockaddr*)&Addr, (int*)&len);
	}
	return true;
}

static bool _InitForClient(tSockCB* SockCB, hostent*& ph, const char* aHost, int* rc, sockaddr_in& Addr)
{
	ph = gethostbyname(aHost);
	if (ph == 0)
	{
		*rc = errSockHost;
		_SetError(SockCB);
		return false;
	}
	Addr.sin_family = ph->h_addrtype;
	memcpy(&Addr.sin_addr, ph->h_addr, ph->h_length);
	return true;
}

static int _Wait(int aPort, uint aMSec, bool onRead, bool* aResult)
{
	struct timeval TimeOut;
	struct timeval* TOP;
	if (aMSec)
	{
		TimeOut.tv_sec = aMSec / 1000;
		TimeOut.tv_usec = (aMSec % 1000) * 1000;
		TOP = &TimeOut;
	}
	else
		TOP = 0;
	fd_set OnSet;
	FD_ZERO(&OnSet);
	FD_SET((unsigned)aPort, &OnSet);
	int rc = select(FD_SETSIZE, (onRead == true ? &OnSet : 0), (onRead == true ? 0 : &OnSet), 0, TOP);
	if (rc <= 0)
		return errSockTimeout;
	*aResult = FD_ISSET(aPort, &OnSet) ? true : false;
	return 0;
}

static int _Read(tSockCB* sockCB, char* buffer, int len)
{
#if defined(USE_OPENSSL)
	if (sockCB->ssl != 0)
	{
		for (;;)
		{
			int bytes_read = SSL_read(sockCB->ssl, buffer, len);
			if (bytes_read < 0)
			{
				int code = SSL_get_error(sockCB->ssl, bytes_read);
				if (code == SSL_ERROR_WANT_READ)
					continue;
				_Set_SSL_Error(sockCB);
				return -1;
			}
			return bytes_read;
		}
	}
#endif
	int port = sockCB->CommsPort;
	int rc = recv(port, buffer, len, 0);
	return rc;
}

static int _Write(tSockCB* sockCB, const char* buffer, int len)
{
#if defined(USE_OPENSSL)
	if (sockCB->ssl != 0)
	{
		for (;;)
		{
			int bytes_written = SSL_write(sockCB->ssl, buffer, len);
			if (bytes_written == len)
				return bytes_written;
			if (bytes_written <= 0)
			{
				int code = SSL_get_error(sockCB->ssl, bytes_written);
				if (code == SSL_ERROR_WANT_WRITE)
					continue;
				_Set_SSL_Error(sockCB);
				return -1;
			}
			return -1;
		}
	}
#endif
	int port = sockCB->CommsPort;
	int rc = send(port, buffer, len, 0);
	return rc;
}

static int _CloseComms(tSockCB* sockCB)
{
	int port = sockCB->CommsPort;

	int rc = closesocket(port);
#if defined(USE_OPENSSL)
	if (sockCB->ssl != 0)
	{
		int rc1 = SSL_shutdown(sockCB->ssl);
		SSL_free(sockCB->ssl);         /* release SSL state */
		sockCB->ssl = 0;
	}
#endif
	return rc;
}

static int _CloseListen(tSockCB* sockCB)
{
	int port = sockCB->ListenPort;
	int rc = closesocket(port);
#if defined(USE_OPENSSL)
	if (sockCB->ctx != 0)
	{
		SSL_CTX_free(sockCB->ctx);
		sockCB->ctx = 0;
	}
#endif
	return rc;
}

static int _ReadAll(tSockCB* SockCB, char* Buff, int Size)
{
#if defined(USE_OPENSSL)
	if (SockCB->ssl != 0)
		return _SSL_ReadAll(SockCB, Buff, Size);
	else
#endif
		return _Socket_ReadAll(SockCB, Buff, Size);
}

static int _Socket_ReadAll(tSockCB* SockCB, char* Buff, int Size)
{
	int  BytesRead = 0, n, Try = 0;
	bool Result;
	while (BytesRead < Size)
	{
		if (SockCB->TimeOut)
		{
			if (_Wait(SockCB->CommsPort, SockCB->TimeOut, true, &Result) == 0)
			{
				if (Result == false)
				{
					if (Try++ < SockCB->Retries)
						continue;
					else
						return -1;
				}
			}
			else
			{
				return -1;
			}
		}
		n = _Read(SockCB, Buff, Size - BytesRead);
		if (n < 0) // underflow ??
			return n;
		if (n == 0)
			return BytesRead;
		BytesRead += n;
		Buff += n;
	}
	return BytesRead;
}
static void _SetError(tSockCB* SockCB)
{
	SockCB->ErrorNo = WSAGetLastError();
}

const char* SockErrorText(int rc)
{
	switch (rc)
	{
	case WSAEACCES:           return "Access denied";
	case WSAEADDRINUSE:       return "Address already in use";
	case WSAEADDRNOTAVAIL:    return "Can't assign requested address";
	case WSAEAFNOSUPPORT:     return "Address family not supported by protocol family";
	case WSAEALREADY:         return "Operation already in progress";
	case WSAEBADF:            return "Bad file number";
	case WSAECONNABORTED:     return "Software caused connection abort";
	case WSAECONNREFUSED:     return "Connection refused";
	case WSAECONNRESET:       return "Connection reset by peer";
	case WSAEDESTADDRREQ:     return "Destination address required";
	case WSAEDISCON:          return "Disconnected";
	case WSAEDQUOT:           return "Disk quota exceeded";
	case WSAEFAULT:           return "Bad address";
	case WSAEHOSTDOWN:        return "Host is down";
	case WSAEHOSTUNREACH:     return "Host is unreachable";
	case WSAEINPROGRESS:      return "Operation now in progress";
	case WSAEINTR:            return "Interrupted system call";
	case WSAEINVAL:           return "Invalid argument";
	case WSAEISCONN:          return "Socket is already connected";
	case WSAELOOP:            return "Too many levels of symbolic links";
	case WSAEMFILE:           return "Too many open files";
	case WSAEMSGSIZE:         return "Message too long";
	case WSAENAMETOOLONG:     return "Name too long";
	case WSAENETDOWN:         return "Network is down";
	case WSAENETRESET:        return "Network was reset";
	case WSAENETUNREACH:      return "ICMP network unreachable";
	case WSAENOBUFS:          return "No buffer space is supported";
	case WSAENOPROTOOPT:      return "Bad protocol option";
	case WSAENOTCONN:         return "Socket is not connected";
	case WSAENOTEMPTY:        return "Directory not empty";
	case WSAENOTSOCK:         return "Socket operation on non-socket";
	case WSAEOPNOTSUPP:       return "Operation not supported on socket";
	case WSAEPFNOSUPPORT:     return "Protocol family not supported";
	case WSAEPROCLIM:         return "EPROCLIM returned";
	case WSAEPROTONOSUPPORT:  return "Protocol not supported";
	case WSAEPROTOTYPE:       return "Protocol is wrong type for socket";
	case WSAEREMOTE:          return "The object is remote";
	case WSAESHUTDOWN:        return "Can't send after socket shutdown";
	case WSAESOCKTNOSUPPORT:  return "Socket type not supported";
	case WSAESTALE:           return "ESTALE returned";
	case WSAETIMEDOUT:        return "Connection timed out";
	case WSAETOOMANYREFS:     return "Too many references";
	case WSAEUSERS:           return "EUSERS returned";
	case WSAEWOULDBLOCK:      return "Operation would block";
	case WSAHOST_NOT_FOUND:   return "Host not found";
	case WSANOTINITIALISED:   return "Not initialized";
	case WSANO_DATA:          return "No data record available";
	case WSANO_RECOVERY:      return "Non-recoverable error";
	case WSASYSNOTREADY:      return "System not ready";
	case WSATRY_AGAIN:        return "Try again";
	case WSAVERNOTSUPPORTED:  return "Version is not supported";
	}
	return "Unknown Error";
}

