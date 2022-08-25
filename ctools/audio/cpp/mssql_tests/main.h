#ifndef __MAIN_MSSQL_TESTS_H__
#define __MAIN_MSSQL_TESTS_H__

template <size_t N>
inline char* zzcopy(char(&target)[N], const char* source)
{
  size_t n = N - 1;
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


#endif

