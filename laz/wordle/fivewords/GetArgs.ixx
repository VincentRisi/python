export module GetArgs;

#include "addlist.h"
#include <cstring>

static int stoi(char** instr);

char getargs_switch_char = '-';
bool getargs_passthru = false;

export struct GetArg
{
	enum as_type { INTEGER, BOOLEAN, CHARACTER, STRING };
	char  arg;              // command line switch char
	const char* verb;       // command line switch verb
	as_type type;           // variable type
	void* variable;         // pointer to variable
	const char* usage;      // pointer to error message
	GetArg(char arg, const char* verb, int* variable, const char* usage)
	{
		this->arg = arg;
		this->verb = verb;
		this->type = INTEGER;
		this->variable = variable;
		this->usage = usage;
	};
	GetArg(char arg, const char* verb, bool* variable, const char* usage)
	{
		this->arg = arg;
		this->verb = verb;
		this->type = BOOLEAN;
		this->variable = variable;
		this->usage = usage;
	};
	GetArg(char arg, const char* verb, char* variable, const char* usage)
	{
		this->arg = arg;
		this->verb = verb;
		this->type = CHARACTER;
		this->variable = variable;
		this->usage = usage;
	};
	GetArg(char arg, const char* verb, const char** variable, const char* usage)
	{
		this->arg = arg;
		this->verb = verb;
		this->type = STRING;
		this->variable = variable;
		this->usage = usage;
	};
	void printUsage()
	{
		switch (type)
		{
		case INTEGER:
			printf("%c%c<num> %-40s [%-5d]\n", getargs_switch_char,
				arg, usage, *((int*)variable));
			break;
		case BOOLEAN:
			printf("%c%c      %-40s [%-5s]\n", getargs_switch_char,
				arg, usage, *((int*)variable) ? "TRUE" : "FALSE");
			break;
		case CHARACTER:
			printf("%c%c<c>   %-40s [%-5c]\n", getargs_switch_char,
				arg, usage, *((int*)variable));
			break;
		case STRING:
			printf("%c%c<str> %-40s [%s]\n", getargs_switch_char,
				arg, usage, *(char**)variable);
			break;
		}
	}
	void setValue(char* value)
	{
		switch (type)
		{
		case INTEGER:
			*((int*)variable) = stoi(&value);
			break;
		case BOOLEAN:
			*((int*)variable) = true;
			break;
		case CHARACTER:
			*((char*)variable) = *value;
			break;
		case STRING:
			*(char**)variable = value;
			break;
		}
	}
};

export typedef TAddList<GetArg, int> GetArgList;

void printUsage(GetArgList& argList)
{
	for (int i = 0; i < argList.getCount(); i++)
		argList[i].printUsage();
}

export int getArgs(int argc, char** argv, GetArgList& argList)
{
	int nargc;
	char** nargv, * p;
	GetArg* argp;

	nargc = 1;
	for (nargv = ++argv; --argc > 0; argv++)
	{
		if (**argv != getargs_switch_char)
		{
			*nargv++ = *argv;
			nargc++;
		}
		else
		{
			p = (*argv) + 1;
			for (int i = 0; i < argList.getCount(); i++)
			{
				if (argList[i].arg == *p)
				{
					argp = &argList[i];
					argp->setValue(p);
					break;
				}
			}
			//				while (*p)
			//				{
			//					if ((argp = findarg(*p, tabp, tabsize)) != 0)
			//						p = setarg(argp, p);
			//					else if (getargs_passthru)
			//					{
			//						*nargv++ = *argv;
			//						nargc++;
			//						break;
			//					}
			//					else
			//					{
			//						prUsage(tabp, tabsize);
			//#if defined(_WIN32) || defined(_WIN64)
			//						return -1;
			//#else
			//						exit(1);
			//#endif
			//					}
			//				}
		}
	}
	return nargc;
}

int stoi(char** instr)
{
	int num = 0;
	char* str;
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
				|| ('a' <= *str && *str <= 'f')
				|| ('A' <= *str && *str <= 'F'))
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
