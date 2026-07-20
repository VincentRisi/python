export module book;
import machine;
import ociapi;

export struct DBook
{
  char   authorId[11];
  char   bookId[11];
  int16  partNo;
  char   bookName[251];
  char   fileName[251];
  char   album[251];
  char   authors[251];
  char   narrators[251];
  char   comment[501];
  char   description[4001];
  void Clear()
  {
      memset(authorId, 0, sizeof(authorId));
      memset(bookId, 0, sizeof(bookId));
      partNo = 0;
      memset(bookName, 0, sizeof(bookName));
      memset(fileName, 0, sizeof(fileName));
      memset(album, 0, sizeof(album));
      memset(authors, 0, sizeof(authors));
      memset(narrators, 0, sizeof(narrators));
      memset(comment, 0, sizeof(comment));
      memset(description, 0, sizeof(description));
  }
  DBook() 
  { 
    Clear(); 
  }
};

export using OBook = DBook;

struct DBookDeleteOne
{
  char   authorId[11];
  char   bookId[11];
  int16  partNo;
  void Clear()
  {
      memset(authorId, 0, sizeof(authorId));
      memset(bookId, 0, sizeof(bookId));
      partNo = 0;
  }
  DBookDeleteOne() { Clear(); }
  #ifdef swapbytesH
  void Swaps()
  {
      SwapBytes(partNo);
  }
  #endif
};

struct TBookDeleteOne : public DBookDeleteOne
{
    TJQuery q_;
    void Exec()
    {
      if (q_.command == 0)
          q_.command = new char [86];
      memset(q_.command, 0, 86);
      strcat(q_.command, "delete from Book""\n"
          " where authorId = ?""\n"
          "   and bookId = ?""\n"
          "   and partNo = ?");
      q_.Open(q_.command, 3);
      q_.Bind(0, authorId, 10, SQL_PARAM_INPUT , 0, 0);
      q_.Bind(1, bookId, 10, SQL_PARAM_INPUT , 0, 0);
      q_.Bind(2, partNo, SQL_PARAM_INPUT );
      q_.Exec();
    }
    void Exec(DBookDeleteOne& Rec) 
    {
      *DRec() = Rec;
      Exec();
    }
    void Exec(const char* aauthorId, const char* abookId, const int16 apartNo)
    {
      strncpy(authorId, aauthorId, sizeof(authorId)-1);
      strncpy(bookId, abookId, sizeof(bookId)-1);
      partNo = apartNo;
      Exec();
    }
    TBookDeleteOne(TJConnector &conn, const char *aFile=__FILE__, long aLine=__LINE__)
    : q_(conn)
    {
      Clear();q_.FileAndLine(aFile,aLine);
    }
    DBookDeleteOne* DRec() 
    {
      return this;
    }
};
