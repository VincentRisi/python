unit AHICards;
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
  ICards         : TStringList;

implementation

procedure Add(const aName        : string;
              const aExpansion   : EExpansion;
              const aFullName    : string;
              const aICardType   : EICardType;
              const aNoOf        : integer;
              const aCost        : integer;
              const aHanded      : integer;
              const aUpKeep      : string;
              const aExhaust     : string;
              const aDescription : string);
var
  ICard : TICard;
begin
  ICard := TICard.Create;
  with ICard do begin
    name         := aName;
    expansion    := aExpansion;
    fullname     := aFullName;
    icardtype    := aICardType;
    noOf         := aNoOf;
    cost         := aCost;
    handed       := aHanded;
    upkeep       := aUpKeep;
    exhaust      := aExhaust;
    description  := aDescription;
  end;
  ICards.AddObject(aName, ICard);
end;

function makeKey(name : string) : string;
var
  i : integer;
begin
  name := UpperCase(name);
  result := '';
  for i := 1 to length(name) do begin
    if (name[i] <> ' ') and (name[i] <> '''') and (name[i] <> '-') then
      result := result + name[i];
  end;
end;

procedure AddCorrupt(const aName        : string;
                     const aColor       : string;
                     const aFaction     : EFactionType;
                     const aNoOf        : integer;
                     const aDescription : string);
var
  ICard : TICard;
begin
  ICard := TICard.Create;
  with ICard do begin
    name         := makeKey(aName);
    expansion    := EXP_TBGOTW;
    fullname     := aName;
    if aColor = 'Green' then
      icardtype    := GCORRUPT
    else
      icardtype    := RCORRUPT;
    noOf         := aNoOf;
    cost         := 0;
    handed       := 0;
    upkeep       := 'N';
    exhaust      := 'N';
    description  := aDescription;
  end;
  ICards.AddObject(aName, ICard);
end;

procedure AddCult(const aName        : string;
                  const aNoOf        : integer;
                  const aDescription : string);
var
  ICard : TICard;
begin
  ICard := TICard.Create;
  with ICard do begin
    name         := makeKey(aName);
    expansion    := EXP_TBGOTW;
    fullname     := aName;
    icardtype    := CULT;
    noOf         := aNoOf;
    cost         := 0;
    handed       := 0;
    upkeep       := 'N';
    exhaust      := 'N';
    description  := aDescription;
  end;
  ICards.AddObject(aName, ICard);
end;

procedure AddBlight(const aName        : string;
                    const aFullname    : string;
                    const aDescription : string);
var
  ICard : TICard;
begin
  ICard := TICard.Create;
  with ICard do begin
    name         := makeKey(aName);
    expansion    := EXP_TKIY;
    fullname     := aFullname;
    icardtype    := BLIGHT;
    noOf         := 1;
    cost         := 0;
    handed       := 0;
    upkeep       := 'N';
    exhaust      := 'N';
    description  := aDescription;
  end;
  ICards.AddObject(aName, ICard);
end;

procedure AddDarkPact(const aName        : string;
                     const aFullname    : string;
                     const aDescription : string);
var
  ICard : TICard;
begin
  ICard := TICard.Create;
  with ICard do begin
    name         := makeKey(aName);
    expansion    := EXP_TLATT;
    fullname     := aFullname;
    icardtype    := DARKPACT;
    noOf         := 1;
    cost         := 0;
    handed       := 0;
    upkeep       := 'N';
    exhaust      := 'N';
    description  := aDescription;
  end;
  ICards.AddObject(aName, ICard);
end;

procedure AddDifficulty(const aName    : string;
                        const aCost    : integer;
                        const aSetup   : string;
                        const aMythos  : string;
                        const aScoring : string);
var
  ICard : TICard;
begin
  ICard := TICard.Create;
  with ICard do begin
    name         := makeKey(aName);
    expansion    := EXP_TBGOTW;
    fullname     := aName;
    icardtype    := DIFFICULTY;
    noOf         := 1;
    cost         := aCost;
    handed       := 0;
    upkeep       := 'N';
    exhaust      := 'N';
    description  := format('%s %s %s', [aSetup, aMythos, aScoring]);
  end;
  ICards.AddObject(aName, ICard);
end;

procedure AddRelationShip(const aName        : string;
                          const aFullname    : string;
                          const aDescription : string);
var
  ICard : TICard;
begin
  ICard := TICard.Create;
  with ICard do begin
    name         := makeKey(aName);
    expansion    := EXP_TLATT;
    fullname     := aFullName;
    icardtype    := RELATIONSHIP;
    noOf         := 1;
    cost         := 0;
    handed       := 0;
    upkeep       := 'N';
    exhaust      := 'N';
    description  := aDescription;
  end;
  ICards.AddObject(aName, ICard);
end;

procedure AddReckoning(const aName        : string;
                          const aFullname    : string;
                          const aDescription : string);
var
  ICard : TICard;
begin
  ICard := TICard.Create;
  with ICard do begin
    name         := makeKey(aName);
    expansion    := EXP_TLATT;
    fullname     := aFullName;
    icardtype    := RECKONING;
    noOf         := 1;
    cost         := 0;
    handed       := 0;
    upkeep       := 'N';
    exhaust      := 'N';
    description  := aDescription;
  end;
  ICards.AddObject(aName, ICard);
end;

procedure Load;
begin
  Add('ANNAKASLOW', EXP_AH, 'Anna Kaslow', ALLY, 1, 0, 0, 'N','N',
       '+2 Luck Gain 2 Clue tokens when Anna Kaslow joins you.');
  Add('DAVIDPACKARD', EXP_COTDP, 'David Packard', ALLY, 1, 0, 0, 'N','N',
       '+1 Fight +1 Sneak Draw 1 Skill card when David Packard joins you.');
  Add('DRALIKAFOUR', EXP_COTDP, 'Dr. Ali Kafour', ALLY, 1, 0, 0, 'N','N',
       '+1 Will +1 Lore Search the Unique item deck, taking the first tome you find.');
  Add('DUKE', EXP_AH, 'Duke', ALLY, 1, 0, 0, 'N','N',
       '+1 Maximum Sanity Discard to immediately restore your Sanity to its maximum.');
  Add('ERICACARLYLE', EXP_COTDP, 'Erica Carlyle', ALLY, 1, 0, 0, 'N','N',
       '+2 Spell Gain a Retainer card when Erica Carlyle joins you.');
  Add('ERICCOLT', EXP_AH, 'Eric Colt', ALLY, 1, 0, 0, 'N','N',
       '+2 Speed You take no Sanity loss from the Nightmarish ability.');
  Add('ERICHWEISS', EXP_COTDP, 'Erich Weiss', ALLY, 1, 0, 0, 'N','N',
       '+2 Evade You cannot be delayed.');
  Add('FATHERIWANICKI', EXP_COTDP, 'Father Iwanicki', ALLY, 1, 0, 0, 'N','N',
       '+2 Horror You cannot be cursed.');
  Add('JOHLEGRASSE', EXP_AH, 'John Legrasse', ALLY, 1, 0, 0, 'N','N',
       '+2 Will You can claim monsters with the Endless ability as trophies.');
  Add('PROFARMITAGE', EXP_AH, 'Professor Armitage', ALLY, 1, 0, 0, 'N','N',
       '+2 Lore Your attacks are not affected by Magical Resistance.');
  Add('RICHARDPICKMAN', EXP_AH, 'Richard Upton Pickman', ALLY, 1, 0, 0, 'N','N',
       '+1 Luck, +1 Speed Your attacks are not affected by Physical Resistance.');
  Add('RUBYSTANDISH', EXP_AH, 'Ruby Standish', ALLY, 1, 0, 0, 'N','N',
       '+2 Sneak Draw I Unique Item when Ruby Standish joins you.');
  Add('RYANDEAN', EXP_AH, 'Ryan Dean', ALLY, 1, 0, 0, 'N','N',
       '+1 Will, +1 Sneak Draw 1 Common Item when Ryan Dean joins you.');
  Add('SARAHDANFORTH', EXP_COTDP, 'Sarah Danforth', ALLY, 1, 0, 0, 'N','N',
       '+1 Focus Draw 1 Exhibit item when Sarah Danforth joins you.');
  Add('SIRBRINTON', EXP_AH, 'Sir William Brinton', ALLY, 1, 0, 0, 'N','N',
       '+1 Maximum Stamina Discard to immediately restore your Stamina to its maximum.');
  Add('THEMESSENGER', EXP_COTDP, 'The Messenger', ALLY, 1, 0, 0, 'N','N',
      '-1 All Skill checks After being devoured, return this card to the box and remove '+
      'two doom tokens from the doom track.');
  Add('THOMASFMALONE', EXP_AH, 'Thomas F. Malone', ALLY, 1, 0, 0, 'N','N',
       '+1 Lore, +1 Fight Draw I Spell When Thomas F. Malone joins you.');
  Add('TOMMURPHY', EXP_AH, 'Tom "Mountain" Murphy', ALLY, 1, 0, 0, 'N','N',
       '+2 Fight You take no Stamina loss from the Overwhelming ability.');
  Add('BARREDFROMDOWNTOWN', EXP_COTDP, 'Barred from Downtown', BARRED, 2, 0, 0, 'N','N',
      'Move to the street when you receive this card. You may not enter any Downtown '+
      'locations during the Movement phase except those with open gates. You may enter '+
      'Downtown locations via other means during other phases (for instance, as a '+
      'result of an Arkham encounter or when being sent to Arkham Asylum). Discard this '+
      'card if the terror level increases.');
  Add('BARREDFROMEASTTOWN', EXP_COTDP, 'Barred from Easttown', BARRED, 2, 0, 0, 'N','N',
      'You may not enter any Easttown locations during the Movement phase unless they '+
      'have gates. You may enter Easttown locations via other means during other phases '+
      '(for instance, as a result of an Arkham encounter or when being arrested. '+
      'Discard this card if the terror level increases.');
  Add('BARREDFROMFRENCHHILL', EXP_COTDP, 'Barred from French Hill', BARRED, 2, 0, 0, 'N','N',
      'Move to the street when you receive this card. You may not enter any French Hill '+
      'locations during the Movement phase except those with open gates. You may enter '+
      'French Hill locations via other means during other phases (for instance, as a '+
      'result of an Arkham encounter or when returning from being Lost in Time and '+
      'Space). Discard this card if the terror level increases.');
  Add('BARREDFROMMERCHANTDISTRICT', EXP_COTDP, 'Barred from Merchant District', BARRED, 2, 0, 0, 'N','N',
      'Move to the street when you receive this card. You may not enter any Merchant '+
      'District locations during the Movement phase except those with open gates. You '+
      'may enter Merchant District locations via other means during other phases (for '+
      'instance, as a result of an Arkham encounter or when returning from being Lost '+
      'in Time and Space). Discard this card if the terror level increases.');
  Add('BARREDFROMMISKATONICU.', EXP_COTDP, 'Barred from Miskatonic U.', BARRED, 2, 0, 0, 'N','N',
      'Move to the street when you receive this card. You may not enter any Miskatonic '+
      'University locations during the Movement phase except those with open gates. You '+
      'may enter Miskatonic University locations via other means during other phases '+
      '(for instance, as a result of an Arkham encounter or when returning from being '+
      'Lost in Time and Space). Discard this card if the terror level increases.');
  Add('BARREDFROMNORTHSIDE', EXP_COTDP, 'Barred from Northside', BARRED, 2, 0, 0, 'N','N',
      'Move to the street when you receive this card. You may not enter any Northside '+
      'locations during the Movement phase except those with open gates. You may enter '+
      'Northside locations via other means during other phases (for instance, as a '+
      'result of an Arkham encounter or when returning from being Lost in Time and '+
      'Space). Discard this card if the terror level increases.');
  Add('BARREDFROMRIVERTOWN', EXP_COTDP, 'Barred from Rivertown', BARRED, 2, 0, 0, 'N','N',
      'Move to the street when you receive this card. You may not enter any Rivertown '+
      'locations during the Movement phase except those with open gates. You may enter '+
      'Rivertown locations via other means during other phases (for instance, as a '+
      'result of an Arkham encounter or when returning from being Lost in Time and '+
      'Space). Discard this card if the terror level increases.');
  Add('BARREDFROMSOUTHSIDE', EXP_COTDP, 'Barred from Southside', BARRED, 2, 0, 0, 'N','N',
      'Move to the street when you receive this card. You may not enter any Southside '+
      'locations during the Movement phase except those with open gates. You may enter '+
      'Southside locations via other means during other phases (for instance, as a '+
      'result of an Arkham encounter or when returning from being Lost in Time and '+
      'Space). Discard this card if the terror level increases.');
  Add('BARREDFROMUPTOWN', EXP_COTDP, 'Barred from Uptown', BARRED, 2, 0, 0, 'N','N',
      'Move to the street when you receive this card. You may not enter any Uptown '+
      'locations during the Movement phase except those with open gates. You may enter '+
      'Uptown locations via other means during other phases (for instance, as a result '+
      'of an Arkham encounter or when being sent to St. Marys Hospital). Discard this '+
      'card if the terror level increases.');
  Add('.18DERRINGER', EXP_AH, '.18 Derringer', COMMON, 2, 3, 1, 'N','N',
      'Physical Weapon +2 to Combat checks 18 Derringer cannot be lost or stolen unless '+
      'you choose to allow it.');
  Add('.357MAGNUM', EXP_TBGOTW, '.357 Magnum', COMMON, 2, 8, 1, 'N','N',
      'Physical weapon Any: Exhaust to gain +5 to Combat checks until the end of this '+
      'combat. Upkeep: .357 Magnum does not refresh unless you spend $1.');
  Add('.38REVOLVER', EXP_AH, '.38 Revolver', COMMON, 2, 4, 1, 'N','N',
      'Physical Weapon +3 to Combat checks');
  Add('.45AUTOMATIC', EXP_AH, '.45 Automatic', COMMON, 2, 5, 1, 'N','N',
      'Physical Weapon +4 to Combat checks');
  Add('ANCIENTTOME', EXP_AH, 'Ancient Tome', COMMON, 2, 4, 0, 'N','N',
      'Tome Movement: Exhaust and spend 2 movement points to make a Lore (-1) check. If '+
      'you pass, draw 1 Spell and discard Ancient Tome. If you fail, nothing happens.');
  Add('AXE', EXP_AH, 'Axe', COMMON, 2, 3, 1, 'N','N',
      'Physical Weapon +2 to Combat checks (+3 instead if your other hand is empty)');
  Add('BULLWHIP', EXP_AH, 'Bullwhip', COMMON, 2, 2, 1, 'N','N',
      'Physical Weapon +1 to Combat checks Any Phase: Exhaust to re-roll 1 die after '+
      'making a Combat check');
  Add('CAVALRYSABER', EXP_AH, 'Cavalry Saber', COMMON, 2, 3, 1, 'N','N',
      'Physical Weapon +2 to Combat checks');
  Add('CROSS', EXP_AH, 'Cross', COMMON, 2, 3, 1, 'N','N',
      'Magical Weapon +0 to Combat checks (+3 if Opponent is Undead) +1 to Horror '+
      'checks');
  Add('CROWBAR', EXP_TBGOTW, 'Crowbar', COMMON, 2, 4, 1, 'N','N',
      'Physical weapon +2 to Combat checks Movement: Discard Crowbar to make a Sneak '+
      '(-2) check. Draw a Common item for each success you roll. If you fail, you are '+
      'arrested.');
  Add('DARKCLOAK', EXP_AH, 'Dark Cloak', COMMON, 2, 2, 0, 'N','N',
       '+1 to Evade checks');
  Add('DYNAMITE', EXP_AH, 'Dynamite', COMMON, 2, 4, 2, 'N','N',
      'Physical Weapon +8 to Combat checks (Discard after use)');
  Add('FOOD', EXP_AH, 'Food', COMMON, 2, 1, 0, 'N','N',
      'Any Phase: Discard Food to reduce any Stamina loss by 1');
  Add('GRAYSANATOMY', EXP_TBGOTW, 'Grays Anatomy', COMMON, 1, 3, 0, 'N','N',
      'Arkham Encounters: Exhaust when spending a monster trophy to increase the '+
      'toughness value of that trophy by 1.');
  Add('KNIFE', EXP_AH, 'Knife', COMMON, 2, 2, 1, 'N','N',
      'Physical Weapon +1 to Combat checks');
  Add('LANTERN', EXP_AH, 'Lantern', COMMON, 2, 3, 0, 'N','N',
       '+1 to Luck checks');
  Add('LUCKYCIGCASE', EXP_AH, 'Lucky Cigarette Case', COMMON, 2, 1, 0, 'N','N',
      'Any Phase: Discard Lucky Cigarette Case to re- roll any one skill check.');
  Add('LUCKYRABBITSFOOT', EXP_TBGOTW, 'Lucky Rabbits Foot', COMMON, 1, 4, 0, 'N','N',
      'Arkham Encounters: After you draw an encounter card, exhaust and discard Lucky '+
      'Rabbits Foot to draw a different encounter card. Any: Exhaust to gain +1 to a '+
      'Luck check.');
  Add('MAGNIFYINGGLASS', EXP_TBGOTW, 'Magnifying Glass', COMMON, 2, 2, 0, 'N','N',
      'Any phase: Exhaust and discard after you gain a Clue token to gain 1 additional '+
      'Clue token. Movement: Exhaust to gain +2 to Lore checks when reading Tomes.');
  Add('MAPOFARKHAM', EXP_AH, 'Map of Arkham', COMMON, 2, 2, 0, 'N','N',
      'Movement: Exhaust to get 1 extra movement point.');
  Add('MILITARYMOTORCYCLE', EXP_TBGOTW, 'Military Motorcycle', COMMON, 1, 6, 0, 'N','N',
      'Bonus: +1 to Evade checks. Movement: Exhaust to gain 2 extra movement points.');
  Add('MOTORCYCLE', EXP_AH, 'Motorcycle', COMMON, 2, 4, 0, 'N','N',
      'Movement: Exhaust to get 2 extra movement points.');
  Add('OLDJOURNAL', EXP_AH, 'Old Journal', COMMON, 2, 1, 0, 'N','N',
      'Tome Movement: Exhaust and spend 1 movement point to make a Lore (-1) check. If '+
      'you pass, gain 3 Clue tokens and discard Old Journal. If you fail, nothing '+
      'happens.');
  Add('RESEARCH', EXP_AH, 'Research Materials', COMMON, 2, 1, 0, 'N','N',
      'Any Phase: Discard Research Materials instead of spending 1 Clue token.');
  Add('RIFLE', EXP_AH, 'Rifle', COMMON, 2, 6, 2, 'N','N',
      'Physical Weapon +5 to Combat checks');
  Add('SHOTGUN', EXP_AH, 'Shotgun', COMMON, 2, 6, 2, 'N','N',
      'Physical Weapon +4 to Combat checks Any Phase: When using Shotgun in Combat, all '+
      '6"s rolled count as 2 successes.');
  Add('STUDENTNEWSPAPER', EXP_TBGOTW, 'Student Newspaper', COMMON, 2, 1, 0, 'N','N',
      'Movement: Discard Student Newspaper to choose a Clue token in any location. Take '+
      'that Clue token.');
  Add('TOMMYGUN', EXP_AH, 'Tommy Gun', COMMON, 2, 7, 2, 'N','N',
      'Physical Weapon +6 to Combat checks');
  Add('WHISKEY', EXP_AH, 'Whiskey', COMMON, 2, 1, 0, 'N','N',
      'Any Phase: Discard Whiskey to reduce any Sanity loss by 1.');
  Add('ATHAME', EXP_TKIY, 'Athame', COMMON, 2, 3, 1, 'N','N',
      'Physical weapon Bonus: +1 to Combat check +3 instead if opponent has Magical '+
      'Resistance +6 instead if opponent has Magical Immunity.');
  Add('DIRECTORSDIARY', EXP_TKIY, 'Directors Diary', COMMON, 2, 4, 0, 'N','N',
      'Tome Any: Discard this card when the terror level is increased to reduce the '+
      'amount by which it is being increased by 1.');
  Add('LEYLINEMAP', EXP_TKIY, 'Ley Line Map', COMMON, 2, 2, 0, 'N','N',
      'You may ignore all penalties to Skill checks caused by Environment Mythos cards.');
  Add('PRESSPASS', EXP_TKIY, 'Press Pass', COMMON, 2, 5, 0, 'N','N',
      'Any: Exhaust when you gain one or more Clue tokens to gain 1 extra Clue token.');
  Add('SAFETYDEPOSITKEY', EXP_TKIY, 'Safety Deposit Key', COMMON, 3, 2, 0, 'N','N',
      'Movement: Spend 1 movement point and discard this card while in the Bank of '+
      'Arkham to make a Luck (-2) check. If you succeed, draw 1 Unique item. If you '+
      'fail, gain 2 Clue tokens.');
  Add('SEDANETTE', EXP_TKIY, 'Sedanette', COMMON, 2, 4, 0, 'N','N',
      'You may automatically Evade monsters of toughness 1 while in the street.');
  Add('TIMEBOMB', EXP_TKIY, 'Time Bomb', COMMON, 3, 3, 0, 'N','N',
      'Upkeep: If this card is on a location or street area, discard 1 Clue token from '+
      'it. If there are no Clue tokens left to discard, return all monsters in the '+
      'location/area to the cup, reduce all investigators in the location/area to 0 '+
      'Stamina, and discard this card. Movement: You may place this card on your '+
      'current Arkham location or street area with up to 3 Clue tokens from the bank on '+
      'it.');
  Add('UNDERSTUDYSSCRIPT', EXP_AH, 'Understudys Script', COMMON, 3, 3, 0, 'N','N',
      'Upkeep: If this card is on a location or street area, discard 1 Clue token from '+
      'it. If there are no Clue tokens left to discard, return all monsters in the '+
      'location/area to the cup, reduce all investigators in the location/area to 0 '+
      'Stamina, and discard this card. Movement: You may place this card on your '+
      'current Arkham location or street area with up to 3 Clue tokens from the bank on '+
      'it.');
  Add('FINECLOTHING', EXP_TKIY, 'Fine Clothing', COMMON, 1, 3, 0, 'N','N',
      'Upkeep: If this card is on a location or street area, discard 1 Clue token from '+
      'it. If there are no Clue tokens left to discard, return all monsters in the '+
      'location/area to the cup, reduce all investigators in the location/area to 0 '+
      'Stamina, and discard this card. Movement: You may place this card on your '+
      'current Arkham location or street area with up to 3 Clue tokens from the bank on '+
      'it.');
  Add('HANDCAMERA', EXP_TKIY, 'Hand Camera', COMMON, 1, 3, 0, 'N','N',
      'Type: Tome Movement: Exhaust and spend 2 movement points to make a Will (-2) '+
      'check. If you pass, draw 1 Spell, gain 2 Clue tokens, and discard Understudys '+
      'Script. If you fail, you lose 1 Sanity.');
  Add('KINGJAMESBIBLE', EXP_TKIY, 'King James Bible', COMMON, 1, 3, 0, 'N','N',
      'Type: Tome Movement: Exhaust and spend 2 movement points to regain 1 Sanity and '+
      'gain +1 to Horror checks until the end of the turn.');
  Add('SLEDGEHAMMER', EXP_TKIY, 'Sledgehammer', COMMON, 1, 6, 2, 'N','N',
      'Physical weapon Bonus: +3 to Combat checks and +1 to Fight checks. Reduce the '+
      'toughness of monsters you fight by 1 to a minimum of 1 (this does not affect '+
      'their value as trophies).');
  Add('BOOKOFANUBIS', EXP_COTDP, 'Book of Anubis', EXHIBIT, 1, 0, 0, 'N','N',
      'Tome When another investigator goes insane, goes unconscious, or is devoured, '+
      'you gain 1 Stamina and 1 Sanity, and gain any Clue tokens that he discards.');
  Add('CHIMEOFRA', EXP_COTDP, 'Chime of Ra', EXHIBIT, 2, 0, 0, 'N','N',
      'When you lose Sanity due to a Horror check, you may exhaust this card to reduce '+
      'the Sanity loss by 1 to a minimum of 0, even if the monster has the Nightmarish '+
      'ability.');
  Add('EYEOFLIGHTANDDARKNESS', EXP_COTDP, 'Eye of Light and Darkness', EXHIBIT, 2, 0, 0, 'N','N',
      'Before you make a skill check, you may return this card to the box and lose up '+
      'to 3 Sanity or Stamina in any combination. For each point of Sanity or Stamina '+
      'lost, you gain +2 on the skill check.');
  Add('MASKOFTHEBLACKPHARAOH', EXP_COTDP, 'Mask of the Black Pharaoh', EXHIBIT, 1, 0, 0, 'N','N',
      'Any: Exhaust this card to either use your Fight -1 instead of your Will for '+
      'making a Will check or use your Will -1 instead of your Fight for making a Fight '+
      'check.');
  Add('MASKOFTHEMESSENGER', EXP_COTDP, 'Mask of the Messenger', EXHIBIT, 1, 0, 0, 'N','N',
      'Any: Exhaust this card to either use your Sneak -1 instead of your Speed for '+
      'making a Speed check or use your Speed -1 instead of your Sneak for making a '+
      'Sneak check.');
  Add('MASKOFTHETHREEFATES', EXP_COTDP, 'Mask of the Three Fates', EXHIBIT, 1, 0, 0, 'N','N',
      'Any: Exhaust this card and spend 1 Clue token before drawing from any deck '+
      'except the Mythos deck to examine the top card and return it to either the top '+
      'or bottom of the deck.');
  Add('MASKOFVICE', EXP_COTDP, 'Mask of Vice', EXHIBIT, 1, 0, 0, 'N','N',
      'Any: Exhaust this card to gain any Common Item or Unique Item you currently have '+
      'the opportunity to purchase without paying for it.');
  Add('MASKOFWISDOM', EXP_COTDP, 'Mask of Wisdom', EXHIBIT, 1, 0, 0, 'N','N',
      'Any: Exhaust this card to either use your Lore -1 instead of your Luck for '+
      'making a Luck check or use your Luck -1 instead of your Lore for making a Lore '+
      'check.');
  Add('PARCHMENTOFTHEELDERSIGN', EXP_COTDP, 'Parchment of the Elder Sign', EXHIBIT, 3, 0, 0, 'N','N',
      'Any: You may discard this card before attempting to close a gate with a Fight '+
      'check or Lore check. If you succeed, remove 1 token from the doom track and the '+
      'gate is sealed.');
  Add('PENTAGRAMOFBLOOD', EXP_COTDP, 'Pentagram of Blood', EXHIBIT, 2, 0, 0, 'N','N',
      'Movement: Spend X Stamina and discard this card to remove one monster with X '+
      'toughness from Arkham and return it to the monster cup.');
  Add('SCALESOFTHOTH', EXP_COTDP, 'Scales of Thoth', EXHIBIT, 1, 0, 0, 'N','N',
      ' You may exhaust this card to reduce your Sanity to equal your Stamina or reduce '+
      'your Stamina to equal your Sanity. While this card is exhausted and your Sanity '+
      'and Stamina are equal, gain +1 on all skill checks.');
  Add('SPIRITVESSEL', EXP_COTDP, 'Spirit Vessel', EXHIBIT, 2, 0, 0, 'N','N',
      'All of your monster trophies count as being one toughness higher for the '+
      'purposes of spending them.');
  Add('SUMMONINGGLASS', EXP_COTDP, 'Summoning Glass', EXHIBIT, 2, 0, 0, 'N','N',
      'Arkham Encounters: In addition to your normal encounter, discard this card to '+
      'resolve the special ability of any Arkham location without a gate. You may trade '+
      'in trophies or money as if you were there.');
  Add('TABLETOFBAST', EXP_COTDP, 'Tablet of Bast', EXHIBIT, 2, 0, 0, 'N','N',
      'Tome Arkham Encounters: Discard this card after you fail a skill check to ignore '+
      'the effects of the check.');
  Add('DEPUTYOFARKHAM', EXP_AH, 'Deputy of Arkham', PATROL, 1, 0, 0, 'N','N',
      'When you gain this card, take the Deputy"s Revolver and the Patrol Wagon as '+
      'well. Upkeep: Gain $1.');
  Add('DEPUTYREVOLVER', EXP_AH, 'Deputy Revolver', PATROL, 1, 0, 1, 'N','N',
      'Physical Weapon +3 to Combat checks Deputy"s Revolver cannot be lost or stolen '+
      'unless you choose to allow it.');
  Add('PATROLWAGON', EXP_AH, 'Patrol Wagon', PATROL, 1, 0, 0, 'N','N',
      'Movement: If you are in Arkham, you may move to any street area or location in '+
      'Arkham instead of your normal movement. Roll a die at the end of each Combat and '+
      'whenever you return to Arkham from an Other World. On a l, return this card to '+
      'the box.');
  Add('BRAVERY', EXP_AH, 'Bravery', SKILL, 2, 0, 0, 'N','N',
      'Any Phase: Exhaust to re-roll a Horror check.');
  Add('EXPERTOCCULTIST', EXP_AH, 'Expert Occultist', SKILL, 2, 0, 0, 'N','N',
      'Any Phase: Exhaust to re-roll a Spell check.');
  Add('FIGHT', EXP_AH, 'Fight', SKILL, 2, 0, 0, 'N','N',
       '+1 Fight When you spend a Clue token to add to any Fight check, add one extra '+
      'bonus die.');
  Add('LORE', EXP_AH, 'Lore', SKILL, 2, 0, 0, 'N','N',
       '+1 Lore When you spend a Clue token to add to any Lore check, add one extra '+
      'bonus die.');
  Add('LUCK', EXP_AH, 'Luck', SKILL, 2, 0, 0, 'N','N',
       '+1 Luck When you spend a Clue token to add to any Luck check, add one extra '+
      'bonus die.');
  Add('MARKSMAN', EXP_AH, 'Marksman', SKILL, 2, 0, 0, 'N','N',
      'Any Phase: Exhaust to re-roll a Combat check.');
  Add('SNEAK', EXP_AH, 'Sneak', SKILL, 2, 0, 0, 'N','N',
       '+1 Sneak When you spend a Clue token to add to any Sneak check, add one extra '+
      'bonus die.');
  Add('SPEED', EXP_AH, 'Speed', SKILL, 2, 0, 0, 'N','N',
       '+1 Speed When you spend a Clue token to add to any Speed check, add one extra '+
      'bonus die.');
  Add('STEALTH', EXP_AH, 'Stealth', SKILL, 2, 0, 0, 'N','N',
      'Any Phase: Exhaust to re-roll an Evade check.');
  Add('WILL', EXP_AH, 'Will', SKILL, 2, 0, 0, 'N','N',
       '+1 Will When you spend a Clue token to add to any Will check, add one extra '+
      'bonus die.');
  Add('ANOINTED', EXP_COTDP, 'Anointed(benefit)', SPECIAL, 1, 0, 0, 'N','N',
      'When you receive this card, discard a Curse card, if you have one. Upkeep: You '+
      'may choose one other investigator in Arkham to re-roll the roll to discard a '+
      'Curse card. Discard this card if you are Cursed.');
  Add('BANKLOAN', EXP_AH, 'Bank Loan', SPECIAL, 8, 0, 0, 'N','N',
      'Gain $10 when you take this card. Upkeep: Roll a die. On a 1-3, pay $1 or '+
      'discard all of your items along with this card. You cannot get another Bank Loan '+
      'this game. Any Phase: Pay $10 to pay off your Bank Loan and discard this card. '+
      'You may choose to take out a new Bank Loan later on during this game.');
  Add('BLESSING', EXP_AH, 'Blessing', SPECIAL, 8, 0, 0, 'N','N',
      'Upkeep: Roll a die and discard this card on a 1. When rolling dice, you score '+
      'successes on a 4, 5, or 6. If you are Cursed, discard this card instead of '+
      'gaining a Curse card.');
  Add('CURSE', EXP_AH, 'Cursed', SPECIAL, 8, 0, 0, 'N','N',
      'Upkeep: Roll a die and discard this card on a 1. When rolling dice, you only '+
      'score successes on 6. If you are Blessed, discard this card instead of gaining '+
      'a Blessing card.');
  Add('HARRIED', EXP_COTDP, 'Harried(detriment)', SPECIAL, 1, 0, 0, 'N','N',
      'When you receive this card, lose 1 Sanity. Upkeep: If you are in a street area, '+
      'you must choose one monster in Arkham or the Sky to move to your location. '+
      'Discard this card when you defeat a monster with 2 or more toughness.');
  Add('LOCALGUIDE', EXP_COTDP, 'Local Guide(detriment)', SPECIAL, 1, 0, 0, 'N','N',
      'When you receive this card, you are delayed. Upkeep: If you are in Arkham, your '+
      'focus is reduced by 1 (to a minimum of 0). Discard this card when you have $10 '+
      'or more.');
  Add('PRIVATEINVESTIGATOR', EXP_COTDP, 'Private Investigator(benefit)', SPECIAL, 1, 0, 0, 'N','N',
      'When you receive this card, gain 3 Clue tokens. Upkeep: You may choose one other '+
      'investigator in Arkham who is delayed to no longer be delayed. Discard this card '+
      'if you are arrested.');
  Add('PSYCHIC', EXP_COTDP, 'Psychic(benefit)', SPECIAL, 1, 0, 0, 'N','N',
      'Upkeep: You may allow any one investigator to loan a Skill card to another '+
      'investigator (regardless of their locations) for this turn only. Discard this '+
      'card if you are Lost in Time and Space.');
  Add('RETAINER', EXP_AH, 'Retainer', SPECIAL, 8, 0, 0, 'N','N',
      'Upkeep: Gain $2, then roll a die Discard this card on a 1.');
  Add('STLMEMBER', EXP_AH, 'Silver Twighlight Lodge Member', SPECIAL, 8, 0, 0, 'N','N',
      'Any Phase: Whenever you have an encounter at the Silver Twilight Lodge, you have '+
      'an encounter at the Inner Sanctum instead.');
  Add('TAINTED', EXP_COTDP, 'Tainted(detriment)', SPECIAL, 1, 0, 0, 'N','N',
      'When you receive this card, discard a Blessing card, if you have one. Upkeep: '+
      'When rolling to determine whether or not you keep a Curse card, you must roll '+
      'twice and take the worse of the two rolls. Discard this card if you are Blessed.');
  Add('VISIONS', EXP_COTDP, 'Visions(benefit)', SPECIAL, 1, 0, 0, 'N','N',
      'Upkeep: You may allow any other investigator to discard a Spell in order to gain '+
      'Clue tokens equal to 1 plus the Spells Sanity cost. Discard this card if you are '+
      'drawn through a gate during the Mythos phase.');
  Add('WANTED', EXP_COTDP, 'Wanted(detriment)', SPECIAL, 1, 0, 0, 'N','N',
      'When you receive this card, move to the street area of your current '+
      'neighborhood. Upkeep: If you are in Arkham, pay $1 or set your skill slider to '+
      'your lowest possible Speed score before you adjust skills. Discard this card '+
      'when you seal a gate.');
  Add('ASTRALTRAVEL', EXP_COTDP, 'Astral Travel', SPELL, 3, 0, 0, 'N','N',
      'Casting Modifier: -2 Sanity Cost: 1 Casting phase: Arkham Encounters Effect: '+
      'When in Arkham, instead of having an encounter, cast and discard to move to the '+
      'first area of any Other World.');
  Add('BINDMONSTER', EXP_AH, 'Bind Monster', SPELL, 2, 0, 2, 'N','N',
      'Casting Modifier: +4 Sanity Cost: 2 Magical Spell Any Phase: Cast and discard '+
      'this spell to pass one Combat check. You must roll success equal to the monsters '+
      'toughness to cast this spell. not in end game');
  Add('CALLANCIENTONE', EXP_TBGOTW, 'Call Ancient One', SPELL, 1, 0, 0, 'N','N',
      'Casting Modifier: -X Sanity Cost: X Casting phase: Any Effect: Discard X monster '+
      'and/or gate trophies, then cast and discard this spell to immediately awaken the '+
      'Ancient One. Then, remove X doom tokens from its doom track.');
  Add('DENYINGTHEANCIENTONE', EXP_COTDP, 'Denying the Ancient One', SPELL, 2, 0, 0, 'N','N',
      'Casting Modifier: -1 Sanity Cost: 1 Casting phase: Upkeep Effect: Worshippers of '+
      'the Ancient One lose any abilities granted to them by the Ancient One this turn.');
  Add('DREADCURSEAZAROTH', EXP_AH, 'Dread Curse of Azathoth', SPELL, 4, 0, 2, 'N','N',
      'Castmod: -2 Sanity Cost: 2 Magical Spell Any Phase: Cast and exhaust to gain +9 '+
      'to Combat checks until the end of this combat.');
  Add('ENCHANTWEAPON', EXP_AH, 'Enchant Weapon', SPELL, 3, 0, 0, 'N','N',
      'Castmod: 0 Sanity Cost: 1 Magical Spell Any Phase: Cast and exhaust to make one '+
      'Physical Weapon a Magical Weapon until the end of this combat.');
  Add('FEEDINGTHEMIND', EXP_COTDP, 'Feeding the Mind', SPELL, 2, 0, 0, 'N','N',
      'Casting Modifier: -1 Sanity Cost: 0 Casting phase: Upkeep Effect: You may cast, '+
      'exhaust, and sacrifice an amount of Stamina up to the number of successes you '+
      'rolled on your Spell check. For each Stamina sacrificed you gain 2 Sanity.');
  Add('FINDGATE', EXP_AH, 'Find Gate', SPELL, 4, 0, 0, 'N','N',
      'Castmod: -1 Sanity Cost: 1 Magical Spell Movement: Cast and exhaust to '+
      'immediately return to Arkham from an Other World.');
  Add('FLESHWARD', EXP_AH, 'Flesh Ward', SPELL, 4, 0, 0, 'N','N',
      'Casting Modifier: -2 Sanity Cost: 1 Magical Spell Any Phase: Cast and exhaust to '+
      'ignore all Stamina loss being dealt to you from one source. Discard this card if '+
      'the Ancient One awakens.');
  Add('HEAL', EXP_AH, 'Heal', SPELL, 3, 0, 0, 'N','N',
      'Casting Modifier: +1 Sanity Cost: 1 Upkeep: You may cast and exhaust.  You or '+
      'another investigator in your area gains Stamina equal to the successes you '+
      'rolled on your Spell check. Stamina cant be split between investigators.');
  Add('MARKINGSOFISIS', EXP_COTDP, 'Markings of Isis', SPELL, 3, 0, 1, 'N','N',
      'Casting Modifier: Special Sanity Cost: 0 Casting phase: Any Effect: Cast and '+
      'exhaust to pass a Horror check. The casting modifier is equal to the monsters '+
      'horror rating.');
  Add('MISTSOFRELEH', EXP_AH, 'Mists of Releh', SPELL, 4, 0, 0, 'N','N',
      'Casting Modifier: Special Sanity Cost: 0 Magical Spell Any Phase: Cast and '+
      'exhaust to pass an Evade check.  The casting modifer is equal to the monster"s '+
      'awareness.');
  Add('PLAGUEOFLOCUSTS', EXP_COTDP, 'Plague of Locusts', SPELL, 3, 0, 0, 'N','N',
      'Casting Modifier: -2 Sanity Cost: 1 Casting phase: Movement Effect: This spell '+
      'effects all investigators and monsters in this neighborhood. Investigators lose '+
      '1 Stamina, and monsters toughness is reduced by 1. Monsters with 0 toughness are '+
      'returned to the cup.');
  Add('PREMONITION', EXP_COTDP, 'Premonition', SPELL, 2, 0, 0, 'N','N',
      'Casting Modifier: -1 Sanity Cost: 1 Casting phase: Any Effect: Cast and exhaust '+
      'to move one skill slider up to 2 stops.');
  Add('REDSIGNSHUDDEMELL', EXP_AH, 'Red Sign of Shudde Mell', SPELL, 2, 0, 1, 'N','N',
      'Casting Modifier: -1 Sanity Cost: 1 Magical Spell Any Phase: Cast and exhaust to '+
      'lower a monsters toughness by 1 (minimum 1) and ignore one of its special '+
      'abilities other than Magical Immunity until the end of this combat.');
  Add('REVELATIONOFSCRIPT', EXP_COTDP, 'Revelation of Script', SPELL, 3, 0, 0, 'N','N',
      'Casting Modifier: +1 Sanity Cost: 0 Casting phase: Any Effect: Cast and exhaust '+
      'to gain +3 to all Lore checks (except Spell checks) until the end of this phase.');
  Add('SHRIVELLING', EXP_AH, 'Shrivelling', SPELL, 5, 0, 1, 'N','N',
      'Casting Modifier: -1 Sanity Cost: 1 4 Magical Spell Any Phase: Cast and exhaust '+
      'to gain +6 to Combat checks until the end of this combat.');
  Add('SHROUDOFSHADOW', EXP_COTDP, 'Shroud of Shadow', SPELL, 3, 0, 0, 'N','N',
      'Casting Modifier: -1 Sanity Cost: Special Casting phase: Any Effect: Cast, '+
      'exhuast, and discard an amount of Sanity of your choice. For each point of '+
      'Sanity you choose to discard, gain +2 to a Sneak check.');
  Add('STEALLIFE', EXP_TBGOTW, 'Steal Life', SPELL, 2, 0, 2, 'N','N',
      'Casting Modifier: -2 Sanity Cost: 1 Casting phase: Any Effect: Cast and exhuast '+
      'to gain +3 to Combat checks until the end of this combat. For every success you '+
      'roll, gain 1 Stamina.');
  Add('SUMMONMONSTER', EXP_TBGOTW, 'Summon Monster', SPELL, 1, 0, 0, 'N','N',
      'Casting Modifier: +0 Sanity Cost: 1 Casting phase: Movement Effect: Cast and '+
      'exhaust to draw a monster from the cup and place it in your current location.');
  Add('VOICEOFRA', EXP_AH, 'Voice of Ra', SPELL, 3, 0, 0, 'N','N',
      'Casting Modifier: -1 Sanity Cost: 1 Magical Spell Upkeep: You may cast and '+
      'exhaust to gain +1 to all skill checks for the rest of this turn.');
  Add('WITHER', EXP_AH, 'Wither', SPELL, 4, 0, 1, 'N','N',
      'Casting Modifier: +0 Sanity Cost: 0 Magical Spell Any Phase: Cast and exhaust to '+
      'gain +3 to Combat checks until the end of this combat.');
  Add('ANCIENTSPEAR', EXP_TBGOTW, 'Ancient Spear', UNIQUE, 2, 6, 2, 'N','N',
      'Type: Physical weapon Bonus: +4 to Combat checks Any: Exhaust to change Ancient '+
      'Spear to a Magical weapon until the end of this combat.');
  Add('ASTRALMIRROR', EXP_TBGOTW, 'Astral Mirror', UNIQUE, 1, 3, 0, 'N','N',
      'Discard Astral Mirror to discard an Environment mythos card from play, then lose '+
      '1 Sanity.');
  Add('MILKOFSHUBNIGGURATH', EXP_TBGOTW, 'Milk of Shub-Niggurath', UNIQUE, 3, 4, 0, 'N','N',
      'Discard Milk of Shub-Niggurath to move all non- Spawn monsters in play to your '+
      'current location. Then reduce your Sanity to 0 and go insane.');
  Add('NAACALKEY', EXP_TBGOTW, 'Naacal Key', UNIQUE, 1, 5, 0, 'N','N',
      'Type: Tome Movement: Exhaust and spend 2 movement points to make a Lore (-2) '+
      'check. If you pass, search the available game markers for a gate of your choice '+
      'and open it at your current location, then lose 1 Sanity and discard Naacal Key. '+
      'If you fail, nothing happens.');
  Add('RITUALBLADE', EXP_TBGOTW, 'Ritual Blade', UNIQUE, 2, 5, 1, 'N','N',
      'Type: Magical weapon Bonus: +2 to Combat checks +1 to Spell checks');
  Add('SOULGEM', EXP_TBGOTW, 'Soul Gem', UNIQUE, 2, 0, 3, 'N','N',
      'Upkeep: Discard Soul Gem and all monsters on it to gain X Stamina. X is equal to '+
      'the total toughness of all monster markers on Soul Gem. Any: Exhaust when you '+
      'defeat a monster to place it on Soul Gem instead of claiming it as a trophy.');
  Add('ALIENSTATUE', EXP_AH, 'Alien Statue', UNIQUE, 1, 5, 0, 'N','N',
      'Movement: Exhaust and spend 2 movement points and 1 Sanity to roll a die. If the '+
      'die is a success, draw 1 Spell or gain 3 Clue tokens. If it is a failure, lose 2 '+
      'Stamina.');
  Add('ANCIENTTABLET', EXP_AH, 'Ancient Tablet', UNIQUE, 1, 8, 0, 'N','N',
      'Movement: Spend 3 movement points and discard Ancient Tablet to roll 2 dice. For '+
      'every success rolled, draw 1 Spell. For every failure rolled, gain 2 Clue '+
      'tokens.');
  Add('BLUEWATCHERPYR', EXP_AH, 'Blue Watcher of the Pyramid', UNIQUE, 1, 4, 0, 'N','N',
      'Any Phase: Lose 2 Stamina and discard Blue Watcher of the Pyramid to '+
      'automatically succeed at a Combat check or a Fight or Lore check made to close a '+
      'gate. This cannot be used against an Ancient One.');
  Add('BOOKOFDZYAN', EXP_AH, 'Book of Dzyan', UNIQUE, 1, 3, 0, 'N','N',
      'Tome Movement: Exhaust and spend 2 movement points to make a Lore (-1) check. If '+
      'you pass, draw 1 Spell, lose 1 Sanity, and put 1 Stamina token from the bank on '+
      'Book of Dzyan. If there are 2 Stamina tokens on it, discard Book of Dzyan. If '+
      'you fail, nothing happens.');
  Add('CABALAOFSABOTH', EXP_AH, 'Cabala of Saboth', UNIQUE, 2, 5, 0, 'N','N',
      'Tome Movement: Exhaust and spend 2 movement points to make a Lore (-2) check. If '+
      'you pass, draw 1 Skill and discard Cabala of Saboth. If you fail, nothing '+
      'happens.');
  Add('COULTESDESGOULES', EXP_AH, 'Cultes des Goules', UNIQUE, 1, 3, 0, 'N','N',
      'Tome Movement: Exhaust and spend 2 movement points to make a Lore (-2) check. If '+
      'you pass, draw 1 Spell and gain 1 Clue token, but lose 2 Sanity and discard '+
      'Cultes des Goules. If you fail, nothing happens.');
  Add('DRAGONSEYE', EXP_AH, 'Dragons Eye', UNIQUE, 1, 6, 0, 'N','N',
      'Any Phase: Exhaust and lose 1 Sanity after drawing a gate or location card to '+
      'draw a new card in its place.');
  Add('ELDERSIGN', EXP_AH, 'Elder Sign', UNIQUE, 4, 5, 0, 'N','N',
      'Any Phase: When sealing a gate, lose 1 Stamina and 1 Sanity and return this card '+
      'to the box. You do not need to make a skill check or spend any Clue tokens to '+
      'seal the gate.  In addition, remove one doom token from the Ancient One"s doom '+
      'track.');
  Add('ENCHANTEDBLADE', EXP_AH, 'Enchanted Blade', UNIQUE, 2, 6, 1, 'N','N',
      'Magical Weapon +4 to Combat checks.');
  Add('ENCHANTEDJEWELRY', EXP_AH, 'Enchanted Jewelry', UNIQUE, 1, 3, 0, 'N','N',
      'Any Phase: Put 1 Stamina token from the bank on Enchanted Jewelry to avoid '+
      'losing 1 Stamina. If there are 3 Stamina tokens on it, discard Enchanted '+
      'Jewelry.');
  Add('ENCHANTEDKNIFE', EXP_AH, 'Enchanted Knife', UNIQUE, 1, 5, 1, 'N','N',
      'Magical Weapon +3 to Combat checks.');
  Add('FLUTEOUTERGODS', EXP_AH, 'Flute of the Outer Gods', UNIQUE, 1, 8, 0, 'N','N',
      'Any Phase: Lose 3 Sanity and 3 Stamina and discard Flute of the Outer Gods '+
      'before making a Combat check to defeat all monsters in your current area. This '+
      'does not affect Ancient Ones.');
  Add('GATEBOX', EXP_AH, 'Gate Box', UNIQUE, 1, 4, 0, 'N','N',
      'Any Phase: When you return to Arkham from an Other World, you can return to any '+
      'location With an open gate, not just those leading to the Other World you were '+
      'in.');
  Add('HEALINGSTONE', EXP_AH, 'Healing Stone', UNIQUE, 1, 8, 0, 'N','N',
      'Upkeep: Exhaust to gain 1 Stamina or 1 Sanity. Discard this card if the Ancient '+
      'One awakens.');
  Add('HOLYWATER', EXP_AH, 'Holy Water', UNIQUE, 3, 4, 2, 'N','N',
      'Magical Weapon +6 to Combat checks (Discard after use)');
  Add('LAMPOFALHAZEED', EXP_AH, 'Lamp of Alhazred', UNIQUE, 1, 7, 2, 'N','N',
      'Magical Weapon +5 to Combat checks');
  Add('NAMELESSCULTS', EXP_AH, 'Nameless Cults', UNIQUE, 2, 3, 0, 'N','N',
      'Tome Movement: Exhaust and spend 1 movement point to make a Lore (-1) check. If '+
      'you pass, draw 1 Spell, lose 1 Sanity, and discard Nameless Cults. If you fail, '+
      'nothing happens.');
  Add('NECRONOMICON', EXP_AH, 'Necronomicon', UNIQUE, 1, 6, 0, 'N','N',
      'Tome Movement: Exhaust and spend 2 movement points to make a Lore (-2) check. If '+
      'you pass, draw 1 Spell and lose 2 Sanity. If you fail, nothing happens.');
  Add('OBSIDIANSTATUE', EXP_AH, 'Obsidian Statue', UNIQUE, 1, 4, 0, 'N','N',
      'Any Phase: Discard Obsidian Statue to cancel all Stamina or Sanity loss being '+
      'dealt to you from one source.');
  Add('PALLIDMASK', EXP_AH, 'Pallid Mask', UNIQUE, 1, 4, 0, 'N','N',
       '+2 to Evade checks');
  Add('POWEROFIBN-GHAZI', EXP_AH, 'Powder of Ibn-Ghazi', UNIQUE, 2, 6, 2, 'N','N',
      'Magical Weapon +9 to Combat checks (Lose 1 Sanity and discard after use)');
  Add('RUBYOFRLYEH', EXP_AH, 'Ruby of Rlyeh', UNIQUE, 1, 8, 0, 'N','N',
      'Movement: You get 3 extra movement points.');
  Add('SILVERKEY', EXP_AH, 'Silver Key', UNIQUE, 1, 4, 0, 'N','N',
      'Any Phase: Put 1 Stamina token from the bank on Silver Key before making an '+
      'Evade check to automatically pass it. Discard Silver Key after using it if there '+
      'are 3 Stamina tokens on it.');
  Add('SWORDOFGLORY', EXP_AH, 'Sword of Glory', UNIQUE, 1, 8, 2, 'N','N',
      'Magical Weapon +6 to Combat checks');
  Add('THEKINGINYELLOW', EXP_AH, 'The King in Yellow', UNIQUE, 2, 2, 0, 'N','N',
      'Tome Movement: Exhaust and spend 2 movement points to make a Lore (-2) check. If '+
      'you pass, gain 4 Clue tokens, lose 1 Sanity, and discard The King in Yellow. If '+
      'you fail, nothing happens.');
  Add('WARDINGSTATUE', EXP_AH, 'Warding Statue', UNIQUE, 1, 6, 0, 'N','N',
      'Any Phase: Discard Warding Statue after failing a Combat check to reduce the '+
      'monster"s combat damage to 0 Stamina. This can also be used to cancel an Ancient '+
      'One"s entire attack for 1 turn.');
//------------------------------------------------------------------------------------------------------------------------------------------                                                                                                 
  AddCorrupt('Call the Beast',       'Green', SQUARE,                         2,       'Exchange one monster in play with one in the '+
                                                                                       'Outskirts, if able.');
  AddCorrupt('Creeping Doom',        'Green', SLASH,                          2,       'Discard the top 2 cards of the Corruption deck.');
  AddCorrupt('Downward Spiral',      'Green', CROSS,                          2,       'Draw 2 Corruption cards.');
  AddCorrupt('Endless Greed',        'Green', HEX,                            2,       'Gain $4 and draw a Corruption card. Constant '+
                                                                                       'effect: You cannot lose money unless you choose to '+
                                                                                       'spend it, and you do not have to roll to keep '+
                                                                                       'Retainers, but you cannot give money to other '+
                                                                                       'investigators.');
  AddCorrupt('Jealous Guardian',     'Green', ROUNDEL,                        2,       'Choose to discard half your items, or draw a '+
                                                                                       'Corruption card. Constant effect: You cannot lose '+
                                                                                       'items unless you choose to do so, but you also '+
                                                                                       'cannot trade items with other investigators');
  AddCorrupt('Nightmarish Visions',  'Green', STAR,                           2,       'Lose 2 Sanity, and gain 2 Clue tokens.');
  AddCorrupt('Primal Surge',         'Green', DIAMOND,                        2,       'You may move any of your skill sliders a total of '+
                                                                                       '3 stops. All other investigators must move a skill '+
                                                                                       'slider 1 stop.');
  AddCorrupt('Speak to Your Friend', 'Green', TRIANGLE,                       2,       'Choose an investigator. That investigator may '+
                                                                                       'take a Cult Membership. If he refuses, discard the '+
                                                                                       'top card of the Corruption deck.');
  AddCorrupt('Fate and Fortune',     'Red',   SQUARE,                         2,       'Each investigator with at least 1 Corruption card '+
                                                                                       'is Cursed. Each investigator with no Corruption '+
                                                                                       'cards is Blessed.');
  AddCorrupt('Mental Paralysis',     'Red',   ROUNDEL,                        2,       'Each investigator with at least 1 Corruption card '+
                                                                                       'skips the next Upkeep Phase.');
  AddCorrupt('Ruination',            'Red',   CROSS,                          2,       'Each investigator with at least 1 Corruption card '+
                                                                                       'loses 1 Sanity and draws a Corruption card.');
  AddCorrupt('Strength of Flesh',    'Red',   STAR,                           2,       'Restore your Stamina to its maximum. Then, each '+
                                                                                       'investigator with at least 1 Corruption card loses '+
                                                                                       '1 Sanity.');
  AddCorrupt('The Skin Crawls',      'Red',   TRIANGLE,                       2,       'Raise the terror level by 1, then draw a '+
                                                                                       'Coruption card. Constant effect: Any investigator '+
                                                                                       'who ends his movement in the same location as you '+
                                                                                       'must pass a Will (-2) check or lose 2 Sanity.');
  AddCorrupt('Uncontrollable Rage',  'Red',   SLASH,                          2,       'If you are in town, you are arrested. Lose 1 '+
                                                                                       'Sanity and remove 1 Ally from the game. If you are '+
                                                                                       'in an Other World, you lose 1 Sanity and are '+
                                                                                       'delayed.');
  AddCorrupt('Vessel of the Mythos', 'Red',   HEX,                            2,       'Add 1 doom token to the doom track. Constant '+
                                                                                       'effect: Increase your maximum Stamina and decrease '+
                                                                                       'your maximum Sanity by 1 for each Corruption card '+
                                                                                       'you have. If this ever reduces your Sanity to 0, '+
                                                                                       'you are devoured. You cannot enter stable '+
                                                                                       'locations.');
  AddCorrupt('Weakness of Mind',     'Red',   DIAMOND,                        2,       'Reduce your Sanity to 1. Then, each investigator '+
                                                                                       'with at least 1 Corruption card gains 1 Stamina.');
//------------------------------------------------------------------------------------------------------------------------------------------                                                                                                 
  AddCult('A Simple Choice',                                                  2,       'Draw 1 Common item, then either discard a '+
                                                                                       'different item or draw a Corruption card.');
  AddCult('Baptized in Blood',                                                1,       'You may choose to be blessed, then lose 2 Sanity '+
                                                                                       'and draw a Corruption card. If you choose not to '+
                                                                                       'do so, you are Cursed and must discard your Cult '+
                                                                                       'Membership, then move to the street.');
  AddCult('Birthing Chant',                                                   1,       'Out of the darkness a grotesque monster appears!');
  AddCult('Blood Offering',                                                   1,       'Either discard 1 Ally, discard 2 toughness worth '+
                                                                                       'of monster trophies, or lose 3 Stamina. If you '+
                                                                                       'cannot or will not do any of these things, discard '+
                                                                                       'your Cult Membership and move to the street.');
  AddCult('Blood-drenched Altar',                                             1,       'Raise the terror level by 1.');
  AddCult('Calling forth the Darkness',                                       1,       'If you participate in the ceremony, each '+
                                                                                       'investigator must draw a Corruption card. If you '+
                                                                                       'choose not to do so, a monster surge occurs.');
  AddCult('Curious Endowment',                                                1,       'You may draw 2 Unique items, choose one to keep, '+
                                                                                       'and discard the other. If you do, draw a '+
                                                                                       'Corruption card. Otherwise, move to the street.');
  AddCult('Dance of the Chosen',                                              2,       'You may draw 2 Spells, choose one to keep, and '+
                                                                                       'discard the other. If you do, draw a Corruption '+
                                                                                       'card. Otherwise, move to the street.');
  AddCult('No Turning Back',                                                  2,       'Draw a Corruption card.');
  AddCult('Questioned Loyalty',                                               1,       'Discard 2 Clue tokens, if able. You may reduce '+
                                                                                       'this loss by 1 for each Corruption card you have. '+
                                                                                       'If you cannot or will not, lose 2 Stamina and move '+
                                                                                       'to the street.');
  AddCult('Startling Revelation',                                             1,       'Return 2 Allies from the Ally deck to the box. '+
                                                                                       'They have joined "One of the Thousand" Cult!');
  AddCult('Teetering Sanity',                                                 1,       'The reality of the situation suddenly slaps you '+
                                                                                       'in the face. Questioning your motives, you wonder '+
                                                                                       'when all of this became so compelling... Lose 2 '+
                                                                                       'Sanity.');
  AddCult('Temptations of Power',                                             1,       'You may search the Spell deck for a card of your '+
                                                                                       'choice, then lose 1 Sanity and draw a Corruption '+
                                                                                       'card. If you choose not to do so, discard your '+
                                                                                       'Cult Membership and move to the street.');
  AddCult('The Chosen One',                                                   1,       'You stand before the stone altar, knife in hand. '+
                                                                                       'Will it be another''s blood, or your own that you '+
                                                                                       'shed? You must either draw 2 Corruption cards and '+
                                                                                       'add 1 doom token to the doom track, or remove 1 '+
                                                                                       'doom token from the doom track and be devoured.');
  AddCult('Tithes That Bind',                                                 2,       'Spend $3 (or discard items worth at least $3) to '+
                                                                                       'gain 2 Clue tokens and a Corruption card. If you '+
                                                                                       'cannot or will not, discard your Cult Membership '+
                                                                                       'and move to the street.');
  AddCult('Unbreakable Oath',                                                 1,       '"The Mother''s milk is her most sacred gift. '+
                                                                                       'Drink deeply." You may search the Unique item deck '+
                                                                                       'for a Milk of Shub-Niggurath card, if it is '+
                                                                                       'available. If you do, draw a Corruption card. '+
                                                                                       'Otherwise move to the street.');
  AddCult('Watching and Waiting',                                             2,       'Cautious subterfuge earns you a glimpse at things '+
                                                                                       'to come, yet there is truth in the old adage about '+
                                                                                       'the bliss of ignorance. You may either gain 1 Clue '+
                                                                                       'token, or 3 Clue tokens and a Corruption card.');
  AddCult('Whispers in Shadows',                                              2,       '"Take this to help with your cause, friend." You '+
                                                                                       'may either gain $3 and draw a Corruption card, or '+
                                                                                       'move to the street.');
//------------------------------------------------------------------------------------------------------------------------------------------                                                                                                 
  AddBlight('AbigailForeman', 'Abigail Foreman', 'The number of gates that can be open at once before the Ancient One '+
                                                 'awakens is reduced by 1.');
  AddBlight('DoctorMintz',    'Doctor Mintz',    'After an investigator pays to restore his Sanity to its maximum value '+
                                                 'at Arkham Asylum, he loses 1 Stamina.');
  AddBlight('DoyleJeffries',  'Doyle Jefferies', 'Place the 3 Riot monsters in their starting areas. Notes Newspaper '+
                                                 'encounters from cards other than those in The King in Yellow, give '+
                                                 'this personality''s surname as "Jefferies". Even, the subsequently '+
                                                 'published The Black Goat of the Woods.');
  AddBlight('FatherMichael',  'Father Michael',  'Blessings are discarded during the Upkeep phase on a roll of 1-5.');
  AddBlight('JoeyTheRat',     'Joey "The Rat"',  'If the Ancient One awakens, the investigators need one extra success '+
                                                 'to remove each doom token during the battle.');
  AddBlight('MaMathison',     'Ma Mathison',     'Discard all Allies from play. Ma''s Boarding House is closed for the rest of the game.');
  AddBlight('MiriamBeecher',  'Miriam Beecher',  'The Sanity cost of all spells is increased by 1.');
  AddBlight('NurseSharon',    'Nurse Sharon',    'After an investigator pays to restore his Stamina to its maximum value at '+
                                                 'St. Mary''s Hospital, he loses 1 Sanity.');
  AddBlight('OliverThomas',   'Oliver Thomas',   'The cost to seal gates is increased by 1 Clue token.');
  AddBlight('SheriffEngle',   'Sheriff Engle',   'Return the Deputy cards to the box, even if an investigator '+
                                                 'has them. Lower the Outskirts limit by 2 (minimum 0).');
  AddBlight('TheDean',        'The Dean',        'Choose and discard 1 Elder Sign token from the board. Investigators '+
                                                 'may only refresh 1 card each during Upkeep.');
  AddBlight('TheShopkeeper',  'The Shopkeeper',  'The list price of all items is increased by $3 when buying them.');
  AddBlight('Velma',          'Velma',           'The terror level is increased by 1 (triggering another Yellow Sign).');
//------------------------------------------------------------------------------------------------------------------------------------------                                                                                                 
  AddDarkPact('BLOODPACT', 'Blood Pact', 'When you gain a Blood Pact, restore your Stamina to full. Any Phase: '+
                                         'While this card is refreshed, any time you would gain any amount of '+
                                         'Stamina, you may instead gain that amount of Power. You may spend a '+
                                         'Power token as either a Clue token or as 1 Sanity when you suffer a '+
                                         'Sanity loss. Upkeep: Exhaust Blood Pact and lose X Stamina to gain X '+
                                         'Power.');
  AddDarkPact('SOULPACT',  'Soul Pact',  'When you gain a Soul Pact, restore your Sanity to full. Any Phase: '+
                                         'While this card is refreshed, anytime you would gain any amount of '+
                                         'Sanity, you may instead gain that amount of Power. You may spend a Power '+
                                         'token as either a Clue token or as 1 Stamina when you suffer a Stamina '+
                                         'loss. Upkeep: Exhaust Soul Pact and lose X Sanity to gain X Power.');
  AddDarkPact('BOUNDALLY', 'Bound Ally', 'When you gain a Bound Ally, take the top card of the Ally deck and '+
                                         'attach it to this card. You gain the services of that Ally. When the '+
                                         'Ancient One awakens, discard the Ally and put this card on the Ancient '+
                                         'One. For each Bound Ally on the Ancient One, it takes one additional '+
                                         'success to remove a doom token. You may spend a Power token as either a '+
                                         'Clue token or as $1.');
//------------------------------------------------------------------------------------------------------------------------------------------
  AddDifficulty('Discomforting', -4
              , 'During step 2 of the game setup, place an additional Clue token on each unstable location on the game board.'
              , 'When a Mythos card makes a Clue token appear, an additional Clue token appears in each listed location.'
              , 'If scoring your victory at the end of the game, this card is worth -4.');
  AddDifficulty('Nauseating', -2
              , 'Sister Mary begins the game with 3 additional Clue tokens.'
              , 'All investigators are immediately Blessed at the start of the game.'
              , 'If scoring your victory at the end of the game, this card is worth -2.');
  AddDifficulty('Mind-damaging', 0
              , ''
              , ''
              , 'Standard Game');
  AddDifficulty('Ye Liveliest Awfulness', 2
              , 'Rex Murphy begins the game with no Clue tokens.'
              , 'All investigators are immediately Cursed at the start of the game.'
              , 'If scoring your victory at the end of the game, this card is worth +2.');
  AddDifficulty('Ultimate Cosmic Evil', 6
              , 'Set the terror level to 5. Close the General Store and remove 5 randomly '+
                'selected allies from the game. Investigators that begin in the General Store '+
                'instead begin in Rivertown streets.'
              , 'After the first turn, one additional Mythos card is drawn and resolved each turn.'
              , 'If scoring your victory at the end of the game, this card is worth +6.');
//-----------------------------------------------------------------------------------------------------
  AddRelationShip('BestofFriends', 'Best of Friends',
    'If you or your partner are in the same neighborhood, either of you may exhaust '+
    'this card before making a check to gain +1 on that check. If the Ancient One has '+
    'awakened, this card may not be used.');
  AddRelationShip('BusinessAssociates', 'Business Associates',
    'After the initial setup, any time either you or your partner gains $1 or more '+
    '(from any game effect other than this card), the other gains $1.');
  AddRelationShip('Collectors', 'Collectors',
    'After the initial setup, any time either you or your partner gains 1 or more '+
    'Common Items or Unique Items (from any game effect other than this card), the '+
    'other may draw a random card of the same type and purchase it for the list '+
    'price.');
  AddRelationShip('CourageousInspirations', 'Courageous Inspirations',
    'Either you or your partner may exhaust this card before making a Horror check to '+
    'gain a +1 to the check.');
  AddRelationShip('FellowTravelers', 'Fellow Travelers',
    'Either you or your partner may exhaust this card to gain 1 extra movement point.');
  AddRelationShip('FriendlyRivals', 'Friendly Rivals',
    'Between you and your partner, the investigator with fewer monster trophies gains '+
    'a +1 on Combat checks, and the investigator with fewer Gate trophies gains a +1 '+
    'on Fight or Lore checks to close Gates. There is no effect in the case of ties.');
  AddRelationShip('PractitionersoftheArt', 'Practitioners of the Art',
    'Whenever you or your partner casts a Spell, either or both of you may contribute '+
    'toward paying the Sanity cost. Either you or your partner may exhaust this card '+
    'before making a Spell check to gain a +1 to the check.');
  AddRelationShip('Skullcrackers', 'Skullcrackers',
    'Either you or your partner may exhaust this card before making a Combat check to '+
    'gain a +1 to the check.');
  AddRelationShip('SociallyConnected', 'Socially Connected',
    'After the initial setup, any time either you or your partner gains an Ally (from '+
    'any game effect other than this card), the other draws an Ally at random from '+
    'the Ally deck. If he currently has no Allies, he keeps it. If he does have one '+
    'or more Allies, he keeps it and then chooses one of his Allies to reshuffle back '+
    'into the Ally deck.');
  AddRelationShip('StudentsoftheArcane', 'Students of the Arcane',
    'After the initial setup, any time either you or your partner gains a Spell (from '+
    'any game effect other than this card), the other draws a random Spell from the '+
    'Spell deck.');
  AddRelationShip('Survivors', 'Survivors',
    'Either you or your partner may exhaust this card before making an Evade check to '+
    'gain a +1 to the check.');
  AddRelationShip('WorldAintBigEnoughforUs', 'World Ain''t Big Enough for Us',
    'If you or your partner is in an Other World location, either of you may exhaust '+
    'this card before making a check to gain +1 on that check. If the Ancient One has '+
    'awakened, this card may not be used.');
//-----------------------------------------------------------------------------------------------
  AddReckoning('AHumbleServant', 'A Humble Servant',
    'Add 1 doom token to the doom track for each investigator with 3 Dark Pacts.');
  AddReckoning('ALittleTaste', 'A Little Taste',
    'The investigator(s) with the least Power gain 1 Power, even if he does not have '+
    'a Dark Pact. Note, however, that an investigator needs a Dark Pact to spend '+
    'Power.');
  AddReckoning('AnOfferYouCantRefuse', 'An Offer You Can''t Refuse',
    'The first player chooses an investigator. That investigator must take a Dark '+
    'Pact if able. If not able, that investigator is devoured.');
  AddReckoning('BargainoftheGate', 'Bargain of the Gate',
    'The investigator with the most Power moves to the Other World of his choice '+
    '(ties broken by the first player).');
  AddReckoning('DarkReward', 'Dark Reward',
    'Each investigator with a Dark Pact gains 1 Power per Dark Pact he has.');
  AddReckoning('DebtComesDue', 'Debt Comes Due',
    'For each 3 Power possessed by the investigators as a group, add 1 doom token to '+
    'the doom track (round down).');
  AddReckoning('DevilsBargain', 'Devil''s Bargain',
    'The investigators must choose: either each investigator with Power must discard '+
    'a Common or Unique Item, or add 1 doom token to the doom track.');
  AddReckoning('FurtherTemptation', 'Further Temptation',
    'Each investigator with a Dark Pact draws 1 Spell.');
  AddReckoning('GivetheDevilhisDue', 'Give the Devil his Due',
    'Each investigator with a Dark Pact must discard 1 Gate trophy or 5 toughness '+
    'worth of monster trophies or 5 Clue tokens, if able. If he cannot, he must '+
    'discard all his monster trophies and Clues.');
  AddReckoning('HeIsEverywhere', 'He Is Everywhere',
    'If every investigator has 1 or more Dark Pacts and/or 1 or more Power, add a '+
    'doom token to the doom track.');
  AddReckoning('HumanityLost', 'Humanity Lost',
    'The investigator with the most Power is devoured (ties broken by the first '+
    'player). If no investigators have Power, there is no effect.');
  AddReckoning('InTooDeep', 'In Too Deep',
    'Each investigator with only 1 Dark Pact must immediately choose and take a '+
    'second Dark Pact.');
  AddReckoning('PowerBegets', 'Power Begets',
    'Each investigator with at least 1 Power gains 1 Power.');
  AddReckoning('PowerCorrodes', 'Power Corrodes',
    'Each investigator loses 1 Sanity for each Power he has.');
  AddReckoning('PowerCorrupts', 'Power Corrupts',
    'Each investigator loses 1 Sanity or 1 Stamina for each Power he has.');
  AddReckoning('PowerDecays', 'Power Decays',
    'Each investigator loses 1 Stamina for each Power he has.');
  AddReckoning('PrisonersDilemma', 'Prisoner''s Dilemma',
    'The investigators must choose: either the investigator with the most Power is '+
    'devoured, or the investigator with the least Power is driven insane.');
  AddReckoning('SpreadtheWord', 'Spread the Word',
    'Each investigator may choose to gain one or more Dark Pacts. Then, if there is '+
    'at least one investigator who does not have a Dark Pact, each investigator who '+
    'does have a Dark Pact is Cursed.');
  AddReckoning('StrangeBehavior', 'Strange Behavior',
    'Each investigator with a Bound Ally must discard 3 Clue tokens. For each '+
    'investigator that fails to do this, increase the terror level by 1.');
  AddReckoning('TerribleRealization', 'Terrible Realization',
    'Each investigator with a Blood Pact loses 2 Sanity.');
  AddReckoning('TheBodyaTemple', 'The Body a Temple',
    'Each investigator with a Soul Pact loses 2 Stamina.');
  AddReckoning('TheBodyDecays', 'The Body Decays',
    'Each investigator with a Dark Pact loses 1 Stamina per Dark Pact he has.');
  AddReckoning('TheMasterofMagic', 'The Master of Magic',
    'Each investigator with at least 1 Spell gains 1 Power.');
  AddReckoning('TheMindUnravels', 'The Mind Unravels',
    'Each investigator with a Dark Pact loses 1 Sanity per Dark Pact he has.');
  AddReckoning('ThroughtheThreshold', 'Through the Threshold',
    'Every investigator in Arkham with 1 or more Power is drawn through the closest '+
    'open Gate (his choice if there is a tie).');
  AddReckoning('TurningOnOneAnother', 'Turning On One Another',
    'Discard 1 Ally from the Ally deck for each Bound Ally card in play. For each '+
    'Ally that you cannot discard (because the deck is empty), increase the terror '+
    'level by 1.');
  AddReckoning('UncertainFuture', 'Uncertain Future',
    'Shuffle the Reckoning deck and its discard pile together (including this card), '+
    'then draw a new Reckoning card.');
  AddReckoning('UnsettlingAura', 'Unsettling Aura',
    'If the total Power possessed by the investigators as a group is greater than the '+
    'total number of investigators in the game, increase the terror level by 1.');

end;

initialization
  ICards        := TStringList.Create;
  Load;
  ICards.Sort;
end.

