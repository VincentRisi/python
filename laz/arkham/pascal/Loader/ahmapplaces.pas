unit AHMapPlaces;
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
  MapPlaces       : TStringList;

implementation

procedure Add(const aName        : string;
              const aExpansion   : EExpansion;
              const aTRow, aBRow : integer;
              const aLCol, aRCol : integer);
var
  MapPlace : TMapPlace;
begin
  MapPlace := TMapPlace.Create;
  with MapPlace do begin
    name         := aName;
    expansion    := aExpansion;
    trow         := aTRow;
    brow         := aBRow;
    lcol         := aLCol;
    rcol         := aRCol;
  end;
  MapPlaces.AddObject(aName, MapPlace);
end;

procedure Load;
begin
  Add('ABUILDING',   EXP_AH, 490, 516,   7, 115);
  Add('ABYSS',       EXP_AH, 529, 614, 574, 716);
  Add('ANOTHER',     EXP_AH, 615, 700, 574, 716);
  Add('ARKASYLUM',   EXP_AH,  16,  42, 412, 532);
  Add('BCAVE',       EXP_AH, 385, 413, 405, 492);
  Add('BOARKHAM',    EXP_AH,  16,  38, 268, 384);
  Add('CELEANO',     EXP_AH, 270, 359, 574, 716);
  Add('CSHOPPE',     EXP_AH, 143, 177,  19,  93);
  Add('DOWNTOWN',    EXP_AH, 100, 124, 264, 364);
  Add('DREAMLAND',   EXP_AH, 183, 269, 574, 716);
  Add('EASTTOWN',    EXP_AH, 205, 234, 269, 356);
  Add('FHILL',       EXP_AH, 480, 504, 273, 369);
  Add('GENSTORE',    EXP_AH, 387, 410, 196, 297);
  Add('GRAVEYARD',   EXP_AH, 318, 345, 407, 494);
  Add('GREATRACE',   EXP_AH, 444, 528, 574, 716);
  Add('HROADHOUSE',  EXP_AH, 161, 188, 405, 541);
  Add('HSOCIETY',    EXP_AH, 651, 680, 272, 392);
  Add('INDSQUARE',   EXP_AH, 102, 123, 403, 563);
  Add('ISANCTUM',    EXP_AH, 536, 562, 396, 562);
  Add('LIBRARY',     EXP_AH, 539, 562,  49, 110);
  Add('MBHOUSE',     EXP_AH, 592, 622, 408, 559);
  Add('MDISTRICT',   EXP_AH, 293, 329, 141, 225);
  Add('MUNIVERSITY', EXP_AH, 481, 521, 140, 236);
  Add('NEWSPAPER',   EXP_AH,  61,  87,  18, 110);
  Add('NORTHSIDE',   EXP_AH,  99, 127, 134, 217);
  Add('OUTSKIRTS',   EXP_AH, 749, 850, 388, 488);
  Add('PLATLENG',    EXP_AH,  95, 182, 574, 716);
  Add('PSTATION',    EXP_AH, 260, 283, 407, 510);
  Add('RDOCKS',      EXP_AH, 298, 322,  23, 112);
  Add('RIVERTOWN',   EXP_AH, 303, 328, 272, 361);
  Add('RLYEH',       EXP_AH,   9,  94, 574, 716);
  Add('SBUILDING',   EXP_AH, 434, 460,   7, 129);
  Add('SCHURCH',     EXP_AH, 652, 680, 411, 512);
  Add('SKY',         EXP_AH, 749, 850, 489, 599);
  Add('SOUTHSIDE',   EXP_AH, 596, 621, 275, 363);
  Add('SPACETIME',   EXP_AH, 749, 850, 600, 710);
  Add('STLODGE',     EXP_AH, 536, 562, 396, 562);
  Add('STMHOSPITAL', EXP_AH, 585, 620,  12,  85);
  Add('TSTATION',    EXP_AH,  14,  41, 122, 214);
  Add('TUNNAMABLE',  EXP_AH, 363, 385,  10, 123);
  Add('TWHOUSE',     EXP_AH, 478, 507, 403, 547);
  Add('UISLE',       EXP_AH, 234, 256,  22, 123);
  Add('UPTOWN',      EXP_AH, 594, 617, 140, 216);
  Add('VDINER',      EXP_AH, 209, 220, 408, 512);
  Add('WOODS',       EXP_AH, 647, 675, 147, 200);
  Add('YOMSHOPPE',   EXP_AH, 645, 682,   7, 119);
  Add('YUGGOTH',     EXP_AH, 360, 443, 574, 716);
end;

initialization
  MapPlaces := TStringList.Create;
  Load;
  MapPlaces.Sort;
end.

