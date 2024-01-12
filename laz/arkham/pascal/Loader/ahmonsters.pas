unit AHMonsters;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}{$H+}

interface

uses
  Classes, SysUtils, Types, AHTypes;

var
  Monsters      : TStringList;
  MonsterArray  : TIntegerDynArray;
  
implementation

procedure Add(const aName: string;
              const aExpansion  : EExpansion;
              const aMonsterType: EMonsterType;
              const aFaction: EFactionType;
              const aAttributes: string;
              const aAwareness: integer;
              const aSanity: integer;
              const aSanityloss: integer;
              const aLife: integer;
              const aStamina: integer;
              const aStaminaloss: integer;
              const aNoof: integer;
              const aNotes: string);
var
  Monster : TMonster;
begin
  Monster := TMonster.Create;
  with Monster do begin
    name        := aName;
    expansion   := aExpansion;
    monsterType := aMonsterType;
    faction     := aFaction;
    attributes  := aAttributes;
    awareness   := aAwareness;
    sanity      := aSanity;      // Horror Rating
    sanityloss  := aSanityloss;  // Horror Damage
    life        := aLife;        // Toughness
    stamina     := aStamina;     // Combat Rating
    staminaloss := aStaminaloss; // Combat Damage
    noof        := aNoof;
    notes       := aNotes;
  end;
  Monsters.AddObject(aName, Monster);
end;

