
#include <stdio.h>
import std;
import getargs;
import encoders;
import logfile;
import tbuffer;

static const char* logfile_name;
static const char* binfile_name;

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
  log.lprintf(eLogDebug, "%ld %ld %s", size, encoded.length(), encoded.c_str());
	std::string decoded = base64_decode(encoded, Basic);
	bool equal = compare_buffers(buffer, (unsigned char*)decoded.c_str(), size);
  if (!equal)
    log.lprintf(eLogError, "Decoded buffer does not match original buffer for Basic encoding");
  else
		log.lprintf(eLogInfo, "Decoded buffer matches original buffer for Basic encoding");
	encoded = base64_encode(buffer, size, Mime);
  log.lprintf(eLogDebug, "%ld %ld %s", size, encoded.length(), encoded.c_str());
  decoded = base64_decode(encoded, Mime);
  equal = compare_buffers(buffer, (unsigned char*)decoded.c_str(), size);
  if (!equal)
    log.lprintf(eLogError, "Decoded buffer does not match original buffer for Mime encoding");
  else
    log.lprintf(eLogInfo, "Decoded buffer matches original buffer for Mime encoding");
  encoded = base64_encode(buffer, size, URL_Safe);
  log.lprintf(eLogDebug, "%ld %ld %s", size, encoded.length(), encoded.c_str());
  decoded = base64_decode(encoded, URL_Safe);
  if (!equal)
    log.lprintf(eLogError, "Decoded buffer does not match original buffer for URL_Safe encoding");
  else
    log.lprintf(eLogInfo, "Decoded buffer matches original buffer for URL_Safe encoding");
}

int main(int argc, char** argv)
{
  static GetArgList arg_list;
  TGetArg arg_binfile_name('b', "binfile", &binfile_name, "String");
  TGetArg arg_logfile_name('l', "logfile", &logfile_name, "String");
  arg_list.add(arg_binfile_name);
  arg_list.add(arg_logfile_name);
  argc = getArgs(argc, argv, arg_list);
  if (argc == -1 || logfile_name == 0)
  {
    printUsage(arg_list, stdout);
    return 1;
  }
  LogFile log = LogFile(logfile_name);
  log.Log(logfile_name);
  log.Log(binfile_name);
	FILE* f = fopen(binfile_name, "rb");
	fseek(f, 0, SEEK_END);
	long size = ftell(f);
	fseek(f, 0, SEEK_SET);
  TBUChar buffer(size);
	fread(buffer, 1, size, f);
  fclose(f);
	base64_test(log, 2000, buffer);
  log.Log("Done");
}