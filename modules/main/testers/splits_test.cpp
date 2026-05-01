#include <cstdio>
import splits;
import getargs;

static const char* testFile = "";

void get_args(int& argc, char** argv)
{
  static GetArgList argList;
  TGetArg arg_tester('t', "tester",  &testFile, "Test file");
  argList.add(arg_tester);
  argc = getArgs(argc, argv, argList);
  if (argc == -1) 
  { 
    printUsage(argList, stdout);
    fflush(stdout); 
  }
}

int main(int argc, char** argv)
{
  get_args(argc, argv);
	if (argc == -1) return 1;
  return 0;
}