export module logfile;
import machine;
import <corecrt.h>;
import <cstdarg>;
import <cstdio>;
import <cstdlib>;
import <ctime>;
import <exception>;
import <iosfwd>;
import <ostream>;
import <print>;
import <string>;
import <sys/timeb.h>;
import <windows.h>;
import <exception>;
import <iostream>;
import xdir;

using namespace std;

export enum eLevel { eLogDebug, eLogInfo, eLogWarning, eLogError };

const char *LevelStr[] = { "DBG", "INF", "WRN", "ERR"};

export struct XLogFile : public exception
{
	XLogFile(const char* file, const int line, const std::string error)
	{
		println("LogFile : {} {} {}", file, line, error);
	}
	XLogFile(const XLogFile& aX)
	{
	}
};

constexpr size_t LOGFILE_BUFFER_LENGTH = 32*1024;

export class LogFile
{
public:
	static bool defRotate;
	static bool defDisplay;
	static int  defMaxFileSize;
	static LogFile* __logFile__;
	static LogFile* singleton(const char* aFileName, eLevel aDoLevel = eLogDebug, int aMaxFileSize = defMaxFileSize, bool aDisplay = defDisplay, bool aRotate = defRotate)
	{
		if (__logFile__ == 0)
			__logFile__ = new LogFile(aFileName, aDoLevel, aMaxFileSize);
		else
		{
			if (__logFile__->FileName.compare(aFileName) != 0)
				__logFile__->Switch(aFileName, aDoLevel, aMaxFileSize);
			else
			{
				__logFile__->doLevel = aDoLevel;
				__logFile__->maxFileSize = aMaxFileSize;
				__logFile__->Display = aDisplay;
				__logFile__->Rotate = aRotate;
			}
		}
		return __logFile__;
	}
	static eLevel level(std::string logLevel)
	{
		if (logLevel.length() > 0)
		{
			if (logLevel[0] == 'E' || logLevel[0] == 'e') return eLogError;
			if (logLevel[0] == 'W' || logLevel[0] == 'w') return eLogWarning;
			if (logLevel[0] == 'I' || logLevel[0] == 'i') return eLogInfo;
		}
		return eLogDebug;
	}
	std::string CustomString;
	void SetCustomString(std::string aCustomString) { CustomString = aCustomString; }
	LogFile()
	{
		doLevel = eLogDebug;
		Display = defDisplay;
		maxFileSize = defMaxFileSize;
		historyExtention = "hst";
		Rotate = defRotate;
		CustomString = "";
		fLog = 0;
		PrevDate = 99991231;
		memset(buffer, 0, sizeof(buffer));
	}
	LogFile(const char* aFileName, eLevel aDoLevel = eLogDebug, int aMaxFileSize = defMaxFileSize, bool aDisplay = defDisplay, bool aRotate = defRotate)
		: doLevel(aDoLevel)
		, Display(aDisplay)
		, maxFileSize(aMaxFileSize)
		, historyExtention("hst")
		, Rotate(aRotate)
		, CustomString("")
		, fLog(0)
		, PrevDate(99991231)
	{
		memset(buffer, 0, sizeof(buffer));
		if (aFileName && aFileName[0])
			Open(aFileName);
#if defined(M_AIX) || defined(M_GNU)
		sem = semget(ftok(aFileName, 'A'), 1, 0666 | IPC_CREAT);
#endif
	}
	~LogFile()
	{
		if (fLog)
			fclose(fLog);
		fLog = 0;
	}
	void Switch(const char* aFileName)
	{
		if (fLog) {
			fclose(fLog);
		}
		Open(aFileName);
	}
	void Switch(const char* aFileName, eLevel aDoLevel, int aMaxFileSize, bool aDisplay = defDisplay, bool aRotate = defRotate)
	{
		doLevel = aDoLevel;
		maxFileSize = aMaxFileSize;
		Display = aDisplay;
		FileName = aFileName;
		Rotate = aRotate;
		Switch(aFileName);
	}
	void Log(const char* Msg, eLevel MsgLevel = eLogDebug)
	{
		LogToFile(Msg, MsgLevel);
	}
	//void Log(xCept& x, eLevel MsgLevel = eLogError)
	//{
	//  lprintf(msgLevel, "Caught exception Name %s In %s(%d) Error : %s",
	//          x.Name(), x.FileName(), x.Line(), x.ErrorStr());
	//}
	void lprintf(eLevel MsgLevel, const char* fmt, ...)
	{
		va_list  argp;
		if (this) {
			va_start(argp, fmt);
			vsnprintf(buffer, LOGFILE_BUFFER_LENGTH, fmt, argp);
			LogToFile(buffer, MsgLevel);
		}
		else {
			va_start(argp, fmt);
			vprintf(fmt, argp);
			va_end(argp);
		}
		va_end(argp);
	}
	void Progress(const char* fmt, ...)
	{
		if (doLevel > eLogDebug)
			return;
		if (Display)
		{
			va_list  argp;
			va_start(argp, fmt);
			vprintf(fmt, argp);
			va_end(argp);
		}
	}
	void SetMaxFileSize(int aMaxFileSize) { maxFileSize = aMaxFileSize; }
	void LimitSize(FILE* fLog)
	{
		char renFileName[DIRMAX_PATH];
		char dir[DIRMAX_DIR];
		char name[DIRMAX_NAME];
		char ext[DIRMAX_EXT];
		if (Rotate == true || maxFileSize < 1)
			return;
		int now = ftell(fLog);
		if (now > maxFileSize)
		{
#if defined(M_AIX) || defined(M_GNU)
			autoWait here(sem);
#endif
			fclose(fLog);
			FNameSplit(FileName.c_str(), dir, name, ext);
			FNameMerge(renFileName, dir, name, historyExtention.c_str());
			unlink(renFileName);
			rename(FileName.c_str(), renFileName);
			fLog = fopen(FileName.c_str(), "w");
		}
	}
	void LogLevel(const char* aStrLogLevel)
	{
		char strLogLevel[50];
		strncpy(strLogLevel, aStrLogLevel, sizeof(strLogLevel) - 1);
		strLogLevel[sizeof(strLogLevel) - 1] = 0;
		strupr(strLogLevel);
		if (strcmp(strLogLevel, "DEBUG") == 0
			|| strcmp(strLogLevel, "DBG") == 0)
			doLevel = eLogDebug;
		else if (strcmp(strLogLevel, "INFO") == 0
			|| strcmp(strLogLevel, "INF") == 0)
			doLevel = eLogInfo;
		else if (strcmp(strLogLevel, "WARNING") == 0
			|| strcmp(strLogLevel, "WRN") == 0)
			doLevel = eLogWarning;
		else if (strcmp(strLogLevel, "ERROR") == 0
			|| strcmp(strLogLevel, "ERR") == 0)
			doLevel = eLogError;
		else
			doLevel = eLogDebug;
	}
	void SetLogLevel(eLevel level) { doLevel = level; }
	void SetHistoryExtension(const char* ext) { historyExtention = ext; }
	void SetDisplay(bool value) { Display = value; }
	std::string FileName;
	eLevel doLevel;
	bool Display;
	int  PrevDate;
protected:
	std::string historyExtention;
	FILE* fLog;
	int  maxFileSize;
	char buffer[LOGFILE_BUFFER_LENGTH + 1];
	void Open(const char* fileName, const char* mode = "a")
	{
		char errorStr[4096];
		std::string TBFileName = fileName;
		FileName = fileName;
		if (Rotate)
			GetDatedFilename(TBFileName);
		if (fLog)
			fclose(fLog);
		fLog = fopen(TBFileName.c_str(), mode);
		if (!fLog)
		{
			snprintf(errorStr, sizeof(errorStr), "Failed to open file(%s)", TBFileName.c_str());
			throw XLogFile(__FILE__, __LINE__, errorStr);
		}
	}
	void LogToFile(const char* msg, eLevel msgLevel)
	{
		time_t      now;
		tm* nowTm;
		char        currentDate[13];
		char strBuff[512];
		const char* aCustomString = "";
		if (this && this->fLog)
		{
			aCustomString = CustomString.c_str();
		}
		if (msgLevel < doLevel)
			return;
		time(&now);
		nowTm = localtime(&now);
		if (this && this->fLog && Rotate)
		{
			snprintf(currentDate,
				sizeof(currentDate) - 1,
				"%04d%02d%02d",
				nowTm->tm_year + 1900,
				nowTm->tm_mon + 1,
				nowTm->tm_mday);
			// If it is a new day, rotate the log from logfile.txt to logfile_YYYMMDD.txt and reopen logfile.txt
			// Previous date is initialised as 99999999 to prevent hitting this the first time, if the year is past 99999999, WOW!
			if (atoi(currentDate) > PrevDate)
				SwitchOnDate();
			//Make the previous date = current date
			PrevDate = atoi(currentDate);
		}
#ifdef WIN32
		_timeb curTime;
		_ftime(&curTime);
#else
		timeb curTime;
		ftime(&curTime);
#endif
		snprintf(strBuff, sizeof(strBuff), "%04d%02d%02d%02d%02d%02d.%03d %-4s %s",
			nowTm->tm_year + 1900,
			nowTm->tm_mon + 1,
			nowTm->tm_mday,
			nowTm->tm_hour,
			nowTm->tm_min,
			nowTm->tm_sec,
			curTime.millitm,
			LevelStr[(int)msgLevel],
			aCustomString);
		if (this && this->fLog)
		{
			fwrite(strBuff, 1, strlen(strBuff), fLog);
			fwrite(msg, 1, strlen(msg), fLog);
			fputc('\n', fLog);
			fflush(fLog);
			LimitSize(fLog);
			if (Display)
				std::cout << strBuff << msg << std::endl << std::flush;
		}
		else
			std::cout << strBuff << msg << std::endl << std::flush;
	}
	void GetDatedFilename(std::string& aFilename)
	{
		time_t Now;
		tm* NowTm;
		char   currentDate[20];
		time(&Now);
		NowTm = localtime(&Now);
		snprintf(currentDate,
			sizeof(currentDate) - 1,
			"_%04d%02d%02d",
			NowTm->tm_year + 1900,
			NowTm->tm_mon + 1,
			NowTm->tm_mday);
		char work[512];
		strncpy(work, aFilename.c_str(), sizeof(work) - 1);
		char* pch = strrchr(work, '.');
		if (pch != 0)
			*pch = 0;
		aFilename = work;
		aFilename.append(currentDate);
		if (pch != 0)
		{
			*pch = '.';
			aFilename.append(pch);
		}
	}
	void SwitchOnDate()
	{
		Open(FileName.c_str());
	}
#if defined(M_AIX) || defined(M_GNU)
	int  sem;
#endif
	bool Rotate;
};

