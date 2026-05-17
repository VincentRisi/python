export module addlist;
export import <iostream>;
import machine;
import <cstdlib>;

using namespace std;

int error(int code, std::string err) 
{ 
	std::cout << err << std::endl;
  throw code; 
}

export using fptr = int (*)(const void*, const void*);
export template <class TELEMENT, class TINDEX>
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
				std::string err = std::format("Memory Allocation Failure for {}", sizeof(rec) * allocCount);
        error(1, err);
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
			std::string err = std::format("Deletion of non existing item {}", index);
      error(1, err);
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
			std::string err = std::format("No sort/search compare function defined {}", count);
      error(1, err);
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
			std::string err = std::format("No sort/search compare function defined {}", count);
      error(1, err);
    }
    if (count > 1)
    qsort(list, (int)count, sizeof(TELEMENT), (fptr)compare);
  }
  TELEMENT& operator [](TINDEX i)
  {
    if (i >= count || i < 0)
    {
			std::string err = std::format("Accessing out of range {}", i);
      error(1, err);
    }
    return list[i];
  }
private:
  TINDEX allocCount;
  TELEMENT* list;
  TINDEX count;
};
