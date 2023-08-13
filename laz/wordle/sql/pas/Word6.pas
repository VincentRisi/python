unit Word6;
// This code was generated, do not modify it, modify it at source and regenerate it.

{$mode objfpc}{$H+}

interface

uses Classes, SysUtils, SQLDB, SQLite3Conn;

type TWord6 = Class
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
  function ByStatus : TSQLQuery;
  function ByStatus(
    const astatus : Integer
  ) : TSQLQuery; overload;
  function nextByStatus(const Query : TSQLQuery) : Boolean;
end;

var
  Word6Insert : AnsiString =
    'insert into Word6 (' +
    '  word,' +
    '  status' +
    ' ) ' +
    ' values (' +
    '   :word,' +
    '   :status' +
    ' )';

var
  Word6Update : AnsiString =
    'update Word6' +
    ' set' +
    '  status = :status' +
    ' where word = :word';

var
  Word6SelectOne : AnsiString =
    'select' +
    '  status' +
    ' from Word6' +
    ' where word = :word';

var
  Word6SelectAll : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word6';

var
  Word6SelectAllSorted : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word6' +
    ' order by word';

var
  Word6ByStatus : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word6' +
    ' where status = :status' +
    ' order by word';

implementation

constructor TWord6.Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
begin
  Conn := aConn;
  Tran := aTran;
  word := '';
  status := 0;
end;

procedure TWord6.Insert;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word6Insert;
    Query.Params.ParamByName('word').AsString := word;
    Query.Params.ParamByName('status').AsInteger := status;
    Query.ExecSQL;
  finally
    Query.Destroy;
  end;
end;

procedure TWord6.Insert(
    const aword : AnsiString
  ; const astatus : Integer
); overload;
begin
  word := aword;
  status := astatus;
  Insert;
end;

procedure TWord6.Update;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word6Update;
    Query.Params.ParamByName('status').AsInteger := status;
    Query.Params.ParamByName('word').AsString := word;
    Query.ExecSQL;
  finally
    Query.Destroy;
  end;
end;

procedure TWord6.Update(
    const astatus : Integer
  ; const aword : AnsiString
); overload;
begin
  status := astatus;
  word := aword;
  Update;
end;

function TWord6.SelectOne : Boolean;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word6SelectOne;
    Query.Params.ParamByName('word').AsString := word;
    Query.Open;
    if not Query.eof then begin
        status := Query.FieldByName('status').AsInteger;
      result := true;
    end
    else
      result := false;
  finally
    Query.Destroy;
  end;
end;

function TWord6.SelectOne(
    const aword : AnsiString
) : Boolean; overload;
begin
  word := aword;
  result := SelectOne;
end;

function TWord6.SelectAll : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word6SelectAll;
    result.Open;
  except
    result.Destroy;
  end;
end;

function TWord6.nextSelectAll(const Query : TSQLQuery) : Boolean;
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

function TWord6.SelectAllSorted : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word6SelectAllSorted;
    result.Open;
  except
    result.Destroy;
  end;
end;

function TWord6.nextSelectAllSorted(const Query : TSQLQuery) : Boolean;
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

function TWord6.ByStatus : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word6ByStatus;
    result.Params.ParamByName('status').AsInteger := status;
    result.Open;
  except
    result.Destroy;
  end;
end;

procedure TWord6.ByStatus(
    const astatus : Integer
);
begin
  status := astatus;
  result := ByStatus;
end;

function TWord6.nextByStatus(const Query : TSQLQuery) : Boolean;
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
