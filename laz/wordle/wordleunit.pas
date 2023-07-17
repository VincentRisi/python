unit WordleUnit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, SQLite3Conn, Forms, Controls, Graphics, Dialogs, //Grids,
  StdCtrls, ExtCtrls;

type

  { TWordleForm }

  TWordleForm = class(TForm)
    BEnter: TButton;
    Button1: TButton;
    Button2: TButton;
    Guess1: TEdit;
    Guess2: TEdit;
    Guess3: TEdit;
    Guess4: TEdit;
    Guess5: TEdit;
    Guess6: TEdit;
    L1W1: TEdit;
    L1W2: TEdit;
    L1W3: TEdit;
    L1W4: TEdit;
    L1W5: TEdit;
    L1W6: TEdit;
    L2W1: TEdit;
    L2W2: TEdit;
    L2W3: TEdit;
    L2W4: TEdit;
    L2W5: TEdit;
    L2W6: TEdit;
    L3W1: TEdit;
    L3W2: TEdit;
    L3W3: TEdit;
    L3W4: TEdit;
    L3W5: TEdit;
    L3W6: TEdit;
    L4W1: TEdit;
    L4W2: TEdit;
    L4W3: TEdit;
    L4W4: TEdit;
    L4W5: TEdit;
    L4W6: TEdit;
    L5W1: TEdit;
    L5W2: TEdit;
    L5W3: TEdit;
    L5W4: TEdit;
    L5W5: TEdit;
    L5W6: TEdit;
    LogMemo: TMemo;
    Result1: TEdit;
    Result2: TEdit;
    Result3: TEdit;
    Result4: TEdit;
    Result5: TEdit;
    Result6: TEdit;
    SQLite3Connection: TSQLite3Connection;
    TBA: TPanel;
    TBB: TPanel;
    TBC: TPanel;
    TBD: TPanel;
    TBE: TPanel;
    TBF: TPanel;
    TBG: TPanel;
    TBH: TPanel;
    TBI: TPanel;
    TBJ: TPanel;
    TBK: TPanel;
    TBL: TPanel;
    TBM: TPanel;
    TB0: TPanel;
    TB1: TPanel;
    TB2: TPanel;
    TBN: TPanel;
    TBO: TPanel;
    TBP: TPanel;
    TBQ: TPanel;
    TBR: TPanel;
    TBS: TPanel;
    TBT: TPanel;
    TBU: TPanel;
    TBV: TPanel;
    TBW: TPanel;
    TBX: TPanel;
    TBY: TPanel;
    TBZ: TPanel;
    procedure BEnterClick(Sender: TObject);
    procedure GuessBackspaceClick(Sender: TObject);
    procedure FormActivate(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure LettersClick(Sender: TObject);
    procedure ResultBackspaceClick(Sender: TObject);
  private
    procedure Load;
    procedure Process(no: integer; guesslist, resultlist : array of string);
  public

  end;

var
  FirstTime: boolean;
  WordleForm: TWordleForm;
  WordLetter: Array [1..6, 1..5] of TEdit;
  Guesses   : Array [1..6] of TEdit;
  Results   : Array [1..6] of TEdit;
  Letters   : Array [1..26] of TPanel;
  Alphabet  : AnsiString;
  GameWords : TStringList;
  UsedWords : TStringList;
  CollWords : TStringList;
  CurrWords : TStringList;
  Distrib   : array ['A'..'Z'] of integer;


implementation

{$R *.lfm}

{ TWordleForm }

procedure CountLetters(word : string);
var
  i : integer;
  seen : string;
  letter : char;
begin
  seen := '';
  for i := 1 to 5 do begin
     letter := word[i];
     if (seen.IndexOf(letter) = -1) then inc(Distrib[letter]);
     seen := seen + letter;
  end;
end;

procedure SumWordLetters(word : string; var sumof : integer; var sumlist : string);
var
  plus, endp : string;
  seen : string;
  letter : char;
  n, count : integer;
begin
  sumof   := 0;
  sumlist := '';
  plus    := '(';
  if (currwords.indexof(word) <> -1) then
    endp    := ')'
  else if (usedwords.indexof(word) <> -1) then
    endp  := 'u)'
  else if (collwords.indexof(word) <> -1) then
    endp  := 'c)';
  seen := '';
  for n := 1 to 5 do begin
    letter := word[n];
    if (seen.IndexOf(letter) = -1) then count := Distrib[letter] else count := 1;
    seen := seen + letter;
    sumlist += format('%s%d',[plus,count]);
    plus := ' + ';
    inc(sumof, count);
  end;
  sumlist += endp;
end;

function check(word, guess: string): string;
var
  n,p : integer;
  letter, x : char;
begin
  result := '00000';
  for n := 1 to 5 do begin
    if (guess[n] = word[n]) then begin
      result[n] := '2';
      guess[n] := '2';
      word[n] := '2';
    end;
  end;
  for n := 1 to 5 do begin
    letter := guess[n];
    if (letter = '2') then
      continue;
    for p := 1 to 5 do begin
      x := word[p];
      if (letter = x) then begin
        result[n] := '1';
        word[p] := '1';
        guess[n] := '1';
        break;
      end;
    end;
  end;
end;

function WordSolvesGuessAnswerList(word: string; no: integer; guesslist, resultlist : array of string): boolean;
var
  guess, answer, gives: string;
  i : integer;
begin
  for i:= 0 to no-1 do begin
    guess  := guesslist[i];
    answer := resultlist[i];
    gives := check(word, guess);
    if (gives <> answer) then begin
      result := False;
      exit;
    end;
  end;
  result := True;
end;

procedure TWordleForm.Process(no: integer; guesslist, resultlist : array of string);
var
  WordsLeft : TStringList;
  ShowList  : TStringList;
  word      : string;
  sumlist   : string;
  detail    : string;
  i : integer;
  sumof : integer;
begin
  sumof := 0;
  sumlist := '';
  WordsLeft := TStringList.Create;
  for i:= 0 to CurrWords.Count - 1 do begin
    word := CurrWords.strings[i];
    if (WordSolvesGuessAnswerList(word, no, guesslist, resultlist)) then begin
      CountLetters(word);
      WordsLeft.Append(word);
    end;
  end;
  if (WordsLeft.Count = 0) then begin
    for i:= 0 to CollWords.Count - 1 do begin
      word := CollWords.strings[i];
      if (WordSolvesGuessAnswerList(word, no, guesslist, resultlist)) then begin
        WordsLeft.Append(word);
      end;
    end;
  end;
  if (WordsLeft.Count <> 0) then begin
    ShowList := TStringList.Create;
    for i:= 0 to WordsLeft.Count - 1 do begin
      word := WordsLeft.strings[i];
      SumWordLetters(word, sumof, sumlist);
      detail := Format('%04d %s %s',[sumof, word, sumlist]);
      ShowList.Append(detail);
    end;
    ShowList.Sort;
    for i := 0 to ShowList.Count - 1 do begin
      LogMemo.Append(ShowList[i]);
    end;
  end;
end;

procedure TWordleForm.Load;
var
  i : integer;
  word : string;
  procedure LoadWords(wordList: TStringList; fileName: ansistring);
  var
    i : integer;
    wordsIn: TextFile;
    words: ansistring;
    slist:  TStringArray;
    delim: array [1..1] of char;
  begin
    delim[1] := ' ';
    assignFile(wordsIn, fileName);
    reset(wordsIn);
    while not EOF(wordsIn) do begin
      readln(wordsIn, words);
      words := words.ToUpper;
      slist := words.Split(delim);
      for i := 0 to length(slist)-1 do begin
        wordList.Append(slist[i]);
      end;
    end;
    CloseFile(wordsIn);
  end;
begin
  LoadWords(GameWords, 'gamewords.txt');
  LoadWords(UsedWords, 'usedwords.txt');
  LoadWords(CollWords, 'collins2019.txt');
  LogMemo.Append(format('GameWords: %d', [GameWords.Count-1]));
  LogMemo.Append(format('UsedWords: %d', [UsedWords.Count-1]));
  LogMemo.Append(format('CollWords: %d', [CollWords.Count-1]));
  CurrWords := TStringList.Create;
  for i := 0 to GameWords.Count-1 do begin
    word := GameWords.Strings[i];
    if UsedWords.IndexOf(word) >= 0 then continue;
    CurrWords.Add(word);
  end;
  LogMemo.Append(format('CurrWords: %d', [CurrWords.Count-1]));
end;

procedure SetWordLetter(letter, w, l, colour : integer);
begin
   WordLetter[w,l].Text := Alphabet[letter+1];
   WordLetter[w,l].Color := colour;
end;

procedure SetLetter(letter, colour : integer);
begin
   Letters[letter].Color := colour;
end;

procedure ClearWordLetters();
var
  letter, w,l : integer;
  ch : char;
begin
  for w := 1 to 6 do begin
      for l := 1 to 5 do begin
          SetWordLetter(0,w,l,clDefault);
      end;
  end;
  for letter := 1 to 26 do
      SetLetter(letter, clDefault);
  for ch := 'A' to 'Z' do
      Distrib[ch] := 0;
end;

procedure DisplayGuess(w : integer; guess, answer: ansistring);
var
  l,g: integer;
  a: char;
  colour: integer;
begin
  for l := 1 to 5 do begin
      g := Alphabet.IndexOf(guess[l]);
      a := answer[l];
      case a of
         '0' : colour := clSilver;
         '1' : colour := clYellow;
         '2' : colour := clLime;
         else colour := clDefault;
      end;
      SetWordLetter(g,w,l,colour);
      SetLetter(g, colour);
  end;
end;

procedure TWordleForm.BEnterClick(Sender: TObject);
var
  w,no: integer;
  guess, answer : ansistring;
  guesslist, resultlist : array [0..5] of string;
  //word : string;
begin
  LogMemo.Clear;
  ClearWordLetters;
  no := 0;
  for w := 1 to 6 do begin
    guess := guesses[w].Text;
    answer := results[w].Text;
    if (length(guess) = 5) and (length(answer) = 5) then no := w else break;
  end;
  for w := 1 to no do begin
    guess := guesses[w].Text;
    answer := results[w].Text;
    guesslist[w-1] := guess;
    resultlist[w-1] := answer;
    DisplayGuess(w, guess, answer);
  end;
  Process(no, guesslist, resultlist);
end;

procedure TWordleForm.GuessBackspaceClick(Sender: TObject);
var
  i, len : integer;
  edit : TEdit;
begin
  for i := 6 downto 1 do begin
    edit := Guesses[i];
    len := length(edit.Text);
    if (len > 0) then begin
      if (len = 1) then
        edit.text := ''
      else
        edit.text := copy(edit.text, 1, len-1);
      break;
    end;
  end;
end;

procedure TWordleForm.FormActivate(Sender: TObject);
begin
   if (FirstTime = False) then Exit;
   FirstTime := False;
   SQLite3Connection.Open;
   Load;
end;

procedure TWordleForm.FormCreate(Sender: TObject);
begin
   FirstTime := True;
   SQLiteLibraryName := '.\sqlite3.dll';
   GameWords     := TStringList.Create;
   UsedWords     := TStringList.Create;
   CollWords  := TStringList.Create;
   Alphabet :=  ' ABCDEFGHIJKLMNOPQRSTUVWXYZ';
   WordLetter[1, 1] := L1W1;
   WordLetter[1, 2] := L2W1;
   WordLetter[1, 3] := L3W1;
   WordLetter[1, 4] := L4W1;
   WordLetter[1, 5] := L5W1;
   WordLetter[2, 1] := L1W2;
   WordLetter[2, 2] := L2W2;
   WordLetter[2, 3] := L3W2;
   WordLetter[2, 4] := L4W2;
   WordLetter[2, 5] := L5W2;
   WordLetter[3, 1] := L1W3;
   WordLetter[3, 2] := L2W3;
   WordLetter[3, 3] := L3W3;
   WordLetter[3, 4] := L4W3;
   WordLetter[3, 5] := L5W3;
   WordLetter[4, 1] := L1W4;
   WordLetter[4, 2] := L2W4;
   WordLetter[4, 3] := L3W4;
   WordLetter[4, 4] := L4W4;
   WordLetter[4, 5] := L5W4;
   WordLetter[5, 1] := L1W5;
   WordLetter[5, 2] := L2W5;
   WordLetter[5, 3] := L3W5;
   WordLetter[5, 4] := L4W5;
   WordLetter[5, 5] := L5W5;
   WordLetter[6, 1] := L1W6;
   WordLetter[6, 2] := L2W6;
   WordLetter[6, 3] := L3W6;
   WordLetter[6, 4] := L4W6;
   WordLetter[6, 5] := L5W6;
   Guesses[1] := Guess1;
   Guesses[2] := Guess2;
   Guesses[3] := Guess3;
   Guesses[4] := Guess4;
   Guesses[5] := Guess5;
   Guesses[6] := Guess6;
   Results[1] := Result1;
   Results[2] := Result2;
   Results[3] := Result3;
   Results[4] := Result4;
   Results[5] := Result5;
   Results[6] := Result6;
   Letters[1]  := TBA;
   Letters[2]  := TBB; 
   Letters[3]  := TBC; 
   Letters[4]  := TBD; 
   Letters[5]  := TBE;
   Letters[6]  := TBF;
   Letters[7]  := TBG;
   Letters[8]  := TBH;
   Letters[9]  := TBI;
   Letters[10] := TBJ;
   Letters[11] := TBK;
   Letters[12] := TBL;
   Letters[13] := TBM;
   Letters[14] := TBN;
   Letters[15] := TBO;
   Letters[16] := TBP;
   Letters[17] := TBQ;
   Letters[18] := TBR;
   Letters[19] := TBS;
   Letters[20] := TBT;
   Letters[21] := TBU;
   Letters[22] := TBV;
   Letters[23] := TBW;
   Letters[24] := TBX;
   Letters[25] := TBY;
   Letters[26] := TBZ;
end;

procedure TWordleForm.LettersClick(Sender: TObject);
var
  i : integer;
  edit: TEdit;
  ch: char;
begin
  with Sender as TPanel do
    ch := Caption[1];
  if 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.Contains(ch) then begin
    for i := 1 to 6 do begin
      edit := Guesses[i];
      if length(edit.Text) < 5 then begin
        edit.Text := edit.Text+ch;
        break;
      end;
    end;
  end
  else if '012'.Contains(ch) then begin
    for i := 1 to 6 do begin
      edit := Results[i];
      if length(edit.Text) < 5 then begin
        edit.Text := edit.Text+ch;
        break;
      end;
    end;
  end;
end;

procedure TWordleForm.ResultBackspaceClick(Sender: TObject);
var
  i, len : integer;
  edit : TEdit;
begin
  for i := 6 downto 1 do begin
    edit := Results[i];
    len := length(edit.Text);
    if (len > 0) then begin
      if (len = 1) then
        edit.text := ''
      else
        edit.text := copy(edit.text, 1, len-1);
      break;
    end;
  end;
end;


end.

