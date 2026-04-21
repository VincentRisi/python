export module encoders;
import machine;

// The code from base64.cpp and base64.h which was used to derive this module

// Copyright (C) 2004-2008 René Nyffenegger

// This source code is provided 'as-is', without any express or implied
// warranty. In no event will the author be held liable for any damages
// arising from the use of this software.

// Permission is granted to anyone to use this software for any purpose,
// including commercial applications, and to alter it and redistribute it
// freely, subject to the following restrictions:

// 1. The origin of this source code must not be misrepresented; you must not
//    claim that you wrote the original source code. If you use this source code
//    in a product, an acknowledgment in the product documentation would be
//    appreciated but is not required.

// 2. Altered source versions must be plainly marked as such, and must not be
//    misrepresented as being the original source code.

// 3. This notice may not be removed or altered from any source distribution.

// René Nyffenegger rene.nyffenegger@adp-gmbh.ch

// Adding code for Three Primary Types of Base64 Encoding:

// Basic: The standard algorithm that maps 6-bit segments to a 64-character 
// table (A-Z, a-z, 0-9, +, /). It uses + and / and may include = padding. 

// URL-Safe: Specifically designed to be used in URLs and filenames. 
// It replaces the + with - and / with _, and generally skips padding characters. 

// MIME: Used in email formatting, it adheres to specific 
// line length limitations (usually 76 characters) and uses the same characters as basic. 

import <exception>;
import <iostream>;
import <format>;
import tbuffer;

using namespace std;

const char* basic = "+/";
const char* url_safe = "-_";
const char* fill = "=";

static const std::string base64_alphanum_chars =
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"abcdefghijklmnopqrstuvwxyz"
"0123456789";

enum base64_type { Basic, URL_Safe, Mime };

#include <cctype>
static inline bool is_base64(unsigned char c)
{
	return (isalnum(c) || (c == '+') || (c == '/') || (c == '-') || (c == '_'));
}

export std::string base64_encode(unsigned char const* bytes_to_encode, unsigned int in_len, base64_type type = Basic, bool use_padding = true)
{
	std::string ret;
	int i = 0;
	int j = 0;
	int so_far = 0;
	unsigned char char_array_3[3];
	unsigned char char_array_4[4];
	std::string base64_chars = base64_alphanum_chars;
	switch (type)
	{
	case Basic:
	case Mime:
		base64_chars += basic;
		break;
	case URL_Safe:
		base64_chars += url_safe;
		use_padding = false;
		break;
	default:
		base64_chars += basic;
		break;
	}
	while (in_len--)
	{
		char_array_3[i++] = *(bytes_to_encode++);
		if (i == 3)
		{
			char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
			char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
			char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
			char_array_4[3] = char_array_3[2] & 0x3f;
			for (i = 0; (i < 4); i++)
				ret += base64_chars[char_array_4[i]];
			i = 0;
		}
	}
	if (i)
	{
		for (j = i; j < 3; j++)
			char_array_3[j] = '\0';
		char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
		char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
		char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
		char_array_4[3] = char_array_3[2] & 0x3f;
		for (j = 0; (j < i + 1); j++)
		{
			so_far++;
			ret += base64_chars[char_array_4[j]];
			if (type == Mime)
			{
				if (so_far % 76 == 0)
					ret += '\n';
			}
		}
		if (use_padding == true)
			while ((i++ < 3))
				ret += '=';
	}
	return ret;
}

export std::string base64_decode(std::string const& encoded_string, base64_type type = Basic)
{
	int in_len = encoded_string.size();
	int i = 0;
	int j = 0;
	int in_ = 0;
	unsigned char char_array_4[4], char_array_3[3];
	std::string base64_chars = base64_alphanum_chars;
	switch (type)
	{
	case Basic:
	case Mime:
		base64_chars += basic;
		break;
	case URL_Safe:
		base64_chars += url_safe;
		break;
	default:
		base64_chars += basic;
		break;
	}
	std::string ret;
	while (in_len-- && (encoded_string[in_] != '=') && (encoded_string[in_] != '\n') && is_base64(encoded_string[in_]))
	{
		char_array_4[i++] = encoded_string[in_]; in_++;
		if (i == 4) {
			for (i = 0; i < 4; i++)
				char_array_4[i] = (unsigned char)base64_chars.find(char_array_4[i]);
			char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
			char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
			char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];
			for (i = 0; (i < 3); i++)
				ret += char_array_3[i];
			i = 0;
		}
	}
	if (i)
	{
		for (j = i; j < 4; j++)
			char_array_4[j] = 0;
		for (j = 0; j < 4; j++)
			char_array_4[j] = (unsigned char)base64_chars.find(char_array_4[j]);
		char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
		char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
		char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];
		for (j = 0; (j < i - 1); j++) ret += char_array_3[j];
	}
	return ret;
}


