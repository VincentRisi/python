unit AHTypes;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}{$H+}

interface

uses
  Classes, SysUtils;

const
  CLUE_IMAGE = 0;
  MONSTERS_IMAGE = 1;
  INVESTIGATORS_IMAGE = 6;

type
  EDirection     = (EAST, NORTH, NORTHEAST, NORTHWEST, SOUTH, SOUTHEAST, SOUTHWEST, DEADEND, WEST);

type
  EEncounterType = (ALLIES, BLESSINGS, CLUES, COMMONS, MONEYS, SANITY, SKILLS, SPELLS, STAMINA, UNIQUES);

type
  EExpansion     = (EXP_AH, EXP_COTDP, EXP_TBGOTW, EXP_TKIY, EXP_TLATT);
  SExpansion     = set of EExpansion;

type
  EFactionType   = (HEX, SLASH, TRIANGLE, STAR, CROSS, MOON, ROUNDEL, SQUARE, DIAMOND);
  SFaction       = set of EFactionType;

type
  EGateState     = (GATE_NONE, GATE_OPEN, GATE_SEALED);

type
  EGraceType     = (NORMAL, BLESSED, CURSED);

type
  EICardType     = (ALLY, BARRED, BLIGHT, COMMON, CULT, DARKPACT,
                    DIFFICULTY, EXHIBIT, GCORRUPT, PATROL,
                    RCORRUPT, RECKONING, RELATIONSHIP, SKILL,
                    SPECIAL, SPELL, UNIQUE );
                    
const
  ICardTypeNames   : array[EICardType] of string =
                   ('Ally', 'Barred', 'Blight', 'Common', 'Cult', 'Darkpact',
                    'Difficulty', 'Exhibit', 'GCorrupt', 'Patrol', 
                    'RCorrupt', 'Reckoning', 'Relationship', 'Skill', 
                    'Special', 'Spell','Unique');

type     
  ELocation      = (NORTHSIDE, DOWNTOWN, EASTTOWN, MDISTRICT, RIVERTOWN, MUNIVERSITY, FHILL, UPTOWN, SOUTHSIDE);
  
type
  EMonsterAttr   = (MASK, ENDLESS, MAGICR, MAGICI, PHYSR, PHYSI, UNDEAD, N1, O1, AMBUSH);

type
  EMonsterPath   = (BLACKROUTE, WHITEROUTE, BLACKWHITE, NONEROUTE);
  SMonsterPath   = set of EMonsterPath;

type
  EMonsterType   = (M_BLACK, M_RED, M_GREEN, M_BLUE, M_YELLOW);

type
  EMythosType    = (ENVIRONMENT, HEADLINE, RUMOR);

type
  EPhase         = (PHASE_SETUP, PHASE_UPKEEP, PHASE_MOVEMENT,
                    PHASE_ARHAM_ENCOUNTER, PHASE_OTHER_WORLD_ENCOUNTER,
                    PHASE_MYTHOS, PHASE_END_GAME);

type
  EOWorldGroup   = (GROUPR, GROUPG, GROUPB, GROUPY);

type
  EOWorldPlace   = (ABYSS, ANOTHER, CELEANO, DREAMLAND,
                    GREATRACE, PLATLENG, RLYEH, YUGGOTH);

const   
  OWorldPlaceNames : array[EOWorldPlace] of string =
                   ('Abyss', 'Another', 'Celeano', 'Dreamland',
                    'GreatRace', 'PlatLeng', 'RLyeh', 'Yuggoth');

type
  EPlaceType     = (PLACE, DISTRICT, GATE, OUTTOWN);

