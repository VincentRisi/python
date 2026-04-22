export module machine;

export typedef struct
{
  char p[2];
} byte2;

export typedef struct
{
  char p[4];
} byte4;

export typedef struct
{
  char p[8];
} byte8;

export const unsigned int _MACHINE_FLOAT_SIZE_  = sizeof(float);
export const unsigned int _MACHINE_DOUBLE_SIZE_ = sizeof(double);
#if defined _MSC_VER
export const unsigned int _MACHINE_LONG_SIZE_   = sizeof(long long);
#else
export const unsigned int _MACHINE_LONG_SIZE_   = sizeof(long);
#endif
export const unsigned int _MACHINE_INT_SIZE_    = sizeof(int);
export const unsigned int _MACHINE_SHORT_SIZE_  = sizeof(short);
export const unsigned int _MACHINE_CHAR_SIZE_   = sizeof(char);

#if defined(_MSC_VER)
   export typedef __int8  int8;
   export typedef __int16 int16;
   export typedef __int32 int32, int32_t;
   export typedef __int64 int64;
   export typedef unsigned __int8  uint8;
   export typedef unsigned __int16 uint16;
   export typedef unsigned __int32 uint32;
   export typedef unsigned __int64 uint64;
#elif defined(__GNUC__)
   #include <sys/types.h>
   #define int8   int8_t
   #define int16  int16_t
   #define int32  int32_t
   #define int64  int64_t
   #define uint8  u_int8_t
   #define uint16 u_int16_t
   #define uint32 u_int32_t
   #define uint64 u_int64_t
#endif
