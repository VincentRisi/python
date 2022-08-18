#include "main.h"
#include <inttypes.h>
#include "cover_snips.h"
#include "message_snips.h"
#include "reply_snips.h"
#include "response_snips.h"
#include "streams_snips.h"

void add_messages(TJConnector& conn)
{
  try
  {
    DMessage rec;
    for (int i = 0; i < 10; i++)
    {
      unsigned char buff[8000]; buff[7999] = 0;
      for (int j = 0; j < 7999; j++)
        buff[j] = (91 * i + j) % 255;
      memcpy(rec.MessageData.data, buff, sizeof(buff));
      rec.MessageData.len = 8000;
      rec.MessageLen = 8000;
      memcpy(rec.USId, "BANDIT", 7);
      MessageInsert(&conn, &rec);
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
    for (int i = 0; i < 10; i++)
    {
      unsigned char buff[8000]; buff[7999] = 0;
      for (int j = 0; j < 7999; j++)
        buff[j] = (23 * i + j) % 255;
      memcpy(rec.MessageData.data, buff, sizeof(buff));
      rec.MessageData.len = 8000;
      rec.MessageLen = 8000;
      memcpy(rec.USId, "BANDIT", 7);
      ReplyInsert(&conn, &rec);
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
    for (int i = 0; i < 10; i++)
    {
      unsigned char buff[8000]; buff[7999] = 0;
      for (int j = 0; j < 7999; j++)
        buff[j] = (47 * i + j) % 255;
      memcpy(rec.MessageData.data, buff, sizeof(buff));
      rec.MessageData.len = 8000;
      rec.MessageLen = 8000;
      memcpy(rec.USId, "BANDIT", 7);
      ResponseInsert(&conn, &rec);
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
    for (int i = 0; i < 10; i++)
    {
      unsigned char buff[8000]; buff[7999] = 0;
      for (int j = 0; j < 7999; j++)
        buff[j] = (47 * i + j) % 255;
      memcpy(rec.MessageData.data, buff, sizeof(buff));
      rec.MessageData.len = 8000;
      rec.MessageLen = 8000;
      memcpy(rec.USId, "BANDIT", 7);
      StreamsInsert(&conn, &rec);
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
  try 
  {
    conn.Logon(0, 0, 0, 0, 0, 
      "Driver={ODBC Driver 17 for SQL Server};"
      "Server=192.168.1.102;"
      "Database=mcpe;"
      "UID=sa;"
      "PWD=WelcomeVR@0195;"
      );
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

int main(int argc, char* argv)
{
  do_mcpe_sequences();
  return 0;
}