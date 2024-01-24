unit AHGame;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}{$H+}

interface

uses
  Classes, SysUtils, Types, Forms, StdCtrls, Graphics, ExtCtrls, Controls,
  Buttons, ComCtrls, AHTypes, AHGamePieces, InvestigatorUnit, AHLogger;

type
  { TGameVars }
  TGameVars = class
    ancient            : TAncient;
    first              : integer;
    doomTrackCount     : integer;
    terrorTrackCount   : integer;
    gamePhase          : EPhase;
    mythosCard         : integer;
    environmentCard    : integer;
    rumorCard          : integer;
    investigatorsStats : array of TInvestigatorStats;
    monsters           : array of integer;
    gates              : array of integer;
    constructor Create;
    procedure Log(message : string);
    procedure MakeInvestigatorForms(ScreenPages: TPageControl; chosen : TListBox);
    procedure InvestigatorDoneClick(Sender: TObject);
    procedure SendNote(index : integer; value : string);
    procedure SetupInvestigator(index : integer; investigatorId : integer);
    procedure SetupAncient(ancientId : integer);
    procedure DrawDoomtrack;
    procedure SetupPhase;
    procedure UpkeepPhase;
    procedure MovementPhase;
    procedure ArkhamEncounterPhase;
    procedure OutworldEncounterPhase;
    procedure MythosPhase;
    procedure ApplyMythosCard;
    procedure EndGame;
    function  MaxGates : boolean;
    function  MaxTownMonsters : boolean;
    function  MaxOutskirtsMonsters : boolean;
    function  NoOfGateOpenMonsters : integer;
    function  BlockGateOpen(gamePlace : TGamePlace) : boolean;
    function  BlockMonsterPlace(gamePlace : TGamePlace) : boolean;
    procedure PlaceMonster(gamePlace : TGamePlace);
    procedure ClearOutskirts;
    procedure AddOneToTerrorLevel;
    procedure OpenGate(location : string);
    procedure PlaceClue(location : string);
    procedure MoveWhites(dimensions : string);
    procedure MoveBlacks(dimensions : string);
    procedure MoveWhiteDirection(var gamePlace : TGamePlace; monsterId : integer);
    procedure MoveBlackDirection(var gamePlace : TGamePlace; monsterId : integer);
    procedure MoveBlackMonster(var gamePlace : TGamePlace; monsterId : integer; path : SMonsterPath);
    procedure MoveRedMonster(var gamePlace : TGamePlace; monsterId : integer; path : SMonsterPath);
    procedure MoveBlueMonster(var gamePlace : TGamePlace; monsterId : integer; path : SMonsterPath);
    procedure MoveGreenMonster(var gamePlace : TGamePlace; monsterId : integer; path : SMonsterPath);
    procedure EachPlayerLosesSanity(amount : integer);
    function RollADice : integer;
    function GetInvestigatorName(playerNo : integer) : string;
  end;

var
  parentForm          : TForm;
  ancientsMemo        : TMemo;
  mythosMemo          : TMemo;
  gameMemo            : TMemo;
  townMap             : TImage;
  DoomTrack           : TImage;
  ScreenPages         : TPageControl;
  DoomTrackImages     : TImageList;
  gameImages          : TImageList;
  GameVars            : TGameVars;

procedure LoadCards(memo : TMemo);
procedure PlaceClues;
procedure Log(message: string);
procedure AOIRemove(var AOI : TIntegerDynArray; id : integer);

implementation

procedure ReduceTo11Allies;
var
  i,id : integer;
  AllyCard : TICard;
  AllyCards : TCardDeck;
begin
  AllyCards := ICardDecks[Ally];
  while length(AllyCards.deck) > 11 do begin
    i := random(length(AllyCards.deck));
    id := AllyCards.deck[i];
    AllyCard := ICardRecs[id];
    if AllyCard.name = 'DUKE' then continue;
    AllyCards.Remove(i);
  end;
end;

procedure LoadCards(memo : TMemo);
var
  ei : EICardType;
  eo : EOWorldPlace;
