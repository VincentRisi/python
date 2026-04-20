export module encoders;

// Three Primary Types of Base64 Encoding:

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

static const std::string base64_chars =
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"abcdefghijklmnopqrstuvwxyz"
"0123456789+/";

#include <ctype.h>
static inline bool is_base64(unsigned char c)
{
	return (isalnum(c) || (c == '+') || (c == '/'));
}

export std::string base64_encode(unsigned char const* bytes_to_encode, unsigned int in_len)
{
	std::string ret;
	int i = 0;
	int j = 0;
	unsigned char char_array_3[3];
	unsigned char char_array_4[4];
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
			ret += base64_chars[char_array_4[j]];
		while ((i++ < 3))
			ret += '=';
	}
	return ret;
}

export std::string base64_decode(std::string const& encoded_string) {
	int in_len = encoded_string.size();
	int i = 0;
	int j = 0;
	int in_ = 0;
	unsigned char char_array_4[4], char_array_3[3];
	std::string ret;
	while (in_len-- && (encoded_string[in_] != '=') && is_base64(encoded_string[in_])) {
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
	if (i) {
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

void ascii85_encode(TBUChar& buff, unsigned char* input, int data_size)
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
        outwork[4] = (as % 85)+33; as /= 85;
        outwork[3] = (as % 85)+33; as /= 85;
        outwork[2] = (as % 85)+33; as /= 85;
        outwork[1] = (as % 85)+33; as /= 85;
        outwork[0] = as + 33;
        buff.append(outwork, 5);
    }
}

void ascii85_decode(TBUChar& buff, unsigned char* input, int data_size)
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

const char* z85code = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#";

void z85_encode(TBUChar &buff, unsigned char *input, int data_size)
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

void z85_decode(TBUChar& buff, unsigned char* input, int data_size)
{
    buff.clear();
    char k[2] = ".";
    for (int i = 0; i < data_size; i += 5)
    {
        unsigned char inwork[5] = {0, 0, 0, 0, 0};
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
