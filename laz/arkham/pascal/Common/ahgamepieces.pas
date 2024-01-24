unit AHGamePieces;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}{$H+}

interface

uses
  Classes, SysUtils, StdCtrls, AHTypes, Types, AHLogger;

type
  TAHBaseRecs         = array of AHBase;
var
  AncientRecs         : array of TAncient;
  BackStoryRecs       : array of TBackStory;
  DistrictRecs        : array of TDistrict;
  EncounterRecs       : array of TEncounter;
  EncounterCountRecs  : array of TEncounterCount;
  FixedPossessionRecs : array of TFixedPossession;
  GateRecs            : array of TGate;
  GamePlaceRecs       : array of TGamePlace;
  InvestigatorRecs    : array of TInvestigator;
  ICardRecs           : array of TICard;
  LocationRecs        : array of TLocation;
  MapPlaceRecs        : array of TMapPlace;
  MonsterRecs         : array of TMonster;
  MythosRecs          : array of TMythos;
  OtherWorldRecs      : array of TOtherWorld;
  PictureNoRecs       : array of TPictureNo;
  PlaceRecs           : array of TPlace;
  RoadRecs            : array of TRoad;
  GateArray           : array of integer;
  MonsterArray        : array of integer;
  ICardArrays         : array [EICardType]   of TIntegerDynArray;
  ICardDecks          : array [EICardType]   of TCardDeck;
  OWorldArrays        : array [EOWorldPlace] of TIntegerDynArray;
  OWorldDecks         : array [EOWorldPlace] of TCardDeck;
  AncientCards        : TCardDeck;
  InvestigatorCards   : TCardDeck;
  GateCards           : TCardDeck;
  MonsterCards        : TCardDeck;
  MythosCards         : TCardDeck;

procedure LoadGamePieces(const filename : string; aExpansions : SExpansion; memo : TMemo);

function Search(const Recs : TAHBaseRecs; key : string) : integer;
function AncientIndexOf(name : string) : integer;
function BackStoryIndexOf(name : string) : integer;
function ICardIndexOf(name : string) : integer;
function MapPlaceIndexOf(name : string) : integer;
function DistrictIndexOf(name:string) : integer;
function NearestDistrictWithPlayer(name : string) : integer;
function SameDistrictWithPlayer(name : string) : integer;
function EncounterIndexOf(name:string; no:integer) : integer;
function EncounterCountIndexOf(name:string) : integer;
function GateIndexOf(name:string) : integer;
function GamePlaceIndexOf(name:string) : integer;
function InvestigatorIndexOf(name:string) : integer;
function LocationIndexOf(name:string) : integer;
function MonsterIndexOf(name:string) : integer;
function MythosIndexOf(name:string) : integer;
function OtherWorldIndexOf(groupId:EOWorldGroup; place:EOWorldPlace; no:integer) : integer;
function PictureNoIndexOf(name:string) : integer;
function PlaceIndexOf(name:string) : integer;
function RoadIndexOf(location1:string; location2:string) : integer;
function FirstRoadIndexOf(location1:string) : integer;
function RoadNextMonsterPlace(name: string; path: SMonsterPath) : integer;

function GetRange(no : integer): TIntegerDynArray;
function GetPlaceEncounter(name : string) : string;
function GetLocationDescription(name : string; var special : string) : string;
function SplitWrap(value: string; size: integer) : TStringDynArray;
function Split(const value: string) : TStringDynArray;

procedure Log(message: string);

implementation

