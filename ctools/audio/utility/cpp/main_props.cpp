#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>
#include <sys/stat.h>
#include <ctype.h>

const int SIZE = 256 * 1024;
static int endsat;

static void hexDumpBuffer(unsigned char* buffer, int size);

struct autoFile
{
  FILE* filein;
  autoFile(const char* filename, const char* mode)
  {
    filein = fopen(filename, mode);
  }
  ~autoFile()
  {
    if (filein)
      fclose(filein);
  }
};

struct autoChar
{
  char* data;
  int size;
  autoChar(int size)
  {
    this->size = size;
    data = (char*)calloc(size, 1);
  }
  ~autoChar()
  {
    free(data);
  }
};

unsigned char * hexout(unsigned char * p, int size)
{
  while (size--)
  {
    fprintf(stdout, "%02X", *p); 
    p++;
  }
  fprintf(stdout, "\n");
  return p;
}

int getint(unsigned char * p)
{
  return (p[0] << 24) + (p[1] << 16) + (p[2] << 8) + p[3];
}

int get3bytes(unsigned char * p)
{
  return (p[0] << 16) + (p[1] << 8) + p[2];
}

unsigned char * lastrec(unsigned char * p)
{
  fprintf(stdout, "%d|%4.4s|%d|%4.4s\n"
    , getint(p)
    , p + 4
    , getint(p + 8)
    , p + 12
    );
  return p + 16;
}

unsigned char * firstrec(unsigned char * p)
{
  fprintf(stdout, "%4.4s|%8.8s\n"
    , p
    , p + 12
    );
  return p + 29;
}

unsigned char * sizerec(unsigned char * p)
{
  int size = getint(p);
  fprintf(stdout, "%d|%s\n", size, p + 4);
  return p + 8;
}

unsigned char * chapter(unsigned char * p)
{
  int length = getint(p);
  int dlen = length - 24;
  fprintf(stdout, "%d|%3.3s|%d|%4.4s|%d|%d|%*.*s\n"
    , length
    , p + 5
    , getint(p + 8)
    , p + 12
    , getint(p + 16)
    , getint(p + 20)
    , dlen, dlen, p + 24
    );
  return p + length;
}

void dump_stco(unsigned char * buffer)
{
  int length = getint(buffer);
  int no_of = getint(buffer + 12);
  fprintf(stdout, "%d|%4.4s|%d|%d\n"
    , length
    , buffer + 4
    , getint(buffer + 8)
    , no_of
    );
  unsigned char *p = buffer + 16;
  for (int i = 0; i < no_of; i++)
  {
    int time = getint(p + 4);
    fprintf(stdout, "%d\n"
      , getint(p)
      );
    p += 4;
  }
  fprintf(stdout, "%d\n", endsat);
}

int bitrate = 22050;

inline char* hms(char* work, double value)
{
  int xxx = int(value / bitrate);
  int h, m, s;
  h = xxx / 3600; xxx %= 3600;
  m = xxx / 60; xxx %= 60;
  s = xxx;
  //sprintf(work, "%d:%02d.%d", h, m, s);
  sprintf(work, "%d.%d", h*60 + m, s);
  return work;
}

void get_bitrate(unsigned char * buffer)
{
    unsigned char* p = buffer;
    bitrate = getint(p + 20);
    fprintf(stdout, "bitrate %d\n", bitrate);
}

void dump_stts(unsigned char* buffer)
{
  int length = getint(buffer);
  int no_of = getint(buffer + 12);
  fprintf(stdout, "%d|%4.4s|%d|%d\n"
    , length
    , buffer + 4
    , getint(buffer+8)
    , no_of
    );
  unsigned char *p = buffer + 16;
  char work[64],work2[64];
  double sumtime = 0.0;
  for (int i = 0; i < no_of; i++)
  {
    double otime = (double)getint(p + 4);
    fprintf(stdout, "%d|%0.1f|%s|%s\n"
      , getint(p)
      , otime
      , hms(work, otime)
      , hms(work2, sumtime)
      );
    sumtime += otime;
    p += 8;
  }
  fprintf(stdout, "%s\n", hms(work, sumtime));
}

void dump_mdirappl(unsigned char * buffer)
{
  unsigned char *p = buffer;
  p = firstrec(p);
  p = sizerec(p);
  while (p[4] == 169)
    p = chapter(p);
  p = lastrec(p);
}

void hexDumpBuffer(unsigned char * buffer, int size)
{
  char pos[20];
  char line[200];
  char last[32];
  int i, j;
  for (i = 0; i<size; i += 16)
  {
    sprintf(pos, "%06X[%06d]  ", i, i);
    memset(line, ' ', sizeof(line));
    for (j = 0; j < 16; j++)
    {
      if (j + i < size)
        sprintf(line + j * 2 + j / 4, "%02X ", buffer[i + j]);
      else
        sprintf(line + j * 2 + j / 4, "   ");
    }
    for (j = 0; j < 16; j++)
    {
      if (j + i < size)
      {
        if (isprint(buffer[i + j]))
          sprintf(last + j, "%c", buffer[i + j]);
        else
          sprintf(last + j, ".");
      }
      else
        sprintf(last + j, " ");
    }
    fprintf(stdout, "%s%s [%s]\n", pos, line, last);
  }
}


void process(const char* filename)
{
  autoFile aax(filename, "rb");
  if (aax.filein == 0)
  {
    fprintf(stderr, "%s file not opened - ignoring it.\n", filename);
    return;
  }
  autoChar ab1(SIZE), ab2(SIZE);
  char *buffer = ab1.data;
  char *fpath = ab2.data;
  endsat = (int)fseek(aax.filein, (long)0, SEEK_END);
  endsat = (int)ftell(aax.filein);
  fseek(aax.filein, (long)406, SEEK_SET);
  fread(buffer, 1, 4, aax.filein);
  int mpos = getint((unsigned char *)buffer)+406;
  fseek(aax.filein, (long)mpos, SEEK_SET);
  size_t pos = 0;
  int no = 0;
  memset(fpath, 0, SIZE);
  int start = 0, length = 0;
  while (true)
  {
    size_t size;
    size = fread(buffer, 1, SIZE, aax.filein);
    if (size == 0) break;
    for (size_t i = 0; i < size; i++)
    {
      if (buffer[i] < ' ')
      {
        if (pos > 3)
        {
          char* mdhd = strstr(fpath, "mdhd");
          if (mdhd != 0)
          {
              get_bitrate((unsigned char*)buffer + (i - 8));
          }
          char* stts = strstr(fpath, "stts");
          if (stts != 0)
          {
            dump_stts((unsigned char *)buffer + (i - 8));
          }
          char* stco = strstr(fpath, "stco");
          if (stco != 0)
          {
            dump_stco((unsigned char *)buffer + (i - 8));
          }
          if (strncmp(fpath, "mdirappl", 8) == 0)
          {
            if (start == 0)
            {
              start = i - 20;
              dump_mdirappl((unsigned char *)(buffer + start));
            }
            else
              length = (i - start) + 9;
          }
          if (strncmp(fpath, "!2222222", 8) == 0)
          {
            hexDumpBuffer((unsigned char *)buffer, i);
            return;
          }
        }
        memset(fpath, 0, SIZE);
        pos = 0;
        continue;
      }
      fpath[pos++] = buffer[i];
    }
    if (no++ > 1000) break;
  }
  return;
}

int main(int argc, char* argv[])
{
  for (int argno = 1; argno < argc; argno++)
  {
    char* arg = argv[argno];
    process(arg);
  }
}