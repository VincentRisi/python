#ifndef __ADDLIST_H__
#define __ADDLIST_H__

typedef int (*fptr)(const void*, const void*);
template <class TELEMENT, class TINDEX>
struct TAddList
{
  int (*compare)(TELEMENT *a, TELEMENT *b);
  TAddList(unsigned long aAllocCount=32) {list = 0; count=0; compare=0; allocCount=aAllocCount>0?aAllocCount:32;}
  virtual ~TAddList() {if (list) free(list);}
  void add(TELEMENT& rec)
  {
    if (count % allocCount == 0)   // if count == 0 || count == allocCount
    {
      allocCount += count;         // if count = 0 then allocCount else count == allocCount and allocCount doubles
      list = (TELEMENT*) realloc(list, sizeof(rec)*(allocCount));
      if (list == 0)
      {
        printf("Memory Allocation Failure for %ld\n", sizeof(rec) * allocCount);
        exit(1);
      }
    }
    list[count++] = rec;           // will shallow copy; if you have a copy constructor then beware of leaks
  }
  TINDEX getCount() {return count;}
  TELEMENT* getList() {return list;}
  void remove(TINDEX index)
  {
    if (index < count)
    {
      count--;
      TINDEX i;
      for (i=index; i<count; i++)
        list[i] = list[i+1];
    }
    else
    { 
      printf("Deletion of non existing item %ld\n", index);
      exit(1);
    }
  }
  void clear()
  {
    count = 0;
  }
  int search(TELEMENT* lookup)
  {
    if (compare == 0)
    {
      printf("No sort/search compare function defined %d\n", count);
      exit(1);
    }
    TELEMENT* found = (TELEMENT*)bsearch(lookup, list, (int)count, sizeof(TELEMENT), (fptr)compare);
    if (found)
      return found - list;
    return -1;
  }
  void sort()
  {
    if (compare == 0)
    {
      printf("No sort/search compare function defined %d\n", count);
      exit(1);
    }
    if (count > 1)
    qsort(list, (int)count, sizeof(TELEMENT), (fptr)compare);
  }
  TELEMENT& operator [](TINDEX i)
  {
    if (i >= count || i < 0)
    {
      printf("Accessing out of range %d", i);
      exit(1);
    }
    return list[i];
  }
private:
  TINDEX allocCount;
  TELEMENT* list;
  TINDEX count;
};

#endif

