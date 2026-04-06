/**
 *  This template class only really works well with scalar type like
 *  char, short, int, long. It works with pointers as well (they
 *  are really only in essence scalars (ie. 4 byte ints). It should
 *  be noted that zero in data is not catered for as it is primarily
 *  used for zero terminated vectors like char* in c. See ByteBuffer.h
 *  for a simple bytebuffer manager that stores disparate data, like
 *  length+data+length+otherData.
 *
 *  The purpose for this class is to supply a memory allocation mechanism
 *  that will deallocate when going out of scope. It is also useful for
 *  passing in as a reference parameter for functions that need to
 *  supply variable sized data that is only known at run time.
 */

export module tbuffer;
export import <iostream>;
export import xcstring;

using namespace std;

int error(int code, std::string err)
{
	std::cout << err << std::endl;
	throw code;
}

export template <class T> struct TBuffer
{
	T* data;
	size_t size, bytelen, used;
	TBuffer(size_t insize = 512)
		: size(insize)
	{
		if (size <= 0) size = 512;
		bytelen = size * sizeof(T);
		used = 0;
		data = (T*)calloc(size, sizeof(T));
		if (data == 0)
			//throw XBUFFERXCEPT(eMemoryError);
		{
			std::string err = std::format("Memory Allocation Failure for {}", size * sizeof(T));
			error(1, err);
		}

	}

	TBuffer(const TBuffer& from)
		: size(from.size)
	{
		set(from.data);
	}

	virtual ~TBuffer()
	{
		if (data)
			free(data);
	}

	operator T* ()
	{
		return data;
	}

	virtual void clear()
	{
		used = 0;
		memset(data, 0, bytelen);
	}

	virtual void resize(const size_t minimum)
	{
		if (minimum > size)
			grow(minimum - size);
	}

	virtual void sizeto(const size_t exact)
	{
		size = exact;
		bytelen = size * sizeof(T);
		if (used > exact)
			used = exact;

		T* tmp = (T*)realloc(data, bytelen);

		if (bytelen != 0 && tmp == 0)
			//throw XBUFFERXCEPT(eMemoryError);
		{
			std::string err = std::format("Memory Allocation Failure for {}", bytelen);
			error(2, err);
		}


		data = tmp;
	}

	virtual void grow(const size_t add)
	{
		size_t newsize = size + add;
		bytelen = newsize * sizeof(T);
		T* tmp = (T*)realloc(data, bytelen);

		if (tmp == 0)
			//throw XBUFFERXCEPT(eMemoryError);
		{
			std::string err = std::format("Memory Allocation Failure for {}", bytelen);
			error(3, err);
		}

		data = tmp;

		char* b = (char*)(data + size);
		size = newsize;
		memset(b, 0, add * sizeof(T));
	}

	void set(const T inp)
	{
		T W[2];
		W[0] = inp;
		W[1] = 0;
		set(W, 1);
	}

	virtual void set(const T* inp, const size_t insize = 0)
	{
		clear();
		append(inp, insize);
	}

	virtual void append(const T inp)
	{
		T W[2];
		W[0] = inp;
		W[1] = 0;
		append(W, 1);
	}

	virtual void append(const T* inp, size_t insize = 0)
	{
		// If no size given count non zero elements for input size
		if (insize == 0)
			while (inp[insize] != 0)
				insize++;

		for (; (used < size) && (data[used] != 0); used++)
			;

		// check if enough space to append data
		size_t left = size - used;
		while (left < insize + 1)
		{
			left += size;
			grow(size);
		}

		// Append to end moving endpoint
		memcpy(data + used, inp, insize * sizeof(T));
		used += insize;
	}

	virtual size_t toMallocedCharPointer(char*& dest)
	{
		if (size <= 0)
		{
			dest = 0;
			return 0;
		}

		dest = (char*)malloc(used + 1);

		if (!dest)
			//throw XBUFFERXCEPT(eMemoryError);
		{
			std::string err = std::format("Memory Allocation Failure for {}", used + 1);
			error(4, err);
		}

		memcpy(dest, data, used);
		dest[used] = 0;

		return used;
	}

};

export typedef TBuffer<char> TBChar;

static char* _amp;
static char* _lt;
static char* _gt;
static char* _quot;
static char* _apos;

export struct TBAmp : public TBChar
{
	TBAmp(size_t insize = 512) : TBChar(insize)
	{
		if (_amp == 0)
		{
			_amp = strdup("&amp;");
			_lt = strdup("&lt;");
			_gt = strdup("&gt;");
			_quot = strdup("&quot;");
			_apos = strdup("&apos;");
		}
	}

	char* encode(char inp, char* ch)
	{
		ch[0] = inp; ch[1] = 0;
		switch (ch[0])
		{
		case '&': return _amp;
		case '<': return _lt;
		case '>': return _gt;
		case '\"': return _quot;
		case '\'': return _apos;
		}
		return ch;
	}

	size_t neededSize(char inp)
	{
		char work[32];
		return strlen(encode(inp, work));
	}

	void ampappend(const char* inp)
	{
		size_t insize = 0, extra = 0;
		while (inp[insize] != 0)
		{
			extra += neededSize(inp[insize]) - 1;
			insize++;
		}

		size_t left = 0;
		size_t pos, i;

		for (pos = 0; pos < size; pos++)
			if (data[pos] == 0)
			{
				left = size - pos;
				break;
			}

		while (left < insize + extra + 1)
		{
			left += size;
			grow(size);
		}

		for (i = 0; i < insize; i++)
		{
			char work[32];
			char* ch = encode(inp[i], work);
			strcpy(data + pos, ch);
			pos += strlen(ch);
		}
	}

	char* encodeElem(char inp, char* ch)
	{
		ch[0] = inp; ch[1] = 0;
		switch (ch[0])
		{
		case '&': return _amp;
		case '<': return _lt;
		case '>': return _gt;
		}
		return ch;
	}

	size_t neededSizeElem(char inp)
	{
		char work[32];
		return strlen(encodeElem(inp, work));
	}

	void ampappendElem(const char* inp)
	{
		size_t insize = 0, extra = 0;
		while (inp[insize] != 0)
		{
			extra += neededSize(inp[insize]) - 1;
			insize++;
		}

		size_t left = 0;
		size_t pos, i;

		for (pos = 0; pos < size; pos++)
			if (data[pos] == 0)
			{
				left = size - pos;
				break;
			}

		while (left < insize + extra + 1)
		{
			left += size;
			grow(size);
		}

		for (i = 0; i < insize; i++)
		{
			char work[32];
			char* ch = encodeElem(inp[i], work);
			strcpy(data + pos, ch);
			pos += strlen(ch);
		}
	}
};