function SplitWrap(value: string; size: integer) : TStringDynArray;
var
  work, wrapped : string;
  e, no    : integer;
  function warptext(size : integer) : string;
  var
    i, k : integer;
    done : boolean;
  begin
    result := value+#10;
    i := 0;
    repeat
      if i + size < length(result) then begin
        done := false;
        for k := i + size downto i do begin
          if result[k] = ' ' then begin
            result[k] := #10;
            i := k+1;
            done := true;
            break;
          end
        end;
        if done = false then begin
          k := i + size;
          insert(#10, result, k);
          i := k + 1;
        end;
      end else begin
        break;
      end;
    until i > length(result);
  end;
begin
  wrapped := warptext(size);
  work    := wrapped;
  no := 0;
  repeat
    e := pos(#10, work);
    if e <> 0 then begin
      inc(no);
      work := copy(work, e+1, length(work));
    end;
  until (length(work) = 0) or (e = 0);
  setlength(result, no);
  work    := wrapped;
  no := 0;
  repeat
    e := pos(#10, work);
    if e <> 0 then begin
      result[no] := copy(work, 1, e-1);
      inc(no);
      work := copy(work, e+1, length(work));
    end;
  until (length(work) = 0) or (e = 0);
end;

function Split(const value: string): TStringDynArray;
var
  work : string;
  no, e : integer;
begin
  work := value+',';
  no := 0;
  repeat
    e := pos(',', work);
    if e <> 0 then begin
      inc(no);
      work := copy(work, e+1, length(work));
    end;
  until (length(work) = 0) or (e = 0);
  setlength(result, no);
  work := value+',';
  no := 0;
  repeat
    e := pos(',', work);
    if e <> 0 then begin
      result[no] := trim(copy(work, 1, e-1));
      inc(no);
      work := copy(work, e+1, length(work));
    end;
  until (length(work) = 0) or (e = 0);
end;

procedure Log(message: string);
begin
  AHLogger.Log(format('ahgamepieces: %s',[message]));
end;

function Search(const recs: TAHBaseRecs; key: string): integer;
var
  hi, lo : integer;
begin
  lo := 0;
  hi := high(recs);
  while lo <= hi do begin
    result := (lo + hi) div 2;
    if key = recs[result].GetKey then
      exit
    else if key < recs[result].GetKey then
      hi := result - 1
    else
      lo := result + 1;
  end;
  result := -1;
end;

function AncientIndexOf(name: string): integer;
begin
  result := Search(TAHBaseRecs(AncientRecs), name);
end;

function BackStoryIndexOf(name: string): integer;
begin
  result := Search(TAHBaseRecs(BackStoryRecs), name);
end;

function ICardIndexOf(name :string) : integer;
begin
  result := Search(TAHBaseRecs(ICardRecs), name);
end;

function MapPlaceIndexOf(name :string) : integer;
begin
  result := Search(TAHBaseRecs(MapPlaceRecs), name);
end;

function DistrictIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(DistrictRecs), name);
end;

function NearestDistrictWithPlayer(name: string): integer;
var
  i, j, k, r1, c1 : integer;
  no, r2, c2, rd1, cd1, rd2, cd2 : integer;
  mapPlace : TMapPlace;
  gamePlace : TGamePlace;
begin
  log('NearestDistrictWithPlayer');
  result := -1;
  i := MapPlaceIndexOf(name);
  if i = -1 then exit;
  with MapPlaceRecs[i] do begin
    r1 := trow + brow div 2;
    c1 := lcol + rcol div 2;
  end;
  rd1 := 999999;
  cd1 := 999999;
  for i := 0 to high(DistrictRecs) do begin
    j := MapPlaceIndexOf(DistrictRecs[i].name);
    k := GamePlaceIndexOf(DistrictRecs[i].name);
    if k = -1 then continue;
    if length(GamePlaceRecs[k].playerNos) = 0 then continue;
    with MapPlaceRecs[j] do begin
      r2 := trow + brow div 2;
      c2 := trow + brow div 2;
      rd2 := (r2-r1)*(r2-r1);
      cd2 := (c2-c1)*(c2-c1);
      if (rd1+cd1) > (rd2+cd2) then begin
        result := i;
        rd1 := rd2;
        cd1 := cd2;
      end;
    end;
  end;
end;

function SameDistrictWithPlayer(name: string): integer;
var
  i,j : integer;
  district : string;
begin
  log('SameDistrictWithPlayer');
  result := -1;
  i := LocationIndexOf(name);
  if i = -1 then begin
    log(format('warning: No district found for %s', [name]));
    exit;
  end;
  district := LocationRecs[i].district;
  for i := 0 to high(LocationRecs) do begin
    if LocationRecs[i].district = district then begin
      j := GamePlaceIndexOf(LocationRecs[i].name);
      if i = -1 then begin
        log(format('warning: No GamePlace found for %s', [LocationRecs[i].name]));
        exit;
      end;
      if length(GamePlaceRecs[j].playerNos) > 0 then begin
        result := j;
        exit;
      end;
    end;
  end;
end;

function EncounterIndexOf(name:string; no:integer) : integer;
begin
  result := Search(TAHBaseRecs(EncounterRecs), TEncounter.Key(name,no));
end;

function EncounterCountIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(EncounterCountRecs), name);
end;

function GateIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(GateRecs), name);
end;

function GamePlaceIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(GamePlaceRecs), name);
end;

function InvestigatorIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(InvestigatorRecs), name);
end;

function LocationIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(LocationRecs), name);
end;

function MonsterIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(MonsterRecs), name);
end;

function MythosIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(MythosRecs), name);
end;

function OtherWorldIndexOf(groupId:EOWorldGroup; place:EOWorldPlace; no:integer) : integer;
begin
  result := Search(TAHBaseRecs(OtherWorldRecs), TOtherWorld.Key(groupId, place, no));
end;

function PictureNoIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(PictureNoRecs), name);
end;

function PlaceIndexOf(name:string) : integer;
begin
  result := Search(TAHBaseRecs(PlaceRecs), name);
end;

function RoadIndexOf(location1:string; location2:string) : integer;
begin
  result := Search(TAHBaseRecs(RoadRecs), TRoad.Key(location1, location2));
end;

function FirstRoadIndexOf(location1: string): integer;
begin
  for result := 0 to high(RoadRecs) do begin
    if RoadRecs[result].location1 = location1 then exit;
  end;
  result := -1;
end;

function RoadNextMonsterPlace(name: string; path: SMonsterPath): integer;
var
  i : integer;
  road : TRoad;
begin
  result := FirstRoadIndexOf(name);
  if result = -1 then begin
    log(format('error: cannot move monster due to no road map for %s.',[name]));
    exit;
  end;
  repeat
    road := RoadRecs[result];
    if road.mpath in path then exit;
    inc(result);
  until (result > high(RoadRecs)) or (RoadRecs[result].location1 <> name);
  result := -1;
end;

function GetRange(no : integer): TIntegerDynArray;
var
  i : integer;
begin
  setlength(result, no);
  for i := 0 to high(result) do result[i] := i;
end;

function GetPlaceEncounter(name : string) : string;
var
  i,j,no : integer;
  encounterCount : TEncounterCount;
  encounter      : TEncounter;
begin
  result := '';
  i := EncounterCountIndexOf(name);
  if i = -1 then exit;
  encounterCount := EncounterCountRecs[i];
  no := Random(encounterCount.count)+1;
  Log(format('No of encounters for %s=%d %d chosen', [name, encounterCount.count, no]));
  j := EncounterIndexOf(name, no);
  if j = -1 then exit;
  encounter := EncounterRecs[j];
  result := encounter.description;
end;

function GetLocationDescription(name : string; var special : string) : string;
var
  index     : integer;
  location  : TLocation;
  place1    : TPlace;
  district1 : TDistrict;
  gate1     : TGate;
begin
  Log('GetLocationDescription');
  result := name;
  special := '';
  index := LocationIndexOf(name);
  if index = -1 then exit;
  location := LocationRecs[index];
  case location.placeType of
    PLACE: begin
      index := PlaceIndexOf(name);
      if index = -1 then exit;
      place1 := PlaceRecs[index];
      result := place1.description;
      special := place1.special;
    end;
    DISTRICT: begin
      index := DistrictIndexOf(name);
      if index = -1 then exit;
      district1 := DistrictRecs[index];
      result := district1.description;
    end;
    GATE: begin
      index := GateIndexOf(name);
      if index = -1 then exit;
      gate1 := GateRecs[index];
      result := gate1.description;
    end;
    OUTTOWN: begin
    end;
  end;
