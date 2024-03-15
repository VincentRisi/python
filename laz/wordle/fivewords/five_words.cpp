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
#define MEASURE "millis"
double system_current_time()
{
	steady_clock::time_point time_point;
	time_point = steady_clock::now();
	steady_clock::duration pig = time_point.time_since_epoch();
	return pig.count() / 1000000.0;
}
#else
#include <sys/time.h>
#define MEASURE "millis"
double system_current_time()
{
	struct timeval tv;
	gettimeofday(&tv, 0);
	return (double)((tv.tv_sec * 1000000) + tv.tv_usec) / 1000.0;
}
#endif

struct TWordSum
{
	char word[6];
	int sum;
	TWordSum(const char* word, const int sum)
	{
		this->word[5] = 0;
		memcpy(this->word, word, 5);
		this->sum = sum;
	};
};

typedef TAddList<TWordSum, int> TWordSumList;

static int wordsLeftSort(TWordSum* A, TWordSum* B)
{
	int n = B->sum - A->sum;
	if (n == 0)
		n = strncmp(B->word, A->word, 5);
	return n;
}

static int distrib[26];

inline bool haschr(const char* seen, int size, char letter)
{
	for (int i = 0; i < size; i++)
		if (seen[i] == letter)
			return true;
	return false;
}

static int no_words = 4;
enum { gap_count = 1, zero_count = 6 };
static const char* for_words[5];
static const char* vowels;

static void countLetters(const char* word)
{
	char seen[5];
	char letter;
	for (int i = 0; i < 5; i++)
	{
		letter = word[i];
		if (haschr("XJVZQKCB", zero_count, letter)) continue;
		if (haschr(seen, i, letter) == false)
			distrib[letter - 'A'] += gap_count;
		seen[i] = letter;
	}
}

static void sumWordLetters(const char* word, int& sumof)
{
	char letter;
	sumof = 0;
	for (int i = 0; i < 5; i++)
	{
		letter = word[i];
		int offset = letter - 'A';
		sumof += distrib[offset];
	}
}

static void unique(TWordSumList& wordsLeft, const TWordSum& word, int turn)
{
	char letter;
	char seen[6];
	memset(seen, 0, 5);
	bool has_vowel = false;
	for (int i = 0; i < no_words; i++)
		if (strncmp(word.word, for_words[i], 5) == 0) return;
	for (int i = 0; i < 5; i++)
	{
		letter = word.word[i];
		if (turn == 0 && haschr(seen, i, letter))
			return;
		for (int j = 0; j < no_words; j++)
			if (haschr(for_words[j], 5, letter))
				return;
		if (turn == 0)
		{
			if (haschr(vowels, 5, letter))
			{
				if (has_vowel)
					return;
				has_vowel = true;
			}
			seen[i] = letter;
		}
	}
	TWordSum entry(word.word, word.sum);
	wordsLeft.add(entry);
}

static int wordsSumSort(TWordSum* A, TWordSum* B)
{
	int	n = A->sum - B->sum;
	if (n == 0)
		n = strncmp(A->word, B->word, 5);
	return n;
}

static bool isAnagram(int i, TWordSumList& words)
{
	char letter;
	for (int k = i - 1; k >= 0; k--)
	{
		if (words[i].sum != words[k].sum)
			return false;
		for (int j = 0; j < 5; j++)
		{
			letter = words[i].word[j];
			if (haschr(words[k].word, 5, letter) == false)
				return false;
		}
		return true;

	}
	return false;
}

static int deriveFive(int turn, TWordSumList& words)
{
	int result = 0;
	TWordSumList wordsLeft(words.getCount());
	no_words = turn;
	if (turn > 4)
	{
		for (int i = 0; i < turn; i++)
			printf("%s\n", for_words[i]);
		return 5;
	}
	for (int i = 0; i < words.getCount(); i++)
	{
		if (turn == 0 && i > 0 && isAnagram(i, words))
			continue;
		unique(wordsLeft, words[i], turn);
	}
	for (int i = 0; i < wordsLeft.getCount(); i++)
	{
		for_words[turn] = wordsLeft[i].word;
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

static void loadFromFile(const char* in_file_name, TWordSumList& sumList)
{
	FILE* in_file = fopen(in_file_name, "rb");
	setvbuf(in_file, 0, _IOFBF, 1024 * 1024);
#define LINE_SIZE 1024*256
	char line[LINE_SIZE];
	char word[6];
	word[5] = 0;
	while (!feof(in_file))
	{
		fgets(line, LINE_SIZE, in_file);
		for (int p = 0; true; p += 6)
		{
			memcpy(word, line + p, 5);
			countLetters(word);
			TWordSum entry(word, 0);
			sumList.add(entry);
			if (line[p + 5] != ' ')
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
		TWordSum entry(word, 0);
		sumList.add(entry);
	}
}

int main(int argc, char** argv)
{
	int result;
	vowels = "AIOUY";
	if (argc > 2)
		LogFile = fopen(argv[2], "wt");
	else
		LogFile = stdout;
	double start = system_current_time();
	TWordSumList sumList(noGameWords);
	if (argc > 1)
		loadFromFile(argv[1], sumList);
	if (argc == 1)
		loadFromCode(sumList);
	double loaded = system_current_time();
	fprintf(stdout, "Loaded %d words load %f %s\n", sumList.getCount(), loaded - start, MEASURE);
	for (int i = 0; i < sumList.getCount(); i++)
		sumWordLetters(sumList[i].word, sumList[i].sum);
	sumList.compare = wordsSumSort;
	sumList.sort();
	double distrib = system_current_time();
	fprintf(stdout, "Sorted %f sort %f %s\n", distrib - start, distrib - loaded, MEASURE);
	result = deriveFive(0, sumList);
	double ends = system_current_time();
	fprintf(stdout, "Elapsed %f derived %f %s\n", ends - start, ends - distrib, MEASURE);
	return 0;
}
