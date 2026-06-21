export module ociapi;
import machine;

#if defined(_MSC_VER)
#include <malloc.h>
#endif
#include <string.h>
#include <cstdlib>
#include <ctime>
#include "oci.h"
#include <cstdio>
import <exception>;
import <iostream>;
import <format>;
import <print>;

using namespace std;

export struct XOciApi : public exception
{
	XOciApi(const char* file, const int line, const std::string error)
	{
		std::println("OciApi : {} {} {}", file, line, error);
	}
	XOciApi(const XOciApi& aX)
	{
	}
};

static int32 JP_GregDate(int32 year, int32 month, int32 day)
{
	if (year < 1)
		year = 1;
	if (month > 2)
		month = month - 3;
	else
	{
		month = month + 9;
		year = year - 1;
	}
	int32 century = year / 100;
	int32 cy = year - 100 * century;
	return (146097 * century) / 4
		+ (1461 * cy) / 4
		+ (153 * month + 2) / 5
		+ day
		+ 1721119;
}

static int32 JP_GregDate(char* YYYYMMDD)
{
	int32 day, month, year;
	char work[5];
	strncpy(work, YYYYMMDD, 4);
	work[4] = 0;
	year = atoi(work);
	strncpy(work, YYYYMMDD + 4, 2);
	work[2] = 0;
	month = atoi(work);
	strncpy(work, YYYYMMDD + 6, 2);
	work[2] = 0;
	day = atoi(work);
	return  JP_GregDate(year, month, day);
}

static int32 JP_Seconds(char* HHMISS)
{
	int32 secs, mins, hours;
	char work[5];
	strncpy(work, HHMISS, 2);
	work[2] = 0;
	hours = atoi(work);
	strncpy(work, HHMISS + 2, 2);
	work[2] = 0;
	mins = atoi(work);
	strncpy(work, HHMISS + 4, 2);
	work[2] = 0;
	secs = atoi(work);
	return  hours * 60 * 60 + mins * 60 + secs;
}

static void JP_CalendarDate(int32 juldate, int32& year, int32& month, int32& day)
{
	int32 temp = juldate - 1721119;
	year = (4 * temp - 1) / 146097;
	temp = 4 * temp - 1 - 146097 * year;
	day = temp / 4;
	temp = (4 * day + 3) / 1461;
	day = 4 * day + 3 - 1461 * temp;
	day = (day + 4) / 4;
	month = (5 * day - 3) / 153;
	day = 5 * day - 3 - 153 * month;
	day = (day + 5) / 5;
	year = 100 * year + temp;
	if (month < 10)
		month += 3;
	else
	{
		month -= 9;
		year++;
	}
}

static void JP_CalendarDate(int32 jul, char* YYYYMMDD)
{
	int32 day, month, year;
	JP_CalendarDate(jul, year, month, day);
	char work[20];
	sprintf(work, "%04.4d%02.2d%02.2d", year, month, day);
	strncpy(YYYYMMDD, work, 8);
	YYYYMMDD[8] = 0;
}

static int32 JP_NewConnector(TJConnector*& conn)
{
	try
	{
		conn = new TJConnector;
		return 0;
	}
	catch (...)
	{
		return -1;
	}
}

static int32 JP_NewQuery(TJQuery*& qry, TJConnector& conn)
{
	try
	{
		qry = new TJQuery(conn);
		return 0;
	}
	catch (...)
	{
		return -1;
	}
}

static int32 JP_FreeConnector(TJConnector*& conn)
{
	try
	{
		delete conn;
		conn = 0;
		return 0;
	}
	catch (...)
	{
		return -1;
	}
}

static int32 JP_FreeQuery(TJQuery*& qry)
{
	try
	{
		delete qry;
		qry = 0;
		return 0;
	}
	catch (...)
	{
		return -1;
	}
}

export struct TJOCIDate
{
	uchar cc, yy, mm, dd, hh, mi, ss;
	uchar filler;
};

const TJOCIDate ZERO_DATE = { 100, 100, 1, 1, 1, 1, 1 };

static void _FromOracleDate(TJOCIDate& ocidate, int32& yyyymmdd, int32& hhmmss)
{
	if (memcmp(&ocidate, &ZERO_DATE, 7) == 0)
	{
		yyyymmdd = hhmmss = 0;
		return;
	}
	yyyymmdd = (ocidate.cc - 100) * 1000000
		+ (ocidate.yy - 100) * 10000;
	if (yyyymmdd >= 0)
		yyyymmdd += (ocidate.mm * 100 + ocidate.dd);
	else
		yyyymmdd -= (ocidate.mm * 100 + ocidate.dd);
	hhmmss = (ocidate.hh - 1) * 10000
		+ (ocidate.mi - 1) * 100
		+ (ocidate.ss - 1);
}

static void _ToOracleDate(TJOCIDate& ocidate, int32 yyyymmdd, int32 hhmmss)
{
	ocidate = ZERO_DATE;
	if (yyyymmdd == 0 && hhmmss == 0)
		return;
	if (hhmmss)
	{
		ocidate.ss = (unsigned char)(hhmmss % 100 + 1);
		hhmmss /= 100;
		ocidate.mi = (unsigned char)(hhmmss % 100 + 1);
		hhmmss /= 100;
		ocidate.hh = (unsigned char)(hhmmss % 100 + 1);
	}
	if (yyyymmdd)
	{
		int32 BC = yyyymmdd < 0;
		if (BC)
			yyyymmdd = -yyyymmdd;
		ocidate.dd = (unsigned char)(yyyymmdd % 100);
		yyyymmdd /= 100;
		ocidate.mm = (unsigned char)(yyyymmdd % 100);
		yyyymmdd /= 100;
		ocidate.yy = (unsigned char)(yyyymmdd % 100);
		yyyymmdd /= 100;
		ocidate.cc = (unsigned char)yyyymmdd;
		if (BC)
		{
			ocidate.yy = (unsigned char)(100u - ocidate.yy);
			ocidate.cc = (unsigned char)(100u - ocidate.cc);
		}
		else
		{
			ocidate.yy = (unsigned char)(ocidate.yy + 100u);
			ocidate.cc = (unsigned char)(ocidate.cc + 100u);
		}
	}
}

export struct TJDate
{
	char* date;
	TJDate(char* aDate)
	{
		date = aDate;
	}
};

