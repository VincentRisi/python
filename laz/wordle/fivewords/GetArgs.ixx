export module GetArgs;

#include "addlist.h"
#include <cstring>

export enum as_type { INTEGER, BOOLEAN, CHARACTER, STRING };
export struct GetArg
{
    char  arg;              // command line switch
    as_type type;           // variable type
    void  *variable;        // pointer to variable
    const char *usage;     // pointer to error message
    GetArg (char arg, int *variable, const char* usage)
    {
      this->arg = arg;
      this->type = INTEGER;
      this->variable = variable;
      this->usage = usage;
    };
    GetArg(char arg, bool* variable, const char* usage)
    {
      this->arg = arg;
      this->type = BOOLEAN;
      this->variable = variable;
      this->usage = usage;
    };
    GetArg(char arg, char* variable, const char* usage)
    {
      this->arg = arg;
      this->type = CHARACTER;
      this->variable = variable;
      this->usage = usage;
    };
    GetArg(char arg, const char** variable, const char* usage)
    {
      this->arg = arg;
      this->type = STRING;
      this->variable = variable;
      this->usage = usage;
    };
};

export typedef TAddList<GetArg, int> GetArgList;

export char getargs_switch_char = '-';
export bool getargs_passthru = false;

static int stoi(char **instr)
{
  int num = 0;
  char *str;
  int sign = 1;

  str = *instr;
  while (*str == ' ' || *str == '\t' || *str == '\n')
    str++;
  if (*str == '-')
  {
    sign = -1;
    str++;
  }
  if (*str == '0')
  {
    ++str;
    if (*str == 'x' || *str == 'X')
    {
      str++;
      while (('0' <= *str && *str <= '9')
      ||   ('a' <= *str && *str <= 'f')
      ||   ('A' <= *str && *str <= 'F'))
      {
        num *= 16;
        num += ('0' <= *str && *str <= '9')
           ? *str - '0'
           : toupper(*str) - 'A' + 10;
        str++;
      }
    }
    else
    {
      while ('0' <= *str && *str <= '7')
      {
        num *= 8;
        num += *str++ - '0';
      }
    }
  }
  else
  {
    while ('0' <= *str && *str <= '9')
    {
      num *= 10;
      num += *str++ - '0';
    }
  }
  *instr = str;
  return num * sign;
}

export int getArgs(int argc, char **argv, GetArgList& argList)
{
  int nargc;
  char **nargv, *p;

  nargc = 1;
  for (nargv = ++argv;  --argc > 0;  argv++)
  {
    if (**argv != getargs_switch_char)
    {
      *nargv++ = *argv;
      nargc++;
    }
    else
    {
      p = (*argv) + 1;
      while (*p)
      {
        if ((argp = findarg(*p, tabp, tabsize))!=0)
          p = setarg(argp, p);
        else if (getargs_passthru)
        {
          *nargv++ = *argv;
          nargc++;
          break;
        }
        else
        {
          prUsage(tabp, tabsize);
#if defined(_WIN32) || defined(_WIN64)
          return -1;
#else
          exit(1);
#endif
        }
      }
    }
  }
  return nargc;
}