end;

procedure SetupICardDecks;
var
  noOf            : array [EICardType] of integer;
  i               : integer;
  eIndex              : EICardType;
  icard           : TICard;
  procedure AddCardToList(var cardList : array of integer; var noOf : integer; cardId : integer; count : integer);
  var
    i: integer;
  begin
    for i := 0 to pred(count) do begin
      cardList[noOf] := cardId;
      inc(noOf);
    end;
  end;
begin
  Log('SetupICardDecks');
  for eIndex := low(EICardType) to high(EICardType) do
    noOf[eIndex] := 0;
  for i := 0 to High(ICardRecs) do begin
    icard := ICardRecs[i];
    inc(noOf[icard.icardtype], icard.noOf);
  end;
  for eIndex := low(EICardType) to high(EICardType) do
    setLength(ICardArrays[eIndex], noOf[eIndex]);
  for eIndex := Ally to Unique do
    noOf[eIndex] := 0;
  for i := 0 to High(ICardRecs) do begin
    icard := ICardRecs[i];
    eIndex := icard.icardtype;
    AddCardToList(ICardArrays[eIndex], noOf[eIndex], i, icard.noOf);
  end;
end;

procedure SetupOtherWorldDecks;
var
  noOf : array [EOWorldPlace] of integer;
  i           : integer;
  eIndex      : EOWorldPlace;
  otherWorld  : TOtherWorld;
  procedure AddCardToList(var cardList: TIntegerDynArray; var noOf : integer; cardNo : integer);
  begin
    cardList[noOf] := cardNo;
    inc(noOf);
  end;
begin
  Log('SetupOtherWorldDecks');
  for eIndex := low(EOWorldPlace) to high(EOWorldPlace) do
    noOf[eIndex] := 0;
  for i := 0 to high(OtherWorldRecs) do begin
    otherWorld := OtherWorldRecs[i];
    with otherWorld do begin
      if (place = ABYSS)     or ((place = ANOTHER) and (groupId in [GROUPR, GROUPB]))  then inc(noOf[Abyss]);
      if (place = ANOTHER)                                                             then inc(noOf[AnOther]);
      if (place = CELEANO)   or ((place = ANOTHER) and (groupId in [GROUPB, GROUPG]))  then inc(noOf[Celeano]);
      if (place = DREAMLAND) or  (place = ANOTHER)                                     then inc(noOf[Dreamland]);
      if (place = GREATRACE) or ((place = ANOTHER) and (groupId in [GROUPG, GROUPY]))  then inc(noOf[GreatRace]);
      if (place = PLATLENG)  or ((place = ANOTHER) and (groupId in [GROUPR, GROUPG]))  then inc(noOf[Platleng]);
      if (place = RLYEH)     or ((place = ANOTHER) and (groupId in [GROUPR, GROUPY]))  then inc(noOf[Rlyeh]);
      if (place = YUGGOTH)   or ((place = ANOTHER) and (groupId in [GROUPB, GROUPY]))  then inc(noOf[Yuggoth]);
    end;
  end;
  for eIndex := low(EOWorldPlace) to high(EOWorldPlace) do
    setLength(OWorldArrays[eIndex], noOf[eIndex]);
  for eIndex := low(EOWorldPlace) to high(EOWorldPlace) do
    noOf[eIndex] := 0;
  for i := 0 to high(OtherWorldRecs) do begin
    otherWorld := OtherWorldRecs[i];
    with otherWorld do begin
      if (place = ABYSS)     or ((place = ANOTHER) and (groupId in [GROUPR, GROUPB])) then AddCardToList(OWorldArrays[Abyss],     noOf[Abyss],     i);
      if (place = ANOTHER)                                                            then AddCardToList(OWorldArrays[AnOther],   noOf[AnOther],   i);
      if (place = CELEANO)   or ((place = ANOTHER) and (groupId in [GROUPB, GROUPG])) then AddCardToList(OWorldArrays[Celeano],   noOf[Celeano],   i);
      if (place = DREAMLAND) or  (place = ANOTHER)                                    then AddCardToList(OWorldArrays[Dreamland], noOf[Dreamland], i);
      if (place = GREATRACE) or ((place = ANOTHER) and (groupId in [GROUPG, GROUPY])) then AddCardToList(OWorldArrays[GreatRace], noOf[GreatRace], i);
      if (place = PLATLENG)  or ((place = ANOTHER) and (groupId in [GROUPR, GROUPG])) then AddCardToList(OWorldArrays[Platleng],  noOf[Platleng],  i);
      if (place = RLYEH)     or ((place = ANOTHER) and (groupId in [GROUPR, GROUPY])) then AddCardToList(OWorldArrays[Rlyeh],     noOf[Rlyeh],     i);
      if (place = YUGGOTH)   or ((place = ANOTHER) and (groupId in [GROUPB, GROUPY])) then AddCardToList(OWorldArrays[Yuggoth],   noOf[Yuggoth],   i);
    end;
  end;