export struct TJTime
{
	char* time;
	TJTime(char* aTime)
	{
		time = aTime;
	}
};

export struct TJDateTime
{
	char* dateTime;
	TJDateTime(char* aDateTime)
	{
		dateTime = aDateTime;
	}
};

export template <int32 size> class TJBlob
{
	uchar _data[size + 4];
public:
	int32 len() { return *(int32*)_data; }
	uchar* data() { return _data + 4; }
	void setData(int32 len, unsigned char* data)
	{
		memset(_data, 0, size + 4);
		*(int32*)_data = len;
		memcpy(_data + 4, data, len);
	}
	uchar* getData() { return _data; }
	void Swaps()
	{
#ifdef swapbytesH
		int32 _len = *(int32*)_data;
		SwapBytes(_len);
#endif
	}
};

export const short JP_NULL = -1;
export const short JP_NOT_NULL = 0;

#define TJ_CAST (const OraText*)
export struct TJConnector
{
	int32 signature;
	int32 result;
	text msgbuf[2048];
	int32 error;
	sb4 ociErrCode;
	char* user;
	char* server;
	time_t serverTime;
	time_t systemTime;
	OCIEnv* ociEnv;
	OCIError* ociError;
	OCISvcCtx* ociSvcCtx;
	int32 LoggedOn;
	static void _SqlError(TJConnector& conn)
	{
		if (conn.result != 0)
		{
			if (conn.ociError)
			{
				OCIErrorGet(conn.ociError,
					1,
					0,
					&conn.ociErrCode,
					conn.msgbuf,
					sizeof(conn.msgbuf),
					OCI_HTYPE_ERROR);
			}
			else
				sprintf((char*)conn.msgbuf, "Oracle error no handle (RC==%d)", conn.result);
		}
		else
			strcpy((char*)conn.msgbuf, "No oracle error (RC==0)");
	}
	static int32 _Result(TJConnector& conn)
	{
		_SqlError(conn);
		return conn.result;// ? conn.ociErrCode : 0;
	}
	TJConnector()
	{
		signature = 0xFACE0FF0;
		result = 0;
		memset(msgbuf, 0, sizeof(msgbuf));
		error = 0;
		ociErrCode = 0;
		user = 0;
		server = 0;
		serverTime = 0;
		systemTime = 0;
		ociEnv = 0;
		ociError = 0;
		ociSvcCtx = 0;
		LoggedOn = 0;
	}
	~TJConnector()
	{
		if (ociSvcCtx)
			Logoff();
	}
	static int32 JP_Logon(TJConnector& conn, const text* aUser, const text* aPassword, const text* aServer)
	{
		conn.user = strdup((char*)aUser);
		conn.server = strdup((char*)aServer);
		conn.result = OCIInitialize(OCI_DEFAULT, 0, 0, 0, 0);
		if (conn.result == 0)
			conn.result = OCIEnvInit(&conn.ociEnv, OCI_DEFAULT, 0, 0);
		if (conn.result == 0)
			conn.result = OCIHandleAlloc(conn.ociEnv, (void**)&conn.ociError, OCI_HTYPE_ERROR, 0, 0);
		if (conn.result == 0)
			conn.result = OCILogon(conn.ociEnv, conn.ociError, &conn.ociSvcCtx,
				TJ_CAST aUser, (ub4)strlen((char*)aUser),
				TJ_CAST aPassword, (ub4)strlen((char*)aPassword),
				TJ_CAST aServer, (ub4)strlen((char*)aServer));
		return _Result(conn);
	}
	void Logon(const char* aUser, const char* aPassword, const char* aServer)
	{
		if (JP_Logon(*this, (text*)aUser, (text*)aPassword, (text*)aServer))
			ThrowOnError("Logon");
		LoggedOn = 1;
	}
	static int32 JP_Logoff(TJConnector& conn)
	{
		if (conn.user) free(conn.user);
		if (conn.server) free(conn.server);
		conn.result = OCILogoff(conn.ociSvcCtx, conn.ociError);
		conn.ociSvcCtx = 0;
		conn.user = 0;
		conn.server = 0;
		return _Result(conn);
	}
	void Logoff()
	{
		if (LoggedOn == 0 || JP_Logoff(*this))
			ThrowOnError("Logoff");
		LoggedOn = 0;
	}
	static int32 JP_Commit(TJConnector& conn)
	{
		conn.result = OCITransCommit(conn.ociSvcCtx, conn.ociError,
			OCI_DEFAULT);
		return _Result(conn);
	}
	void Commit()
	{
		if (LoggedOn == 0 || JP_Commit(*this))
			ThrowOnError("Commit");
	}
	static int32 JP_Rollback(TJConnector& conn)
	{
		conn.result = OCITransRollback(conn.ociSvcCtx, conn.ociError,
			OCI_DEFAULT);
		return _Result(conn);
	}
	void Rollback()
	{
		if (LoggedOn == 0 || JP_Rollback(*this))
			ThrowOnError("Rollback");
	}
	void TimeStamp(char* timeStamp);
	static int32 JP_Error(TJConnector& conn, char* Msg, int32 MsgLen)
	{
		MsgLen--;
		memcpy(Msg, conn.msgbuf, MsgLen > sizeof(conn.msgbuf) ? sizeof(conn.msgbuf) : MsgLen);
		Msg[MsgLen] = 0;
		return conn.result;
	}
	void Error(char* Msg, int32 MsgLen)
	{
		if (JP_Error(*this, Msg, MsgLen))
			ThrowOnError("Error");
		LoggedOn = 0;
	}
	void ThrowOnError(const char* file = 0, int32 line = 0)
	{
		if (result != 0)
			throw file;// TOciApiException(result, (char*)msgbuf, file, line);
	}
};

