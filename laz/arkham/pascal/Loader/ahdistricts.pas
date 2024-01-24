unit AHDistricts;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}{$H+}

interface

uses
  Classes, SysUtils, AHTypes;

var
  Districts: TStringList;
  
implementation

procedure Add(const aName          : string;
              const aExpansion     : EExpansion;
              const aDescription   : string);
var
  District : TDistrict;
begin
  District := TDistrict.Create;
  with District do begin
    name          := aName;
    expansion     := aExpansion;
    description   := aDescription;
  end;
  Districts.AddObject(aName, District);
end;

procedure LoadDistricts();
begin
  Add('DOWNTOWN',    EXP_AH, 'Downtown');
  Add('EASTTOWN',    EXP_AH, 'Easttown');
  Add('FHILL',       EXP_AH, 'French Hill');
  Add('MDISTRICT',   EXP_AH, 'Merchant District');
  Add('MUNIVERSITY', EXP_AH, 'Miskatonic University');
  Add('NORTHSIDE',   EXP_AH, 'Northside');
  Add('RIVERTOWN',   EXP_AH, 'Rivertown');
  Add('SOUTHSIDE',   EXP_AH, 'Southside');
  Add('UPTOWN',      EXP_AH, 'Uptown');
end;
             
initialization
  Districts := TStringList.Create;
  LoadDistricts;
  Districts.sort;
end.

