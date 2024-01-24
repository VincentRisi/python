unit AHLogger;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}

interface

uses
  Classes, SysUtils;

procedure StartLog(fileName: string);
procedure Log(message: string);

implementation

var
  LogFile: TextFile;

procedure StartLog(fileName: string);
var
  yyyymmddhhnn : string;
begin
  DateTimeToString(yyyymmddhhnn, 'yyyymmddhhnn', now);
  Assign(LogFile, yyyymmddhhnn+fileName);
  Rewrite(LogFile);
end;

procedure Log(message: string);
begin
  writeln(LogFile, format('%s: %s', [datetimetostr(now), message]));
  flush(LogFile);
end;

end.

