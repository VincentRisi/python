#include <cstdio>
import splits;
import getargs;
#include "aaxlist.h" 

static const char* testFile = "";
static const char* pipeFile = "";

void get_args(int& argc, char** argv)
{
	static GetArgList argList;
	TGetArg arg_tester('t', "tester", &testFile, "Test file");
	TGetArg arg_piper('p', "piper", &pipeFile, "Pipe Test file");
	argList.add(arg_tester);
	argList.add(arg_piper);
	argc = getArgs(argc, argv, argList);
	if (argc == -1)
	{
		printUsage(argList, stdout);
		fflush(stdout);
	}
}

int first_test();
int second_test();
int third_test();
int fourth_test();

enum TestOneFields { Username, Identifier, Password, RecoveryCode, FirstName, LastName, Department, Location, noof };

int main(int argc, char** argv)
{
	int result = 0;
	get_args(argc, argv);
	if (argc == -1) return 1;
	result = first_test() | second_test() | third_test() | fourth_test();
	return result;
}

int first_test()
{
	bool header = true;
	int result = 0;
	FILE* fp = fopen(testFile, "r");
	while (fp && !feof(fp))
	{
		char line[1024];
		if (fgets(line, sizeof(line), fp))
		{
			Splits* data;
			splits_init(&data, noof);
			if (splits_read(data, line, ','))
			{
				printf("Error reading line: %s\n", line);
				result = 1;
				break;
			}
			if (header)
			{
				printf("Header: ");
				for (int i = 0; i < data->no_flds; i++)
					printf("%s ", data->flds[i]);
				printf("\n");
				header = false;
			}
			else
			{
				printf("Data: ");
				for (int i = 0; i < data->no_flds; i++)
					printf("%s ", data->flds[i]);
				printf("\n");
			}
		}
	}
	if (fp) fclose(fp);
	return result;
}

int second_test()
{
	bool header = true;
	int result = 0;
	FILE* fp = fopen(testFile, "r");
	while (fp && !feof(fp))
	{
		char line[1024];
		if (fgets(line, sizeof(line), fp))
		{
			Splits* data;
			splits_init(&data, noof);
			if (splits_read(data, line, ','))
			{
				printf("Error reading line: %s\n", line);
				result = 1;
				break;
			}
			if (header)
			{
				if (strcmp(data->flds[Username], "Username") != 0
					|| strcmp(data->flds[Identifier], "Identifier") != 0
					|| strcmp(data->flds[Password], "Password") != 0
					|| strcmp(data->flds[RecoveryCode], "RecoveryCode") != 0
					|| strcmp(data->flds[FirstName], "FirstName") != 0
					|| strcmp(data->flds[LastName], "LastName") != 0
					|| strcmp(data->flds[Department], "Department") != 0
					|| strcmp(data->flds[Location], "Location") != 0)
				{
					printf("Header mismatch: %s\n", line);
					result = 1;
					break;
				}
				printf("Header matches expected values.\n\n");
				header = false;
				continue;
			}
			printf("User: %s\tId: %s\tName: %s %s\n", data->flds[Username], data->flds[Identifier], data->flds[FirstName], data->flds[LastName]);
		}
	}
	if (fp) fclose(fp);
	return result;
}

int third_test()
{
	bool header = true;
	int result = 0;
	FILE* fp = fopen(testFile, "r");
	while (fp && !feof(fp))
	{
		char line[1024];
		if (fgets(line, sizeof(line), fp))
		{
			Splitter splitter(noof);
			if (splitter.read(line, ','))
			{
				printf("Error reading line: %s\n", line);
				result = 1;
				break;
			}
			char** flds = splitter.flds();
			if (header)
			{
				if (strcmp(flds[Username], "Username") != 0
					|| strcmp(flds[Identifier], "Identifier") != 0
					|| strcmp(flds[Password], "Password") != 0
					|| strcmp(flds[RecoveryCode], "RecoveryCode") != 0
					|| strcmp(flds[FirstName], "FirstName") != 0
					|| strcmp(flds[LastName], "LastName") != 0
					|| strcmp(flds[Department], "Department") != 0
					|| strcmp(flds[Location], "Location") != 0)
				{
					printf("Header mismatch: %s\n", line);
					result = 1;
					break;
				}
				printf("Header matches expected values.\n\n");
				header = false;
				continue;
			}
			printf("User: %s\tId: %s\tName: %s %s\n", flds[Username], flds[Identifier], flds[FirstName], flds[LastName]);
		}
	}
	if (fp) fclose(fp);
	return result;
}

int fourth_test()
{
	bool header = true;
	int result = 0;
	FILE* fp = fopen(pipeFile, "r");
	while (fp && !feof(fp))
	{
		char line[4096];
		if (fgets(line, sizeof(line), fp))
		{
			Splitter splitter(BookFieldsCount);
			if (splitter.read(line, '|'))
			{
				printf("Error reading line: %s\n", line);
				result = 1;
				break;
			}
			char** flds = splitter.flds();
			if (header) 
			{
				printf("Header: ");
				for (int i = 0; i < splitter.no_flds(); i++)
					printf("%s ", flds[i]);
				printf("\n");
				header = false;
				continue;
			}
			printf("Album: %s\tAuthor: %s\t%s\n", flds[album], flds[author], flds[comment]);
		}
	}
	if (fp) fclose(fp);
	return result;
}
