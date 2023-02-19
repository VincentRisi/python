#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>
#include <sys/stat.h>
#include <ctype.h>

const int SIZE = 8 * 1024 * 1024;
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
  unsigned char* data;
  int size;
  autoChar(int size)
  {
    this->size = size;
    data = (unsigned char*)calloc(size, 1);
  }
  ~autoChar()
  {
    free(data);
  }
};

unsigned char* hexout(unsigned char* p, int size)
{
  while (size--)
  {
    fprintf(stdout, "%02X", *p);
    p++;
  }
  fprintf(stdout, "\n");
  return p;
}

int getint(unsigned char* p)
{
  return (p[0] << 24) + (p[1] << 16) + (p[2] << 8) + p[3];
}

int get3bytes(unsigned char* p)
{
  return (p[0] << 16) + (p[1] << 8) + p[2];
}

unsigned char* lastrec(unsigned char* p)
{
  fprintf(stdout, "%d|%4.4s|%d|%4.4s\n"
    , getint(p)
    , p + 4
    , getint(p + 8)
    , p + 12
  );
  return p + 16;
}

unsigned char* firstrec(unsigned char* p)
{
  fprintf(stdout, "%4.4s|%8.8s\n"
    , p
    , p + 12
  );
  return p + 29;
}

unsigned char* sizerec(unsigned char* p)
{
  int size = getint(p);
  fprintf(stdout, "%d|%s\n", size, p + 4);
  return p + 8;
}

unsigned char* chapter(unsigned char* p)
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

void dump_stco(unsigned char* buffer)
{
  int length = getint(buffer);
  int no_of = getint(buffer + 12);
  fprintf(stdout, "%d|%4.4s|%d|%d\n"
    , length
    , buffer + 4
    , getint(buffer + 8)
    , no_of
  );
  unsigned char* p = buffer + 16;
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
  sprintf(work, "%d.%d", h * 60 + m, s);
  return work;
}

void get_bitrate(unsigned char* buffer)
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
    , getint(buffer + 8)
    , no_of
  );
  unsigned char* p = buffer + 16;
  char work[64], work2[64];
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

void dump_mdirappl(unsigned char* buffer)
{
  unsigned char* p = buffer;
  p = firstrec(p);
  p = sizerec(p);
  while (p[4] == 169)
    p = chapter(p);
  p = lastrec(p);
}

void hexDumpBuffer(unsigned char* buffer, int size)
{
  char pos[20];
  char line[200];
  char last[32];
  int i, j;
  //fprintf(stdout, "%P\n", buffer);
  for (i = 0; i < size; i += 16)
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
  fprintf(stdout, "\n");
}

void checkData(char* tag, unsigned char* data)
{
  if (memcmp(data + 8, "data", 4) == 0)
  {
    int length = getint(data + 4);
    int count = getint(data + 12);
    int occur = getint(data + 16);
    autoChar ab1(length + 1);
    memcpy(ab1.data, data + 20, length);
    fprintf(stdout, "%s|%s\n", tag, ab1.data);
    //hexDumpBuffer(data, 12+length);
  }
  else
    fprintf(stdout, "#%s\n", tag);
}

#define CPR "\xA9"

