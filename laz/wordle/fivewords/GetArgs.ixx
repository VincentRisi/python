export module GetArgs;

#include "addlist.h"
#include <cstring>

export enum as_type { BOOLEAN, STRING, INTEGER };
export struct GetArg
{
    char  arg;              // command line switch
    as_type type;           // variable type
    void  *variable;        // pointer to variable
    const char *errmsg;     // pointer to error message
    GetArg (char arg, as_type type, void* variable, const char* errmsg)
    {
      this->arg = arg;
      this->type = type;
      this->variable = variable;
      this->errmsg = errmsg;
    };
};

export typedef TAddList<GetArg, int> GetArgList;