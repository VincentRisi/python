export module WordList;

int exit(int code) { throw code; }
#include "addlist.h"
#include <cstring>

export typedef unsigned int uint;

export struct WordSum
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

export typedef TAddList<WordSum, int> WordSumList;

