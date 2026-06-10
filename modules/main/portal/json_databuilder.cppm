#include "json/json.h"
#include <string.h>
#include <cstdio>
#include <sstream>
#include <string>
#include <json/value.h>
#include <json/writer.h>

export module json_databuilder;
import databuilder;
import xcstring;
import encoders;

using namespace std;
using namespace Json;

export class DataBuilderJson : public DataBuilder
{
	int _count;
	string _name;
	Value record;
	char sn_buff[512];
public:
	DataBuilderJson()
	{
		_count = 0;
		memset(sn_buff, 0, sizeof(sn_buff));
	}

  virtual ~DataBuilderJson()
  {
    
  }
	void setRecord(const char* data)
	{
		clear();
		stringstream sstr(data);
		sstr >> record;
	}

	void setValue(Value inValue)
	{
		clear();
		record = inValue;
	}

	Value getRecord(string& data)
	{
		StreamWriterBuilder swb;
		data = writeString(swb, record);
		return record;
	}

  void clear() 
  { 
    record.clear(); 
  }

	void count(int value)
	{
		_count = value;
	}

	void name(const char* value)
	{
		_name = value;
	}

	void add(const char* name, const int8 value)
	{
		record[name] = value;
	}

	void addByte(const char* name, const int8 value)
	{
		record[name] = value;
	}

	void addByte(const char* name, const int8* value, const size_t size)
	{

	}

	void add(const char* name, const int16   value)
	{
		record[name] = value;
	}

	void add(const char* name, const int32   value)
	{
		record[name] = value;
	}

	void add(const char* name, const int64 value)
	{
		record[name] = value;
	}

	void add(const char* name, const char* value)
	{
		record[name] = value;
	}

	void add(const char* name, const size_t len, const unsigned char* value)
	{

	}

	void add(const char* name, const double value)
	{
		record[name] = value;
	}

	void add(const char* name, const int8 value, const int16 isNull)
	{
		if (isNull == 0)
			record[name] = value;
	}

	void addByte(const char* name, const int8 value, const int16 isNull)
	{
		if (isNull == 0)
			record[name] = value;
	}

	void addByte(const char* name, const int8* value, const size_t size, const int16 isNull)
	{

	}

	void add(const char* name, const int16 value, const int16 isNull)
	{
		if (isNull == 0)
			record[name] = value;
	}

	void add(const char* name, const int32 value, const int16 isNull)
	{
		if (isNull == 0)
			record[name] = value;
	}

	void add(const char* name, const int64 value, const int16 isNull)
	{
		if (isNull == 0)
			record[name] = value;
	}

	void add(const char* name, const char* value, const int16 isNull)
	{
		if (isNull == 0)
			record[name] = value;
	}

	void add(const char* name, const size_t len, const unsigned char* value, const int16 isNull)
	{

	}

	void add(const char* name, const double  value, const int16 isNull)
	{
		if (isNull == 0)
			record[name] = value;
	}

	void set(const char* name, int8& value, const size_t size)
	{
		int64 work = record[name].asInt64();
		if (work > -127 && work < 128)
			value = (int8)work;
		else
		{
			snprintf(sn_buff, sizeof(sn_buff), "Value %s exceeds range for int8 %d.", name, (int)work);
			throwRuntimeError(sn_buff);
		}
	}

	void setByte(const char* name, int8& value, const size_t size)
	{
		int64 work = record[name].asInt64();
		if (work > -127 && work < 128)
			value = (int8)work;
		else
		{
			snprintf(sn_buff, sizeof(sn_buff), "Value %s exceeds range for int8 %d.", name, (int)work);
			throwRuntimeError(sn_buff);
		}
	}

	void setByte(const char* name, int8* value, const size_t size)
	{
		string work = record[name].asString();
		size_t from_size = work.length();
		if (from_size < size)
			strncpyz((char*)value, work.c_str(), from_size);
		else
		{
			snprintf(sn_buff, sizeof(sn_buff), "Value %s sizeof string %d exceeds allowed size %d.", name, from_size, size);
			throwRuntimeError(sn_buff);
		}
	}

	void set(const char* name, int16& value, const size_t size)
	{
		int64 work = record[name].asInt64();
		if (work >= -32768 && work <= 32768)
			value = (int16)work;
		else
		{
			snprintf(sn_buff, sizeof(sn_buff), "Value %s exceeds range for int16 %d.", name, (int)work);
			throwRuntimeError(sn_buff);
		}
	}

	void set(const char* name, int32& value, const size_t size)
	{
		int64 work = record[name].asInt64();
		if (work >= -2147483647 && work <= 2147483648)
			value = (int32)work;
		else
		{
			snprintf(sn_buff, sizeof(sn_buff), "Value %s exceeds range for int32 %d.", name, (int)work);
			throwRuntimeError(sn_buff);
		}
	}

	void set(const char* name, int64& value, const size_t size)
	{
		value = record[name].asInt64();
	}

	void set(const char* name, char* value, const size_t size)
	{
		string work = record[name].asString();
		size_t from_size = work.length();
		if (from_size < size)
			strncpyz(value, work.c_str(), from_size);
		else
		{
			snprintf(sn_buff, sizeof(sn_buff), "Value %s sizeof string %d exceeds allowed size %d.", name, (int)from_size, (int)size);
			throwRuntimeError(sn_buff);
		}
	}

	void set(const char* name, int& len, unsigned char* value, const size_t size)
	{
		string from4 = record[name].asString();
		string as3 = base64_decode(from4);
		size_t as3_size = as3.length();
		if (as3_size + 4 <= size)
		{
			len = as3_size + 4;
			memset(value, 0, size);
			*(int*)value = as3_size;
			memcpy((char*)value + 4, (void*)as3.c_str(), as3_size);
		}
		else
		{
			snprintf(sn_buff, sizeof(sn_buff), "Value %s sizeof string %d exceeds allowed size %d.", name, (int)as3_size, (int)size);
			throwRuntimeError(sn_buff);
		}
	}

	void set(const char* name, double& value, const size_t size)
	{
		value = record[name].asDouble();
	}

	void set(const char* name, int8& value, const size_t size, int16& null)
	{
		if (null == 0) set(name, value, size);
	}

	void setByte(const char* name, int8& value, const size_t size, int16& null)
	{
		if (null == 0) set(name, value, size);
	}

	void setByte(const char* name, int8* value, const size_t size, int16& null)
	{
		if (null == 0) setByte(name, value, size);
	}

	void set(const char* name, int16& value, const size_t size, int16& null)
	{
		if (null == 0) set(name, value, size);
	}

	void set(const char* name, int32& value, const size_t size, int16& null)
	{
		if (null == 0) set(name, value, size);
	}

	void set(const char* name, int64& value, const size_t size, int16& null)
	{
		if (null == 0) set(name, value, size);
	}

	void set(const char* name, char* value, const size_t size, int16& null)
	{
		if (null == 0) set(name, value, size);
	}

	void set(const char* name, int& len, unsigned char* value, const size_t size, int16& null)
	{
		if (null == 0) set(name, len, value, size);
	}

	void set(const char* name, double& value, const size_t size, int16& null)
	{
		if (null == 0) set(name, value, size);
	}

};