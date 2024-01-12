unit AHRoads;
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
  Roads: TStringList;

function noOfRoads(location : string) : integer;

implementation

function noOfRoads(location : string) : integer;
var
  i    : integer;
  road : TRoad;
begin
  result := 0;
  for i := 0 to pred(Roads.Count) do begin
    road := TRoad(roads.objects[i]);
    if road.location1 = location then
      inc(result);
  end;
end;

procedure Add(const aLocation1  : string;
              const aLocation2  : string;
              const aExpansion  : EExpansion;
              const aDirection1 : EDirection;
              const aDirection2 : EDirection;
              const aMpath1     : EMonsterPath;
              const aMpath2     : EMonsterPath);
var
  Road : TRoad;
begin
  Road := TRoad.Create;
  with Road do begin
    location1 := aLocation1;
    location2 := aLocation2;
    expansion := aExpansion;
    direction := aDirection1;
    mpath     := aMpath1;
  end;
  Roads.AddObject(Road.GetKey, Road);
  Road := TRoad.Create;
  with Road do begin
    location1 := aLocation2;
    location2 := aLocation1;
    expansion := aExpansion;
    direction := aDirection2;
    mpath     := aMpath2;
  end;
  Roads.AddObject(Road.GetKey, Road);
end;

procedure LoadRoads();
begin
  Add('ABUILDING',   'MUNIVERSITY', EXP_AH, EAST,      WEST,      BLACKWHITE, NONEROUTE);
  Add('ARKASYLUM',   'DOWNTOWN',    EXP_AH, SOUTHWEST, NORTHEAST, BLACKWHITE, NONEROUTE);
  Add('BCAVE',       'RIVERTOWN',   EXP_AH, NORTHWEST, SOUTHEAST, BLACKWHITE, NONEROUTE);
  Add('BOARKHAM',    'DOWNTOWN',    EXP_AH, SOUTH,     NORTH,     BLACKWHITE, NONEROUTE);
  Add('CSHOPPE',     'NORTHSIDE',   EXP_AH, NORTHEAST, SOUTHWEST, BLACKWHITE, NONEROUTE);
  Add('EASTTOWN',    'DOWNTOWN',    EXP_AH, NORTH,     SOUTH,     BLACKROUTE, WHITEROUTE);
  Add('FHILL',       'RIVERTOWN',   EXP_AH, NORTH,     SOUTH,     BLACKROUTE, WHITEROUTE);
  Add('GENSTORE',    'RIVERTOWN',   EXP_AH, NORTHEAST, SOUTHWEST, BLACKWHITE, NONEROUTE);
  Add('GRAVEYARD',   'RIVERTOWN',   EXP_AH, WEST,      EAST,      BLACKWHITE, NONEROUTE);
  Add('HROADHOUSE',  'EASTTOWN',    EXP_AH, SOUTHWEST, NORTHEAST, BLACKWHITE, NONEROUTE);
  Add('HSOCIETY',    'SOUTHSIDE',   EXP_AH, NORTH,     SOUTH,     BLACKWHITE, NONEROUTE);
  Add('INDSQUARE',   'DOWNTOWN',    EXP_AH, WEST,      EAST,      BLACKWHITE, NONEROUTE);
  Add('ISANCTUM',    'FHILL',       EXP_AH, NORTHWEST, DEADEND,   NONEROUTE,  NONEROUTE);
  Add('LIBRARY',     'MUNIVERSITY', EXP_AH, NORTHEAST, SOUTHWEST, BLACKWHITE, NONEROUTE);
  Add('MBHOUSE',     'SOUTHSIDE',   EXP_AH, WEST,      EAST,      BLACKWHITE, NONEROUTE);
  Add('MDISTRICT',   'DOWNTOWN',    EXP_AH, NORTHEAST, SOUTHWEST, NONEROUTE,  NONEROUTE);
  Add('MDISTRICT',   'NORTHSIDE',   EXP_AH, NORTH,     SOUTH,     WHITEROUTE, BLACKROUTE);
  Add('MDISTRICT',   'RIVERTOWN',   EXP_AH, EAST,      WEST,      NONEROUTE,  NONEROUTE);
  Add('MUNIVERSITY', 'FHILL',       EXP_AH, EAST,      WEST,      NONEROUTE,  NONEROUTE);
  Add('MUNIVERSITY', 'MDISTRICT',   EXP_AH, NORTH,     SOUTH,     WHITEROUTE, BLACKROUTE);
  Add('NEWSPAPER',   'NORTHSIDE',   EXP_AH, SOUTHEAST, NORTHWEST, BLACKWHITE, NONEROUTE);
  Add('NORTHSIDE',   'DOWNTOWN',    EXP_AH, EAST,      WEST,      WHITEROUTE, BLACKROUTE);
  Add('PSTATION',    'EASTTOWN',    EXP_AH, NORTHWEST, SOUTHEAST, BLACKWHITE, NONEROUTE);
  Add('RDOCKS',      'MDISTRICT',   EXP_AH, EAST,      WEST,      BLACKWHITE, NONEROUTE);
  Add('RIVERTOWN',   'EASTTOWN',    EXP_AH, NORTH,     SOUTH,     BLACKROUTE, WHITEROUTE);
  Add('SBUILDING',   'MUNIVERSITY', EXP_AH, SOUTHEAST, NORTHWEST, BLACKWHITE, NONEROUTE);
  Add('SCHURCH',     'SOUTHSIDE',   EXP_AH, NORTHWEST, SOUTHEAST, BLACKWHITE, NONEROUTE);
  Add('SOUTHSIDE',   'FHILL',       EXP_AH, NORTH,     SOUTH,     BLACKROUTE, WHITEROUTE);
  Add('STLODGE',     'FHILL',       EXP_AH, NORTHWEST, SOUTHEAST, BLACKWHITE, NONEROUTE);
  Add('STMHOSPITAL', 'UPTOWN',      EXP_AH, EAST,      WEST,      BLACKWHITE, NONEROUTE);
  Add('TSTATION',    'NORTHSIDE',   EXP_AH, SOUTH,     NORTH,     BLACKWHITE, NONEROUTE);
  Add('TUNNAMABLE',  'MDISTRICT',   EXP_AH, NORTHEAST, SOUTHWEST, BLACKWHITE, NONEROUTE);
  Add('TWHOUSE',     'FHILL',       EXP_AH, WEST,      EAST,      BLACKWHITE, NONEROUTE);
  Add('UISLE',       'MDISTRICT',   EXP_AH, SOUTHEAST, NORTHWEST, BLACKWHITE, NONEROUTE);
  Add('UPTOWN',      'MUNIVERSITY', EXP_AH, NORTH,     SOUTH,     WHITEROUTE, BLACKROUTE);
  Add('UPTOWN',      'SOUTHSIDE',   EXP_AH, EAST,      WEST,      BLACKROUTE, WHITEROUTE);
  Add('VDINER',      'EASTTOWN',    EXP_AH, WEST,      EAST,      BLACKWHITE, NONEROUTE);
  Add('WOODS',       'UPTOWN',      EXP_AH, NORTH,     SOUTH,     BLACKWHITE, NONEROUTE);
  Add('YOMSHOPPE',   'UPTOWN',      EXP_AH, NORTHEAST, SOUTHWEST, BLACKWHITE, NONEROUTE);
end;
             
initialization
  Roads := TStringList.Create;
  LoadRoads;
  Roads.Sort;
end.

