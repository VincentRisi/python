export module xcstring;
import machine;
import <string.h>;
import <cctype>;

/// The xcstring module provides a collection of string manipulation functions that operate on C-style strings (null-terminated character arrays).
// These functions include:
// - `strltrim`: Removes leading whitespace characters (spaces and tabs) from a string.
// - `strcpad`: Pads a string to a specified field length with a given character, centering the original string within the padded result.
// - `strlpad`: Pads a string to a specified field length with a given character, aligning the original string to the right.
// - `strrpad`: Pads a string to a specified field length with a given character, aligning the original string to the left.
// - `tolower_stricmp`: Compares two strings in a case-insensitive manner, converting characters to lowercase before comparison.
// - `tolower_strnicmp`: Compares two strings in a case-insensitive manner for a specified number of characters.
// - `stricmp`: A wrapper around `tolower_stricmp` for case-insensitive string comparison.
// - `strnicmp`: A wrapper around `tolower_strnicmp` for case-insensitive string comparison of a specified number of characters.
// - `streq`: Checks if two strings are equal using a case-sensitive comparison.
// - `strieq`: Checks if two strings are equal using a case-insensitive comparison.
// - `strrtrim`: Removes trailing whitespace characters (spaces and tabs) from a string.
// - `strtrim`: Removes both leading and trailing whitespace characters from a string.
// - `strupr`: Converts all characters in a string to uppercase.
// - `strlwr`: Converts all characters in a string to lowercase.
// - `strncpyz`: A safe version of `strncpy` that ensures the destination string is null-terminated.

export char* strltrim(char* s)
{
	char* t = s;
	while (*t == ' ' || *t == '\t')
		t++;
	if (t != s)
		strcpy(s, t);
	return s;
}

export char* strcpad(char* s, const int fldlen, const char padchar)
{
	int len = strlen(s), len1, len2;
	if (len < fldlen)
	{
		len1 = (fldlen - len) / 2;
		len2 = fldlen - len - len1;
		memmove(s + len1, s, len);
		memset(s, padchar, len1);
		memset(s + fldlen - len2, padchar, len2);
	}
	return s;
}

export char* strlpad(char* s, const int fldlen, const char padchar)
{
	int len = strlen(s);
	if (len < fldlen)
	{
		memmove(s + fldlen - len, s, len);
		memset(s, padchar, fldlen - len);
	}
	return s;
}

export char* strrpad(char* s, const int fldlen, const char padchar)
{
	int len = strlen(s);
	while (len < fldlen)
		s[len++] = padchar;
	s[fldlen] = 0;
	return s;
}

export int tolower_stricmp(const char* a, const char* b)
{
	int n;
	if (a == 0 || b == 0)
	{
		if (a == b) return 0;
		if (a == 0) return -1;
		return 1;
	}
	for (; ; a++, b++)
	{
		n = tolower((unsigned char)*a) - tolower((unsigned char)*b);
		if (n || !*a)
			break;
	}
	return n;
}

export int tolower_strnicmp(const char* a, const char* b, int n)
{
	int i, ret;
	if (a == 0 || b == 0)
	{
		if (a == b) return 0;
		if (a == 0) return -1;
		return 1;
	}

	for (i = 0; i < (int)n; i++)
	{
		ret = tolower((unsigned char)*a) - tolower((unsigned char)*b);
		if (ret || !*a)
			break;
		a++;
		b++;
	}
	return ret;
}

export int stricmp(const char* a, const char* b)
{
	return tolower_stricmp(a, b);
}

export int strnicmp(const char* a, const char* b, int n)
{
	return tolower_strnicmp(a, b, n);
}

export bool streq(const char* s, const char* t)
{
	return (strcmp(s, t) == 0);
}

export bool strieq(const char* s, const char* t)
{
	return (stricmp(s, t) == 0);
}

export char* strrtrim(char* s)
{
	int len = strlen(s);
	while (len && (s[len - 1] == ' ' || s[len - 1] == '\t'))
		s[--len] = 0;
	return s;
}

export char* strtrim(char *s)
{
  return strltrim(strrtrim(s));
}

export char* strupr(char* s)
{
	char* t = s;
	while (*t)
	{
		*t = toupper(*t);
		t++;
	}
	return s;
}

export char* strlwr(char* s)
{
	char* t = s;
	while (*t)
	{
		*t = tolower(*t);
		t++;
	}
	return s;
}

export char *strncpyz(char *dest, const char *src, int n)
{
   strncpy(dest, src, n);
   dest[n] = 0;
   return dest;
}