// Z85 would possibly be best for json based comms.

// Four bytes can represent 2^32 = 4,294,967,296 possible values.
// Five radix - 85 digits provide 85^5 = 4,437,053,125 possible values, 
// enough to provide for a unique representation for each possible 32 - bit value.
// Because five radix - 84 digits only provide 84^5 = 4,182,119,424 representable values,
// 85 is the minimum possible integral base that will represent four bytes in five characters,
// hence its choice.

// When encoding, each group of 4 bytes is taken as a 32 - bit binary number, 
// most significant byte first(Ascii85 uses a big - endian convention).
// This is converted, by repeatedly dividing by 85 and taking the remainder, 
// into 5 radix - 85 digits.Then each digit(again, most significant first) is 
// encoded as an ASCII printable character by adding 33 to it, giving the
// ASCII characters 33 ("!") through 117 ("u").

// Because all - zero data is quite common, an exception is made for the sake
// of data compression, and an all - zero group is encoded as a single
// character "z" instead of "!!!!!".

// Also a group of 4 spaces is encoded as a single character "y" instead of 
// some common 5 bytes, which is moot.

// A way to deal with the last 4 bytes being being padded with 1 2 or 3 extra zero bytes
// is to write the encoded with a extra starting '0' '1' '2' or '3' to indicate
// number of zeroes being padded. Then for decoding do not forget to skip this extra
// byte.

export void ascii85_encode(TBUChar& buff, unsigned char* input, int data_size)
{
	buff.clear();
	for (int i = 0; i < data_size; i += 4)
	{
		const char* p = (char*)(input + i);
		if (data_size >= 4 && strncmp(p, "    ", 4) == 0)
		{
			buff.append((unsigned char*)"y");
			continue;
		}
		const unsigned int* v = (unsigned int*)(input + i);
		if (data_size >= 4 && *v == 0)
		{
			buff.append((unsigned char*)"z");
			continue;
		}
		int n = i;
		unsigned int as = input[n++] << 24;
		if (n < data_size) as += input[n++] << 16;
		if (n < data_size) as += input[n++] << 8;
		if (n < data_size) as += input[n++];
		unsigned char outwork[5];
		outwork[4] = (as % 85) + 33; as /= 85;
		outwork[3] = (as % 85) + 33; as /= 85;
		outwork[2] = (as % 85) + 33; as /= 85;
		outwork[1] = (as % 85) + 33; as /= 85;
		outwork[0] = as + 33;
		buff.append(outwork, 5);
	}
}

export void ascii85_decode(TBUChar& buff, unsigned char* input, int data_size)
{
	buff.clear();
	for (int i = 0; i < data_size; i++)
	{
		const char* p = (char*)(input + i);
		unsigned char outwork[4];
		if (*p == 'z')
		{
			memset(outwork, 0, sizeof(outwork));
			buff.append(outwork, 4);
			continue;
		}
		if (*p == 'y')
		{
			memset(outwork, ' ', sizeof(outwork));
			buff.append(outwork, 4);
			continue;
		}
		unsigned char inwork[5];
		memset(inwork, 0, sizeof(inwork));
		int n = i;
		i += 4;
		inwork[0] = input[n++] - 33;
		if (n < data_size) inwork[1] = input[n++] - 33;
		if (n < data_size) inwork[2] = input[n++] - 33;
		if (n < data_size) inwork[3] = input[n++] - 33;
		if (n < data_size) inwork[4] = input[n++] - 33;
		unsigned int as = (((((((inwork[0] * 85) + inwork[1]) * 85) + inwork[2]) * 85) + inwork[3]) * 85) + inwork[4];
		outwork[0] = (as & 0xFF000000) >> 24;
		outwork[1] = (as & 0x00FF0000) >> 16;
		outwork[2] = (as & 0x0000FF00) >> 8;
		outwork[3] = (as & 0x000000FF);
		buff.append(outwork, 4);
	}
}

// Z85, the ZeroMQ base-85 encoding algorithm, is a string-safe variant of base85.
// By avoiding the double-quote, single-quote, and backslash characters,
// Z85-encoded data can be better embedded in command-line interpreter strings.
// Z85 uses the characters 0..9 a..z A..Z . - : + = ^ ! / * ? & < > ( ) [ ] { } @ % $ #
// See ascii85 note above used for discussion why base-85.

// A way to deal with the last 4 bytes being being padded with 1 2 or 3 extra zero bytes
// is to write the encoded with a extra starting '0' '1' '2' or '3' to indicate
// number of zeroes being padded. Then for decoding do not forget to skip this extra
// byte.

// Z85 would possibly be best for json based comms.


const char* z85code = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#";

