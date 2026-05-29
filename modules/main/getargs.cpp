export module getargs;
import machine;
import addlist;

static int stoi(char** instr);

export char GETARGS_SWITCH_CHAR = '-';
export bool GETARGS_PASSTHRU = false;

export struct TGetArg
{
	enum as_type { INTEGER, BOOLEAN, CHARACTER, STRING };
	char  sw;               // command line switch char
	const char* verb;       // command line switch verb
	as_type type;           // variable type
	void* variable;         // pointer to variable
	const char* usage;      // pointer to error message
	TGetArg(char sw, const char* verb, int* variable, const char* usage)
	{
		this->sw = sw;
		this->verb = verb;
		this->type = INTEGER;
		this->variable = variable;
		this->usage = usage;
	};
	TGetArg(char sw, const char* verb, bool* variable, const char* usage)
	{
		this->sw = sw;
		this->verb = verb;
		this->type = BOOLEAN;
		this->variable = variable;
		this->usage = usage;
	};
	TGetArg(char sw, const char* verb, char* variable, const char* usage)
	{
		this->sw = sw;
		this->verb = verb;
		this->type = CHARACTER;
		this->variable = variable;
		this->usage = usage;
	};
	TGetArg(char sw, const char* verb, const char** variable, const char* usage)
	{
		this->sw = sw;
		this->verb = verb;
		this->type = STRING;
		this->variable = variable;
		this->usage = usage;
	};
	void printUsage(FILE* logFile)
	{
		switch (type)
		{
		case INTEGER:
			fprintf(logFile, "%c%c<num> %-40s [%-5d]\n", GETARGS_SWITCH_CHAR,
				sw, usage, *((int*)variable));
			break;
		case BOOLEAN:
			fprintf(logFile, "%c%c      %-40s [%-5s]\n", GETARGS_SWITCH_CHAR,
				sw, usage, *((int*)variable) ? "TRUE" : "FALSE");
			break;
		case CHARACTER:
			fprintf(logFile, "%c%c<c>   %-40s [%-5c]\n", GETARGS_SWITCH_CHAR,
				sw, usage, *((int*)variable));
			break;
		case STRING:
			fprintf(logFile, "%c%c<str> %-40s [%s]\n", GETARGS_SWITCH_CHAR,
				sw, usage, *(char**)variable);
			break;
		}
	}
	bool setValue(char* value, bool set_bool)
	{
		switch (type)
		{
		case INTEGER:
			*((int*)variable) = stoi(&value);
			break;
		case BOOLEAN:
			*((int*)variable) = set_bool;
			break;
		case CHARACTER:
			*((char*)variable) = *value;
			break;
		case STRING:
			*(char**)variable = value;
			break;
		}
		return type != BOOLEAN;
	}
};

export using GetArgList = TAddList<TGetArg, int>;

export void printUsage(GetArgList& argList, FILE* logFile)
{
	for (int i = 0; i < argList.getCount(); i++)
		argList[i].printUsage(logFile);
}

static int getVerb(GetArgList& argList, char* verb)
{
  for (int i = 0; i < argList.getCount(); i++)
  {
    if (strcmp(argList[i].verb, verb) == 0)
      return i;
  }
  return -1;
}

static int getSwitch(GetArgList& argList, char sw)
{
	for (int i = 0; i < argList.getCount(); i++)
	{
		if (argList[i].sw == sw)
			return i;
	}
	return -1;
}


static bool setValue(TGetArg arg, char* argv, bool set_bool)
{
	return arg.setValue(argv, set_bool);
}

export int getArgs(int argc, char* argv[], GetArgList& argList)
{
	int gap = 0;
	for (int i = 1, no = 1; i < argc;)
	{
		char* p = argv[i];
		if (strcmp(p, "--help") == 0)
		{
			argc = -1;
			break;
		}
		int n = strlen(p);
		bool set_bool = true;
		gap = 0;
		if (p[0] != GETARGS_SWITCH_CHAR)
		{
			i++;
			continue;
		}
		if (n > 2 && p[n - 1] == '-')
		{
			set_bool = false;
			p[n - 1] = 0;
		}
		if (p[1] == GETARGS_SWITCH_CHAR)
		{
			char* verb = p + 2;
			int n = getVerb(argList, verb);
			if (n == -1)
			{
				if (GETARGS_PASSTHRU) continue;
				return -1;
			}
			bool used = setValue(argList[n], argv[i + 1], set_bool);
			gap = used ? 2 : 1;
		}
		else
		{
			char sw = p[1];
			int n = getSwitch(argList, sw);
			if (n == -1)
			{
				if (GETARGS_PASSTHRU) continue;
				return -1;
			}
			gap = 1;
			if (strlen(p + 2) == 0)
			{
				if (setValue(argList[n], argv[i + 1], set_bool))
					gap++;
			}
			else setValue(argList[n], p + 2, set_bool);
		}
		argc -= gap;
		for (int j = i; j < argc; j++)
			argv[j] = argv[j + gap];
	}
	return argc;
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