end;

procedure SetupEncounterCounts;
var
  eId, ecId : integer;
  encounter      : TEncounter;
  encounterCount : TEncounterCount;
begin
  Log('SetupEncounterCounts');
  for eId := 0 to high(EncounterRecs) do begin
    encounter := EncounterRecs[eId];
    ecId := EncounterCountIndexOf(encounter.name);
    if ecId = -1 then begin
      ecId := length(EncounterCountRecs);
      setLength(EncounterCountRecs, ecId+1);
      EncounterCountRecs[ecId] := TEncounterCount.Create;
      encounterCount := EncounterCountRecs[ecId];
      encounterCount.name := encounter.name;
      encounterCount.count := 1;
      continue;
    end;
    encounterCount := EncounterCountRecs[ecId];
    inc(encounterCount.count);
  end;
end;

procedure SetupGateDeck;
var
  i : integer;
begin
  Log('SetupGateDeck');
  SetLength(GateArray, length(GateRecs)*2);
  for i := 0 to high(GateRecs) do begin
    GateArray[i*2] := i;
    GateArray[i*2+1] := i;
  end;
end;

procedure SetupMonsterDeck;
var
  i, j, no : integer;
begin
  Log('SetupMonsterDeck');
  no := 0;
  for i := 0 to high(MonsterRecs) do
    inc(no, MonsterRecs[i].noof);
  setLength(MonsterArray, no);
  no := 0;
  for i := 0 to high(MonsterRecs) do begin
    for j := 1 to MonsterRecs[i].noof do begin
      MonsterArray[no] := i;
      inc(no);
    end;
  end;
end;

var
  lines      : TStringDynArray;
  expansions : SExpansion;

procedure StringSplit(const line : string; var lines : TStringDynArray);
var
  p, no : integer;
  work : string;
