unit Word7;
// This code was generated, do not modify it, modify it at source and regenerate it.

{$mode objfpc}{$H+}

interface

uses Classes, SysUtils, SQLDB, SQLite3Conn;

type TWord7 = Class
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
  Word7Insert : AnsiString =
    'insert into Word7 (' +
    '  word,' +
    '  status' +
    ' ) ' +
    ' values (' +
    '   :word,' +
    '   :status' +
    ' )';

var
  Word7Update : AnsiString =
    'update Word7' +
    ' set' +
    '  status = :status' +
    ' where word = :word';

var
  Word7SelectOne : AnsiString =
    'select' +
    '  status' +
    ' from Word7' +
    ' where word = :word';

var
  Word7SelectAll : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word7';

var
  Word7SelectAllSorted : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word7' +
    ' order by word';

var
  Word7ListByStatus : AnsiString =
    'select' +
    '  word' +
    ', status' +
    ' from Word7' +
    ' where status = :status' +
    ' order by word';

implementation

constructor TWord7.Create(const aConn : TSQLite3Connection; const aTran : TSQLTransaction);
begin
  Conn := aConn;
  Tran := aTran;
  word := '';
  status := 0;
end;

procedure TWord7.Insert;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word7Insert;
    Query.Params.ParamByName('word').AsString := word;
    Query.Params.ParamByName('status').AsInteger := status;
    Query.ExecSQL;
  finally
    Query.Free;
  end;
end;

procedure TWord7.Insert(
    const aword : AnsiString
  ; const astatus : Integer
); overload;
begin
  word := aword;
  status := astatus;
  Insert;
end;

procedure TWord7.Update;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word7Update;
    Query.Params.ParamByName('status').AsInteger := status;
    Query.Params.ParamByName('word').AsString := word;
    Query.ExecSQL;
  finally
    Query.Free;
  end;
end;

procedure TWord7.Update(
    const astatus : Integer
  ; const aword : AnsiString
); overload;
begin
  status := astatus;
  word := aword;
  Update;
end;

function TWord7.SelectOne : Boolean;
var
  Query : TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.Database := Conn;
    Query.SQL.Text := Word7SelectOne;
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

function TWord7.SelectOne(
    const aword : AnsiString
) : Boolean; overload;
begin
  word := aword;
  result := SelectOne;
end;

function TWord7.SelectAll : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word7SelectAll;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord7.nextSelectAll(const Query : TSQLQuery) : Boolean;
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

function TWord7.SelectAllSorted : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word7SelectAllSorted;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord7.nextSelectAllSorted(const Query : TSQLQuery) : Boolean;
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

function TWord7.ListByStatus : TSQLQuery;
begin
  result := TSQLQuery.Create(nil);
  try
    result.Database := Conn;
    result.SQL.Text := Word7ListByStatus;
    result.Params.ParamByName('status').AsInteger := status;
    result.Open;
  except
    result.Free;
  end;
end;

function TWord7.ListByStatus(
    const astatus : Integer
) : TSQLQuery;
begin
  status := astatus;
  result := ListByStatus;
end;

function TWord7.nextListByStatus(const Query : TSQLQuery) : Boolean;
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