export bool LogFile::defRotate = true;
export bool LogFile::defDisplay = false;
export int  LogFile::defMaxFileSize = 0;

export LogFile* LogFile::__logFile__;

export class SingletonLogFile
{
public:
	static void Initialize(const char* fileName = 0, eLevel doLevel = eLogDebug, bool display = LogFile::defDisplay)
	{
		const char* usefilename = fileName;
		if (usefilename == 0)
		{
			if (LogFile::__logFile__ == 0)
			{
				throw XLogFile(__FILE__, __LINE__, "Can not initialize - No logfile previously constructed");
			}
			usefilename = LogFile::__logFile__->FileName.c_str();
		}
		LogFile::singleton(usefilename, doLevel, 0);
		LogFile::__logFile__->SetDisplay(display);
	}
	static void Assign(LogFile* logFile)
	{
		if (LogFile::__logFile__ == logFile)
			return;
		Destroy();
		LogFile::__logFile__ = logFile;
	}
	static void Destroy(void)
	{
		if (LogFile::__logFile__)
		{
			delete LogFile::__logFile__;
			LogFile::__logFile__ = 0;
		}
	}
	static void Initialize(const char* fileName, const char* doLevel, bool display = LogFile::defDisplay)
	{
		Initialize(fileName, eLogDebug, display);
		LogFile::__logFile__->LogLevel(doLevel);
	}
};
