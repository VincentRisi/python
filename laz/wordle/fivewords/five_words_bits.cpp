#include "five_words.h"
#include <stdio.h>
#include "addlist.h"
#define DIM(a)  (sizeof(a)/sizeof((a)[0]))

using namespace std;

#include "word_list.h"
static int noGameWords = DIM(gameWords);
static FILE* LogFile;
#if defined(_WIN32) || defined(_WIN64)
#include<chrono>
using namespace std::chrono;

static double systemCurrentTime()
{
	steady_clock::time_point time_point;
	time_point = steady_clock::now();
	steady_clock::duration pig = time_point.time_since_epoch();
	return pig.count() / 1000000.0;
}
#else
#include <sys/time.h>
static double systemCurrentTime()
{
	struct timeval tv;
	gettimeofday(&tv, 0);
	return (double)((tv.tv_sec * 1000000) + tv.tv_usec) / 1000.0;
}
#endif

typedef unsigned int uint;

struct TWordSum
{
	char word[6];
	int sum;
	uint charbits;
	TWordSum(const char* word, const int sum=0, const uint charbits=0)
	{
		this->word[5] = 0;
		memcpy(this->word, word, 5);
		this->sum = sum;
		this->charbits = charbits;
	};
};

typedef TAddList<TWordSum, int> TWordSumList;

static int distrib[26];

inline uint offset(char letter) { return letter - 'A'; }

inline bool checkAndSet(uint& seen, char letter)
{
	uint charbit = 0x01 << offset(letter);
	bool result = seen & charbit;
	seen |= charbit;
	return result;
}

inline void charbitSet(uint& charbits, char letter)
{
	uint charbit = 0x01 << offset(letter);
	charbits |= charbit;
}

inline bool charbitSeen(uint& seen, char letter)
{
	uint charbits = 0x01 << offset(letter);
	bool result = seen & charbits;
	return result;
}

static int noWords = 4;
enum { GAP_COUNT = 1 };
static const char* forWords[5];
static uint forCharbits[5];
static uint vowels;
static uint zeroes;

static void setVowels()
{
	for (const char* setChar = "AIOUY"; *setChar; setChar++)
		charbitSet(vowels, *setChar);
}

static void setZeroes()
{
	for (const char* setChar = "XJVZQK"; *setChar; setChar++) // CB
		charbitSet(zeroes, *setChar);
}

static void countLetters(const char* word)
{
	uint seen = 0;
	char letter;
	for (int i = 0; i < 5; i++)
	{
		letter = word[i];
		if (charbitSeen(zeroes, letter)) continue;
		if (checkAndSet(seen, letter) == false)
			distrib[offset(letter)] += GAP_COUNT;
	}
}

static void sumWordLetters(const char* word, int& sumof, unsigned int& mask)
{
	char letter;
	sumof = 0;
	for (int i = 0; i < 5; i++)
	{
		letter = word[i];
		int offset = letter - 'A';
		sumof += distrib[offset];
		mask |= (0x01 << offset);
	}
}

static void addUnique(TWordSumList& wordsLeft, const TWordSum& word, int turn)
{
	char letter;
	uint seen = 0;
	bool hasVowel = false;
	for (int i = 0; i < noWords; i++)
		if (word.charbits == forCharbits[i]) return;
	for (int i = 0; i < 5; i++)
	{
		letter = word.word[i];
		if (turn == 0 && checkAndSet(seen, letter))
			return;
		for (int j = 0; j < noWords; j++)
			if (charbitSeen(forCharbits[j], letter))
				return;
		if (turn == 0)
		{
			if (charbitSeen(vowels, letter))
			{
				if (hasVowel)
					return;
				hasVowel = true;
			}
		}
	}
	TWordSum entry(word.word, word.sum, word.charbits);
	wordsLeft.add(entry);
}