procedure LoadMonsters;
begin
  Add('Byakhee',      EXP_AH, M_BLUE,    ROUNDEL,  '',                     -2, -1,  1,  1,  0,  2,  3,
      'It shrieked and flapped its wings. I thought of the empty shell of a beetle, and the soft loam of rotting earth. '+
      'It cocked its carapace head at me, black teeth clicking against each other.');
  Add('ChildOfTheGoat', EXP_TBGOTW,  M_BLACK,   HEX,      '',              -3,  0,  0,  1, +1,  0,  3,
      'Child of the Goat is treated as a Cultist. If you fail a Combat check or Evade check against Child of the Goat, '+
      'you are delayed.');
  Add('Chthonian',    EXP_AH, M_GREEN,   TRIANGLE, '',                      1, -2,  2,  3, -3,  3,  2,
      'Instead of moving, roll a die. On a 4-6, all investigators in Arkham lose 1 Stamina.');
  Add('Cultist',      EXP_AH, M_BLACK,   MOON,     '',                     -3,  0,  0,  1, +1,  1,  6,
      'la! la! Cthulhu Fthagn! Ph`nglui mglw`nfah Cthulhu R`lyeh wgahi`nagljhtagn!');
  Add('Dark Druid', EXP_TBGOTW, M_GREEN, HEX,      'PHYSR',                -2, -1,  1,  2, -2,  1,  1,
      'Dark Druid is treated as a Cultist. When Dark Druid moves on a black path, all other monsters move on black '+
      'after their normal movement.');
  Add('Dark Young', EXP_TBGOTW, M_YELLOW,  HEX,      'PHYSR,N1',           -2,  0,  3,  3, -1,  3,  3,
      'Physical Resistance Nightmarish 1 The trees trembled, leaves fluttering around us. The earth shook as the thuds '+
      'of giant hooved feet grew ever closer...');
  Add('Dhole',        EXP_AH, M_BLACK,   ROUNDEL,  'PHYSR,MAGICR,N1,O1',   -1, -1,  4,  3, -3,  4,  1,
      'Physical Resistance Magical Resistance Nightmarish 1 Overwhelming 1');
  Add('DimensionalShambler', EXP_AH,  M_RED,     SQUARE,   '',                     -3, -2,  1,  1, -2,  0,  2,
      'If you fail a Combat check against Dimensional Shambler, you are lost in time and space.');
  Add('ElderThing',   EXP_AH, M_BLACK,   DIAMOND,  '',                     -2, -3,  2,  2,  0,  1,  2,
      'When you fail a Cembat check against Elder Thing, you must discard 1 of your Weapons or Spells (your choice), if able.');
  Add('FireVampire',  EXP_AH, M_BLUE,    STAR,     'AMBUSH,PHYSI',          0,  0,  0,  1, -2,  2,  2,
      'Ambush Physical Immunity A thousand tiny fires, the size of match-flames, swept from the night sky. '+
      'The old man was suddenly radiant with light.');
  Add('FlyingPolyp',  EXP_AH, M_BLUE,    HEX,      'PHYSR,N1,O1',           0, -2,  4,  3, -3,  3,  1,
      'Physical Resistance Nightmarish 1 Overwhelming 1');
  Add('FormlessSpawn',EXP_AH, M_BLACK,   HEX,      'PHYSI',                 0, -1,  2,  2, -2,  2,  2,
      'Physical Immunity From the darkened alley a patch of darkness seemed to detach itself curling along '+
      'the bricks and rising to block our path.');
  Add('GoatSpawn', EXP_TBGOTW, M_RED,    HEX,      'PHYSR',                -1, -1,  1,  2, -2,  1,  3,
      'Physical Resistance The creature was at once terrible and graceful, the result of blasphemous '+
      'trafficks with some otherworldly horror.');
  Add('Ghost',        EXP_AH, M_YELLOW,  MOON,     'PHYSI,UNDEAD',         -3, -2,  2,  1, -3,  2,  3,
      'Physical Immunity Undead');
  Add('Ghoul',        EXP_AH, M_BLACK,   HEX,      'AMBUSH',               -3,  0,  1,  1, -1,  1,  3,
      'Ambush Most of the bodies, while roughly bipedal, had a forward slumping, and a vaguely canine cast. '+
      'The texture of the majority was a kind of unpleasant rubberiness.');
  Add('GodOfTheBloodyTongue', EXP_AH, M_BLACK,   DIAMOND,  'MASK,ENDLESS,O1,N1',    1, -3,  3,  4, -4,  4,  1,
      'Mask Endless Nightmarish 1 Overwhelming 1');
  Add('Gug',          EXP_AH, M_BLACK,   SLASH,    'O1',                   -2, -1,  2,  3, -2,  4,  2,
      'Overwhelming 1 I caught confused glimpses of a terrible, wrongly-angled mouth; multi-jointed arms, '+
      'and protrudings eyes as big as a man''s head.');
  Add('HaunterOfTheDark', EXP_AH, M_BLUE,  SQUARE,   'MASK,ENDLESS',       -3, -2,  2,  2, -2,  2,  1,
      'Mask Endless If the Blackest Night card is in play, Haunter of the Dark`s fight rating increases to -5.');
  Add('HighPriest',   EXP_AH, M_BLACK,   CROSS,    'MAGICI',               -2,  1,  1,  2, -2,  2,  1,
      'Magical Immunity "We will not cease our struggle," intoned the robed figure, '+
      '"Until we have built Carcosa upon this land of ruined Reason."');
  Add('HoundOfTindalos', EXP_AH, M_GREEN,   SQUARE,   'PHYSI',             -1, -2,  4,  2, -1,  3,  1,
      'Physical Immunity When it moves, the Hound of Tindalos moves directly to the nearest investigator inside a '+
      'location in Arkham (Other than the Hospital or Asylum).');
  Add('Maniac',       EXP_AH, M_BLACK,   MOON,     '',                     -1,  0,  0,  1,  1,  1,  3,
      'If the terror level is at least 6, Maniac`s fight rating increases to -2, his combat damage increases '+
      'to 3 Stamina, and he gains Endless.');
  Add('MiGo',         EXP_AH, M_BLUE,    ROUNDEL,  '',                     -2, -1,  2,  1,  0,  1,  3,
      'If you pass a Combat check against Migo, return it to the box and draw 1 Unique Item.');
  Add('Nightgaunt',   EXP_AH, M_BLUE,    SLASH,    '',                     -2, -1,  1,  2, -2,  0,  2,
      'When you fail a Combat check against Nightgaunt, you are drawn through the nearest open gate. '+
      'If two or more gates are the same distance from you, you choose which gate you are drwan through.');
  Add('Riot1',        EXP_TKIY, M_BLACK,   MOON,     'SPAWN,O1,NORTHSIDE', -4,  0,  0,  3, -4,  4,  1,
      'If you pass a Combat check against Riot, lose 1 Sanity and roll a die. On a 4-6, the terror level '+
      'is increased by 1.');
  Add('Riot2',        EXP_TKIY, M_BLACK,   MOON,     'SPAWN,O1,SOUTHSIDE', -4,  0,  0,  3, -4,  4,  1,
      'If you pass a Combat check against Riot, lose 1 Sanity and roll a die. On a 4-6, the terror level '+
      'is increased by 1.');
  Add('Riot3',        EXP_TKIY, M_BLACK,   MOON,  'SPAWN,O1,MUNIVERSITY',  -4,  0,  0,  3, -4,  4,  1,
      'If you pass a Combat check against Riot, lose 1 Sanity and roll a die. On a 4-6, the terror level '+
      'is increased by 1.');
  Add('Shoggoth',     EXP_AH, M_RED,     DIAMOND,  'PHYSR,N1',             -1, -1,  3,  3, -1,  3,  2,
      'Physical Resistance Nightmarish 1 The stench was unbearable, and rising to the surface came '+
      'a terrible cry. "Tekeli-li! Tekeli-li!"');
  Add('StarSpawn',    EXP_AH, M_BLACK,   CROSS,    '',                     -1, -3,  2,  3, -3,  3,  2,
      'The bosun was the only one left alive. We dragged him screaming from the cargo hold. '+
      '"That thing!" he wept. "Not a whale... not an island..."');
  Add('TheBlackMan',  EXP_AH, M_BLACK,   MOON,     'MASK,ENDLESS',         -3,  0,  0,  1,  0,  0,  1,
      'Mask Endless Before making a Horror check pass a Luck (-1) check or be devoured. '+
      'If you pass gain 2 Clue tokens. In either case, return the Black Man to the cup.');
  Add('TheBloatedWoman', EXP_AH, M_BLACK,   HEX,      'MASK,ENDLESS',      -1, -1,  2,  2, -2,  2,  1,
      'Mask Endless Before making a Horror check pass a Will (-2) check or automatically '+
      'fail the Horror check and the Combat check.');
  Add('TheDarkPharoah', EXP_AH, M_BLACK,   SLASH,    'MASK,ENDLESS',       -1, -1,  1,  2, -3,  3,  1,
      'Mask Endless Use Lore in combat with Dark Pharoah instead of Fight.');
  Add('Vampire',      EXP_AH, M_BLACK,   MOON,     'UNDEAD,PHYSR',         -3,  0,  2,  2, -3,  3,  1,
      'Undead Physical Resistance It was a beast born in the grave. It stretched its hands toward us '+
      'and curled its lips, drawn to the blood in our veins.');
  Add('Warlock',      EXP_AH, M_YELLOW,  ROUNDEL,  'MAGICI',               -2, -1,  1,  2, -3,  1,  2,
      'Magic Immunity If you pass a Combat check against Warlock, return it to the box and gain 2 Clue tokens.');
  Add('Witch',        EXP_AH, M_BLACK,   ROUNDEL,  'MAGICR',               -1,  0,  0,  1, -3,  2,  2,
      'Magic Resistance She was lovely and terrible all at once. A strnage light shone '+
      'in her eyes as she chanted, "Ia! Ia! Shub-Niggurath! The Goat with a Thousand Young!"');
  Add('Zombie',       EXP_AH, M_BLACK,   MOON,     'UNDEAD',                1, -1,  1,  1, -1,  2,  3,
      'Undead She screamed and fired again, but still the thing shambled on, teeth dripping '+
      'as it groaned its horrible cry.');
end;

initialization
  Monsters := TStringList.Create;
  LoadMonsters;
  Monsters.Sort;
end.

