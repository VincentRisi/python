export module FiveWordsModule;

#include <iostream>
#include <string.h>

export
{
    typedef unsigned int uint;
    struct WordSum
    {
        char word[6];
        int sum;
        uint charbits;
        WordSum(const char* word, const int sum = 0, const uint mask = 0)
        {
            this->word[5] = 0;
            memcpy(this->word, word, 5);
            this->sum = sum;
            this->charbits = mask;
        };

    };

    typedef int (*fptr)(const void*, const void*);

    struct WordSumList
    {
        int (*compare)(WordSum* a, WordSum* b);
        WordSumList(unsigned long aAllocCount = 32) { list = 0; count = 0; compare = 0; allocCount = aAllocCount > 0 ? aAllocCount : 32; }
        virtual ~WordSumList() { if (list) free(list); }
        void add(WordSum& rec)
        {
            if (count % allocCount == 0)   // if count == 0 || count == allocCount
            {
                allocCount += count;         // if count = 0 then allocCount else count == allocCount and allocCount doubles
                list = (WordSum*)realloc(list, sizeof(rec) * (allocCount));
                if (list == 0)
                {
                    printf("Memory Allocation Failure for %ld\n", sizeof(rec) * allocCount);
                    return;
                }
            }
            list[count++] = rec;           // will shallow copy; if you have a copy constructor then beware of leaks
        }
        int getCount() { return count; }
        WordSum* getList() { return list; }
        void remove(int index)
        {
            if (index < count)
            {
                count--;
                int i;
                for (i = index; i < count; i++)
                    list[i] = list[i + 1];
            }
            else
            {
                printf("Deletion of non existing item %ld\n", index);
                return;
            }
        }
        void clear()
        {
            count = 0;
        }
        int search(WordSum* lookup)
        {
            if (compare == 0)
            {
                printf("No sort/search compare function defined %d\n", count);
                return;
            }
            WordSum* found = (WordSum*)bsearch(lookup, list, (int)count, sizeof(WordSum), (fptr)compare);
            if (found)
                return found - list;
            return -1;
        }
        void sort()
        {
            if (compare == 0)
            {
                printf("No sort/search compare function defined %d\n", count);
                return;
            }
            if (count > 1)
                qsort(list, (int)count, sizeof(WordSum), (fptr)compare);
        }
        WordSum& operator [](int i)
        {
            if (i >= count || i < 0)
            {
                printf("Accessing out of range %d", i);
                return;
            }
            return list[i];
        }
    private:
        int allocCount;
        WordSum* list;
        int count;
    };

};
