export module logfile;
import <windows.h>;
import <exception>;
import <iostream>;
import <format>;

using namespace std;

enum eLevel { eLogDebug, eLogInfo, eLogWarning, eLogError };

export struct XLogfileErr : public exception
{
	//static const char* getText(int err)
	//{
	//  switch (err)
	//  {
	//  }
	//}
	XLogfileErr(int error, string context = "")
	{
		string err = std::format("Logfile {} {}", context, error);
		cout << err << endl;
	}
	XLogfileErr(const XLogfileErr& aX)
	{
	}
};

bool tLogFile::defRotate = true;
bool tLogFile::defDisplay = false;
int  tLogFile::defMaxFileSize = 0;

tLogFile* tLogFile::__logFile__;

class tLogFile
{
public:
	static bool defRotate;
	static bool defDisplay;
	static int  defMaxFileSize;
	static tLogFile* __logFile__;
	static tLogFile* singleton(const char* aFileName, eLevel aDoLevel = eLogDebug, int aMaxFileSize = defMaxFileSize, bool aDisplay = defDisplay, bool aRotate = defRotate)
	{
		if (__logFile__ == 0)
			__logFile__ = new tLogFile(aFileName, aDoLevel, aMaxFileSize);
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
	tLogFile();
	tLogFile(const char* FileName, eLevel DoLevel = eLogDebug, int aMaxFileSize = defMaxFileSize, bool aDisplay = defDisplay, bool aRotate = defRotate);
	~tLogFile();
	void Switch(const char* FileName);
	void Switch(const char* aFileName, eLevel aDoLevel, int aMaxFileSize, bool aDisplay = defDisplay, bool aRotate = defRotate);
	void Log(const char* Msg, eLevel MsgLevel = eLogDebug);
	void Log(xCept& x, eLevel MsgLevel = eLogError);
	void lprintf(eLevel MsgLevel, const char* Fmt, ...);
	void Progress(const char* Fmt, ...);
	void SetMaxFileSize(int aMaxFileSize) { maxFileSize = aMaxFileSize; }
	void LimitSize(FILE* fLog);
	void LogLevel(const char* StrLogLevel);
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
	void Open(const char* fileName, const char* mode = "a");
	void LogToFile(const char* msg, eLevel msgLevel);
	void GetDatedFilename(std::string& filename);
	void SwitchOnDate();
#if defined(M_AIX) || defined(M_GNU)
	int  sem;
#endif
	bool Rotate;
};

class SingletonLogFile
{
public :
  static void Initialize(const char *fileName = 0, eLevel doLevel = eLogDebug, bool display = tLogFile::defDisplay) 
  {
    const char* usefilename = fileName;
    if (usefilename == 0) 
    {
      if (tLogFile::__logFile__ == 0) 
      {
        XLogFile1(0, "Can not initialize - No logfile previously constructed");
      }
      usefilename = tLogFile::__logFile__->FileName.c_str();
    }
    tLogFile::singleton(usefilename, doLevel, 0);
    tLogFile::__logFile__->SetDisplay(display);
  }
  static void Assign(tLogFile *logFile)
  {
    if (tLogFile::__logFile__ == logFile)
      return;
    Destroy();
    tLogFile::__logFile__ = logFile;
  }

  static void Destroy(void)
  {
    if (tLogFile::__logFile__)
    {
      delete tLogFile::__logFile__;
      tLogFile::__logFile__ = 0;
    }
  }

  static void Initialize(const char *fileName, const char* doLevel, bool display = tLogFile::defDisplay) 
  {
    Initialize(fileName, eLogDebug, display);
    tLogFile::__logFile__->LogLevel(doLevel);
  }

};
