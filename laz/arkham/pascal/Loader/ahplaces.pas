unit AHPlaces;
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
  Places: TStringList;
  
implementation

procedure Add(const aName          : string;
              const aExpansion     : EExpansion;
              const aDistrict      : string;
              const aStable        : integer;
              const aEncounters    : string;
              const aDescription   : string;
              const aSpecial       : string);
var
  Place : TPlace;
begin
  Place := TPlace.Create;
  with Place do begin
    name          := aName;
    expansion     := aExpansion;
    district      := aDistrict;
    stable        := aStable;
    encounters    := aEncounters;
    description   := aDescription;
    special       := aSpecial;
  end;
  Places.AddObject(aName, Place);
end;

procedure LoadPlaces();
begin
  Add('ABUILDING',   EXP_AH,  'MUNIVERSITY', 1,  'MONEYS,    SKILLS',   'Administration Building', 'Instead of having an encounter here, you may pay $8 to draw 2 Skills. Keep one of them and discard the other.');
  Add('ARKASYLUM',   EXP_AH,  'DOWNTOWN',    1,  'CLUES,     SANITY',   'Arkham Asylum',           'Instead of having an encounter here, you may recover Sanity by receiving psychiatric care. You may either regain 1 Sanity for free, or pay $2 to restore your Sanity to its maximum value.');
  Add('BCAVE',       EXP_AH,  'RIVERTOWN',   0,  'COMMONS,   SPELLS',   'Black Cave',              '');
  Add('BOARKHAM',    EXP_AH,  'DOWNTOWN',    1,  'BLESSINGS, MONEYS',   'Bank Of Arkham',          'Instead of having an encounter here, you may take out a Bank Loan if you don`t have one yet.');
  Add('CSHOPPE',     EXP_AH,  'NORTHSIDE',   1,  'COMMONS,   UNIQUES',  'Curiositie Shoppe',       'Instead of having an encounter here, you may draw 3 Unique Items and purchase one of them for its list price. Discard the other two items.');
  Add('GENSTORE',    EXP_AH,  'RIVERTOWN',   1,  'COMMONS,   MONEYS',   'General Store',           'Instead of having an encounter here, you may draw 3 Common Items and purchase one of them for its list price. Discard the other two items.');
  Add('GRAVEYARD',   EXP_AH,  'RIVERTOWN',   0,  'CLUES,     UNIQUES',  'Graveyard',               '');
  Add('HROADHOUSE',  EXP_AH,  'EASTTOWN',    0,  'COMMONS,   MONEYS',   'Hibb''s Road House',      '');
  Add('HSOCIETY',    EXP_AH,  'SOUTHSIDE',   0,  'SKILLS,    SPELLS',   'Historical Society',      '');
  Add('INDSQUARE',   EXP_AH,  'DOWNTOWN',    0,  'CLUES,     UNIQUES',  'Independance Square',     '');
  Add('ISANCTUM',    EXP_AH,  'FHILL',       1,  'COMMONS,   UNIQUES',  'Inner Sanctum',           '');
  Add('LIBRARY',     EXP_AH,  'MUNIVERSITY', 1,  'UNIQUES,   SPELLS',   'Library',                 '');
  Add('MBHOUSE',     EXP_AH,  'SOUTHSIDE',   1,  'ALLIES,    STAMINA',  'Ma''s Boarding House',    'Instead of having an encounter here, you may spend 10 toughness worth of monster trophies, 2 gate trophies, or 5 toughness worth of monster trophies and 1 gate trophy to take 1 Ally of your choice from the Ally deck.');
  Add('NEWSPAPER',   EXP_AH,  'NORTHSIDE',   1,  'CLUES,     MONEYS',   'Newspaper',               '');
  Add('PSTATION',    EXP_AH,  'EASTTOWN',    1,  'CLUES,     COMMONS',  'Police Station',          'Instead of having an encounter here, you may spend 10 toughness worth of monster trophies, 2 gate trophies, or 5 toughness worth of monster trophies and 1 gate trophy to take the Deputy of Arkham Card.');
  Add('RDOCKS',      EXP_AH,  'MDISTRICT',   1,  'COMMONS,   MONEYS',   'River Docks',             'Instead of having an encounter here, you may spend 5 toughness worth of monster trophies or 1 gate trophy and get 5 dollars.');
  Add('SBUILDING',   EXP_AH,  'MUNIVERSITY', 0,  'CLUES,     UNIQUES',  'Science Building',        'Instead of having an encounter here, you may spend 5 toughness worth of monster trophies or 1 gate trophy and get 2 Clue tokens.');
  Add('SCHURCH',     EXP_AH,  'SOUTHSIDE',   1,  'BLESSINGS, SANITY',   'South Church',            'Instead of having an encounter here, you may spend 5 toughness worth of monster trophies or 1 gate trophy to have any investigator you choose be Blessed.');
  Add('STLODGE',     EXP_AH,  'FHILL',       0,  'COMMONS,   UNIQUES',  'Silver Twilight Lodge',   'Some encounters in this location can earn investigators a Silver Twilight Lodge Membership. If investigators possess such a membership, they may choose to have an encounter in the Inner Sanctum instead of in the Lodge.');
  Add('STMHOSPITAL', EXP_AH,  'UPTOWN',      1,  'CLUES,     STAMINA',  'St. Mary''s Hospital',    'Instead of having an encounter here, you may recover Stamina by receiving medical care. You may either regain 1 Stamina for free, or pay $2 to restore your Stamina to its maximum value.');
  Add('TSTATION',    EXP_AH,  'NORTHSIDE',   1,  'COMMONS,   UNIQUES',  'Train Station',           '');
  Add('TUNNAMABLE',  EXP_AH,  'MDISTRICT',   0,  'CLUES,     UNIQUES',  'The Unnamable',           '');
  Add('TWHOUSE',     EXP_AH,  'FHILL',       0,  'CLUES,     SPELLS',   'The Witch House',         '');
  Add('UISLE',       EXP_AH,  'MDISTRICT',   0,  'CLUES,     SPELLS',   'Unvisited Isle',          '');
  Add('VDINER',      EXP_AH,  'EASTTOWN',    1,  'MONEYS,    STAMINA',  'Velma''s Diner',          '');
  Add('WOODS',       EXP_AH,  'UPTOWN',      0,  'COMMONS,   MONEYS',   'Woods',                   '');
  Add('YOMSHOPPE',   EXP_AH,  'UPTOWN',      1,  'SPELLS,    UNIQUES',  'Ye Olde Magick Shoppe',   'Instead of having an encounter here, you may pay $5 to draw 2 Spells. Keep one of them and discard the other.');
end;
             
initialization
  Places := TStringList.Create;
  LoadPlaces;
  Places.Sort;
end.