void process(const char* filename)
{
  autoFile aax(filename, "rb");
  if (aax.filein == 0)
  {
    fprintf(stderr, "%s file not opened - ignoring it.\n", filename);
    return;
  }
  autoChar ab1(SIZE);// , ab2(SIZE);
  unsigned char* buffer = ab1.data;
  unsigned char* fpath;// = ab2.data;
  endsat = (int)fseek(aax.filein, (long)0, SEEK_END);
  endsat = (int)ftell(aax.filein);
  fseek(aax.filein, (long)406, SEEK_SET);
  fread(buffer, 1, 4, aax.filein);
  int mpos = getint((unsigned char*)buffer) + 406;
  fseek(aax.filein, (long)mpos, SEEK_SET);
  size_t pos = 0;
  int no = 0;
  int start = 0, length = 0;
  unsigned char* atppi = 0;
  unsigned char* atpst = 0;
  unsigned char* atpti = 0;
  unsigned char* sti = 0;
  unsigned char* aacr = 0;
  unsigned char* aart = 0;
  unsigned char* atnu = 0;
  unsigned char* cdek = 0;
  unsigned char* cdet = 0;
  unsigned char* cprt = 0;
  unsigned char* cover = 0;
  unsigned char* guid = 0;
  unsigned char* prid = 0;
  unsigned char* released = 0;
  unsigned char* trkn = 0;
  unsigned char* vers = 0;
  unsigned char* album = 0;
  unsigned char* author = 0;
  unsigned char* comment = 0;
  unsigned char* atday = 0;
  unsigned char* description = 0;
  unsigned char* genre = 0;
  unsigned char* name = 0;
  unsigned char* narrator = 0;
  unsigned char* publisher = 0;
  unsigned char* pasn = 0;
  unsigned char* twos = 0;
  size_t size;
  size = fread(buffer, 1, SIZE, aax.filein);
  fpath = buffer;

  for (size_t i = 0; i < size; i++)
  {
    fpath++;
    if (memcmp(fpath, "@sti", 5) == 0) sti = fpath;
    if (memcmp(fpath, "AACR", 5) == 0) aacr = fpath;
    if (memcmp(fpath, "aART", 5) == 0) aart = fpath;
    if (memcmp(fpath, &CPR"alb", 5) == 0) album = fpath;
    if (memcmp(fpath, &CPR"ART", 5) == 0) author = fpath;
    if (memcmp(fpath, "atnu", 5) == 0) atnu = fpath;
    if (memcmp(fpath, "CDEK", 5) == 0) cdek = fpath;
    if (memcmp(fpath, "CDET", 5) == 0) cdet = fpath;
    if (memcmp(fpath, &CPR"cmt", 5) == 0) comment = fpath;
    if (memcmp(fpath, "covr", 5) == 0) cover = fpath;
    if (memcmp(fpath, "cprt", 5) == 0) cprt = fpath;
    if (memcmp(fpath, &CPR"day", 5) == 0) atday = fpath;
    if (memcmp(fpath, &CPR"des", 5) == 0) description = fpath;
    if (memcmp(fpath, &CPR"gen", 5) == 0) genre = fpath;
    if (memcmp(fpath, "GUID", 5) == 0) guid = fpath;
    if (memcmp(fpath, &CPR"nam", 5) == 0) name = fpath;
    if (memcmp(fpath, &CPR"nrt", 5) == 0) narrator = fpath;
    if (memcmp(fpath, "PASN", 5) == 0) pasn = fpath;
    if (memcmp(fpath, "@ppi", 5) == 0) atppi = fpath;
    if (memcmp(fpath, "prID", 5) == 0) prid = fpath;
    if (memcmp(fpath, "@PST", 5) == 0) atpst = fpath;
    if (memcmp(fpath, "@pti", 5) == 0) atpti = fpath;
    if (memcmp(fpath, &CPR"pub", 5) == 0) publisher = fpath;
    if (memcmp(fpath, "rldt", 5) == 0) released = fpath;
    if (memcmp(fpath, "trkn", 5) == 0) trkn = fpath;
    if (memcmp(fpath, "VERS", 5) == 0) vers = fpath;
    if (memcmp(fpath, "!2222222", 8) == 0) twos = fpath;
    if (twos != 0)
    {
      no = i;
      break;
    }
  }
  if (aacr != 0) checkData("aacr", aacr);
  if (aart != 0) checkData("aart", aart);
  if (album != 0) checkData("album", album);
  if (atday != 0) checkData("atday", atday);
  if (atnu != 0) checkData("atnu", atnu);
  if (atppi != 0) checkData("atppi", atppi);
  if (atpst != 0) checkData("atpst", atpst);
  if (atpti != 0) checkData("atpti", atpti);
  if (author != 0) checkData("author", author);
  if (cdek != 0) checkData("cdek", cdek);
  if (cdet != 0) checkData("cdet", cdet);
  //if (comment != 0) checkData("comment", comment);
  //if (cover != 0) checkData("cover", cover);
  if (cprt != 0) checkData("cprt", cprt);
  if (description != 0) checkData("description", description);
  if (genre != 0) checkData("genre", genre);
  if (guid != 0) checkData("guid", guid);
  if (name != 0) checkData("name", name);
  if (narrator != 0) checkData("narrator", narrator);
  if (pasn != 0) checkData("pasn", pasn);
  if (prid != 0) checkData("prid", prid);
  if (publisher != 0) checkData("publisher", publisher);
  if (released != 0) checkData("released", released);
  if (sti != 0) checkData("sti", sti);
  if (trkn != 0) checkData("trkn", trkn);
  if (vers != 0) checkData("vers", vers);
  //hexDumpBuffer(buffer, no);
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