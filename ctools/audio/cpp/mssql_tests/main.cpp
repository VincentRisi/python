#include "main.h"
#include <inttypes.h>
#include "cover_snips.h"
#include "message_snips.h"
#include "reply_snips.h"
#include "response_snips.h"
#include "streams_snips.h"
#include "getargs.h"
#include "zcompress.h"
static char* driver = "ODBC Driver 17 for SQL Server";
static char* jpeg_directory = "";
static char* password = "WelcomeVR@0195";
static char* server = "192.168.1.102";
static char* user = "sa";

ARG argtab[] =
{
  {'d', STRING, (int*)&driver,         "Driver"},
  {'j', STRING, (int*)&jpeg_directory, "Jpeg Directory"},
  {'p', STRING, (int*)&password,       "Password"},
  {'s', STRING, (int*)&server,         "Server"},
  {'u', STRING, (int*)&user,           "Username"},
};
#define _SKIP_SNIPS_

void hex_dump_buffer(char* tag, unsigned char* buffer, int size);

void add_messages(TJConnector& conn)
{
  try
  {
    DMessage rec;
#if defined _SKIP_SNIPS_
    TMessageInsert szq(conn, JP_MARK);
#endif
    for (int i = 0; i < 10; i++)
    {
      unsigned char buff[8000]; buff[7999] = 0;
      for (int j = 0; j < 7999; j++)
        buff[j] = (91 * i + j) % 255;
      memcpy(rec.MessageData.data, buff, sizeof(buff));
      rec.MessageData.len = 8000;
      rec.MessageLen = 8000;
      memcpy(rec.USId, "BANDIT", 7);
#if defined _SKIP_SNIPS_
      //szq.Exec(rec);
      if (szq.ReadOne(rec))
        rec = *szq.DRec();
#else
      MessageInsert(&conn, &rec);
#endif
      printf("%d", rec.Id);
    }
    conn.Commit();
  }
  catch (TCliApiException ex)
  {
    conn.Rollback();
    printf("%s", ex.ErrorStr());
  }
  catch (xCept xCept_ex)
  {
    conn.Rollback();
    printf("%s", xCept_ex.ErrorStr());
  }
  printf("\n");
}

void add_replies(TJConnector& conn)
{
  try
  {
    DReply rec;
#if defined _SKIP_SNIPS_
    TReplyInsert szq(conn, JP_MARK);
#endif
    for (int i = 0; i < 10; i++)
    {
      unsigned char buff[8000]; buff[7999] = 0;
      for (int j = 0; j < 7999; j++)
        buff[j] = (23 * i + j) % 255;
      memcpy(rec.MessageData.data, buff, sizeof(buff));
      rec.MessageData.len = 8000;
      rec.MessageLen = 8000;
      memcpy(rec.USId, "BANDIT", 7);
#if defined _SKIP_SNIPS_
      //szq.Exec(rec);
      if (szq.ReadOne(rec))
        rec = *szq.DRec();
#else
      ReplyInsert(&conn, &rec);
#endif
      printf("%d", rec.Id);
    }
    conn.Commit();
  }
  catch (TCliApiException ex)
  {
    conn.Rollback();
    printf("%s", ex.ErrorStr());
  }
  catch (xCept xCept_ex)
  {
    conn.Rollback();
    printf("%s", xCept_ex.ErrorStr());
  }
  printf("\n");
}

void add_responses(TJConnector& conn)
{
  try
  {
    DResponse rec;
#if defined _SKIP_SNIPS_
    TResponseInsert szq(conn, JP_MARK);
#endif
    for (int i = 0; i < 10; i++)
    {
      unsigned char buff[8000]; buff[7999] = 0;
      for (int j = 0; j < 7999; j++)
        buff[j] = (47 * i + j) % 255;
      memcpy(rec.MessageData.data, buff, sizeof(buff));
      rec.MessageData.len = 8000;
      rec.MessageLen = 8000;
      memcpy(rec.USId, "BANDIT", 7);
#if defined _SKIP_SNIPS_
      //if (szq.q_.isOpen)
      //  szq.Close();
      szq.Exec(rec);
      //if (szq.ReadOne(rec))
      //  rec = *szq.DRec();
#else
      ResponseInsert(&conn, &rec);
#endif
      printf("%d", rec.Id);
    }
    conn.Commit();
  }
  catch (TCliApiException ex)
  {
    conn.Rollback();
    printf("%s", ex.ErrorStr());
  }
  catch (xCept xCept_ex)
  {
    conn.Rollback();
    printf("%s", xCept_ex.ErrorStr());
  }
  printf("\n");
}

