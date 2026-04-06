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

export const unsigned int _MACHINE_FLOAT_SIZE_ = sizeof(float);
export const unsigned int _MACHINE_DOUBLE_SIZE_ = sizeof(double);
export const unsigned int _MACHINE_LONG_SIZE_ = sizeof(long);
export const unsigned int _MACHINE_INT_SIZE_ = sizeof(int);
export const unsigned int _MACHINE_SHORT_SIZE_ = sizeof(short);
export const unsigned int _MACHINE_CHAR_SIZE_ = sizeof(char);

