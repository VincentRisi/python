#include "four_words.h"

import WordList;
import GetArgs;

#include <stdio.h>

#define DIM(a)  (sizeof(a)/sizeof((a)[0]))

using namespace std;

#include "word_list.h"
static int noGameWords = DIM(gameWords);
static FILE* logFile;
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

static int distrib[26];

static uint offset(char letter) { return letter - 'A'; }

static bool checkAndSet(uint& seen, char letter)
{
	uint charbit = 0x01 << offset(letter);
	bool result = seen & charbit;
	seen |= charbit;
	return result;
}

static void charbitSet(uint& charbits, char letter)
{
	uint charbit = 0x01 << offset(letter);
	charbits |= charbit;
}

static bool charbitSeen(uint& seen, char letter)
{
	uint charbits = 0x01 << offset(letter);
	bool result = seen & charbits;
	return result;
}

static int noWords = 4;
enum { GAP_COUNT = 1 };
static const char* forWords[4];
static uint forCharbits[4];
static uint vowels;
static uint dontuse;

static void setVowels()
{
	for (const char* setChar = "AIOU"; *setChar; setChar++)
		charbitSet(vowels, *setChar);
}

static void setDontUse()
{                           
	for (const char* setChar = "XJVZQ"; *setChar; setChar++) // CB
		charbitSet(dontuse, *setChar);
}

static void addUnique(WordSumList& wordsLeft, const WordSum& word, int turn)
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
	}
	WordSum entry(word.word, word.sum, word.charbits);
	wordsLeft.add(entry);
}

static int wordsSumSort(WordSum* A, WordSum* B)
{
	int n;
	n = B->charbits - A->charbits;
	if (n != 0) return n;
	n = A->sum - B->sum;
	if (n != 0) return n;
	n = strncmp(A->word, B->word, 5);
	return n;
}

static bool isAnagram(int i, WordSumList& words)
{
	// the word sum list is sorted in sum, mask, word order
	WordSum &currword = words[i], &prevword = words[i-1];
	if (currword.sum != prevword.sum)
		return false;
	if (currword.charbits == prevword.charbits)
		return true;
	return false;
}

static int deriveFour(int turn, WordSumList& words)
{
	int result = 0;
	WordSumList wordsLeft(words.getCount());
	noWords = turn;
	if (turn > 3)
	{
		for (int i = 1; i < turn; i++)
			if (strcmp(forWords[i], forWords[i - 1]) < 0) return 4;
		fprintf(logFile, "%s %s %s %s\n", forWords[0], forWords[1], forWords[2], forWords[3]);
		return 4;
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
		result = deriveFour(turn + 1, wordsLeft);
	}
	return result;
}

struct AutoBuff
{
	char* buff;
	AutoBuff(size_t size)	{	buff = (char*) calloc(size, sizeof(char)); }
	~AutoBuff() { free(buff); }
};

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

static bool dropWord(const char* word)
{
	uint seen = 0;
	bool hasVowel = false;
	char letter;
	for (int i = 0; i < 5; i++)
	{
		letter = word[i];
		if (charbitSeen(dontuse, letter)) return true;
		if (checkAndSet(seen, letter) == true) return true;
		if (charbitSeen(vowels, letter))
		{
			if (hasVowel)	return true;
			hasVowel = true;
		}
		distrib[offset(letter)] += GAP_COUNT;
	}
	return false;
}

static void loadFromFile(const char* inFileName, WordSumList& sumList)
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
			if (dropWord(word)) continue;
			WordSum entry(word, 0, 0);
			sumList.add(entry);
			if (line.buff[p + 5] != ' ')
				break;
		}
	}
}

static void loadFromCode(WordSumList& sumList)
{
	for (int i = 0; i < noGameWords; i++)
	{
		const char* word = gameWords[i];
    if (dropWord(word)) continue;
		WordSum entry(word, 0, 0);
		sumList.add(entry);
	}
}

//#include "getargs.h"
static const char* logFileName = "";
static const char* wordFileName = "";
static bool  dontUseY = false;
static bool  dontUseF = false;
static bool  dontUseW = false;

int main(int argc, char** argv)
{
	int result;
	try
	{
		setVowels();
		setDontUse();
		static GetArgList argList;
		GetArg arg_Y('Y', "skipY", &dontUseY, "Do not use Y");
		GetArg arg_F('F', "skipF", &dontUseF, "Do not use F");
		GetArg arg_W('W', "skipW", &dontUseW, "Do not use W");
		GetArg arg_l('l', "logfile", &logFileName, "Log file name.");
		GetArg arg_w('w', "wordfile", &wordFileName, "Words file name.");
		argList.add(arg_Y);
		argList.add(arg_F); 
		argList.add(arg_W);
		argList.add(arg_l);
		argList.add(arg_w);
		argc = getArgs(argc, argv, argList);
		if (strlen(logFileName))
			logFile = fopen(logFileName, "wt");
		else
			logFile = stdout;
		if (dontUseF) charbitSet(dontuse, 'F');
		else if (dontUseY) charbitSet(dontuse, 'Y');
		else charbitSet(dontuse, 'W');
		double start = systemCurrentTime();
		WordSumList sumList(noGameWords);
		if (strlen(wordFileName))
			loadFromFile(wordFileName, sumList);
		if (argc == 1)
			loadFromCode(sumList);
		double loaded = systemCurrentTime();
		fprintf(logFile, "Loaded %d words load %f mill\n", sumList.getCount(), loaded - start);
		for (int i = 0; i < sumList.getCount(); i++)
			sumWordLetters(sumList[i].word, sumList[i].sum, sumList[i].charbits);
		sumList.compare = wordsSumSort;
		sumList.sort();
		double distrib = systemCurrentTime();
		fprintf(logFile, "Sorted %f sort %f mill\n", distrib - start, distrib - loaded);
		result = deriveFour(0, sumList);
		double ends = systemCurrentTime();
		fprintf(logFile, "Elapsed %f derived %f mill\n", ends - start, ends - distrib);
		return 0;
	}
	catch(int err)
	{
		fprintf(logFile, "Exception %d\n", err);
		return err;
	}
}