void add_streams(TJConnector& conn)
{
  try
  {
    DStreams rec;
#if defined _SKIP_SNIPS_
    TStreamsInsert szq(conn, JP_MARK);
#endif
    for (int i = 0; i < 10; i++)
    {
      unsigned char buff[8000]; buff[7999] = 0;
      for (int j = 0; j < 7999; j++)
        buff[j] = (47 * i + j) % 255;
      memcpy(rec.MessageData.data, buff, sizeof(buff));
      rec.MessageData.len = 8000;
      rec.MessageLen = 8000;
      memcpy(rec.USId, "BANDIT", 7);
#if defined _SKIP_SNIPS_
      szq.Exec(rec);
      rec = *szq.DRec();
#else
      StreamsInsert(&conn, &rec);
#endif
      printf("%d", rec.Id);
    }
    conn.Commit();
  }
  catch (TCliApiException ex)
  {
    conn.Rollback();
    printf("%s", ex.ErrorStr());
  }
  catch (xCept xCept_ex)
  {
    conn.Rollback();
    printf("%s", xCept_ex.ErrorStr());
  }
  printf("\n");
}

void do_mcpe_sequences()
{
  TJConnector conn;
  char connectString[2048];
  snprintf(connectString, sizeof(connectString),
    "Driver={%s};"
    "Server=%s;"
    "Database=mcpe;"
    "UID=%s;"
    "PWD=%s;", driver, server, user, password);
  try
  {
    conn.Logon(0, 0, 0, 0, 0, connectString);
    add_messages(conn);
    add_replies(conn);
    add_responses(conn);
    add_streams(conn);
    conn.Commit();
  }
  catch (TCliApiException ex)
  {
    conn.Rollback();
    printf("%s", ex.ErrorStr());
  }
  catch (xCept xCept_ex)
  {
    conn.Rollback();
    printf("%s", xCept_ex.ErrorStr());
  }
  conn.Logoff();
}

void hex_dump_buffer(char* tag, unsigned char* buffer, int size)
{
  char pos[20];
  char line[200];
  char last[32];
  int i, j;
  printf(" [%s]\n", tag);
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
    printf("%s %s [%s]\n", pos, line, last);
  }
}

struct UnChar
{
  unsigned char* uch;
  UnChar(size_t size) {
    uch = new unsigned char[size];
  }
  ~UnChar() { delete[] uch; }
};

inline char* reduce(char* work, char* data)
{
  memset(work, 0, 512);
  int j = 0;
  for (int i = 0; i < strlen(data); i++)
  {
    if ((data[i] >= 'a' && data[i] <= 'z')
      || (data[i] >= 'A' && data[i] <= 'Z')
      || (data[i] >= '0' && data[i] <= '9'))
      work[j++] = data[i];
  }
  return work;
}

inline void get_filename(char* ofilename, size_t buffsize, OCoverSelectUnPosted& inrec, DCoverGetSeries& dsrec)
{
  char author[512];
  char book[512];
  char series[512];
  char bookSeq[512];
  strcpy(series, "");
  strcpy(bookSeq,"1");
  if (strcmp(dsrec.bookSeq, "Single") != 0)
  {
    reduce(series, dsrec.seriesName);
    reduce(bookSeq, dsrec.bookSeq);
  }
  snprintf(ofilename, buffsize, "%s\\%s-%s%s%s.jpg", jpeg_directory, reduce(author, inrec.authorName), series, bookSeq, reduce(book, inrec.bookName));
  printf("%s\n", ofilename);
}

