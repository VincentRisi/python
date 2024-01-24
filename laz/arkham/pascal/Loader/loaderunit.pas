unit LoaderUnit;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,
  AHAncients, AHDistricts, AHEncounters, AHGates, AHInvestigators, AHICards,
  AHLocation, AHMapPlaces, AHMonsters, AHMythos, AHOtherWorlds, AHPictures,
  AHPlaces, AHRoads, AHTypes, AHGamePieces, AHLogger;

type

  { TLoaderForm }

  TLoaderForm = class(TForm)
    LoadButton: TButton;
    SaveButton: TButton;
    MaterialFileEdit: TEdit;
    Label1: TLabel;
    LogMemo: TMemo;
    procedure LoadButtonClick(Sender: TObject);
    procedure SaveButtonClick(Sender: TObject);
  private
    { private declarations }
  public
    { public declarations }
  end;

var
  LoaderForm: TLoaderForm;

implementation

{$R *.lfm}

{ TLoaderForm }

procedure SaveAncients(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Ancients]%s%d', [#9,Ancients.Count]));
  for i := 0 to pred(Ancients.Count) do begin
    with ancients.objects[i] as TAncient do
      writeln(MFile, format('%s%s%d%s%s%s%s%s%s%s%s%s%s%s%s%s%d%s%d',
         [     name
         , #9, expansion
         , #9, combatRating
         , #9, defences
         , #9, worshippers
         , #9, power
         , #9, startOfBattle
         , #9, attack
         , #9, doomTrack
         , #9, useMasks]
         ));
  end;
end;

procedure SaveBackStories(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[BackStories]%s%d', [#9, BackStories.Count]));
  for i := 0 to pred(BackStories.Count) do begin
    with BackStories.objects[i] as TBackStory do
      writeln(MFile, format('%s%s%d%s%s',
      [ name
      , #9, expansion
      , #9, description]
      ));
  end;
end;

procedure SaveDistricts(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Districts]%s%d', [#9, Districts.Count]));
  for i := 0 to pred(Districts.Count) do begin
    with districts.objects[i] as TDistrict do
      writeln(MFile, format('%s%s%d%s%s',
      [ name
      , #9, expansion
      , #9, description]
      ));
  end;
end;

procedure SaveEncounters(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Encounters]%s%d', [#9, Encounters.Count]));
  for i := 0 to pred(Encounters.Count) do begin
    with Encounters.objects[i] as TEncounter do
      writeln(MFile, format('%s%s%d%s%d%s%s',
      [ name
      , #9, expansion
      , #9, no
      , #9, description]
      ));
  end;
end;

procedure SaveFixedPossessions(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[FixedPossessions]%s%d', [#9, Length(FixedPossessions)]));
  for i := 0 to pred(Length(FixedPossessions)) do begin
    with FixedPossessions[i] as TFixedPossession do
      writeln(MFile, format('%s%s%d%s%s',
      [ name
      , #9, expansion
      , #9, item]
      ));
  end;
end;

procedure SaveGates(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Gates]%s%d', [#9, Gates.Count]));
  for i := 0 to pred(Gates.Count) do begin
    with Gates.objects[i] as TGate do
      writeln(MFile, format('%s%s%d%s%s%s%d%s%d',
      [ name
      , #9, expansion
      , #9, description
      , #9, strength
      , #9, faction]
      ));
  end;
end;

procedure SaveInvestigators(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Investigators]%s%d', [#9, Investigators.Count]));
  for i := 0 to pred(Investigators.Count) do begin
    with Investigators.objects[i] as TInvestigator do

      writeln(MFile, format('%s%s%d%s%s%s%s%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%s',
        [     name
        , #9, expansion
        , #9, profession
        , #9, home
        , #9, status
        , #9, sanity
        , #9, stamina
        , #9, clues
        , #9, cash
        , #9, focus
        , #9, speed
        , #9, sneak
        , #9, fight
        , #9, will
        , #9, lore
        , #9, luck
        , #9, common
        , #9, unique
        , #9, spell
        , #9, skill
        , #9, ability]
        ));
  end;
end;

procedure SaveICards(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[ICards]%s%d', [#9, ICards.Count]));
  for i := 0 to pred(ICards.Count) do begin
    with ICards.objects[i] as TICard do
      writeln(MFile, format('%s%s%d%s%s%s%d%s%d%s%d%s%d%s%s%s%s%s%s',
        [     name
        , #9, expansion
        , #9, fullname
        , #9, icardtype
        , #9, noOf
        , #9, cost
        , #9, handed
        , #9, upkeep
        , #9, exhaust
        , #9, description]
        ));
  end;
end;

procedure SaveLocations(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Locations]%s%d', [#9, Locations.Count]));
  for i := 0 to pred(Locations.Count) do begin
    with Locations.objects[i] as TLocation do
      writeln(MFile, format('%s%s%d%s%s%s%d',
      [ name
      , #9, expansion
      , #9, district
      , #9, placeType]
      ));
  end;
end;

procedure SaveMapPlaces(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[MapPlaces]%s%d', [#9, MapPlaces.Count]));
  for i := 0 to pred(MapPlaces.Count) do begin
    with MapPlaces.objects[i] as TMapPlace do
      writeln(MFile, format('%s%s%d%s%d%s%d%s%d%s%d',
      [    name
      ,#9 ,expansion
      ,#9 ,trow
      ,#9 ,brow
      ,#9 ,lcol
      ,#9 ,rcol]
      ));
  end;
end;

procedure SaveMonsters(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Monsters]%s%d', [#9, Monsters.Count]));
  for i := 0 to pred(Monsters.Count) do begin
    with Monsters.objects[i] as TMonster do
      writeln(MFile, format('%s%s%d%s%d%s%d%s%s%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%s',
      [     name
      , #9, expansion
      , #9, monsterType
      , #9, faction
      , #9, attributes
      , #9, awareness
      , #9, sanity
      , #9, sanityloss
      , #9, life
      , #9, stamina
      , #9, staminaloss
      , #9, noof
      , #9, notes]
      ));
  end;
end;

procedure SaveMythoss(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Mythoss]%s%d', [#9, Mythoss.Count]));
  for i := 0 to pred(Mythoss.Count) do begin
    with Mythoss.objects[i] as TMythos do
      writeln(MFile, format('%s%s%d%s%d%s%s%s%s%s%s%s%s%s%s',
      [  name
      , #9, expansion
      , #9, event
      , #9, clue
      , #9, monster
      , #9, white
      , #9, black
      , #9, description]
      ));
  end;
end;

procedure SaveOtherWorlds(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[OtherWorlds]%s%d', [#9, OtherWorlds.Count]));
  for i := 0 to pred(OtherWorlds.Count) do begin
    with OtherWorlds.objects[i] as TOtherWorld do
      writeln(MFile, format('%d%s%d%s%d%s%d%s%s',
      [ groupId
      ,#9 ,expansion
      ,#9 ,place
      ,#9 ,no
      ,#9 ,description]
      ));
  end;
end;

procedure SavePictureNos(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[PictureNos]%s%d', [#9, PictureNos.Count]));
  for i := 0 to pred(PictureNos.Count) do begin
    with PictureNos.objects[i] as TPictureNo do
      writeln(MFile, format('%s%s%d%s%d',
      [ name
      ,#9 ,expansion
      ,#9 ,no]
      ));
  end;
end;

procedure SavePlaces(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Places]%s%d', [#9, Places.Count]));
  for i := 0 to pred(Places.Count) do begin
    with Places.objects[i] as TPlace do
      writeln(MFile, format('%s%s%d%s%s%s%d%s%s%s%s%s%s',
      [    name
      ,#9 ,expansion
      ,#9 ,district
      ,#9 ,stable
      ,#9 ,encounters
      ,#9 ,description
      ,#9 ,special]
      ));
  end;
end;

procedure SaveRoads(var MFile : TextFile);
var
  i : integer;
begin
  writeln(MFile, format('[Roads]%s%d', [#9, Roads.Count]));
  for i := 0 to pred(Roads.Count) do begin
    with Roads.objects[i] as TRoad do
      writeln(MFile, format('%s%s%s%s%d%s%d%s%d',
      [    location1
      ,#9 ,location2
      ,#9 ,expansion
      ,#9 ,direction
      ,#9 ,mpath]
      ));
  end;
end;

procedure TLoaderForm.SaveButtonClick(Sender: TObject);
var
  MFile : TextFile;
begin
  LogMemo.Lines.Add(format('Writing materials to file %s', [MaterialFileEdit.Text]));
  AssignFile(MFile, MaterialFileEdit.Text);
  rewrite(MFile);
  SaveAncients(MFile);
  Flush(MFile);
  SaveBackStories(MFile);
  Flush(MFile);
  SaveDistricts(MFile);
  Flush(MFile);
  SaveEncounters(MFile);
  Flush(MFile);
  SaveGates(MFile);
  Flush(MFile);
  SaveICards(MFile);
  Flush(MFile);
  SaveInvestigators(MFile);
  Flush(MFile);
  SaveFixedPossessions(MFile);
  Flush(MFile);
  SaveLocations(MFile);
  Flush(MFile);
  SaveMapPlaces(MFile);
  Flush(MFile);
  SaveMonsters(MFile);
  Flush(MFile);
  SaveMythoss(MFile);
  Flush(MFile);
  SaveOtherWorlds(MFile);
  Flush(MFile);
  SavePictureNos(MFile);
  Flush(MFile);
  SavePlaces(MFile);
  Flush(MFile);
  SaveRoads(MFile);
  Flush(MFile);
  CloseFile(MFile);
  LogMemo.Lines.Add('done');
end;

procedure TLoaderForm.LoadButtonClick(Sender: TObject);
var
  i : integer;
begin
  LoadGamePieces(MaterialFileEdit.Text, [EXP_AH, EXP_COTDP, EXP_TBGOTW, EXP_TKIY, EXP_TLATT], Logmemo);
  LogMemo.Clear;
  for i := 0 to high(OWorldArrays[Abyss]) do
    LogMemo.Lines.Add(OtherWorldRecs[OWorldArrays[Abyss][i]].description);
end;

initialization
  AHLogger.StartLog('AHLoader.log');
end.