export void z85_encode(TBUChar& buff, unsigned char* input, int data_size)
{
	buff.clear();
	for (int i = 0; i < data_size; i += 4)
	{
		int n = i;
		unsigned int as = input[n++] << 24;
		if (n < data_size) as += input[n++] << 16;
		if (n < data_size) as += input[n++] << 8;
		if (n < data_size) as += input[n++];
		unsigned char outwork[5];
		outwork[4] = z85code[as % 85]; as /= 85;
		outwork[3] = z85code[as % 85]; as /= 85;
		outwork[2] = z85code[as % 85]; as /= 85;
		outwork[1] = z85code[as % 85]; as /= 85;
		outwork[0] = z85code[as];
		buff.append(outwork, 5);
	}
}

export void z85_decode(TBUChar& buff, unsigned char* input, int data_size)
{
	buff.clear();
	char k[2] = ".";
	for (int i = 0; i < data_size; i += 5)
	{
		unsigned char inwork[5] = { 0, 0, 0, 0, 0 };
		int n = i;
		k[0] = input[n++]; inwork[0] = (unsigned char)strcspn(z85code, k);
		if (n < data_size) k[0] = input[n++]; inwork[1] = (unsigned char)strcspn(z85code, k);
		if (n < data_size) k[0] = input[n++]; inwork[2] = (unsigned char)strcspn(z85code, k);
		if (n < data_size) k[0] = input[n++]; inwork[3] = (unsigned char)strcspn(z85code, k);
		if (n < data_size) k[0] = input[n++]; inwork[4] = (unsigned char)strcspn(z85code, k);
		unsigned int as = (((((((inwork[0] * 85) + inwork[1]) * 85) + inwork[2]) * 85) + inwork[3]) * 85) + inwork[4];
		unsigned char outwork[4];
		outwork[0] = (as & 0xFF000000) >> 24;
		outwork[1] = (as & 0x00FF0000) >> 16;
		outwork[2] = (as & 0x0000FF00) >> 8;
		outwork[3] = (as & 0x000000FF);
		buff.append(outwork, 4);
	}
}

typedef unsigned int uint;
typedef unsigned short ushort;
typedef unsigned char* puchar;
typedef unsigned char uchar;

export uint In3Out4(puchar input, uint inlen, puchar output, uint outlen)
{
	uchar in[3];
	uint i, o, n;
	for (i = o = 0; i < inlen; i += 3)
	{
		n = inlen - i;
		memset(in, 0, 3);
		memcpy(in, input + i, n > 3 ? 3 : n);
		output[o++] = (in[0] >> 2) + 32;
		if (o >= outlen) break;
		output[o++] = (((in[0] & 0x03) << 4) | (in[1] >> 4)) + 32;
		if (o >= outlen) break;
		output[o++] = (((in[1] & 0x0F) << 2) | (in[2] >> 6)) + 32;
		if (o >= outlen) break;
		output[o++] = (in[2] & 0x3F) + 32;
		if (o >= outlen) break;
	}
	return o;
}

export uint In4Out3(puchar input, uint inlen, puchar output, uint outlen)
{
	uchar in[4];
	uint i, o, n;
	for (i = o = 0; i < inlen; i += 4)
	{
		n = inlen - i;
		memset(in, 0, 4);
		memcpy(in, input + i, n > 4 ? 4 : n);
		in[0] -= 32;
		in[1] -= 32;
		output[o] = ((in[0] & 0x3F) << 2) | ((in[1] & 0x30) >> 4);
		if (++o >= outlen) break;
		in[2] -= 32;
		output[o] = ((in[1] & 0x0F) << 4) | ((in[2] & 0x3c) >> 2);
		if (++o >= outlen) break;
		in[3] -= 32;
		output[o] = ((in[2] & 0x03) << 6) | (in[3] & 0x3F);
		if (++o >= outlen) break;
	}
	return o;
}

export uint Encode12To8(puchar input, puchar output)
{
	static union
	{
		char c[6];
		ushort u[3];
	} un;
	char work[5];
	work[4] = 0;
	memcpy(work, input, 4);
	un.u[0] = (ushort)atoi(work);
	memcpy(work, input + 4, 4);
	un.u[1] = (ushort)atoi(work);
	memcpy(work, input + 8, 4);
	un.u[2] = (ushort)atoi(work);
	In3Out4((puchar)un.c, 6, output, 8);
	return 0;
}

export uint Decode8To12(puchar input, puchar output)

{
	static union
	{
		char c[6];
		ushort u[3];
	} un;
	char work[6];
	In4Out3(input, 8, (puchar)un.c, 6);
	sprintf(work, "%04u", un.u[0]);
	memcpy(output, work, 4);
	sprintf(work, "%04u", un.u[1]);
	memcpy(output + 4, work, 4);
	sprintf(work, "%04u", un.u[2]);
	memcpy(output + 8, work, 4);
	return 0;
}