void write_jpegs(TJConnector& conn, OCoverSelectUnPosted& inrec)
{
  try
  {
    struct CoverRec
    {
      DCoverGetCover* rec;
      CoverRec() { rec = new DCoverGetCover(); }
      ~CoverRec()
      {
        delete rec;
      }
    } cr;
    zzcopy(cr.rec->bookId, inrec.bookId);
    autoList<OCoverGetCover> list;
#if defined _SKIP_SNIPS_
    TCoverGetCover q1(conn, JP_MARK);
    q1.Exec(*cr.rec);
    while (q1.Fetch())
        SnipAddList(list.outRecs, list.noOf, *q1.ORec(), (int32)q1.NOROWS);
#else
    CoverGetCover(&conn, cr.rec, &list.noOf, list.outRecs);
#endif    
    UnChar d(inrec.coverLen);
    size_t sofar = 0;
    int32 dsize;
    for (int i = 0; i < list.noOf; i++)
    {
      OCoverGetCover* lrec = &list.outRecs[i];
      int rc = ZDecompress(lrec->cover.data, lrec->cover.len, d.uch + sofar, &dsize);
      sofar += dsize;
    }
    OCoverGetSeries *osrec = 0;
    DCoverGetSeries dsrec;
    zzcopy(dsrec.seriesId, inrec.bookId);
#if defined _SKIP_SNIPS_
    TCoverGetSeries q3(conn, JP_MARK);
    q3.Exec(dsrec);
    if (q3.Fetch())
      dsrec = *q3.DRec();
#else
    CoverGetSeries(&conn, &dsrec);
#endif    
    char ofilename[512];
    get_filename(ofilename, sizeof(ofilename), inrec, dsrec);
    printf("%s\n", ofilename);
    FILE* outfile = fopen(ofilename, "wb");
    fwrite(d.uch, 1, sofar, outfile);
    fclose(outfile);
    DCoverUpdatePosted prec;
    zzcopy(prec.bookId,inrec.bookId);
#if defined _SKIP_SNIPS_
    TCoverUpdatePosted q2(conn, JP_MARK);
    q2.Exec(prec);
#else    
    CoverUpdatePosted(&conn, &prec);
#endif    
    conn.Commit();
  }
  catch (...)
  {
    printf("*** failed\n");
  }
}

#undef _SKIP_SNIPS_
void do_book_covers()
{
  TJConnector conn;
  char connectString[2048];
  snprintf(connectString, sizeof(connectString),
    "Driver={%s};"
    "Server=%s;"
    "Database=audio;"
    "UID=%s;"
    "PWD=%s;", driver, server, user, password);
  try
  {
    conn.Logon(0, 0, 0, 0, 0, connectString);
    autoList<OCoverSelectUnPosted> list;
#if defined _SKIP_SNIPS_
    TCoverSelectUnPosted q(conn, JP_MARK);
    q.Exec();
    OCoverSelectUnPosted* rec;
    while (q.Fetch())
    {
      SnipAddList(list.outRecs, list.noOf, *q.ORec(), (int32)q.NOROWS);
      rec = q.ORec();
    }
#else
    CoverSelectUnPosted(&conn, &list.noOf, list.outRecs);
#endif
    for (int i = 0; i < list.noOf; i++)
    {
      OCoverSelectUnPosted* rec = &list.outRecs[i];
      printf("%s%d\n", rec->bookId, rec->coverLen);
      write_jpegs(conn, *rec);
    }
  }
  catch (TCliApiException ex)
  {
    conn.Rollback();
    printf("%s", ex.ErrorStr());
  }
  catch (xCept xCept_ex)
  {
    conn.Rollback();
    printf("%s", xCept_ex.ErrorStr());
  }
  conn.Logoff();
}

int main(int argc, char* argv[])
{
  const int noArgs = sizeof(argtab) / sizeof(ARG);
  argc = GetArgs(argc, argv, argtab, noArgs);
  do_mcpe_sequences();
  do_book_covers();
  return 0;
}