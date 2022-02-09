#ifndef _DBAPI_SHELL_H_
#define _DBAPI_SHELL_H_
#include "machine.h"
using namespace std;

#ifdef _DEBUG
#undef _DEBUG
#endif
#include "Python.h"
#include "tbuffer.h"
#include "logfile.h"

class DBApiShell
{
    wchar_t *program;
public:
    DBApiShell(tLogFile* logFile, const char* name, const char* configfile, const char* prefix);
    ~DBApiShell();
    static char* modulePrefix;
};

void runner(string methodStr, string inputStr, string &outputStr);
void PyErrorHandler(TBChar &ErrorBuf);

#endif