type

  AHBase = class
    function GetKey : string; virtual; abstract;
  end;

  { TAncient }

  TAncient = class(AHBase)
    name          : string;
    expansion     : EExpansion;
    combatRating  : string;
    defences      : string;
    worshippers   : string;
    power         : string;
    startOfBattle : string;
    attack        : string;
    doomTrack     : integer;
    useMasks      : integer;
    function Getkey : string; override;
  end;

  { TBackStory }

  TBackStory      = class(AHBase)
    name          : string;
    expansion     : EExpansion;
    description   : string;
    function Getkey : string; override;
  end;

  //{ TBlightCard }
  //
  //TBlightCard     = class(AHBase)
  //  name          : string;
  //  expansion     : EExpansion;
  //  fullname      : string;
  //  description   : string;
  //  function Getkey : string; override;
  //end;

  { TCardDeck }

  TCardDeck = class
    deck : array of integer;
    constructor Create(const source : array of integer);
    procedure Shuffle;
    procedure Discard(card : integer);
    procedure Top(card : integer);
    procedure Box(card : integer);
    procedure Remove(index : integer);
    function  Draw    : integer;
    function  Bottom  : integer;
    function  Find(card : integer) : integer;
  end;

  //{ TCorruptCard }
  //
  //TCorruptCard    = class(AHBase)
  //  name          : string;
  //  expansion     : EExpansion;
  //  color         : string;
  //  faction       : EFactionType;
  //  noOf          : integer;
  //  description   : string;
  //  function Getkey : string; override;
  //end;

  //{ TCultCard }
  //
  //TCultCard = class(AHBase)
  //  name          : string;
  //  expansion     : EExpansion;
  //  noOf          : integer;
  //  description   : string;
  //  function Getkey : string; override;
  //end;

  //{ TDarkPactCard }

  //TDarkPactCard = class(AHBase)
  //  name          : string;
  //  expansion     : EExpansion;
  //  fullname      : string;
  //  description   : string;
  //  function Getkey : string; override;
  //end;

  { TDistrict }

  TDistrict = class(AHBase)
    name          : string;
    expansion     : EExpansion;
    description   : string;
    function Getkey : string; override;
  end;

  { TEncounter }

  TEncounter = class(AHBase)
    name          : string;
    expansion     : EExpansion;
    no            : integer;
    description   : string;
    function Getkey : string; override;
    class function Key(name: string; no: integer) : string;
  end;

  { TEncounterCount }

  TEncounterCount = class(AHBase)
    name          : string;
    count         : integer;
    function Getkey : string; override;
  end;

  { TFixedPossession }

  TFixedPossession = class(AHBase)
    name          : string;
    expansion     : EExpansion;
    item          : string;
    function Getkey : string; override;
  end;
  
  { TGate }

  TGate = class(AHBase)
    name          : string;
    expansion     : EExpansion;
    description   : string;
    strength      : integer;
    faction       : EFactionType;
    function Getkey : string; override;
  end;

  { TGamePlace }

  TGamePlace = class(AHBase)
    name            : string;
    locationId      : integer;
    placeId         : integer;
    mapPlaceId      : integer;
    stable          : boolean;
    closed          : boolean;
    clues           : integer;
    playerNos       : array of integer;
    monsterIds      : array of integer;
    pending         : array of integer;
    gateId          : integer;
    gateState       : EGateState;
    placeType       : EPlaceType;
    function Getkey : string; override;
  end;

  { TICard }

  TICard = class(AHBase)
    name        : string;
    expansion   : EExpansion;
    fullname    : string;
    icardtype   : EICardType;
    noOf        : integer;
    cost        : integer;
    handed      : integer;
    upkeep      : string;
    exhaust     : string;
    description : string;
    function Getkey : string; override;
  end;

  { TInvestigator }

  TInvestigator = class(AHBase)
    name        : string;
    expansion   : EExpansion;
    profession  : string;
    home        : string;
    status      : EGraceType;
    sanity      : integer;
    stamina     : integer;
    clues       : integer;
    cash        : integer;
    focus       : integer;
    speed       : integer;
    sneak       : integer;
    fight       : integer;
    will        : integer;
    lore        : integer;
    luck        : integer;
    common      : integer;
    unique      : integer;
    spell       : integer;
    skill       : integer;
    ability     : string;
    function Getkey : string; override;
  end;

  { TLocation }

  TLocation = class(AHBase)
    name        : string;
    expansion   : EExpansion;
    district    : string;
    placeType   : EPlaceType;
    function Getkey : string; override;
  end;

  { TMapPlace }

  TMapPlace = class(AHBase)
    name       : string;
    expansion  : EExpansion;
    trow, brow : integer;
    lcol, rcol : integer;
    function Getkey : string; override;
  end;
  
  { TMonster }

  TMonster = class(AHBase)
    name        : string;
    expansion   : EExpansion;
    monsterType : EMonsterType;
    faction     : EFactionType;
    attributes  : string;
    awareness   : integer;
    sanity      : integer;
    sanityloss  : integer;
    life        : integer;
    stamina     : integer;
    staminaloss : integer;
    noof        : integer;
    notes       : string;
    function Getkey : string; override;
  end;

  { TMythos }

  TMythos = class(AHBase)
    name        : string;
    expansion   : EExpansion;
    event       : EMythosType;
    clue        : string; 
    monster     : string;
    white       : string;
    black       : string;
    description : string;
    function Getkey : string; override;
  end;

  { TOtherWorld }

  TOtherWorld = class(AHBase)
    groupId       : EOWorldGroup;
    expansion     : EExpansion;
    place         : EOWorldPlace;
    no            : integer;
    description   : string;
    function Getkey : string; override;
    class function Key(groupId: EOWorldGroup; place: EOWorldPlace;no: integer) : string;
  end;

  { TPictureNo }

  TPictureNo = class(AHBase)
    name          : string;
    expansion     : EExpansion;
    no            : integer;
    function Getkey : string; override;
  end;

  { TPlace }

  TPlace = class(AHBase)
    name          : string;
    expansion     : EExpansion;
    district      : string;
    stable        : integer;
    encounters    : string;
    description   : string;
    special       : string;
    function Getkey : string; override;
  end;

  { TRoad }

  TRoad = class(AHBase)
    location1     : string;
    location2     : string;
    expansion     : EExpansion;
    direction     : EDirection;
    mpath         : EMonsterPath;
    function Getkey : string; override;
    class function Key(location1, location2 : string): string;
  end;
  