begin
  for ei := low(EICardType) to high(EICardType) do
    ICardDecks[ei] := TCardDeck.Create(ICardArrays[ei]);
  ReduceTo11Allies;
  for eo := low(EOWorldPlace) to high(EOWorldPlace) do
    OWorldDecks[eo] := TCardDeck.Create(OWorldArrays[eo]);
  MythosCards               := TCardDeck.Create(GetRange(length(MythosRecs)));
  MonsterCards              := TCardDeck.Create(MonsterArray);
  GateCards                 := TCardDeck.Create(GateArray);
  InvestigatorCards         := TCardDeck.Create(GetRange(length(InvestigatorRecs)));
  AncientCards              := TCardDeck.Create(GetRange(length(AncientRecs)));
end;

procedure PlaceClues;
var
  placeId, mapPlaceId, gamePlaceId, locationId : integer;
  Place : TPlace;
  Location : TLocation;
  GamePlace : TGamePlace;
begin
  Log('PlaceClues');
  for locationId := 0 to high(LocationRecs) do begin
    Location := LocationRecs[locationId];
    mapPlaceId := MapPlaceIndexOf(Location.name);
    placeId := PlaceIndexOf(Location.name);
    gamePlaceId := length(GamePlaceRecs);
    setLength(GamePlaceRecs, gamePlaceId+1);
    GamePlaceRecs[gamePlaceId] := TGamePlace.Create;
    GamePlace := GamePlaceRecs[gamePlaceId];
    GamePlace.name := Location.name;
    GamePlace.locationId := locationId;
    GamePlace.placeId := placeId;
    GamePlace.mapPlaceId := mapPlaceId;
    if placeid <> -1 then begin
      Place := PlaceRecs[placeid];
      GamePlace.stable := Place.stable = 1;
    end
    else
      GamePlace.stable := true;
    GamePlace.closed  := false;
    setlength(GamePlace.playerNos, 0);
    setlength(GamePlace.monsterIds, 0);
    setlength(GamePlace.pending, 0);
    if GamePlace.stable = false then begin
      GamePlace.clues := 1;
      GamePlace.gateState := GATE_NONE;
    end;
    GamePlace.placeType := Location.placeType;
  end;
end;

procedure Log(message: string);
begin
  AHLogger.Log(format('ahgame: %s', [message]));
end;

procedure AOIRemove(var AOI: TIntegerDynArray; id: integer);
var
  i,no : integer;
  found : boolean;
begin
  no := length(AOI);
  found := false;
  for i := 0 to high(AOI) do begin
    if found then
      AOI[i-1] := AOI[i]
    else if AOI[i] = id then
      found := true;
  end;
  if found then begin
    dec(no);
    setLength(AOI, no);
  end;
end;


{ TGameVars }

constructor TGameVars.Create;
begin
  ancient := nil;
  setLength(monsters, 0);
  setLength(gates, 0);
  first := 0;
  doomTrackCount := 0;
  terrorTrackCount := 0;
  gamePhase := PHASE_SETUP;
  mythosCard := -1;
  environmentCard := -1;
  rumorCard := -1;
  setLength(investigatorsStats, 0);
end;

procedure TGameVars.Log(message: string);
begin
  AHLogger.Log(format('gamevars: %s', [message]));
end;

procedure TGameVars.MakeInvestigatorForms(ScreenPages: TPageControl; chosen : TListBox);
var
  index : integer;
  sheet : TTabSheet;
  name  : string;
  form  : TInvestigatorForm;
begin
  log('MakeInvestigatorForms');
  setLength(investigatorsStats, chosen.Count);
  for index := 0 to pred(chosen.Count) do begin
    name := chosen.Items[index];
    sheet := TTabSheet.Create(ScreenPages);
    sheet.PageControl := ScreenPages;
    form := TInvestigatorForm.Create(parentForm);
    investigatorsStats[index] := TInvestigatorStats.Create;
    investigatorsStats[index].form := form;
    investigatorsStats[index].form.gameImages := gameImages;
    investigatorsStats[index].form.townMap := townMap;
    investigatorsStats[index].form.BorderStyle := bsNone;
    investigatorsStats[index].form.Align := alClient;
    investigatorsStats[index].form.Parent := sheet;
    investigatorsStats[index].form.Visible := True;
    investigatorsStats[index].form.Tag := index;
    investigatorsStats[index].form.DoneButton.OnClick := InvestigatorDoneClick;
    ScreenPages.ActivePage := sheet;
    sheet.Caption := name;
    investigatorsStats[index].form.FormCreate(sheet);
    investigatorsStats[index].form.FormActivate(sheet);
  end;