begin
  no := 0;
  setlength(lines, 20);
  work := line;
  repeat
    p := pos(#9, work);
    if p > 0 then begin
      lines[no] := copy(work, 1, p-1);
      work := copy(work, p+1, length(work));
    end
    else
      lines[no] := work;
    inc(no);
    if no > pred(length(lines)) then
      setlength(lines, no+20);
  until p = 0;
  setLength(lines, no);
end;


procedure LoadAncients(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(AncientRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    AncientRecs[used] := TAncient.Create;
    with AncientRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      combatRating  := lines[2];
      defences      := lines[3];
      worshippers   := lines[4];
      power         := lines[5];
      startOfBattle := lines[6];
      attack        := lines[7];
      doomTrack     := strtoint(lines[8]);
      useMasks      := strtoint(lines[9]);
    end;
    inc(used);
  end;
  setlength(AncientRecs, used);
end;

procedure LoadBackStories(var mfile : textfile; noOf : integer);
var
  line    : string;
  i,used  : integer;
  exp     : EExpansion;
begin
  setlength(BackStoryRecs, noOf);
  used := 0;
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    BackStoryRecs[used] := TBackStory.Create;
    with BackStoryRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      description   := lines[2];
    end;
    inc(used);
  end;
  setlength(BackStoryRecs, used);
end;

procedure LoadDistricts(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer;
  exp     : EExpansion;
begin
  setlength(DistrictRecs, noOf);
  used := 0;
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    DistrictRecs[used] := TDistrict.Create;
    with DistrictRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      description   := lines[2];
    end;
    inc(used);
  end;
  setlength(DistrictRecs, used);
end;

procedure LoadEncounters(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer;
  exp     : EExpansion;
begin
  setlength(EncounterRecs, noOf);
  used := 0;
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    EncounterRecs[used] := TEncounter.Create;
    with EncounterRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      no            := strtoint(lines[2]);
      description   := lines[3];
    end;
    inc(used);
  end;
  setlength(EncounterRecs, used);
end;

procedure LoadFixedPossessions(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer;
  exp     : EExpansion;
begin
  setlength(FixedPossessionRecs, noOf);
  used := 0;
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    FixedPossessionRecs[used] := TFixedPossession.Create;
    with FixedPossessionRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      item          := lines[2];
    end;
    inc(used);
  end;
  setlength(FixedPossessionRecs, used);
end;

procedure LoadGates(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(GateRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    GateRecs[used] := TGate.Create;
    with GateRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      description   := lines[2];
      strength      := strtoint(lines[3]);
      faction       := EFactionType(strtoint(lines[4]));
    end;
    inc(used);
  end;
  setlength(GateRecs, used);
end;

procedure LoadInvestigators(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(InvestigatorRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    InvestigatorRecs[used] := TInvestigator.Create;
    with InvestigatorRecs[used] do begin
      name             := lines[0];
      expansion        := EExpansion(strtoint(lines[1]));
      profession       := lines[2];
      home             := lines[3];
      status           := EGraceType(strtoint(lines[4]));
      sanity           := strtoint(lines[5]);
      stamina          := strtoint(lines[6]);
      clues            := strtoint(lines[7]);
      cash             := strtoint(lines[8]);
      focus            := strtoint(lines[9]);
      speed            := strtoint(lines[10]);
      sneak            := strtoint(lines[11]);
      fight            := strtoint(lines[12]);
      will             := strtoint(lines[13]);
      lore             := strtoint(lines[14]);
      luck             := strtoint(lines[15]);
      common           := strtoint(lines[16]);
      unique           := strtoint(lines[17]);
      spell            := strtoint(lines[18]);
      skill            := strtoint(lines[19]);
      ability          := lines[20];
    end;
    inc(used);
  end;
  setlength(InvestigatorRecs, used);
end;

procedure LoadICards(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(ICardRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    ICardRecs[used] := TICard.Create;
    with ICardRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      fullname      := lines[2];
      icardtype     := EICardType(strtoint(lines[3]));
      noOf          := strtoint(lines[4]);
      cost          := strtoint(lines[5]);
      handed        := strtoint(lines[6]);
      upkeep        := lines[7];
      exhaust       := lines[8];
      description   := lines[9];
    end;
    inc(used);
  end;
  setlength(ICardRecs, used);
end;

procedure LoadLocations(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(LocationRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    LocationRecs[used] := TLocation.Create;
    with LocationRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      district      := lines[2];
      placeType     := EPlaceType(strtoint(lines[3]));
    end;
    inc(used);
  end;
  setlength(LocationRecs, used);
end;

procedure LoadMapPlaces(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(MapPlaceRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    MapPlaceRecs[used] := TMapPlace.Create;
    with MapPlaceRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      trow          := strtoint(lines[2]);
      brow          := strtoint(lines[3]);
      lcol          := strtoint(lines[4]);
      rcol          := strtoint(lines[5]);
    end;
    inc(used);
  end;
  setlength(MapPlaceRecs, used);
end;

procedure LoadMonsters(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(MonsterRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    MonsterRecs[used] := TMonster.Create;
    with MonsterRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      monsterType   := EMonsterType(strtoint(lines[2]));
      faction       := EFactionType(strtoint(lines[3]));
      attributes    := lines[4];
      awareness     := strtoint(lines[5]);
      sanity        := strtoint(lines[6]);
      sanityloss    := strtoint(lines[7]);
      life          := strtoint(lines[8]);
      stamina       := strtoint(lines[9]);
      staminaloss   := strtoint(lines[10]);
      noof          := strtoint(lines[11]);
      notes         := lines[12];
    end;
    inc(used);
  end;
  setlength(MonsterRecs, used);
end;

procedure LoadMythoss(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(MythosRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    MythosRecs[used] := TMythos.Create;
    with MythosRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      event         := EMythosType(strtoInt(lines[2]));
      clue          := lines[3];
      monster       := lines[4];
      white         := lines[5];
      black         := lines[6];
      description   := lines[7];
    end;
    inc(used);
  end;
  setlength(MythosRecs, used);
end;

procedure LoadOtherWorlds(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(OtherWorldRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    OtherWorldRecs[used] := TOtherWorld.Create;
    with OtherWorldRecs[used] do begin
      groupId       := EOWorldGroup(strtoint(lines[0]));
      expansion     := EExpansion(strtoint(lines[1]));
      place         := EOWorldPlace(strtoint(lines[2]));
      no            := strtoint(lines[3]);
      description   := lines[4];
    end;
    inc(used);
  end;
  setlength(OtherWorldRecs, used);
end;

procedure LoadPictureNos(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(PictureNoRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    PictureNoRecs[used] := TPictureNo.Create;
    with PictureNoRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      no            := strtoint(lines[2]);
    end;
    inc(used);
  end;
  setlength(PictureNoRecs, used);
end;

procedure LoadPlaces(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(PlaceRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[1]));
    if not (exp in expansions) then continue;
    PlaceRecs[used] := TPlace.Create;
    with PlaceRecs[used] do begin
      name          := lines[0];
      expansion     := EExpansion(strtoint(lines[1]));
      district      := lines[2];
      stable        := strtoint(lines[3]);
      encounters    := lines[4];
      description   := lines[5];
      special       := lines[6];
    end;
    inc(used);
  end;
  setlength(PlaceRecs, used);
end;

procedure LoadRoads(var mfile : textfile; noOf : integer);
var
  line    : string;
  i       : integer;
  used    : integer = 0;
  exp     : EExpansion;
begin
  setlength(RoadRecs, noOf);
  for i := 0 to pred(noOf) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    exp := EExpansion(strtoint(lines[2]));
    if not (exp in expansions) then continue;
    RoadRecs[used] := TRoad.Create;
    with RoadRecs[used] do begin
      location1  := lines[0];
      location2  := lines[1];
      expansion  := EExpansion(strtoint(lines[2]));
      direction  := EDirection(strtoint(lines[3]));
      mpath      := EMonsterPath(strtoint(lines[4]));
    end;
    inc(used);
  end;
  setlength(RoadRecs, used);
end;

procedure LoadGamePieces(const filename : string; aExpansions : SExpansion; memo : TMemo);
var
  MFile : TextFile;
  line  : string;
  lines : TStringDynArray;
begin
  expansions := aExpansions;
  memo.Lines.Add(format('Loading materials from file %s', [filename]));
  AssignFile(MFile, filename);
  reset(MFile);
  setLength(lines, 0);
  while not Eoln(MFile) do begin
    readln(MFile, line);
    StringSplit(line, lines);
    if (length(lines) <> 2) or (lines[0][1] <> '[') then begin
      memo.Lines.Add('Data seems to be invalid');
      memo.Lines.Add(format('%s does not seem to be a vaild starter',[line]));
      break;
    end;
    if lines[0] = '[Ancients]' then begin
      LoadAncients(MFile, strtoint(lines[1]));
      Log(format('AncientRecs %d',[length(AncientRecs)]));
      continue;
    end;
    if lines[0] = '[BackStories]' then begin
      LoadBackStories(MFile, strtoint(lines[1]));
      Log(format('BackStoryRecs %d',[length(BackStoryRecs)]));
      continue;
    end;
    if lines[0] = '[Districts]' then begin
      LoadDistricts(MFile, strtoint(lines[1]));
      Log(format('DistrictRecs %d',[length(DistrictRecs)]));
      continue;
    end;
    if lines[0] = '[Encounters]' then begin
      LoadEncounters(MFile, strtoint(lines[1]));
      Log(format('EncounterRecs %d',[length(EncounterRecs)]));
      continue;
    end;
    if lines[0] = '[FixedPossessions]' then begin
      LoadFixedPossessions(MFile, strtoint(lines[1]));
      Log(format('FixedPossessionRecs %d',[length(FixedPossessionRecs)]));
      continue;
    end;
    if lines[0] = '[Gates]' then begin
      LoadGates(MFile, strtoint(lines[1]));
      Log(format('GateRecs %d',[length(GateRecs)]));
      continue;
    end;
    if lines[0] = '[Investigators]' then begin
      LoadInvestigators(MFile, strtoint(lines[1]));
      Log(format('InvestigatorRecs %d',[length(InvestigatorRecs)]));
      continue;
    end;
    if lines[0] = '[ICards]' then begin
      LoadICards(MFile, strtoint(lines[1]));
      Log(format('ICardRecs %d',[length(ICardRecs)]));
      continue;
    end;
    if lines[0] = '[Locations]' then begin
      LoadLocations(MFile, strtoint(lines[1]));
      Log(format('LocationRecs %d',[length(LocationRecs)]));
      continue;
    end;
    if lines[0] = '[MapPlaces]' then begin
      LoadMapPlaces(MFile, strtoint(lines[1]));
      Log(format('MapPlaceRecs %d',[length(MapPlaceRecs)]));
      continue;
    end;
    if lines[0] = '[Monsters]' then begin
      LoadMonsters(MFile, strtoint(lines[1]));
      Log(format('MonsterRecs %d',[length(MonsterRecs)]));
      continue;
    end;
    if lines[0] = '[Mythoss]' then begin
      LoadMythoss(MFile, strtoint(lines[1]));
      Log(format('MythosRecs %d',[length(MythosRecs)]));
      continue;
    end;
    if lines[0] = '[OtherWorlds]' then begin
      LoadOtherWorlds(MFile, strtoint(lines[1]));
      Log(format('OtherWorldRecs %d',[length(OtherWorldRecs)]));
      continue;
    end;
    if lines[0] = '[PictureNos]' then begin
      LoadPictureNos(MFile, strtoint(lines[1]));
      Log(format('PictureNoRecs %d',[length(PictureNoRecs)]));
      continue;
    end;
    if lines[0] = '[Places]' then begin
      LoadPlaces(MFile, strtoint(lines[1]));
      Log(format('PlaceRecs %d',[length(PlaceRecs)]));
      continue;
    end;
    if lines[0] = '[Roads]' then begin
      LoadRoads(MFile, strtoint(lines[1]));
      Log(format('RoadRecs %d',[length(RoadRecs)]));
      continue;
    end;
    setlength(lines, 0);
    break;
  end;
  CloseFile(MFile);
  memo.lines.add('file load done');
  SetupICardDecks;
  SetupOtherWorldDecks;
  SetupEncounterCounts;
  SetupGateDeck;
  SetupMonsterDeck;
  memo.lines.add('separated decks done');
end;

end.

