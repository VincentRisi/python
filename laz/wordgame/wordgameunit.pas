unit WordGameUnit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, SQLite3Conn, SQLDB, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  Menus, Word5, Word6, Word7, Word8, IniFiles;

type

  { TForm1 }

  TForm1 = class(TForm)
    BEnter: TButton;
    BBack: TButton;
    Sizer: TMenuItem;
    Clear: TMenuItem;
    Possible: TMenuItem;
    Five: TMenuItem;
    Six: TMenuItem;
    Seven: TMenuItem;
    Eight: TMenuItem;
    PopupMenu1: TPopupMenu;
    WL: TEdit;
    LogMemo: TMemo;
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
    procedure FormActivate(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure WordSizeClick(Sender: TObject);
  private
    procedure WriteLog(value : String);
    procedure BoardBuild();
    procedure LoadWords;
    function iniRead(s : string): string;
  public
    property Log : String write WriteLog;
  end;

var
  Form1      : TForm1;
  INI        : TINIFile;
  iniPath    : String;
  dbName     : String;
  hostName   : String;
  Initial    : boolean;
  Alphabet   : AnsiString;
  WordLetter : array of array of TEdit;
  WordSize   : integer;
  Distrib    : array ['A'..'Z'] of integer;
  Conn       : TSQLite3Connection;
  Tran       : TSQLTransaction;
  GameWords  : TStringList;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.WriteLog(value: String);
begin
  LogMemo.Append(value);
end;

procedure TForm1.FormActivate(Sender: TObject);
var
  callResult : string;
begin
  if not Initial then exit;
  Initial    := False;
  iniPath    := Application.Location;
  callResult := iniRead(iniPath);
  LogMemo.Append(callResult);
  Conn     := TSQLite3Connection.Create(nil);
  Tran     := TSQLTransaction.Create(nil);
  Conn.Transaction := Tran;
  Tran.Database := Conn;
  Conn.DatabaseName := dbName;
  Conn.Hostname := hostName;
  Conn.Open;
  Tran.Active := True;
  BoardBuild();
  LoadWords();
end;

procedure TForm1.FormCreate(Sender: TObject);
begin
  Initial  := True;
  Alphabet :=  ' ABCDEFGHIJKLMNOPQRSTUVWXYZ';
end;

procedure TForm1.WordSizeClick(Sender: TObject);
begin
  WordSize := TMenuItem(Sender).Tag;
  BoardBuild();
  LoadWords();
end;

procedure TForm1.BoardBuild();
var
  was, lines, letters, line, letter : integer;
  Edit : TEdit;
begin
  letters := WordSize;
  lines := letters + 1;
  was := length(WordLetter);
  if (was = 0) or (was < lines) then begin
    SetLength(WordLetter, lines, letters);
  end
  else begin
    lines := was;
    letters := was-1;
  end;
  for line := 0 to lines-1 do begin
    for letter := 0 to letters-1 do begin
      if (WordLetter[line][letter] = nil) then begin
        Edit := TEdit.Create(Form1);
        WordLetter[line][letter] := Edit;
        Edit.Parent := Form1;
        Edit.Top := 60+line*32;
        Edit.Left := 48+letter*34;
        Edit.Height := WL.Height;
        Edit.Width := WL.Width;
        Edit.MaxLength := 1;
        Edit.REadOnly := WL.ReadOnly;
        Edit.Font := WL.Font;
        Edit.Alignment := WL.Alignment;
      end
      else begin
        if (line > WordSize) or (letter >= WordSize) then begin
           WordLetter[line][letter].Free;
        end
      end;
    end;
  end;
  SetLength(WordLetter, WordSize + 1, WordSize);
  Form1.Refresh;
end;

procedure TForm1.LoadWords;
  procedure Load5;
  var
    word5 : TWord5;
    query : TSQLQuery;
  begin
    word5 := TWord5.Create(Conn, Tran);
    query := word5.SelectAll;
    while (word5.NextSelectAll(query) = True) do
      GameWords.Append(word5.word);
    word5.Free;
  end;

  procedure Load6;
  var
    word6 : TWord6;
    query : TSQLQuery;
  begin
    word6 := TWord6.Create(Conn, Tran);
    query := word6.SelectAll;
    while (word6.NextSelectAll(query) = True) do
      GameWords.Append(word6.word);
    word6.Free;
  end;

  procedure Load7;
  var
    word7 : TWord7;
    query : TSQLQuery;
  begin
    word7 := TWord7.Create(Conn, Tran);
    query := word7.SelectAll;
    while (word7.NextSelectAll(query) = True) do
      GameWords.Append(word7.word);
    word7.Free;
  end;

  procedure Load8;
  var
    word8 : TWord8;
    query : TSQLQuery;
  begin
    word8 := TWord8.Create(Conn, Tran);
    query := word8.SelectAll;
    while (word8.NextSelectAll(query) = True) do
      GameWords.Append(word8.word);
    word8.Free;
  end;

begin
  if Gamewords = nil then
    GameWords := TStringList.Create
  else
    Gamewords.Clear;
  case WordSize of
  5: Load5;
  6: Load6;
  7: Load7;
  8: Load8;
  end;
  Gamewords.Sort;
  LogMemo.Append(format('GameWords: %d', [GameWords.Count-1]));
end;

function TForm1.iniRead(s: string): string;
begin
  INI := TINIFile.Create('wordgame.ini');
  dbName := INI.ReadString('database','dbName','../wordle/wordle.db');
  hostName := INI.ReadString('database','hostName','localhost');
  WordSize := INI.ReadInteger('database','WordSize',5);
  INI.Destroy;
  result := 'loaded';
end;

end.