end;

procedure TGameVars.InvestigatorDoneClick(Sender: TObject);
begin
  try
    log('InvestigatorDoneClick');
    if ScreenPages.ActivePageIndex < pred(ScreenPages.PageCount) then begin
      ScreenPages.ActivePageIndex := ScreenPages.ActivePageIndex + 1;
      exit;
    end;
    ScreenPages.ActivePageIndex := 0;
    case gamePhase of
      PHASE_SETUP: begin
        SetupPhase;
      end;
      PHASE_MYTHOS: begin
        MythosPhase;
      end;
      PHASE_UPKEEP: begin
        UpkeepPhase;
      end;
      PHASE_MOVEMENT: begin
        MovementPhase;
      end;
      PHASE_ARHAM_ENCOUNTER: begin
        ArkhamEncounterPhase;
      end;
      PHASE_OTHER_WORLD_ENCOUNTER: begin
        OutworldEncounterPhase;
      end;
      PHASE_END_GAME: begin
        EndGame;
      end;
    end;
  except
    on ex: Exception do
      log(format('exception: %s',[ex.Message]));
  end;
end;

procedure TGameVars.SendNote(index: integer; value: string);
begin
end;

procedure TGameVars.SetupInvestigator(index: integer; investigatorId: integer);
  procedure setup(stats : TInvestigatorStats);
  var
    investigator     : TInvestigator;
    fixedPossession  : TFixedPossession;
    icard            : TICard;
    i, icardid       : integer;
    deckCard         : integer;
  begin
    stats.investigatorId := investigatorId;
    investigator := InvestigatorRecs[investigatorId];
    stats.backStoryId := BackStoryIndexOf(investigator.name);
    for i := 0 to high(FixedPossessionRecs) do begin
      fixedPossession := FixedPossessionRecs[i];
      if fixedPossession.name <> investigator.name then
        continue;
      icardid := ICardIndexOf(fixedPossession.item);
      if icardid = -1 then
        continue;
      icard := ICardRecs[icardid];
      deckcard := ICardDecks[icard.icardtype].Find(icardid);
      stats.form.AddICard(deckCard);
    end;
    for i := 1 to investigator.common do begin
      deckCard := ICardDecks[Common].Draw;
      stats.form.AddICard(deckCard);
    end;
    for i := 1 to investigator.unique do begin
      deckCard := ICardDecks[Unique].Draw;
      stats.form.AddICard(deckCard);
    end;
    for i := 1 to investigator.spell do begin
      deckCard := ICardDecks[Spell].Draw;
      stats.form.AddICard(deckCard);
    end;
    for i := 1 to investigator.skill do begin
      deckCard := ICardDecks[Skill].Draw;
      stats.form.AddICard(deckCard);
    end;
    with stats.form do begin
      PicId         := investigatorId;
      PlayerNo      := index;
      Phase         := gamephase;
      Ability       := investigator.ability;
      Cash          := investigator.cash;
      Clues         := investigator.clues;
      InvName       := investigator.name;
      InvHome       := investigator.home;
      InvLocation   := investigator.home;
      InvProfession := investigator.profession;
      MaxSanity     := investigator.sanity;
      Sanity        := investigator.sanity;
      MaxStamina    := investigator.stamina;
      Stamina       := investigator.stamina;
      InvFocus      := investigator.focus;
      MaxFocus      := investigator.focus;
      minSpeed      := investigator.speed;
      maxSneak      := investigator.sneak;
      minFight      := investigator.fight;
      maxWill       := investigator.will;
      maxLuck       := investigator.luck;
      minLore       := investigator.lore;
      Speed         := investigator.speed;
      Sneak         := investigator.sneak;
      Fight         := investigator.fight+1;
      Will          := investigator.will-1;
      Lore          := investigator.lore+2;
      Luck          := investigator.luck-2;
    end;
    townMap.Refresh;
  end;
begin
  log('SetupInvestigator');
  setup(investigatorsStats[index]);
end;

procedure TGameVars.SetupAncient(ancientId: integer);
var
  value   : string;
  index   : integer;
