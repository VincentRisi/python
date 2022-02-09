#include "xcept.h"
#include "utf.hpp"

template <size_t N>
inline char* zzcopy(char(&target)[N], const char* source) 
{ 
    int n = N-1; 
    target[n] = 0; 
    return strncpy(target, source, n); 
}

template <size_t N>
inline unsigned char* zzcopy(unsigned char(&target)[N], const unsigned char* source)
{
  size_t n = N - 1;
  target[n] = 0;
  memcpy(target, source, n);
  return target;
}

template <class T>
struct HeapRec
{
  T* rec;
  HeapRec() { rec = new T(); memset(rec, 0, sizeof(rec)); }
  ~HeapRec() { delete rec; }
};

#include "tbuffer.h"

char* dump(TBChar& buff, unsigned char* data, int len)
{
  char hexLine[81];
  buff.clear();
  buff.append("\n");
  int size;
  for (size = len; size > 0; size--)
  {
    if (data[size - 1] != 0)
      break;
  }
  char printable[64];
  memset(printable, 0, sizeof(printable));
  for (int i = 0; i < size+1; i++)
  {
    char work[256]; 
    unsigned char ch = data[i];
    int n = i % 32;
    snprintf(work, sizeof(work), "%02x", ch);
    printable[n] = ch < ' ' ? '.' : ch;
    buff.append(work);
    if (i % 16 == 15)
      buff.append(" ");
    if (i % 32 == 31)
    {
      buff.append(" | ");
      buff.append(printable);
      buff.append("\n");
      memset(printable, 0, sizeof(printable));
    }
  }
  buff.append(" | ");
  buff.append(printable);
  return buff.data;
}

#include <stdint.h>

/**
 * Encode a code point using UTF-8
 *
 * @author Ond?ej Hruška <ondra@ondrovo.com>
 * @license MIT
 *
 * @param out - output buffer (min 5 characters), will be 0-terminated
 * @param utf - code point 0-0x10FFFF
 * @return number of bytes on success, 0 on failure (also produces U+FFFD, which uses 3 bytes)
 */
int utf8_encode(char* out, uint32_t utf)
{
  if (utf <= 0x7F) {
    // Plain ASCII
    out[0] = (char)utf;
    out[1] = 0;
    return 1;
  }
  else if (utf <= 0x07FF) {
    // 2-byte unicode
    out[0] = (char)(((utf >> 6) & 0x1F) | 0xC0);
    out[1] = (char)(((utf >> 0) & 0x3F) | 0x80);
    out[2] = 0;
    return 2;
  }
  else if (utf <= 0xFFFF) {
    // 3-byte unicode
    out[0] = (char)(((utf >> 12) & 0x0F) | 0xE0);
    out[1] = (char)(((utf >> 6) & 0x3F) | 0x80);
    out[2] = (char)(((utf >> 0) & 0x3F) | 0x80);
    out[3] = 0;
    return 3;
  }
  else if (utf <= 0x10FFFF) {
    // 4-byte unicode
    out[0] = (char)(((utf >> 18) & 0x07) | 0xF0);
    out[1] = (char)(((utf >> 12) & 0x3F) | 0x80);
    out[2] = (char)(((utf >> 6) & 0x3F) | 0x80);
    out[3] = (char)(((utf >> 0) & 0x3F) | 0x80);
    out[4] = 0;
    return 4;
  }
  else {
    // error - use replacement character
    out[0] = (char)0xEF;
    out[1] = (char)0xBF;
    out[2] = (char)0xBD;
    out[3] = 0;
    return 0;
  }
}

void utf8_encode_str(unsigned char* work, unsigned char* data)
{
  work[0] = 0;
  for (int i = 0; i < 1024 && data[i] != 0; i++)
  {
    uint32_t u = data[i];
    char ch[5];
    int size = utf8_encode(ch, u);
    strcat((char*)work, ch);
  }
}


const char* connstring = "Dsn=%s; Uid=%s; Pwd=%s;";
enum { ARG_DRIVER = 1, ARG_USERID, ARG_PASSWORD };
int main(int argc, char* argv[])
{
  TJConnector conn;
  try
  {
      char work[1024];
      snprintf(work, sizeof(work), connstring, argv[ARG_DRIVER], argv[ARG_USERID], argv[ARG_PASSWORD]);
      printf("%s\n", work); fflush(stdout);
      conn.Logon(work);

      conn.Logoff();
  }
  catch (TOdbcApiException ex)
  {
      printf("%d - %s\n", ex.Error(), ex.ErrorStr());
      return -1;
  }
  catch (...)
  {
      return 111;
  }
  return 0;
}

#if 0
Should be normal ODBC

But you need an Oracle driver

odbc - general is just ODBC ... still requires a DB specific ODBC driver installed

#endif
