mod word_list;

use word_list::GAME_WORDS;
const NO_GAME_WORDS: usize = GAME_WORDS.len();

struct TWordSum
{
	word: [&str; 5],
	sum: i32,
	mask: u32
}

fn wordSum(word: &str, sum: i32, mask: u32) -> TWordSum
{
	let result = TWordSum {word, sum, mask};
	//result.word = word;
	//result.sum = sum;
	//result.mask = mask;
	return result;
}



fn main()
{
    println!("word 5 {0} {1}", GAME_WORDS[4], NO_GAME_WORDS);
	let x = wordSum("FREDA", 1234, 0);
}