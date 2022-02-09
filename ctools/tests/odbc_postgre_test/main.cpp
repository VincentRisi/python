#include "xcept.h"

template <size_t N>
inline char* zzcopy(char(&target)[N], const char* source) 
{ 
    int n = N-1; 
    target[n] = 0; 
    return strncpy(target, source, n); 
}

const char* connstring = "Dsn=%s; Uid=%s; Pwd=%s;";
enum {  ARG_DRIVER = 1, ARG_USERID, ARG_PASSWORD };
; int main(int argc, char* argv[])
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
