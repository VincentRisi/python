unit AHLocation;
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
  Locations: TStringList;

implementation

procedure Add(const aName       : string;
              const aExpansion  : EExpansion;
              const aDistrict   : string;
              const aPlaceType  : EPlaceType);
var
  Location : TLocation;
begin
  Location := TLocation.Create;
  with Location do begin
    name       := aName;
    expansion  := aExpansion;
    district   := aDistrict;
    placeType  := aPlaceType;
  end;
  Locations.AddObject(aName, Location);
end;

procedure LoadLocations();
begin
  Add('ABUILDING',   EXP_AH, 'MUNIVERSITY', PLACE); 
  Add('ARKASYLUM',   EXP_AH, 'DOWNTOWN',    PLACE); 
  Add('BCAVE',       EXP_AH, 'RIVERTOWN',   PLACE); 
  Add('BOARKHAM',    EXP_AH, 'DOWNTOWN',    PLACE);
  Add('CSHOPPE',     EXP_AH, 'NORTHSIDE',   PLACE);
  Add('DOWNTOWN',    EXP_AH, 'DOWNTOWN',    DISTRICT);
  Add('EASTTOWN',    EXP_AH, 'EASTTOWN',    DISTRICT);
  Add('FHILL',       EXP_AH, 'FHILL',       DISTRICT);
  Add('GENSTORE',    EXP_AH, 'RIVERTOWN',   PLACE);
  Add('GRAVEYARD',   EXP_AH, 'RIVERTOWN',   PLACE);
  Add('HROADHOUSE',  EXP_AH, 'EASTTOWN',    PLACE);
  Add('HSOCIETY',    EXP_AH, 'SOUTHSIDE',   PLACE);
  Add('INDSQUARE',   EXP_AH, 'DOWNTOWN',    PLACE);
  Add('ISANCTUM',    EXP_AH, 'FHILL',       PLACE);
  Add('LIBRARY',     EXP_AH, 'MUNIVERSITY', PLACE);
  Add('MBHOUSE',     EXP_AH, 'SOUTHSIDE',   PLACE);
  Add('MDISTRICT',   EXP_AH, 'MDISTRICT',   DISTRICT);
  Add('MUNIVERSITY', EXP_AH, 'MUNIVERSITY', DISTRICT);
  Add('NEWSPAPER',   EXP_AH, 'NORTHSIDE',   PLACE);
  Add('NORTHSIDE',   EXP_AH, 'NORTHSIDE',   DISTRICT);
  Add('PSTATION',    EXP_AH, 'EASTTOWN',    PLACE);
  Add('RDOCKS',      EXP_AH, 'MDISTRICT',   PLACE);
  Add('RIVERTOWN',   EXP_AH, 'RIVERTOWN',   DISTRICT);
  Add('SBUILDING',   EXP_AH, 'MUNIVERSITY', PLACE);
  Add('SCHURCH',     EXP_AH, 'SOUTHSIDE',   PLACE);
  Add('SOUTHSIDE',   EXP_AH, 'SOUTHSIDE',   DISTRICT);
  Add('STLODGE',     EXP_AH, 'FHILL',       PLACE);
  Add('STMHOSPITAL', EXP_AH, 'UPTOWN',      PLACE);
  Add('TSTATION',    EXP_AH, 'NORTHSIDE',   PLACE);
  Add('TUNNAMABLE',  EXP_AH, 'MDISTRICT',   PLACE);
  Add('TWHOUSE',     EXP_AH, 'FHILL',       PLACE);
  Add('UISLE',       EXP_AH, 'MDISTRICT',   PLACE);
  Add('UPTOWN',      EXP_AH, 'UPTOWN',      DISTRICT);
  Add('VDINER',      EXP_AH, 'EASTTOWN',    PLACE);
  Add('WOODS',       EXP_AH, 'UPTOWN',      PLACE);
  Add('YOMSHOPPE',   EXP_AH, 'UPTOWN',      PLACE);
  Add('ABYSS',       EXP_AH, 'ABYSS',       GATE);
  Add('CELEANO',     EXP_AH, 'CELEANO',     GATE);
  Add('ANOTHER',     EXP_AH, 'ANOTHER',     GATE);
  Add('YUGGOTH',     EXP_AH, 'YUGGOTH',     GATE);
  Add('PLATLENG',    EXP_AH, 'PLATLENG',    GATE);
  Add('RLYEH',       EXP_AH, 'RLYEH',       GATE);
  Add('DREAMLAND',   EXP_AH, 'DREAMLAND',   GATE);
  Add('GREATRACE',   EXP_AH, 'GREATRACE',   GATE);
  Add('OUTSKIRTS',   EXP_AH, 'OUTSKIRTS',   OUTTOWN);
  Add('SKY',         EXP_AH, 'SKY',         OUTTOWN);
  Add('SPACETIME',   EXP_AH, 'SPACETIME',   OUTTOWN);
end;
             
initialization
  Locations := TStringList.Create;
  LoadLocations;
  Locations.Sort;
end.