begin
  log('SetupAncient');
  ancient := AncientRecs[ancientId];
  if ancient.useMasks = 0 then begin
    index := 0;
    while index <= high(MonsterCards.deck) do begin
      if Pos('MASK', MonsterRecs[MonsterCards.deck[index]].attributes) > 0 then
        MonsterCards.Remove(index)
      else
        inc(index);
    end;
  end;
  ancientsmemo.lines.Clear;
  value := format('%s %s %s', [ancient.name, ancient.combatRating, ancient.defences]);
  if length(ancient.worshippers) > 0 then
    value := value + format(' %s', [ancient.worshippers]);
  if length(ancient.power) > 0 then
    value := value + format(' %s', [ancient.power]);
  value := value + ' End Game:';
  if length(ancient.startOfBattle) > 0 then
    value := value + format(' %s', [ancient.startOfBattle]);
  if length(ancient.attack) > 0 then
    value := value + format(' %s', [ancient.attack]);
  ancientsmemo.Lines.Add(value);
  DrawDoomTrack;
end;

procedure TGameVars.DrawDoomtrack;
var
  i, n, x, y : integer;
  rect    : TRect;
begin
  log('DrawDoomtrack');
  DoomTrack.Width := ancient.doomTrack * 50 + 12;
  rect.Top := 0;
  rect.Bottom := DoomTrack.Height;
  rect.Left := 0;
  rect.Right := DoomTrack.Width;
  with DoomTrack.Canvas do begin
    Brush.Color := clDkGray;
    FillRect(rect);
  end;
  for i := 0 to pred(ancient.doomTrack) do begin
    x := i * 50 + 10;
    y := 4;
    if i < doomTrackCount then n := 19
    else if i = pred(ancient.doomTrack) then n := i+5
    else n := i;
    DoomTrackImages.Draw(DoomTrack.Canvas, x, y, n);
  end;
end;

procedure TGameVars.SetupPhase;
var
  Mythos   : TMythos;
  //value    : string;
  i        : integer;
begin
  log('SetupPhase');
  environmentCard := -1;
  while true do begin
    mythosCard := MythosCards.Draw;
    Mythos   := MythosRecs[mythosCard];
    if (length(Mythos.monster) = 0) or (length(Mythos.clue) = 0) then begin
      MythosCards.Discard(mythosCard);
      continue;
    end;
    break;
  end;
  if Mythos.event = ENVIRONMENT then
    environmentCard := mythosCard
  else
    MythosCards.Discard(mythosCard);
  ApplyMythosCard;
  gamePhase := PHASE_UPKEEP;
  for i := 0 to pred(length(investigatorsStats)) do
    investigatorsStats[i].form.Phase := PHASE_UPKEEP;
end;

procedure TGameVars.UpkeepPhase;
var
  i : integer;
begin
  log('UpkeepPhase');
  gamePhase := PHASE_MOVEMENT;
  for i := 0 to pred(length(investigatorsStats)) do
    investigatorsStats[i].form.Phase := PHASE_MOVEMENT;
end;

procedure TGameVars.MovementPhase;
var
  i : integer;
begin
  log('MovementPhase');
  gamePhase := PHASE_ARHAM_ENCOUNTER;
  for i := 0 to pred(length(investigatorsStats)) do
    investigatorsStats[i].form.Phase := PHASE_ARHAM_ENCOUNTER;
end;

procedure TGameVars.ArkhamEncounterPhase;
var
  i : integer;
begin
  log('ArkhamEncounterPhase');
  gamePhase := PHASE_OTHER_WORLD_ENCOUNTER;
  for i := 0 to pred(length(investigatorsStats)) do
    investigatorsStats[i].form.Phase := PHASE_OTHER_WORLD_ENCOUNTER;
end;

procedure TGameVars.OutworldEncounterPhase;
var
  i : integer;
begin
  log('OutworldEncounterPhase');
  gamePhase := PHASE_MYTHOS;
  for i := 0 to pred(length(investigatorsStats)) do
    investigatorsStats[i].form.Phase := PHASE_MYTHOS;
  mythosCard := MythosCards.Draw;
  ApplyMythosCard;
end;

procedure TGameVars.MythosPhase;
var
  i, j, no : integer;
begin
  log('MythosPhase');
  gamePhase := PHASE_UPKEEP;
  no := length(investigatorsStats);
  first := (first + 1) mod no;
  for i := 0 to pred(length(investigatorsStats)) do begin
    j := (first + i) mod no;
    investigatorsStats[j].form.Parent := ScreenPages.Pages[i];
    ScreenPages.Pages[i].Caption := investigatorsStats[j].form.InvName;
    investigatorsStats[j].form.Phase := PHASE_UPKEEP;
  end;