implementation

{ TPictureNo }

function TPictureNo.Getkey: string;
begin
  result := name;
end;

{ TRoad }

function TRoad.Getkey: string;
begin
  result := Key(location1, location2);
end;

class function TRoad.Key(location1, location2: string): string;
begin
  result := Format('%s|%s', [location1, location2]);
end;

{ TPlace }

function TPlace.Getkey: string;
begin
  result := name;
end;

{ TOtherWorld }

function TOtherWorld.Getkey: string;
begin
  result := Key(groupId, place, no);
end;

class function TOtherWorld.Key(groupId: EOWorldGroup; place: EOWorldPlace; no: integer
  ): string;
begin
  result := Format('%2d|%2d|%2d' , [groupId, place, no]);
end;

{ TMythos }

function TMythos.Getkey: string;
begin
  result := name;
end;

{ TMonster }

function TMonster.Getkey: string;
begin
  result := name;
end;

{ TMapPlace }

function TMapPlace.Getkey: string;
begin
  result := name;
end;

{ TLocation }

function TLocation.Getkey: string;
begin
  result := name;
end;

{ TInvestigator }

function TInvestigator.Getkey: string;
begin
  result := name;
end;

{ TICard }

function TICard.Getkey: string;
begin
  result := name;
end;

{ TGamePlace }

function TGamePlace.Getkey: string;
begin
  result := name;
end;

{ TGate }

function TGate.Getkey: string;
begin
  result := name;
end;

{ TFixedPossession }

function TFixedPossession.Getkey: string;
begin
  result := name;
end;

{ TEncounterCount }

function TEncounterCount.Getkey: string;
begin
  result := name;
end;

{ TEncounter }

function TEncounter.Getkey: string;
begin
  result := Key(name,no);
end;

class function TEncounter.Key(name: string; no: integer): string;
begin
  result := Format('%s|%2d', [name,no]);

end;

{ TDistrict }

function TDistrict.Getkey: string;
begin
  result := name;
end;

//{ TDarkPactCard }
//
//function TDarkPactCard.Getkey: string;
//begin
//  result := name;
//end;

//{ TCultCard }
//
//function TCultCard.Getkey: string;
//begin
//  result := name;
//end;

//{ TBlightCard }
//
//function TBlightCard.Getkey: string;
//begin
//  result := name;
//end;

//{ TCorruptCard }
//
//function TCorruptCard.Getkey: string;
//begin
//  result := name;
//end;

{ TCardDeck }

constructor TCardDeck.Create(const source : array of integer);
var
  i : integer;
begin
  setLength(deck, length(source));
  for i := 0 to high(source) do
    deck[i] := source[i];
  Shuffle;
end;

procedure TCardDeck.Shuffle;
var
  i,m,t: integer;
begin
  randomize;
  for i := 0 to high(deck) do begin
    m := random(i+1);
    if m <> i then begin
      t       := deck[i];
      deck[i] := deck[m];
      deck[m] := t;
    end;
  end;
end;

procedure TCardDeck.Discard(card: integer);
var
  no : integer;
begin
  no := length(deck);
  setLength(deck, no+1);
  deck[no] := card;
end;

procedure TCardDeck.Top(card: integer);
var
  i,no : integer;
begin
  no := length(deck);
  setLength(deck, no+1);
  for i := no downto 1 do
    deck[i] := deck[i-1];
  deck[0] := card;
end;

procedure TCardDeck.Remove(index : integer);
var
  i, no : integer;
begin
  no := length(deck) - 1;
  for i := index to pred(no) do
    deck[i] := deck[i+1];
  setlength(deck, no);
end;

procedure TCardDeck.Box(card: integer);
var
  index : integer;
begin
  index := 0;
  while index < length(deck) do begin
    if deck[index] = card then
      Remove(index)
    else
      inc(index);
  end;
end;

function TCardDeck.Draw: integer;
begin
  if length(deck) = 0 then begin
    result := -1;
    exit;
  end;
  result := deck[0];
  Remove(0);
end;

function TCardDeck.Bottom: integer;
var
  no : integer;
begin
  no := length(deck) - 1;
  if no < 0 then begin
    result := -1;
  end;
  result := deck[no];
  setLength(deck, no);
end;

function TCardDeck.Find(card : integer): integer;
var
  index : integer;
begin
  for index := 0 to high(deck) do begin
    if deck[index] = card then begin
      result := card;
      Remove(index);
      exit;
    end;
  end;
  result := -1;
end;

{ TBackStory }

function TBackStory.Getkey: string;
begin
  result := name;
end;

{ TAncient }

function TAncient.Getkey: string;
begin
  result := name;
end;

end.

