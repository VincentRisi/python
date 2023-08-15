unit Word8;
// This code was generated, do not modify it, modify it at source and regenerate it.

{$mode objfpc}{$H+}

interface

uses Classes, SysUtils, SQLDB, SQLite3Conn;

type TWord8 = Class
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

var
  Word8Insert : AnsiString =
    'insert into Word8 (' +
    '  word,' +
    '  status' +
    ' ) ' +
    ' values (' +
    '   :word,' +
    '   :status' +
    ' )';

var
  Word8Update : AnsiString =
    'update Word8' +
    ' set' +
    '  status = :status' +
    ' where word = :word';

var
  Word8SelectOne : AnsiString =
    'select' +
    '  status' +
    ' from Word8' +
    ' where word = :word';

var
  Word8SelectAll : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word8';

var
  Word8SelectAllSorted : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word8' +
    ' order by word';

var
  Word8ListByStatus : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word8' +
    ' where status = :status' +
    ' order by word';

implementation

constructor TWord8.Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
begin
  Conn := aConn;
  Tran := aTran;
  word := '';
  status := 0;
end;

procedure TWord8.Insert;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word8Insert;
    Query.Params.ParamByName('word').AsString := word;
    Query.Params.ParamByName('status').AsInteger := status;
    Query.ExecSQL;
  finally
    Query.Free;
  end;
end;

procedure TWord8.Insert(
    const aword : AnsiString
  ; const astatus : Integer
); overload;
begin
  word := aword;
  status := astatus;
  Insert;
end;

procedure TWord8.Update;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word8Update;
    Query.Params.ParamByName('status').AsInteger := status;
    Query.Params.ParamByName('word').AsString := word;
    Query.ExecSQL;
  finally
    Query.Free;
  end;
end;

procedure TWord8.Update(
    const astatus : Integer
  ; const aword : AnsiString
); overload;
begin
  status := astatus;
  word := aword;
  Update;
end;

function TWord8.SelectOne : Boolean;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word8SelectOne;
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

function TWord8.SelectOne(
    const aword : AnsiString
) : Boolean; overload;
begin
  word := aword;
  result := SelectOne;
end;

function TWord8.SelectAll : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word8SelectAll;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord8.nextSelectAll(const Query : TSQLQuery) : Boolean;
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

function TWord8.SelectAllSorted : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word8SelectAllSorted;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord8.nextSelectAllSorted(const Query : TSQLQuery) : Boolean;
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

function TWord8.ListByStatus : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word8ListByStatus;
    result.Params.ParamByName('status').AsInteger := status;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord8.ListByStatus(
    const astatus : Integer
) : TSQLQuery;
begin
  status := astatus;
  result := ListByStatus;
end;

function TWord8.nextListByStatus(const Query : TSQLQuery) : Boolean;
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

end.