end;

procedure TGameVars.ApplyMythosCard;
var
  Mythos, EMythos   : TMythos;
  value    : string;
  //i        : integer;
  function _mythos_to_string_(event : EMythosType) : string;
  begin
    result := '';
    case event of
      ENVIRONMENT: result := 'ENVIRONMENT';
      HEADLINE: result := 'HEADLINE';
      RUMOR: result := 'RUMOR';
    end;
  end;
begin
  log('ApplyMythosCard');
  gameMemo.Clear;
  mythosMemo.Clear;
  Mythos   := MythosRecs[mythosCard];
  if (environmentCard <> -1)
  and (mythos.event <> ENVIRONMENT)
  and (environmentCard <> mythosCard) then begin
    EMythos   := MythosRecs[environmentCard];
    value := Format('%s: %s - %s', [_mythos_to_string_(EMythos.event), EMythos.name, EMythos.description]);
    mythosMemo.Lines.add(value);
  end;
  if mythos.event = ENVIRONMENT then begin
    if (environmentCard <> -1) then
      MythosCards.Discard(environmentCard);
    environmentCard := mythosCard;
  end
  else if (mythos.event = RUMOR) and (rumorCard = -1) then
    rumorCard := mythosCard
  else
    MythosCards.Discard(mythosCard);
  value := Format('Clue:%s Monster:%s White:%s Black:%s', [Mythos.clue, Mythos.monster, Mythos.white, Mythos.black]);
  OpenGate(Mythos.monster);
  PlaceClue(Mythos.clue);
  MoveWhites(Mythos.white);
  MoveBlacks(Mythos.black);
  gameMemo.Lines.add(value);
  if mythos.event <> RUMOR then begin
    value := Format('%s: %s - %s', [_mythos_to_string_(Mythos.event), Mythos.name, Mythos.description]);
    mythosMemo.Lines.add(value);
  end;
end;

procedure TGameVars.EndGame;
begin

end;

function TGameVars.MaxGates: boolean;
var
  limit : integer;
begin
  limit := 9 - (length(investigatorsStats) + 1) div 2;
  result := length(gates) >= limit;
end;

function TGameVars.MaxTownMonsters: boolean;
var
  i, noOf, limit : integer;
  GamePlace : TGamePlace;
begin
  limit := length(investigatorsStats) + 3;
  noOf := 0;
  for i := 0 to high(GamePlaceRecs) do begin
    GamePlace := GamePlaceRecs[i];
    if GamePlace.placeType in [PLACE, DISTRICT] then
      inc(noOf, length(GamePlace.monsterIds));
  end;
  result := noOf >= limit;
end;

function TGameVars.MaxOutskirtsMonsters: boolean;
var
  id, limit : integer;
  GamePlace : TGamePlace;
begin
  limit := 8 - length(investigatorsStats);
  id := GamePlaceIndexOf('OUTSKIRTS');
  GamePlace := GamePlaceRecs[id];
  result := length(GamePlace.monsterIds) >= limit;
end;

function TGameVars.NoOfGateOpenMonsters: integer;
begin
  if length(investigatorsStats) > 4 then result := 2 else result := 1;
end;

function TGameVars.BlockGateOpen(gamePlace : TGamePlace): boolean;
var
  i,n : integer;
begin
  result := false;
  for i := 0 to high(gamePlace.playerNos) do begin
    n := gamePlace.playerNos[i];
    if GetInvestigatorName(n) = 'KateWinthrop' then begin
      result := true;
      exit;
    end;
  end;
end;

function TGameVars.BlockMonsterPlace(gamePlace: TGamePlace): boolean;
var
  i,n : integer;
begin
  result := false;
  for i := 0 to high(gamePlace.playerNos) do begin
    n := gamePlace.playerNos[i];
    if GetInvestigatorName(n) = 'KateWinthrop' then begin
      result := true;
      exit;
    end;
  end;
end;

procedure TGameVars.PlaceMonster(gamePlace: TGamePlace);
var
  id, no : integer;
begin
  log('PlaceMonster');
  if BlockMonsterPlace(gamePlace) then exit;
  id := MonsterCards.Draw;
  no := length(gamePlace.monsterIds);
  setLength(gamePlace.monsterIds, no+1);
  gamePlace.monsterIds[no] := id;
