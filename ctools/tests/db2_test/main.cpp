#include "xcept.h"

template <size_t N>
inline char* zzcopy(char(&target)[N], const char* source) 
{ 
    int n = N-1; 
    target[n] = 0; 
    return strncpy(target, source, n); 
}

int main(int argc, char* argv[])
{
  TJConnector conn;
  conn.Logon("bbdmsg", "oracle", "lv01");
  conn.Logoff();
  return 0;
}