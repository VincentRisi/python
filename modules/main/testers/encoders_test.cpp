
#include <cstdio>
import getargs;
import encoders;
import logfile;
import tbuffer;

static const char* logfile_name;
static const char* binfile_name;
static int         use_size = 0;

typedef unsigned int uint;
typedef unsigned short ushort;
typedef unsigned char* puchar;
typedef unsigned char uchar;

bool compare_buffers(unsigned char* buffer1, unsigned char* buffer2, long size)
{
  for (long i = 0; i < size; i++)
  {
    if (buffer1[i] != buffer2[i])
      return false;
  }
  return true;
}

void base64_test(LogFile& log, long size, unsigned char* buffer)
{
	std::string encoded = base64_encode(buffer, size, Basic);
  log.lprintf(eLogDebug, "base64 %ld %ld %s", size, encoded.length(), encoded.c_str());
	std::string decoded = base64_decode(encoded, Basic);
	bool equal = compare_buffers(buffer, (unsigned char*)decoded.c_str(), size);
  if (!equal)
    log.lprintf(eLogError, "Decoded buffer does not match original buffer for Basic encoding");
  else
		log.lprintf(eLogInfo, "Decoded buffer matches original buffer for Basic encoding");
	encoded = base64_encode(buffer, size, Mime);
  log.lprintf(eLogDebug, "base64 %ld %ld %s", size, encoded.length(), encoded.c_str());
  decoded = base64_decode(encoded, Mime);
  equal = compare_buffers(buffer, (unsigned char*)decoded.c_str(), size);
  if (!equal)
    log.lprintf(eLogError, "Decoded buffer does not match original buffer for Mime encoding");
  else
    log.lprintf(eLogInfo, "Decoded buffer matches original buffer for Mime encoding");
  encoded = base64_encode(buffer, size, URL_Safe);
  log.lprintf(eLogDebug, "base64 %ld %ld %s", size, encoded.length(), encoded.c_str());
  decoded = base64_decode(encoded, URL_Safe);
  if (!equal)
    log.lprintf(eLogError, "Decoded buffer does not match original buffer for URL_Safe encoding");
  else
    log.lprintf(eLogInfo, "Decoded buffer matches original buffer for URL_Safe encoding");
}

void asciify_test(LogFile& log, uint insize, unsigned char* buffer, TBUChar& outbuffer)
{
  uint outsize = outbuffer.size;
  uint used = In3Out4(buffer, insize, outbuffer.data, outsize);
	log.lprintf(eLogInfo, "asciify %d %d %d %s", insize, outsize, used, outbuffer.data);
  TBUChar decoded(insize);
	In4Out3(outbuffer, used, decoded.data, insize);
  bool equal = compare_buffers(buffer, decoded, insize);
  if (!equal)
    log.lprintf(eLogError, "Decoded buffer does not match original buffer");
  else
    log.lprintf(eLogInfo, "Decoded buffer matches original buffer");
}

void ascii85_test(LogFile& log, uint insize, unsigned char* buffer, TBUChar& outbuffer)
{
	ascii85_encode(outbuffer, buffer, insize);
  log.lprintf(eLogDebug, "ascii85 %ld %ld %s", insize, outbuffer.size, outbuffer.data);
  TBUChar decoded(insize);
	ascii85_decode(decoded, (unsigned char*)outbuffer.data, outbuffer.size);
  bool equal = compare_buffers(buffer, decoded, insize);
  if (!equal)
    log.lprintf(eLogError, "Decoded buffer does not match original buffer");
  else
    log.lprintf(eLogInfo, "Decoded buffer matches original buffer");
}

void z85_test(LogFile& log, uint insize, unsigned char* buffer, TBUChar& outbuffer)
{
  z85_encode(outbuffer, buffer, insize);
  log.lprintf(eLogDebug, "z85 %ld %ld %s", insize, outbuffer.size, outbuffer.data);
  TBUChar decoded(insize);
  z85_decode(decoded, (unsigned char*)outbuffer.data, outbuffer.size);
  bool equal = compare_buffers(buffer, decoded, insize);
  if (!equal)
    log.lprintf(eLogError, "Decoded buffer does not match original buffer");
  else
    log.lprintf(eLogInfo, "Decoded buffer matches original buffer");
}

int main(int argc, char** argv)
{
  static GetArgList arg_list;
  TGetArg arg_binfile_name('b', "binfile", &binfile_name, "String");
  TGetArg arg_logfile_name('l', "logfile", &logfile_name, "String");
	TGetArg arg_use_size('s', "size", &use_size, "Integer");
  arg_list.add(arg_binfile_name);
  arg_list.add(arg_logfile_name);
  arg_list.add(arg_use_size);
  argc = getArgs(argc, argv, arg_list);
  if (argc == -1 || logfile_name == 0)
  {
    printUsage(arg_list, stdout);
    return 1;
  }
  LogFile log = LogFile(logfile_name);
  log.Log(logfile_name);
  int size = 1024;
  TBUChar buffer(size);
  if (binfile_name)
  {
    log.Log(binfile_name);
    FILE* f = fopen(binfile_name, "rb");
    fseek(f, 0, SEEK_END);
    long file_size = ftell(f);
    fseek(f, 0, SEEK_SET);
    if (use_size > 0 && use_size < file_size)
      size = use_size;
    buffer.resize(size);
	  fread(buffer, 1, size, f);
    fclose(f);
  }
  else
  {
    if (use_size > 0)
			size = use_size;
    buffer.resize(size);
    for (int i = 0; i < size; i++)
			buffer[i] = (unsigned char)(i % 256);
  }
	base64_test(log, size, buffer);
  TBUChar outbuffer((size * 4) / 3 + 16);
	asciify_test(log, size, buffer, outbuffer);
  outbuffer.resize((size * 5) / 4 + 16);
	ascii85_test(log, size, buffer, outbuffer);
  z85_test(log, size, buffer, outbuffer);
}