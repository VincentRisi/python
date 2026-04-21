#include <cstdio>
import getargs;

static const char* stringVar = "";
static bool        boolVar = false;
static int         intVar = 0;
static char        charVar = 'A';

int main(int argc, char** argv)
{
  static GetArgList argList;
  TGetArg arg_String('s', "string",  &stringVar, "String");
  TGetArg arg_Bool('b',   "boolean", &boolVar,   "Boolean");
  TGetArg arg_Int('i',    "integer", &intVar,    "Integer");
  TGetArg arg_Char('c',   "char",    &charVar,   "Char");
  argList.add(arg_String);
  argList.add(arg_Bool); 
  argList.add(arg_Int);
  argList.add(arg_Char);
  argc = getArgs(argc, argv, argList);
  if (argc == -1) printUsage(argList, stdout);
  fprintf(stdout, "done\n");
  fflush(stdout);
}