end;

procedure TGameVars.ClearOutskirts;
var
  i, id : integer;
  GamePlace : TGamePlace;
begin
  log('ClearOutskirts');
  id := GamePlaceIndexOf('OUTSKIRTS');
  GamePlace := GamePlaceRecs[id];
  for i := 0 to high(GamePlace.monsterIds) do
    MonsterCards.Discard(GamePlace.monsterIds[i]);
  setlength(GamePlace.monsterIds, 0);
  MonsterCards.Shuffle;
  AddOneToTerrorLevel;
end;

procedure TGameVars.AddOneToTerrorLevel;
begin
  log('AddOneToTerrorLevel');
  if terrorTrackCount < 10 then
    inc(terrorTrackCount);
end;

procedure TGameVars.OpenGate(location: string);
var
  i, j, k, id, id2, noOf : integer;
  places : TStringDynArray;
  gamePlace : TGamePlace;
  outSkirtsPlace  : TGamePlace;
  openGates : array of integer;
  procedure DrawMonsterCardAt(var townPlace : TGamePlace);
  begin
    if MaxTownMonsters then begin
      if MaxOutskirtsMonsters then begin
        ClearOutskirts;
      end;
      id2 := GamePlaceIndexOf('OUTSKIRTS');
      outSkirtsPlace := GamePlaceRecs[id2];
      PlaceMonster(outSkirtsPlace);
    end else begin
      PlaceMonster(townPlace);
    end;
  end;
begin
  log('OpenGate');
  places := Split(location);
  try
    for i := 0 to high(places) do begin
      id := GamePlaceIndexOf(places[i]);
      if id <> -1 then begin
        gamePlace := GamePlaceRecs[id];
        case gamePlace.gateState of
          GATE_SEALED: begin
            exit;
          end;
          GATE_OPEN: begin
            noOf := 0;
            for j := 0 to high(GamePlaceRecs) do begin
              if GamePlaceRecs[j].gateState = GATE_OPEN then begin
                setLength(openGates, noOf+1);
                openGates[noOf] := j;
                inc(noOf);
              end;
            end;
            if length(investigatorsStats) > noOf then
              noOf := length(investigatorsStats);
            for j := 0 to pred(noOf) do begin
              k := j mod length(openGates);
              gamePlace := GamePlaceRecs[openGates[k]];
              DrawMonsterCardAt(gamePlace);
            end;
            setLength(openGates, 0);
          end;
          GATE_NONE: begin
            if BlockGateOpen(gamePlace) then exit;
            gamePlace.clues := 0;
            inc(doomTrackCount);
            DrawDoomTrack;
            if doomTrackCount >= ancient.doomTrack then begin
              gamePhase := PHASE_END_GAME;
              exit;
            end;
            gamePlace.gateState := GATE_OPEN;
            gamePlace.gateId := GateCards.Draw;
            setLength(gates, length(gates)+1);
            gates[high(gates)] := gamePlace.gateId;
            if maxGates then begin
              gamePhase := PHASE_END_GAME;
              exit;
            end;
            noOf := NoOfGateOpenMonsters;
            for j := 1 to noOf do
              DrawMonsterCardAt(gamePlace);
          end;
        end;
      end;
    end;
  finally
    townMap.Refresh;
    setLength(places, 0);
  end;
end;

procedure TGameVars.PlaceClue(location: string);
var
  i, id, noOf : integer;
  places : TStringDynArray;
  gamePlace : TGamePlace;
  form : TInvestigatorForm;
begin
  log('PlaceClue');
  places := Split(location);
  for i := 0 to high(places) do begin
    id := GamePlaceIndexOf(places[i]);
    if id <> -1 then begin
      gamePlace := GamePlaceRecs[id];
      if gamePlace.gateState <> GATE_OPEN then begin
        inc(gamePlace.clues);
        if length(gamePlace.playerNos) > 0 then begin
          form := GameVars.investigatorsStats[gamePlace.playerNos[0]].form;
          noOf := form.Clues;
          inc(noOf, gamePlace.clues);
          form.Clues := noOf;
          gamePlace.clues := 0;
        end;
      end;
    end;
  end;
  townMap.Refresh;
  setLength(places, 0);
end;