static int wordsSumSort(TWordSum* A, TWordSum* B)
{
	int	n = A->sum - B->sum;
	if (n != 0) return n;
	n = A->charbits - B->charbits;
	if (n != 0) return n;
	n = strncmp(A->word, B->word, 5);
	return n;
}

static bool isAnagram(int i, TWordSumList& words)
{
	// the word sum list is sorted in sum, mask, word order
	TWordSum &currword = words[i], &prevword = words[i-1];
	if (currword.sum != prevword.sum)
		return false;
	if (currword.charbits == prevword.charbits)
		return true;
	return false;
}

static int deriveFive(int turn, TWordSumList& words)
{
	int result = 0;
	TWordSumList wordsLeft(words.getCount());
	noWords = turn;
	if (turn > 4)
	{
		for (int i = 0; i < turn; i++)
			printf("%s\n", forWords[i]);
		return 5;
	}
	for (int i = 0; i < words.getCount(); i++)
	{
		if (turn == 0 && i > 0 && isAnagram(i, words))
			continue;
		addUnique(wordsLeft, words[i], turn);
	}
	for (int i = 0; i < wordsLeft.getCount(); i++)
	{
		forWords[turn] = wordsLeft[i].word;
		forCharbits[turn] = wordsLeft[i].charbits;
		fprintf(LogFile, "turn %d word[%d]=%s %d\n", turn, i, wordsLeft[i].word, wordsLeft[i].sum);
		result = deriveFive(turn + 1, wordsLeft);
		if (result == 5)
		{
			fprintf(stdout, "%d %d\n", turn, words.getCount());
			break;
		}
	}
	return result;
}

struct AutoBuff
{
	char* buff;
	AutoBuff(size_t size)	{	buff = (char*) calloc(size, sizeof(char)); }
	~AutoBuff() { free(buff); }
};

static void loadFromFile(const char* inFileName, TWordSumList& sumList)
{
	FILE* inFile = fopen(inFileName, "rb");
	enum { BUFF_SIZE=1024*1024, LINE_SIZE = 1024 * 256	};
	setvbuf(inFile, 0, _IOFBF, BUFF_SIZE);
	AutoBuff line(LINE_SIZE);
	char word[6];
	word[5] = 0;
	while (!feof(inFile))
	{
		fgets(line.buff, LINE_SIZE, inFile);
		for (int p = 0; true; p += 6)
		{
			memcpy(word, line.buff + p, 5);
			countLetters(word);
			TWordSum entry(word, 0, 0);
			sumList.add(entry);
			if (line.buff[p + 5] != ' ')
				break;
		}
	}
}

static void loadFromCode(TWordSumList& sumList)
{
	for (int i = 0; i < noGameWords; i++)
	{
		const char* word = gameWords[i];
		countLetters(word);
		TWordSum entry(word, 0, 0);
		sumList.add(entry);
	}
}

int main(int argc, char** argv)
{
	int result;
	setVowels();
	setZeroes();
	if (argc > 2)
		LogFile = fopen(argv[2], "wt");
	else
		LogFile = stdout;
	double start = systemCurrentTime();
	TWordSumList sumList(noGameWords);
	if (argc > 1)
		loadFromFile(argv[1], sumList);
	if (argc == 1)
		loadFromCode(sumList);
	double loaded = systemCurrentTime();
	fprintf(stdout, "Loaded %d words load %f mill\n", sumList.getCount(), loaded - start);
	for (int i = 0; i < sumList.getCount(); i++)
		sumWordLetters(sumList[i].word, sumList[i].sum, sumList[i].charbits);
	sumList.compare = wordsSumSort;
	sumList.sort();
	double distrib = systemCurrentTime();
	fprintf(stdout, "Sorted %f sort %f mill\n", distrib - start, distrib - loaded);
	result = deriveFive(0, sumList);
	double ends = systemCurrentTime();
	fprintf(stdout, "Elapsed %f derived %f mill\n", ends - start, ends - distrib);
	return 0;
}
