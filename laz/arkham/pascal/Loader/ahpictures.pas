unit AHPictures;
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
  PictureNos: TStringList;
  
implementation

procedure Add(const aName          : string;
              const aExpansion     : EExpansion;
              const aNo            : integer);
var
  PictureNo : TPictureNo;
begin
  PictureNo := TPictureNo.Create;
  with PictureNo do begin
    name          := aName;
    expansion     := aExpansion;
    no            := aNo;
  end;
  PictureNos.AddObject(aName, PictureNo);
end;

procedure Load();
begin
  Add('AmandaSharpe'   ,EXP_AH,  0);
  Add('AshcanPete'     ,EXP_AH,  1);
  Add('BobJenkins'     ,EXP_AH,  2);
  Add('CarolynFern'    ,EXP_AH,  3);
  Add('DarrellSimmons' ,EXP_AH,  4);
  Add('DexterDrake'    ,EXP_AH,  5);
  Add('GloriaGoldberg' ,EXP_AH,  6);
  Add('HarveyWalters'  ,EXP_AH,  7);
  Add('JennyBarnes'    ,EXP_AH,  8);
  Add('JoeDiamond'     ,EXP_AH,  9);
  Add('KateWinthrop'   ,EXP_AH, 10);
  Add('MandyThompson'  ,EXP_AH, 11);
  Add('MichaelMcGlen'  ,EXP_AH, 12);
  Add('MontereyJack'   ,EXP_AH, 13);
  Add('SisterMary'     ,EXP_AH, 14);
  Add('VincentLee'     ,EXP_AH, 15);
  Add('ABYSS',          EXP_AH,  0);
  Add('ANOTHER',        EXP_AH,  1);
  Add('CELEANO',        EXP_AH,  2);
  Add('DREAMLAND',      EXP_AH,  3);
  Add('GREATRACE',      EXP_AH,  4);
  Add('PLATLENG',       EXP_AH,  5);
  Add('RLYEH',          EXP_AH,  6);
  Add('YUGGOTH',        EXP_AH,  7);
  Add('Byakhee',              EXP_AH,      0);
  Add('ChildOfTheGoat',       EXP_TBGOTW,  1);
  Add('Chthonian',            EXP_AH,      2);
  Add('Cultist',              EXP_AH,      3);
  Add('DarkDruid',            EXP_TBGOTW,  4);
  Add('DarkYoung',            EXP_TBGOTW,  5);
  Add('Dhole',                EXP_AH,      6);
  Add('DimensionalShambler',  EXP_AH,      7);
  Add('ElderThing',           EXP_AH,      8);
  Add('FireVampire',          EXP_AH,      9);
  Add('FlyingPolyp',          EXP_AH,     10);
  Add('FormlessSpawn',        EXP_AH,     11);
  Add('Ghost',                EXP_AH,     12);
  Add('Ghoul',                EXP_AH,     13);
  Add('GoatSpawn',            EXP_TBGOTW, 14);
  Add('GodOfTheBloodyTongue', EXP_AH,     15);
  Add('Gug',                  EXP_AH,     16);
  Add('HaunterOfTheDark',     EXP_AH,     17);
  Add('HighPriest',           EXP_AH,     18);
  Add('HoundOfTindalos',      EXP_AH,     19);
  Add('Maniac',               EXP_AH,     20);
  Add('Mi-Go',                EXP_AH,     21);
  Add('Nightgaunt',           EXP_AH,     22);
  Add('Riot',                 EXP_TKIY,   23);
  Add('Riot2',                EXP_TKIY,   24);
  Add('Riot3',                EXP_TKIY,   25);
  Add('Shoggoth',             EXP_AH,     26);
  Add('StarSpawn',            EXP_AH,     27);
  Add('TheBlackMan',          EXP_AH,     28);
  Add('TheBloatedWoman',      EXP_AH,     29);
  Add('TheDarkPharoah',       EXP_AH,     30);
  Add('Vampire',              EXP_AH,     31);
  Add('Warlock',              EXP_AH,     32);
  Add('Witch',                EXP_AH,     33);
  Add('Zombie',               EXP_AH,     34);
end;
             
initialization
  PictureNos := TStringList.Create;
  Load;
  PictureNos.Sort;
end.