procedure AddToFactionSet(var faction : SFaction; value : string);
begin
  if value =      'HEX'      then faction := faction + [HEX]
  else if value = 'SLASH'    then faction := faction + [SLASH]
  else if value = 'TRIANGLE' then faction := faction + [TRIANGLE]
  else if value = 'STAR'     then faction := faction + [STAR]
  else if value = 'CROSS'    then faction := faction + [CROSS]
  else if value = 'MOON'     then faction := faction + [MOON]
  else if value = 'ROUNDEL'  then faction := faction + [ROUNDEL]
  else if value = 'SQUARE'   then faction := faction + [SQUARE]
  else if value = 'DIAMOND'  then faction := faction + [DIAMOND]
end;

procedure TGameVars.MoveWhites(dimensions: string);
var
  whites : TStringDynArray;
  i,j,id : integer;
  swhites : SFaction = [];
  gamePlace : TGamePlace;
  monster : TMonster;
begin
  log('MoveWhites');
  whites := Split(dimensions);
  try
    for i := 0 to high(whites) do
      AddToFactionSet(swhites, whites[i]);
    for i := 0 to high(GamePlaceRecs) do begin
      gamePlace := GamePlaceRecs[i];
      if gamePlace.name = 'OUTSKIRTS' then continue;
      if length(gamePlace.playerNos) > 0 then continue;
      for j := 0 to high(gamePlace.monsterIds) do begin
        id := gamePlace.monsterIds[j];
        monster := MonsterRecs[id];
        if monster.monsterType = M_YELLOW then continue;
        if monster.faction in swhites then
          MoveWhiteDirection(gamePlace, id);
      end;
   end;
  finally
    setLength(whites, 0);
  end;
end;

procedure TGameVars.MoveWhiteDirection(var gamePlace: TGamePlace; monsterId: integer);
var
  monster : TMonster;
  path    : SMonsterPath;
begin
  log('MoveWhiteDirection');
  monster := MonsterRecs[monsterId];
  path := [WHITEROUTE, BLACKWHITE];
  case monster.monsterType of
    M_BLACK: MoveBlackMonster(gamePlace, monsterId, path);
    M_RED:   MoveRedMonster(gamePlace, monsterId, path);
    M_GREEN: MoveGreenMonster(gamePlace, monsterId, path);
    M_BLUE:  MoveBlueMonster(gamePlace, monsterId, path);
  end;
end;

procedure TGameVars.MoveBlacks(dimensions: string);
var
  blacks : TStringDynArray;
  i, j, id : integer;
  sblacks : SFaction = [];
  gamePlace : TGamePlace;
  monster : TMonster;
begin
  log('MoveBlacks');
  blacks := Split(dimensions);
  try
    for i := 0 to high(blacks) do
      AddToFactionSet(sblacks, blacks[i]);
    for i := 0 to high(GamePlaceRecs) do begin
      gamePlace := GamePlaceRecs[i];
      if gamePlace.name = 'OUTSKIRTS' then continue;
      if length(gamePlace.playerNos) > 0 then continue;
      for j := 0 to high(gamePlace.monsterIds) do begin
        id := gamePlace.monsterIds[j];
        monster := MonsterRecs[id];
        if monster.monsterType = M_YELLOW then continue;
        if monster.faction in sblacks then
          MoveBlackDirection(gamePlace, id);
      end;
   end;
  finally
    setLength(blacks, 0);
  end;
end;

procedure TGameVars.MoveBlackDirection(var gamePlace: TGamePlace; monsterId: integer);
var
  monster : TMonster;
  path    : SMonsterPath;
begin
  log('MoveBlackDirection');
  monster := MonsterRecs[monsterId];
  path := [BLACKROUTE, BLACKWHITE];
  case monster.monsterType of
    M_BLACK: MoveBlackMonster(gamePlace, monsterId, path);
    M_RED:   MoveRedMonster(gamePlace, monsterId, path);
    M_GREEN: MoveGreenMonster(gamePlace, monsterId, path);
    M_BLUE:  MoveBlueMonster(gamePlace, monsterId, path);
  end;
end;

procedure TGameVars.MoveBlackMonster(var gamePlace: TGamePlace;
  monsterId: integer; path: SMonsterPath);
var
  i,k :integer;
  newPlace: TGamePlace;
  name : string;
