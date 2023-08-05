unit Dictionary;
// This code was generated, do not modify it, modify it at source and regenerate it.

{$mode objfpc}{$H+}

interface

uses Classes, SysUtils, SQLDB, SQLite3Conn;

type TDictionary = Class
  Conn : TSQLite3Connection;
  Tran : TSQLTransaction;
  word : AnsiString;
  meaning : AnsiString;
  constructor Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
  procedure Insert;
  procedure Insert(
    const aword : AnsiString
  ; const ameaning : AnsiString
  ); overload;
  procedure Update;
  procedure Update(
    const ameaning : AnsiString
  ; const aword : AnsiString
  ); overload;
  function SelectOne : Boolean;
  function SelectOne(
    const aword : AnsiString
  ) : Boolean; overload;
end;

type TDictionaryExists = Class
  Conn : TSQLite3Connection;
  Tran : TSQLTransaction;
  word : AnsiString;
  noOf : Integer;
  constructor Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
  function Exists : Boolean;
  function Exists(
    const aword : AnsiString
  ) : Boolean; overload;
end;

var
  DictionaryInsert : AnsiString =
    'insert into Dictionary (' +
    '  word,' +
    '  meaning' +
    ' ) ' +
    ' values (' +
    '   :word,' +
    '   :meaning' +
    ' )';

var
  DictionaryUpdate : AnsiString =
    'update Dictionary' +
    ' set' +
    '  meaning = :meaning' +
    ' where word = :word';

var
  DictionarySelectOne : AnsiString =
    'select' +
    '  meaning' +
    ' from Dictionary' +
    ' where word = :word';

var
  DictionaryExists : AnsiString =
    'select count(*) noOf from Dictionary' +
    ' where word = :word';

implementation

constructor TDictionary.Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
begin
  Conn := aConn;
  Tran := aTran;
  word := '';
  meaning := '';
end;

procedure TDictionary.Insert;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := DictionaryInsert;
    Query.Params.ParamByName('word').AsString := word;
    Query.Params.ParamByName('meaning').AsString := meaning;
    Query.ExecSQL;
  finally
    Query.Destroy;
  end;
end;

procedure TDictionary.Insert(
    const aword : AnsiString
  ; const ameaning : AnsiString
); overload;
begin
  word := aword;
  meaning := ameaning;
  Insert;
end;

procedure TDictionary.Update;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := DictionaryUpdate;
    Query.Params.ParamByName('meaning').AsString := meaning;
    Query.Params.ParamByName('word').AsString := word;
    Query.ExecSQL;
  finally
    Query.Destroy;
  end;
end;

procedure TDictionary.Update(
    const ameaning : AnsiString
  ; const aword : AnsiString
); overload;
begin
  meaning := ameaning;
  word := aword;
  Update;
end;

function TDictionary.SelectOne : Boolean;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := DictionarySelectOne;
    Query.Params.ParamByName('word').AsString := word;
    Query.Open;
    if not Query.eof then begin
        meaning := Query.FieldByName('meaning').AsString;
      result := true;
    end
    else
      result := false;
  finally
    Query.Destroy;
  end;
end;

function TDictionary.SelectOne(
    const aword : AnsiString
) : Boolean; overload;
begin
  word := aword;
  result := SelectOne;
end;

constructor TDictionaryExists.Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
begin
  Conn := aConn;
  Tran := aTran;
  word := '';
  noOf := 0;
end;

function TDictionaryExists.Exists : Boolean;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := DictionaryExists;
    Query.Params.ParamByName('word').AsString := word;
    Query.Open;
    if not Query.eof then begin
        noOf := Query.FieldByName('noOf').AsInteger;
      result := true;
    end
    else
      result := false;
  finally
    Query.Destroy;
  end;
end;

function TDictionaryExists.Exists(
    const aword : AnsiString
) : Boolean; overload;
begin
  word := aword;
  result := Exists;
end;

end.
