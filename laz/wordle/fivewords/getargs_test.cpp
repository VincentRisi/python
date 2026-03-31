#include "stdio.h"
import GetArgs;

static const char* stringArg = "";
static bool        boolArg = false;
static int         intArg = 0;
static char        charArg = 'A';

int main(int argc, char** argv)
{
  static GetArgList argList;
  GetArg arg_String('s', "string",  &stringArg, "String");
  GetArg arg_Bool('b',   "boolean", &boolArg,   "Boolean");
  GetArg arg_Int('i',    "integer", &intArg,    "Integer");
  GetArg arg_Char('c',   "char",    &charArg,   "Char");
  argList.add(arg_String);
  argList.add(arg_Bool); 
  argList.add(arg_Int);
  argList.add(arg_Char);
  argc = getArgs(argc, argv, argList);
  if (argc == -1) printUsage(argList, stdout);
  fprintf(stdout, "done\n");
  fflush(stdout);
}