begin
  log('MoveBlackMonster');
  name := gamePlace.name;
  i := RoadNextMonsterPlace(name, path);
  if i = -1 then
    exit;
  name := RoadRecs[i].location2;
  i := GamePlaceIndexOf(name);
  newPlace := GamePlaceRecs[i];
  k := length(newPlace.pending);
  setLength(newPlace.pending, k+1);
  newPlace.pending[k] := monsterId;
  AOIRemove(gamePlace.monsterIds, monsterId);
end;

procedure TGameVars.MoveRedMonster(var gamePlace: TGamePlace;
  monsterId: integer; path: SMonsterPath);
var
  i,k :integer;
  newPlace: TGamePlace;
  name : string;
begin
  log('MoveRedMonster');
  name := gamePlace.name;
  i := RoadNextMonsterPlace(name, path);
  if i = -1 then
    exit;
  name := RoadRecs[i].location2;
  i := GamePlaceIndexOf(name);
  newPlace := GamePlaceRecs[i];
  if length(newPlace.playerNos) = 0 then begin
    name := newPlace.name;
    i := RoadNextMonsterPlace(name, path);
    if i <> -1 then begin
      name := RoadRecs[i].location2;
      i := GamePlaceIndexOf(name);
      newPlace := GamePlaceRecs[i];
    end;
  end;
  k := length(newPlace.pending);
  setLength(newPlace.pending, k+1);
  newPlace.pending[k] := monsterId;
  AOIRemove(gamePlace.monsterIds, monsterId);
end;

procedure TGameVars.MoveBlueMonster(var gamePlace: TGamePlace;
  monsterId: integer; path: SMonsterPath);
var
  i,no : integer;
  newPlace: TGamePlace;
begin
  log('MoveBlueMonster');
  i := NearestDistrictWithPlayer(gamePlace.name);
  if i = -1 then begin
    if gamePlace.name = 'SKY' then exit;
    i := GamePlaceIndexOf('SKY');
  end;
  newPlace := GamePlaceRecs[i];
  no := length(newPlace.pending);
  setLength(newPlace.pending, no+1);
  newPlace.pending[no] := monsterId;
  AOIRemove(gamePlace.monsterIds, monsterId);
end;

procedure TGameVars.MoveGreenMonster(var gamePlace: TGamePlace;
  monsterId: integer; path: SMonsterPath);
var
  i,no : integer;
  newPlace: TGamePlace;
begin
  log('MoveGreenMonster');
  if MonsterRecs[monsterId].name = 'Chthonian' then begin
    if RollADice >= 4 then
      EachPlayerLosesSanity(1);
    exit;
  end;
  if MonsterRecs[monsterId].name = 'DarkDruid' then begin
    // Dark Druid is treated as a Cultist. When Dark Druid moves on a black
    // path, all other monsters move on black
    exit;
  end;
  if MonsterRecs[monsterId].name = 'HoundOfTindalos' then begin
    i := SameDistrictWithPlayer(gamePlace.name);
    if i <> -1 then begin
      newPlace := GamePlaceRecs[i];
      if (newPlace.name <> 'STMHOSPITAL') and (newPlace.name <> 'ARKASYLUM') then begin
        no := length(newPlace.pending);
        setLength(newPlace.pending, no+1);
        newPlace.pending[no] := monsterId;
        AOIRemove(gamePlace.monsterIds, monsterId);
      end;
    end;
    exit;
  end;
end;

procedure TGameVars.EachPlayerLosesSanity(amount: integer);
var
  i, sanity, loss : integer;
  form : TInvestigatorForm;
begin
  for i := 0 to high(investigatorsStats) do begin
    loss := amount;
    if GetInvestigatorName(i) = 'MichaelMcGlen' then
      dec(loss);
    if loss <= 0 then
      continue;
    form := investigatorsStats[i].form;
    sanity := form.Sanity;
    if sanity > 0 then begin
      dec(sanity, loss);
      form.Sanity := sanity;
      SendNote(i, format('You lost %d sanity',[loss]));
    end;
  end;
end;

function TGameVars.RollADice : integer;
begin
  result := Random(6)+1;
end;

function TGameVars.GetInvestigatorName(playerNo: integer): string;
var
  id : integer;
begin
  id := investigatorsStats[playerNo].investigatorId;
  result := InvestigatorRecs[id].name;
end;

initialization
  GameVars := TGameVars.Create;

end.

