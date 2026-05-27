export module machine;

// The machine module provides definitions for various data types and constants 
// related to the underlying hardware architecture.
// It includes definitions for byte-sized structures, as well as constants for the sizes 
// of fundamental data types such as float, double, long, int, short, and char.
// The module also defines fixed-width integer types (int8, int16, int32, int64, uint8, uint16, uint32, uint64)
// based on the compiler being used (MSVC or GCC). These types ensure consistent 
// behavior across different platforms and compilers, allowing for more portable code 
// when working with integer data of specific sizes.

export using byte2 = struct { char p[2]; };
export using byte4 = struct { char p[4]; };
export using byte8 = struct { char p[8]; };

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
   export using int8 = __int8;
   export using int16 = __int16;
   export using int32 = __int32;
   export using int64 = __int64;
   export using uint8 =  unsigned __int8;
   export using uint16 = unsigned __int16;
   export using uint32 = unsigned __int32;
   export using uint64 = unsigned __int64;
#elif defined(__GNUC__) || defined(__clang__)
   #include <sys/types.h>
   export using int8 = int8_t;
   export using int16 = int16_t;
   export using int32 = int32_t;
   export using int64 = int64_t;
   export using uint8 = u_int8_t;
   export using uint16 = u_int16_t;
   export using uint32 = u_int32_t;
   export using uint64 = u_int64_t;
#endif

export using pchar = char*;
export using uchar = unsigned char;
export using schar = signed char;
export using pschar = schar*;
export using pvoid = void*;
export using pshort = short*;
export using pint = int*;
export using plong = long*;
export using pfloat = float*;
export using pdouble = double*;
export using uint = unsigned int;

