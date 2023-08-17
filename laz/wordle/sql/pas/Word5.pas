unit Word5;
// This code was generated, do not modify it, modify it at source and regenerate it.

{$mode objfpc}{$H+}

interface

uses Classes, SysUtils, SQLDB, SQLite3Conn;

type TWord5 = Class
  Conn : TSQLite3Connection;
  Tran : TSQLTransaction;
  word : AnsiString;
  status : Integer;
  constructor Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
  procedure Insert;
  procedure Insert(
    const aword : AnsiString
  ; const astatus : Integer
  ); overload;
  procedure Update;
  procedure Update(
    const astatus : Integer
  ; const aword : AnsiString
  ); overload;
  function SelectOne : Boolean;
  function SelectOne(
    const aword : AnsiString
  ) : Boolean; overload;
  function SelectAll : TSQLQuery;
  function nextSelectAll(const Query : TSQLQuery) : Boolean;
  function SelectAllSorted : TSQLQuery;
  function nextSelectAllSorted(const Query : TSQLQuery) : Boolean;
  function ListByStatus : TSQLQuery;
  function ListByStatus(
    const astatus : Integer
  ) : TSQLQuery; overload;
  function nextListByStatus(const Query : TSQLQuery) : Boolean;
end;

type TWord5DictList = Class
  Conn : TSQLite3Connection;
  Tran : TSQLTransaction;
  word : AnsiString;
  constructor Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
  function DictList : TSQLQuery;
  function nextDictList(const Query : TSQLQuery) : Boolean;
end;

var
  Word5Insert : AnsiString =
    'insert into Word5 (' +
    '  word,' +
    '  status' +
    ' ) ' +
    ' values (' +
    '   :word,' +
    '   :status' +
    ' )';

var
  Word5Update : AnsiString =
    'update Word5' +
    ' set' +
    '  status = :status' +
    ' where word = :word';

var
  Word5SelectOne : AnsiString =
    'select' +
    '  status' +
    ' from Word5' +
    ' where word = :word';

var
  Word5SelectAll : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word5';

var
  Word5SelectAllSorted : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word5' +
    ' order by word';

var
  Word5ListByStatus : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word5' +
    ' where status = :status' +
    ' order by word';

var
  Word5DictList : AnsiString =
    'select w.word ' +
    'from Word5 w, Dictionary d ' +
    'where w.word = d.word ';

implementation

constructor TWord5.Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
begin
  Conn := aConn;
  Tran := aTran;
  word := '';
  status := 0;
end;

procedure TWord5.Insert;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word5Insert;
    Query.Params.ParamByName('word').AsString := word;
    Query.Params.ParamByName('status').AsInteger := status;
    Query.ExecSQL;
  finally
    Query.Free;
  end;
end;

procedure TWord5.Insert(
    const aword : AnsiString
  ; const astatus : Integer
); overload;
begin
  word := aword;
  status := astatus;
  Insert;
end;

procedure TWord5.Update;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word5Update;
    Query.Params.ParamByName('status').AsInteger := status;
    Query.Params.ParamByName('word').AsString := word;
    Query.ExecSQL;
  finally
    Query.Free;
  end;
end;

procedure TWord5.Update(
    const astatus : Integer
  ; const aword : AnsiString
); overload;
begin
  status := astatus;
  word := aword;
  Update;
end;

function TWord5.SelectOne : Boolean;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word5SelectOne;
    Query.Params.ParamByName('word').AsString := word;
    Query.Open;
    if not Query.eof then begin
        status := Query.FieldByName('status').AsInteger;
      result := true;
    end
    else
      result := false;
  finally
    Query.Free;
  end;
end;

function TWord5.SelectOne(
    const aword : AnsiString
) : Boolean; overload;
begin
  word := aword;
  result := SelectOne;
end;

function TWord5.SelectAll : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word5SelectAll;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord5.nextSelectAll(const Query : TSQLQuery) : Boolean;
begin
  if not Query.eof then begin
      word := Query.FieldByName('word').AsString;
      status := Query.FieldByName('status').AsInteger;
    result := true;
    Query.next;
  end
  else
    result := false;
end;

function TWord5.SelectAllSorted : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word5SelectAllSorted;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord5.nextSelectAllSorted(const Query : TSQLQuery) : Boolean;
begin
  if not Query.eof then begin
      word := Query.FieldByName('word').AsString;
      status := Query.FieldByName('status').AsInteger;
    result := true;
    Query.next;
  end
  else
    result := false;
end;

function TWord5.ListByStatus : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word5ListByStatus;
    result.Params.ParamByName('status').AsInteger := status;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord5.ListByStatus(
    const astatus : Integer
) : TSQLQuery;
begin
  status := astatus;
  result := ListByStatus;
end;

function TWord5.nextListByStatus(const Query : TSQLQuery) : Boolean;
begin
  if not Query.eof then begin
      word := Query.FieldByName('word').AsString;
      status := Query.FieldByName('status').AsInteger;
    result := true;
    Query.next;
  end
  else
    result := false;
end;

constructor TWord5DictList.Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
begin
  Conn := aConn;
  Tran := aTran;
  word := '';
end;

function TWord5DictList.DictList : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word5DictList;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord5DictList.nextDictList(const Query : TSQLQuery) : Boolean;
begin
  if not Query.eof then begin
      word := Query.FieldByName('word').AsString;
    result := true;
    Query.next;
  end
  else
    result := false;
end;

end.