export struct TJQuery
{
	int32 signature;
	int32 noBinds;
	int32 noDefines;
	int32 noRows;
	int32 sizeRow;
	int32 noIndicators;
	int32 rowsIndex;
	int32 rowsDone;
	int32 rowsRead;
	int32 rowsWritten;
	int32 doCommit;
	int32 isOpen;
	int32 error;
	char* command;
	char* data;
	int16* indicators;
	char file[65];
	int32 line;
	void FileAndLine(char* aFile, int32 aLine)
	{
		strncpy(file, aFile, sizeof(file) - 1);
		line = aLine;
	}
	TJConnector& conn;
	OCIBind** ociBinds;
	OCIDefine** ociDefines;
	OCIStmt* ociStmt;
	static int32 _Result(TJQuery& qry)
	{
		TJConnector::_SqlError(qry.conn);
		return qry.conn.result;// ? qry.conn.ociErrCode : 0;
	}
	TJQuery(TJConnector& aConnector) : conn(aConnector)
	{
		signature = 0xFACE0FF1;
		noBinds = 0;
		noDefines = 0;
		noRows = 0;
		sizeRow = 0;
		noIndicators = 0;
		rowsIndex = 0;
		rowsDone = 0;
		rowsRead = 0;
		rowsWritten = 0;
		doCommit = 0;
		isOpen = 0;
		error = 0;
		command = 0;
		data = 0;
		indicators = 0;
		ociBinds = 0;
		ociDefines = 0;
		ociStmt = 0;
		file[sizeof(file) - 1] = 0; // just in case
	}
	~TJQuery()
	{
		Close();
	}
	void  SetCommit(int32 commit)
	{
		doCommit = commit;
	}
	static int32 JP_Open(TJQuery& qry, const text* Query)
	{
		if (qry.isOpen == 0)
		{
			qry.conn.result = OCIHandleAlloc(qry.conn.ociEnv,
				(void**)&qry.ociStmt,
				OCI_HTYPE_STMT,
				0, 0);
			if (qry.conn.result == 0)
				qry.conn.result = OCIStmtPrepare(qry.ociStmt,
					qry.conn.ociError,
					TJ_CAST Query,
					(ub4)strlen((char*)Query),
					OCI_NTV_SYNTAX,
					OCI_DEFAULT);
			if (qry.conn.result == 0)
				qry.isOpen = 1;
		}
		return _Result(qry);
	}
	static void JP_Setup(TJQuery& qry, int32 noBinds, int32 noDefines, int32 noRows, int32 sizeRow)
	{
		qry.noBinds = noBinds;
		qry.noDefines = noDefines;
		qry.noRows = noRows;
		qry.sizeRow = sizeRow;
		int32 noIndicators = qry.noIndicators = noBinds + (noDefines * noRows);
		if (noDefines && qry.ociDefines == 0)
			qry.ociDefines = new OCIDefine * [noDefines];
		if (noBinds && qry.ociBinds == 0)
			qry.ociBinds = new OCIBind * [noBinds];
		if (noRows && noDefines && sizeRow)
		{
			if (qry.data == 0)
				qry.data = new char[noRows * sizeRow];
			memset(qry.data, 0, noRows * sizeRow);
		}
		if (noIndicators)
		{
			if (qry.indicators == 0)
				qry.indicators = new int16[noIndicators];
			memset(qry.indicators, 0, noIndicators * sizeof(int16));
		}
	}
	void  Open(const char* Query, int32 noBinds = 0, int32 noDefines = 0, int32 noRows = 0, int32 sizeRow = 0)
	{
		if (JP_Open(*this, (text*)Query))
			conn.ThrowOnError(file, line);
		JP_Setup(*this, noBinds, noDefines, noRows, sizeRow);
	}
	static void JP_SetupArray(TJQuery& qry, int32 noBinds, int32 noRows, int32 sizeRow)
	{
		qry.noDefines = 0;
		qry.noBinds = noBinds;
		qry.noRows = noRows;
		qry.sizeRow = sizeRow;
		int32 noIndicators = qry.noIndicators = noBinds * noRows;
		if (qry.ociBinds == 0)
			qry.ociBinds = new OCIBind * [noBinds];
		if (qry.data == 0)
			qry.data = new char[noRows * sizeRow];
		memset(qry.data, 0, noRows * sizeRow);
		if (qry.indicators == 0)
			qry.indicators = new int16[noIndicators];
		memset(qry.indicators, 0, noIndicators * sizeof(int16));
	}
	void OpenArray(const char* Query, int32 noBinds, int32 noRows, int32 sizeRow)
	{
		if (JP_Open(*this, (text*)Query))
			conn.ThrowOnError(file, line);
		JP_SetupArray(*this, noBinds, noRows, sizeRow);
	}
	static void JP_BindByName(TJQuery& qry, const text* name, int32 bindNo, void* data, int32 dataLen, ub2 dataType, sb2 isNull)
	{
		qry.indicators[bindNo] = isNull == JP_NOT_NULL ? JP_NOT_NULL : JP_NULL;
		qry.conn.result = OCIBindByName2(qry.ociStmt,
			&qry.ociBinds[bindNo],
			qry.conn.ociError,
			TJ_CAST name,
			-1,
			data,
			dataLen,
			dataType,
			&qry.indicators[bindNo],
			0, 0, 0, 0, OCI_DEFAULT);
	}
	static void JP_BindByNameArray(TJQuery& qry, const text* name, int32 bindNo, void* data, int32 dataLen, ub2 dataType)
	{
		qry.conn.result = OCIBindByName2(qry.ociStmt,
			&qry.ociBinds[bindNo],
			qry.conn.ociError,
			TJ_CAST name,
			-1,
			data,
			dataLen,
			dataType,
			&qry.indicators[bindNo * qry.noRows],
			0, 0, 0, 0, OCI_DEFAULT);
	}
	static void JP_DefineByPos(TJQuery& qry, int32 defineNo, void* data, int32 dataLen, ub2 dataType)
	{
		qry.conn.result = OCIDefineByPos2(qry.ociStmt,
			&qry.ociDefines[defineNo],
			qry.conn.ociError,
			defineNo + 1,
			data,
			dataLen,
			dataType,
			&qry.indicators[qry.noBinds + defineNo * qry.noRows],
			0, 0, OCI_DEFAULT);
	}
	static int32 JP_BindString(TJQuery& qry, text* name, int32 bindNo, char* data, int32 dataLen, int32 ansichar)
	{
		JP_BindByName(qry, name, bindNo, data, dataLen, ansichar ? SQLT_CHR : SQLT_STR);
		return _Result(qry);
	}
	static int32 JP_BindStringNull(TJQuery& qry, text* name, int32 bindNo, char* data, int32 dataLen, int16& null, int32 ansichar)
	{
		JP_BindByName(qry, name, bindNo, data, dataLen, ansichar ? SQLT_CHR : SQLT_STR, null);
		return _Result(qry);
	}
	void  Bind(const char* name, int32 bindNo, char* data, int32 dataLen, int16* null = 0, int32 ansichar = 0)
	{
		int32 result;
		if (null)
			result = JP_BindStringNull(*this, (text*)name, bindNo, data, dataLen, *null, ansichar);
		else
			result = JP_BindString(*this, (text*)name, bindNo, data, dataLen, ansichar);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindUtf8(TJQuery& qry, text* name, int32 bindNo, unsigned char* data, int32 dataLen)
	{
		JP_BindByName(qry, name, bindNo, data, dataLen, SQLT_BIN);
		return _Result(qry);
	}

	static int32 JP_BindUtf8Null(TJQuery& qry, text* name, int32 bindNo, unsigned char* data, int32 dataLen, int16& null)
	{
		JP_BindByName(qry, name, bindNo, data, dataLen, SQLT_BIN, null);
		return _Result(qry);
	}

	void BindUtf8(const char* name, int32 bindNo, unsigned char* data, int32 dataLen, int16* null)
	{
		int32 result;
		size_t dlen = strlen((char*)data);
		if (null)
			result = JP_BindUtf8Null(*this, (text*)name, bindNo, data, dlen, *null);
		else
			result = JP_BindUtf8(*this, (text*)name, bindNo, data, dlen);
		if (result)
			conn.ThrowOnError(file, line);
	}
#include <cwchar> 
	static int32 JP_BindUnicodeNull(TJQuery& qry, text* name, int32 bindNo, unsigned char* data, int32 datalen, int16& null)
	{
		JP_BindByName(qry, name, bindNo, data, datalen, SQLT_BIN, null);
		return _Result(qry);
	}

	static int32 JP_BindUnicode(TJQuery& qry, text* name, int32 bindNo, unsigned char* data, int32 datalen)
	{
		int16 null = 0;
		JP_BindUnicodeNull(qry, name, bindNo, data, datalen, null);
		return _Result(qry);
	}
	void BindUnicode(const char* name, int32 bindNo, unsigned char* data, int32 datalen, int16* null)
	{
		int32 result;
		size_t wlen = wcslen((wchar_t*)data) * 2;
		if (null)
			result = JP_BindUnicodeNull(*this, (text*)name, bindNo, data, wlen, *null);
		else
			result = JP_BindUnicode(*this, (text*)name, bindNo, data, wlen);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindBLOB(TJQuery& qry, text* name, int32 bindNo, unsigned char* data, int32 datalen)
	{
		int32* forlen = (int32*)data;
		int32 putlen = *forlen;
		putlen += sizeof(int32);
		if (putlen > datalen)
		{
			*forlen -= (putlen - datalen);
			putlen = datalen;
		}
#ifdef swapbytesH
		SwapBytes(*forlen);
#endif
		JP_BindByName(qry, name, bindNo, data, putlen, SQLT_LBI);
		return _Result(qry);
	}
	void BindBlob(const char* name, int32 bindNo, unsigned char* data, int32 dataSize)
	{
		int32 result;
		result = JP_BindBLOB(*this, (text*)name, bindNo, data, dataSize);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindShort(TJQuery& qry, text* name, int32 bindNo, int16& data)
	{
		JP_BindByName(qry, name, bindNo, &data, sizeof(data), SQLT_INT);
		return _Result(qry);
	}
	static int32 JP_BindShortNull(TJQuery& qry, text* name, int32 bindNo, int16& data, int16& null)
	{
		JP_BindByName(qry, name, bindNo, &data, sizeof(data), SQLT_INT, null);
		return _Result(qry);
	}
	void  Bind(const char* name, int32 bindNo, int16& data, int16* null = 0)
	{
		int32 result;
		if (null)
			result = JP_BindShortNull(*this, (text*)name, bindNo, data, *null);
		else
			result = JP_BindShort(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindInt(TJQuery& qry, text* name, int32 bindNo, int32& data)
	{
		JP_BindByName(qry, name, bindNo, &data, sizeof(data), SQLT_INT);
		return _Result(qry);
	}
	static int32 JP_BindIntNull(TJQuery& qry, text* name, int32 bindNo, int32& data, int16& null)
	{
		JP_BindByName(qry, name, bindNo, &data, sizeof(data), SQLT_INT, null);
		return _Result(qry);
	}
	void  Bind(const char* name, int32 bindNo, int32& data, int16* null = 0)
	{
		int32 result;
		if (null)
			result = JP_BindIntNull(*this, (text*)name, bindNo, data, *null);
		else
			result = JP_BindInt(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindLong(TJQuery& qry, text* name, int32 bindNo, int64& data)
	{
		JP_BindByName(qry, name, bindNo, &data, sizeof(data), SQLT_INT);
		return _Result(qry);
	}
	static int32 JP_BindLongNull(TJQuery& qry, text* name, int32 bindNo, int64& data, int16& null)
	{
		JP_BindByName(qry, name, bindNo, &data, sizeof(data), SQLT_INT, null);
		return _Result(qry);
	}
	void  Bind(const char* name, int32 bindNo, int64& data, int16* null = 0)
	{
		int32 result;
		if (null)
			result = JP_BindLongNull(*this, (text*)name, bindNo, data, *null);
		else
			result = JP_BindLong(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindDouble(TJQuery& qry, text* name, int32 bindNo, double& data)
	{
		JP_BindByName(qry, name, bindNo, &data, sizeof(data), SQLT_FLT);
		return _Result(qry);
	}
	static int32 JP_BindDoubleNull(TJQuery& qry, text* name, int32 bindNo, double& data, int16& null)
	{
		JP_BindByName(qry, name, bindNo, &data, sizeof(data), SQLT_FLT, null);
		return _Result(qry);
	}
	void  Bind(const char* name, int32 bindNo, double& data, int16* null = 0)
	{
		int32 result;
		if (null)
			result = JP_BindDoubleNull(*this, (text*)name, bindNo, data, *null);
		else
			result = JP_BindDouble(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindOCIDate(TJQuery& qry, text* name, int32 bindNo, TJOCIDate& data)
	{
		JP_BindByName(qry, name, bindNo, &data, 7, SQLT_DAT);
		return _Result(qry);
	}
	static int32 JP_BindOCIDateNull(TJQuery& qry, text* name, int32 bindNo, TJOCIDate& data, int16& null)
	{
		JP_BindByName(qry, name, bindNo, &data, 7, SQLT_DAT, null);
		return _Result(qry);
	}
	void  Bind(const char* name, int32 bindNo, TJOCIDate& data, int16* null = 0)
	{
		int32 result;
		if (null)
			result = JP_BindOCIDateNull(*this, (text*)name, bindNo, data, *null);
		else
			result = JP_BindOCIDate(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindStringArray(TJQuery& qry, text* name, int32 bindNo, char* data, int32 dataLen, int32 ansichar)
	{
		JP_BindByName(qry, name, bindNo, data, dataLen, ansichar ? SQLT_CHR : SQLT_STR);
		return _Result(qry);
	}
	void  BindArray(const char* name, int32 bindNo, char* data, int32 datalen, int32 ansichar = 0)
	{
		int32 result;
		result = JP_BindStringArray(*this, (text*)name, bindNo, data, dataLen, ansichar);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindIntArray(TJQuery& qry, text* name, int32 bindNo, int32* data)
	{
		JP_BindByName(qry, name, bindNo, data, sizeof(*data), SQLT_INT);
		return _Result(qry);
	}
	void  BindArray(const char* name, int32 bindNo, int32* data)
	{
		int32 result;
		result = JP_BindIntArray(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindLongArray(TJQuery& qry, text* name, int32 bindNo, int64* data)
	{
		JP_BindByName(qry, name, bindNo, data, sizeof(*data), SQLT_INT);
		return _Result(qry);
	}
	void  BindArray(const char* name, int32 bindNo, int64* data)
	{
		int32 result;
		result = JP_BindLongArray(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindShortArray(TJQuery& qry, text* name, int32 bindNo, int16* data)
	{
		JP_BindByName(qry, name, bindNo, data, sizeof(*data), SQLT_INT);
		return _Result(qry);
	}
	void  BindArray(const char* name, int32 bindNo, int16* data)
	{
		int32 result;
		result = JP_BindShortArray(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindDoubleArray(TJQuery& qry, text* name, int32 bindNo, double* data)
	{
		JP_BindByName(qry, name, bindNo, data, sizeof(*data), SQLT_FLT);
		return _Result(qry);
	}
	void  BindArray(const char* name, int32 bindNo, double* data)
	{
		int32 result;
		result = JP_BindDoubleArray(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_BindOCIDateArray(TJQuery& qry, text* name, int32 bindNo, TJOCIDate* data)
	{
		JP_BindByName(qry, name, bindNo, data, 7, SQLT_DAT);
		return _Result(qry);
	}
	void  BindArray(const char* name, int32 bindNo, TJOCIDate* data)
	{
		int32 result;
		result = JP_BindOCIDateArray(*this, (text*)name, bindNo, data);
		if (result)
			conn.ThrowOnError(file, line);
	}
	static int32 JP_DefineString(TJQuery& qry, int32 defineNo, char* data, int32 dataLen, int32 ansichar)
	{
		JP_DefineByPos(qry, defineNo, data, dataLen, ansichar ? SQLT_CHR : SQLT_STR);
		return _Result(qry);
	}
	static int32 JP_DefineLong(TJQuery& qry, int32 defineNo, int64* data)
	{
		JP_DefineByPos(qry, defineNo, data, sizeof(*data), SQLT_INT);
		return _Result(qry);
	}
	static int32 JP_DefineInt(TJQuery& qry, int32 defineNo, int32* data)
	{
		JP_DefineByPos(qry, defineNo, data, sizeof(*data), SQLT_INT);
		return _Result(qry);
	}
	static int32 JP_DefineShort(TJQuery& qry, int32 defineNo, int16* data)
	{
		JP_DefineByPos(qry, defineNo, data, sizeof(*data), SQLT_INT);
		return _Result(qry);
	}
	static int32 JP_DefineDouble(TJQuery& qry, int32 defineNo, double* data)
	{
		JP_DefineByPos(qry, defineNo, data, sizeof(*data), SQLT_FLT);
		return _Result(qry);
	}
	static int32 JP_DefineDate(TJQuery& qry, int32 defineNo, TJOCIDate* data)
	{
		JP_DefineByPos(qry, defineNo, data, sizeof(TJOCIDate), SQLT_DAT);
		return _Result(qry);
	}
	static int32 JP_DefineBLob(TJQuery& qry, int32 defineNo, char* data, int32 datalen)
	{
		JP_DefineByPos(qry, defineNo, data, datalen, SQLT_LBI);
		return _Result(qry);
	}
	static int32 JP_DefineUtf8(TJQuery& qry, int32 defineNo, unsigned char* data, int32 dataLen)
	{
		JP_DefineByPos(qry, defineNo, data, dataLen, SQLT_BIN);
		return _Result(qry);
	}
	static int32 JP_DefineUnicode(TJQuery& qry, int32 defineNo, unsigned char* data, int32 dataLen)
	{
		JP_DefineByPos(qry, defineNo, data, dataLen, SQLT_BIN);
		return _Result(qry);
	}
	void  Define(int32 defineNo, char* data, int32 dataLen, int32 ansichar = 0)
	{
		if (JP_DefineString(*this, defineNo, data, dataLen, ansichar))
			conn.ThrowOnError(file, line);
	}
	void  DefineUtf8(int32 defineNo, unsigned char* data, int32 dataLen)
	{
		if (JP_DefineUtf8(*this, defineNo, data, dataLen))
			conn.ThrowOnError(file, line);
	}
	void  DefineUnicode(int32 defineNo, unsigned char* data, int32 dataLen)
	{
		if (JP_DefineUnicode(*this, defineNo, data, dataLen))
			conn.ThrowOnError(file, line);
	}
	void  Define(int32 defineNo, int16* data)
	{
		if (JP_DefineShort(*this, defineNo, data))
			conn.ThrowOnError(file, line);
	}
	void  Define(int32 defineNo, int32* data)
	{
		if (JP_DefineInt(*this, defineNo, data))
			conn.ThrowOnError(file, line);
	}
	void  Define(int32 defineNo, int64* data)
	{
		if (JP_DefineLong(*this, defineNo, data))
			conn.ThrowOnError(file, line);
	}
	void  Define(int32 defineNo, double* data)
	{
		if (JP_DefineDouble(*this, defineNo, data))
			conn.ThrowOnError(file, line);
	}
	void  Define(int32 defineNo, TJOCIDate* data)
	{
		if (JP_DefineDate(*this, defineNo, data))
			conn.ThrowOnError(file, line);
	}
	void  DefineBlob(int32 defineNo, char* data, int32 dataSize)
	{
		if (JP_DefineBLob(*this, defineNo, data, datalen))
			conn.ThrowOnError(file, line);
	}
	static int32 JP_Exec(TJQuery& qry)
	{
		qry.rowsDone = 0;
		qry.rowsRead = 0;
		qry.rowsIndex = 0;
		qry.error = 0;
		qry.conn.result = OCIStmtExecute(qry.conn.ociSvcCtx,
			qry.ociStmt,
			qry.conn.ociError,
			qry.noDefines ? 0 : 1,
			0, 0, 0,
			qry.noDefines ? OCI_DEFAULT : OCI_EXACT_FETCH);
		return _Result(qry);
	}
	void  Exec()
	{
		if (JP_Exec(*this))
			conn.ThrowOnError(file, line);
	}
	static int32 JP_Fetch(TJQuery& qry)
	{
		if (qry.rowsDone >= qry.rowsRead)
		{
			if (qry.error == OCI_NO_DATA)
				return qry.error;
			if (qry.rowsDone > 0)
				qry.Clear();
			qry.conn.result = OCIStmtFetch(qry.ociStmt,
				qry.conn.ociError,
				qry.noRows,
				OCI_FETCH_NEXT,
				OCI_DEFAULT);
			if (qry.conn.result)
			{
				qry.error = _Result(qry);
				if (qry.error != OCI_NO_DATA)
					return qry.error;
				qry.conn.result = 0;
			}
			qry.rowsIndex = 0;
			sword AGRC = OCIAttrGet(qry.ociStmt,
				OCI_HTYPE_STMT,
				&qry.rowsRead,
				0,
				OCI_ATTR_ROW_COUNT,
				qry.conn.ociError);
			if (AGRC)
			{
				qry.conn.result = AGRC;
				return _Result(qry);
			}
			if (qry.rowsRead == 0
				|| qry.rowsRead == qry.rowsDone)
				return qry.error;
		}
		else
			qry.rowsIndex++;
		qry.rowsDone++;
		return _Result(qry);
	}
	bool  Fetch()
	{
		int32 result = JP_Fetch(*this);
		if (result == OCI_NO_DATA)
			return false;
		if (result)
			conn.ThrowOnError(file, line);
		return true;
	}
	static int32 JP_Deliver(TJQuery& qry, int32 doit)
	{
		if (qry.rowsIndex + 1 >= qry.noRows
			|| (qry.rowsIndex > 0 && doit == 1))
		{
			if (doit == 0)
				qry.rowsIndex++;
			qry.conn.result = OCIStmtExecute(qry.conn.ociSvcCtx,
				qry.ociStmt,
				qry.conn.ociError,
				qry.rowsIndex,
				0, 0, 0, OCI_DEFAULT);
			if (qry.conn.result == 0 && qry.doCommit != 0)
				qry.conn.Commit();
			qry.rowsIndex = 0;
		}
		else
			qry.rowsIndex++;
		return _Result(qry);
	}
	void  Deliver(int32 doit)
	{
		if (JP_Deliver(*this, doit))
			conn.ThrowOnError(file, line);
	}
	static void JP_GetUtf8(TJQuery& qry, unsigned char* into, unsigned char* from, int32 dataLen)
	{
		memcpy(into, from + (qry.rowsIndex * dataLen), dataLen);
	}
	static void JP_GetUnicode(TJQuery& qry, unsigned char* into, unsigned char* from, int32 dataLen)
	{
		size_t wlen = wcslen((wchar_t*)from);
		memcpy(into, from + (qry.rowsIndex * dataLen), wlen);
	}
	static void JP_GetBLOB(TJQuery& qry, void* into, unsigned char* from, int32 dataLen)
	{
		unsigned char* data = (unsigned char*)into;
		memcpy(data, from + (qry.rowsIndex * dataLen), dataLen);
		int32* len = (int32*)data;
#ifdef swapbytesH
		SwapBytes(*len);
#endif
	}
	static void JP_GetString(TJQuery& qry, char* into, char* from, int32 dataLen)
	{
		memcpy(into, from + (qry.rowsIndex * dataLen), dataLen);
	}
	static void JP_GetLong(TJQuery& qry, int64& into, char* from)
	{
		into = *(int64*)(from + (qry.rowsIndex * sizeof(int64)));
	}
	static void JP_GetInt(TJQuery& qry, int32& into, char* from)
	{
		into = *(int32*)(from + (qry.rowsIndex * sizeof(int32)));
	}
	static void JP_GetShort(TJQuery& qry, int16& into, char* from)
	{
		into = *(int16*)(from + (qry.rowsIndex * sizeof(int16)));
	}
	static void JP_GetDouble(TJQuery& qry, double& into, char* from)
	{
		into = *(double*)(from + (qry.rowsIndex * sizeof(double)));
	}
	static void JP_GetDate(TJQuery& qry, char* into, char* from)
	{
		int32 date;
		int32 time;
		_FromOracleDate(*(TJOCIDate*)(from + qry.rowsIndex * 8), date, time);
		sprintf(into, "%08.8d", date);
	}
	static void JP_GetTime(TJQuery& qry, char* into, char* from)
	{
		int32 date;
		int32 time;
		_FromOracleDate(*(TJOCIDate*)(from + qry.rowsIndex * 8), date, time);
		sprintf(into, "%06.6d", time);
	}
	static void JP_GetDateTime(TJQuery& qry, char* into, char* from)
	{
		int32 date;
		int32 time;
		_FromOracleDate(*(TJOCIDate*)(from + qry.rowsIndex * 8), date, time);
		sprintf(into, "%08.8d%06.6d", date, time);
	}
	static void JP_GetNull(TJQuery& qry, int16& into, int32 defineNo)
	{
		into = qry.indicators[qry.noBinds + defineNo * qry.noRows + qry.rowsIndex];
	}
	void  GetNoNull(char* into, char* from, int32 dataLen)
	{
		JP_GetString(*this, into, from, dataLen);
		if (strlen(into) == 1 && strncmp(into, " ", 1) == 0)
		{
			memset(into, 0, strlen(into));
			into[0] = '\0';
		}
	}
	void  Get(char* into, char* from, int32 dataLen)
	{
		JP_GetString(*this, into, from, dataLen);
	}
	void  GetUtf8(unsigned char* into, unsigned char* from, int32 dataLen)
	{
		JP_GetUtf8(*this, into, (unsigned char*)from, dataLen);
	}
	void  GetUnicode(unsigned char* into, unsigned char* from, int32 dataLen)
	{
		JP_GetUnicode(*this, into, from, dataLen);
	}
	void  GetBlob(unsigned char* into, unsigned char* from, int32 dataLen)
	{
		JP_GetBLOB(*this, into, from, dataLen);
	}
	void  Get(int16& into, char* from)
	{
		JP_GetShort(*this, into, from);
	}
	void  Get(int32& into, char* from)
	{
		JP_GetInt(*this, into, from);
	}
	void  Get(int64& into, char* from)
	{
		JP_GetLong(*this, into, from);
		JP_GetLong(*this, into, from);
	}
	void  Get(double& into, char* from)
	{
		JP_GetDouble(*this, into, from);
	}
	void  Get(TJDate into, char* from)
	{
		JP_GetDate(*this, into.date, from);
	}
	void  Get(TJTime into, char* from)
	{
		JP_GetTime(*this, into.time, from);
	}
	void  Get(TJDateTime into, char* from)
	{
		JP_GetDateTime(*this, into.dateTime, from);
	}
	void  GetNull(int16& into, int32 defineNo)
	{
		JP_GetNull(*this, into, defineNo);
	}
	static void JP_PutString(TJQuery& qry, char* into, char* from, int32 dataLen)
	{
		memcpy(into + (qry.rowsIndex * dataLen), from, dataLen);
	}
	static void JP_PutString(TJQuery& qry, unsigned char* into, unsigned char* from, int32 dataLen)
	{
		memcpy(into + (qry.rowsIndex * dataLen), from, dataLen);
	}
	static void JP_PutLong(TJQuery& qry, char* into, int64& from)
	{
		*(int64*)(into + (qry.rowsIndex * sizeof(int64))) = from;
	}
	static void JP_PutInt(TJQuery& qry, char* into, int32& from)
	{
		*(int32*)(into + (qry.rowsIndex * sizeof(int32))) = from;
	}
	static void JP_PutShort(TJQuery& qry, char* into, int16& from)
	{
		*(int16*)(into + (qry.rowsIndex * sizeof(int16))) = from;
	}
	static void JP_PutDouble(TJQuery& qry, char* into, double& from)
	{
		*(double*)(into + (qry.rowsIndex * sizeof(double))) = from;
	}
	static void JP_PutDate(TJQuery& qry, char* into, char* from)
	{
		char date[9];
		strncpy(date, from, 8);
		date[8] = 0;
		_ToOracleDate(*(TJOCIDate*)(into + qry.rowsIndex * 7), atol(date), 0);
	}
	static void JP_PutTime(TJQuery& qry, char* into, char* from)
	{
		char time[7];
		strncpy(time, from, 6);
		time[6] = 0;
		_ToOracleDate(*(TJOCIDate*)(into + qry.rowsIndex * 7), 0, atol(time));
	}
	static void JP_PutDateTime(TJQuery& qry, char* into, char* from)
	{
		char date[9];
		char time[7];
		strncpy(date, from, 8);
		date[8] = 0;
		strncpy(time, from + 8, 6);
		time[6] = 0;
		_ToOracleDate(*(TJOCIDate*)(into + qry.rowsIndex * 7), atol(date), atol(time));
	}
	static void JP_PutNull(TJQuery& qry, int16& from, int32 bindNo)
	{
		qry.indicators[qry.noRows * bindNo + qry.rowsIndex] = from;
	}
	void Put(char* into, char* from, int32 dataLen)
	{
		JP_PutString(*this, into, from, dataLen);
	}
	void Put(char* into, int32& from)
	{
		JP_PutInt(*this, into, from);
	}
	void Put(char* into, int64& from)
	{
		JP_PutLong(*this, into, from);
	}
	void Put(char* into, int16& from)
	{
		JP_PutShort(*this, into, from);
	}
	void Put(char* into, double& from)
	{
		JP_PutDouble(*this, into, from);
	}
	void Put(char* into, TJDate from)
	{
		JP_PutDate(*this, into, from.date);
	}
	void Put(char* into, TJTime from)
	{
		JP_PutTime(*this, into, from.time);
	}
	void Put(char* into, TJDateTime from)
	{
		JP_PutDateTime(*this, into, from.dateTime);
	}
	void PutNull(int16& from, int32 bindNo)
	{
		JP_PutNull(*this, from, bindNo);
	}
	static int32 JP_Close(TJQuery& qry)
	{
		int32 result = 0;
		if (qry.isOpen == 1)
		{
			if (qry.command)
			{
				delete[] qry.command;
			}
			if (qry.data)
			{
				delete[] qry.data;
			}
			if (qry.indicators)
			{
				delete[] qry.indicators;
			}
			if (qry.ociBinds)
			{
				delete[] qry.ociBinds;
			}
			if (qry.ociDefines)
			{
				delete[] qry.ociDefines;
			}
			if (qry.ociStmt)
			{
				result = OCIHandleFree(qry.ociStmt, OCI_HTYPE_STMT);
			}
			qry.data = 0;
			qry.indicators = 0;
			qry.ociBinds = 0;
			qry.ociDefines = 0;
			qry.ociStmt = 0;
			qry.isOpen = 0;
			if (qry.conn.result == 0)
			{
				qry.conn.result = result;
				return _Result(qry);
			}
		}
		return result;
	}
	void Close()
	{
		int32 rc = conn.result;
		if (JP_Close(*this) && rc == 0)
			conn.ThrowOnError(file, line);
	}
	void Clear()
	{
		if (noRows && sizeRow)
			memset(data, 0, noRows * sizeRow);
		if (noIndicators)
			memset(indicators, 0, noIndicators * sizeof(int16));
	}
	static void JP_Sequence(TJQuery& qry, int32& sequence, char* sequencer)
	{
		TJQuery q(qry.conn);
		q.command = new char[32 + strlen(sequencer)];
		strcpy(q.command, "select ");
		strcat(q.command, sequencer);
		strcat(q.command, ".NEXTVAL from dual");
		q.Open(q.command, 0, 1, 1, 8);
		q.Define(0, (int32*)(q.data));
		q.Exec();
		if (q.Fetch())
			q.Get(sequence, q.data);
		else
			sequence = 0;
	}
	virtual int32& Sequence(int32& sequence, char* sequencer)
	{
		JP_Sequence(*this, sequence, sequencer);
		return sequence;
	}
	static void JP_BigSequence(TJQuery& qry, int64& sequence, char* sequencer)
	{
		TJQuery q(qry.conn);
		q.command = new char[32 + strlen(sequencer)];
		strcpy(q.command, "select ");
		strcat(q.command, sequencer);
		strcat(q.command, ".NEXTVAL from dual");
		q.Open(q.command, 0, 1, 1, 8);
		q.Define(0, (int64*)(q.data));
		q.Exec();
		if (q.Fetch())
			q.Get(sequence, q.data);
		else
			sequence = 0;
	}
	virtual int64& Sequence(int64& sequence, char* sequencer)
	{
		JP_BigSequence(*this, sequence, sequencer);
		return sequence;
	}
	static void JP_UserStamp(TJQuery& qry, char* userStamp)
	{
		strcpy(userStamp, qry.conn.user);
	}
	virtual char* UserStamp(char* userStamp)
	{
		JP_UserStamp(*this, userStamp);
		return userStamp;
	}
	static void JP_Date(TJQuery& qry, TJOCIDate& ocidate, char* aDate)
	{
		char date[9];
		strncpy(date, aDate, 8);
		date[8] = 0;
		_ToOracleDate(ocidate, atol(date), 0);
	}
	virtual TJOCIDate& Date(TJOCIDate& ocidate, char* date)
	{
		JP_Date(*this, ocidate, date);
		return ocidate;
	}
	static void JP_Time(TJQuery& qry, TJOCIDate& ocidate, char* aTime)
	{
		char time[7];
		strncpy(time, aTime, 6);
		time[6] = 0;
		_ToOracleDate(ocidate, 0, atol(time));
	}
	virtual TJOCIDate& Time(TJOCIDate& ocidate, char* time)
	{
		JP_Time(*this, ocidate, time);
		return ocidate;
	}
	static void JP_DateTime(TJQuery& qry, TJOCIDate& ocidate, char* dateTime)
	{
		char date[9];
		char time[7];
		strncpy(date, dateTime, 8);
		date[8] = 0;
		strncpy(time, dateTime + 8, 6);
		time[6] = 0;
		_ToOracleDate(ocidate, atol(date), atol(time));
	}
	virtual TJOCIDate& DateTime(TJOCIDate& ocidate, char* dateTime)
	{
		JP_DateTime(*this, ocidate, dateTime);
		return ocidate;
	}
	static void JP_TimeStamp(TJQuery& qry, TJOCIDate& ocidate, char* timeStamp)
	{
		qry.conn.TimeStamp(timeStamp);
		JP_DateTime(qry, ocidate, timeStamp);
	}
	virtual TJOCIDate& TimeStamp(TJOCIDate& ocidate, char* timeStamp)
	{
		JP_TimeStamp(*this, ocidate, timeStamp);
		return ocidate;
	}
};

void TJConnector::TimeStamp(char* timeStamp)
{
	if (serverTime == 0)
	{
		time(&systemTime);
		TJQuery q(*this);
		q.command = new char[32];
		strcpy(q.command, "select SYSDATE from dual");
		q.Open(q.command, 0, 1, 1, 8);
		q.Define(0, (TJOCIDate*)(q.data));
		q.Exec();
		serverTime = systemTime;
		if (q.Fetch())
		{
			q.Get(TJDateTime(timeStamp), q.data);
			serverTime = JP_GregDate(timeStamp) - JP_GregDate("19700101");
			serverTime = serverTime * (24 * 60 * 60) + JP_Seconds(timeStamp + 8);
		}
	}
	time_t tt;
	struct tm* lt;
	time(&tt);
	tt += (serverTime - systemTime);
	lt = gmtime(&tt);
	int32 dateNow = 19000000 + (10000 * lt->tm_year)
		+ (100L * (lt->tm_mon + 1))
		+ lt->tm_mday;
	int32 timeNow = 10000L * lt->tm_hour
		+ 100 * (lt->tm_min)
		+ lt->tm_sec;
	sprintf(timeStamp, "%08.8d%06.6d", dateNow, timeNow);
}

class TJAlloc
{
	static bool Failed;
public:
	static bool NoMemory()
	{
		return Failed;
	}
	static char* newChar(int32 size)
	{
		char* result = new char[size];
		Failed = (result == 0);
		if (result != 0)
			memset(result, 0, size);
		else
		{
			char work[256];
			snprintf(work, sizeof(work), "TJAlloc::newChar(%d) Memory allocation Error", size);
		}
		return result;
	}
	static int32* newInt(int32 size)
	{
		int32* result = new int32[size];
		Failed = (result == 0);
		if (result != 0)
			memset(result, 0, size);
		else
		{
			char work[256];
			snprintf(work, sizeof(work), "TJAlloc::newInt(%d) Memory allocation Error", size);
		}
		return result;
	}
	static char* dupChar(const char* value)
	{
		char* result = new char[strlen(value) + 1];
		if (result != 0)
			strcpy(result, value);
		return result;
	}
	static void deleteChar(char*& data)
	{
		if (data != 0)
		{
			delete[] data;
			data = 0;
		}
	}
	static void deleteInt(int32*& data)
	{
		if (data != 0)
		{
			delete[] data;
			data = 0;
		}
	}
};

struct TJCppRet
{
	const char* head;
	const char* output;
	const char* sequence;
	const char* tail;
	bool useField;
	bool useSequencer;
	bool hasTrigger;
	TJCppRet()
	{
		head = "";
		output = "";
		sequence = "";
		tail = "";
		useField = true;
		useSequencer = false;
		hasTrigger = false;
	}
	size_t setup(const char* serverName, const char* tableName, const char* procName, const char* fieldName, bool hasReturning)
	{
		size_t len = 0;
		if (hasReturning)
		{
			len += strlen("begin ");
			len += strlen(procName);
			len += strlen("(");
			len += strlen(fieldName);
			len += strlen(", :");
			len += strlen(fieldName);
			len += strlen("); end;");
		}
		else
		{
			len += strlen("begin ");
			len += strlen(procName);
			len += strlen("(");
			len += strlen(fieldName);
			len += strlen("); end;");
		}
		return len;
	}
	const char* checkUse(const char* fieldName)
	{
		if (useField)
			return fieldName;
		return "";
	}
};
