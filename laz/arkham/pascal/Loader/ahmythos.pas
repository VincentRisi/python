unit AHMythos;
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
  Mythoss      : TStringList;

implementation

procedure Add(const aName        : string;
              const aExpansion   : EExpansion;
              const aEvent       : EMythosType;
              const aClue        : string; 
              const aMonster     : string;
              const aWhite       : string; //SFactionSet;
              const aBlack       : string; //SFactionSet;
              const aDescription : string);
var
  Mythos : TMythos;
begin
  Mythos := TMythos.Create;
  with Mythos do begin
    name          := aName;
    expansion     := aExpansion;
    event         := aEvent;
    clue          := aClue; 
    monster       := aMonster;
    white         := aWhite;
    black         := aBlack;
    description   := aDescription;
  end;
  Mythoss.AddObject(aName, Mythos);
end;

procedure LoadMythoses();
begin
  Add('ADarkWindCoversArkham', EXP_COTDP, ENVIRONMENT, 'TWHOUSE', 'UISLE', 'SQUARE,DIAMOND', 'ROUNDEL',
      'The terror level increases by 1. The maximum Stamina of all investigators in '+
      'Arkham is reduced by 1. Horror checks in Arkham are made at a -2 penalty.');
  Add('AStrangePlague', EXP_AH, ENVIRONMENT, 'TUNNAMABLE', 'INDSQUARE', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Investigators cannot gain Stamina except by receiving medical care in St. Marys '+
      'Hospital (or from Vincent Lee).');
  Add('AlienTechnology', EXP_AH, ENVIRONMENT, 'SBUILDING', 'UISLE', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Mi-Go have their toughness increased by 2. If an investigator passes a Combat '+
      'check against a Mi- Go, he draws 1 extra Unique Item.');
  Add('AllQuietInArkham', EXP_AH, HEADLINE, 'HSOCIETY', 'WOODS', 'HEX', 'SLASH,TRIANGLE,STAR',
      'Each player may pass a Luck(1) check to be Blessed');
  Add('AnEvilFog', EXP_AH, ENVIRONMENT, 'UISLE', 'GRAVEYARD', 'CROSS', 'MOON',
      'Will checks in Arkham are made at a -l penalty. Sneak checks in Arkham are made '+
      'at a +l bonus. Fliers do not move.');
  Add('BankForeclosure', EXP_COTDP, HEADLINE, 'INDSQUARE', 'WOODS', 'MOON', 'CROSS',
      'Any investigators in Arkham with Bank Loans must pay them off immediately. You '+
      'may sell items at half their list price (round down) if you do not have the $10; '+
      'if you cannot or will not pay, you are arrested.');
  Add('BigStormSweepsArkham', EXP_AH, HEADLINE, 'TUNNAMABLE', 'INDSQUARE', 'MOON', 'CROSS',
      'All monsters in the Sky and Outskirts are returned to the cup.');
  Add('BizarreDreamsPlagueCitizens', EXP_AH, HEADLINE, 'TWHOUSE', 'SBUILDING', 'HEX', 'SLASH,TRIANGLE,STAR',
      'All Gugs and Nightgaunts in Arkham are returned to the cup. If at least one '+
      'monster returns to the cup, raise the terror level by l');
  Add('BlackestNight', EXP_AH, ENVIRONMENT, 'HROADHOUSE', 'BCAVE', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Luck checks in Arkham are made at a -1 penalty. Sneak checks in Arkham are made '+
      'at a +1 bonus.');
  Add('BloodMagic', EXP_AH, ENVIRONMENT, 'TUNNAMABLE', 'INDSQUARE', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Investigators who end their movement in Rivertown streets may choose to delve '+
      'into dark mysteries using their life force. They roll dice equal to their '+
      'current Stamina, and for every failed die, they lose l Stamina. If this reduces '+
      'them to 0 Stamina, they are devoured and the player must start a new character. '+
      'Otherwise, they gain 3 Clue tokens.');
  Add('BlueFlu', EXP_AH, HEADLINE, 'WOODS', 'TUNNAMABLE', 'HEX', 'SLASH,TRIANGLE,STAR',
      'All investigators in jail are released. No investigators may be arrested until '+
      'the end of next turn. Leave this card in play until then to indicate this.');
  Add('CampusSecurityIncreased', EXP_AH, HEADLINE, 'TUNNAMABLE', 'INDSQUARE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'All Monsters in the Miskatonic U. streets or locations are returned to the cup');
  Add('CharityAuction!', EXP_TBGOTW, HEADLINE, 'WOODS', 'HROADHOUSE', 'HEX', 'SLASH,STAR,TRIANGLE',
      'Deal a number of cards from the top of the Common Item deck equal to the number '+
      'of players. Each player may purchase one item at its listed cost plus $1. '+
      'Discard any items not purchased.');
  Add('CheckeredCabTrialsBegin!', EXP_TBGOTW, HEADLINE, 'WOODS', 'TWHOUSE', 'SLASH,STAR,TRIANGLE', 'HEX',
      'All investigators in Arkham may move directly to any street location in Arkham '+
      'as their entire move (ignore all monsters between their current location and '+
      'their destination).');
  Add('ChurchBoycottsExhibit', EXP_COTDP, ENVIRONMENT, 'HROADHOUSE', 'HSOCIETY', 'MOON', 'CROSS',
      'Lore checks in Arkham are made at a -2 penalty. Will checks in Arkham are made '+
      'at a +2 bonus.');
  Add('ChurchGroupReclaimsSouthside', EXP_AH, HEADLINE, 'HROADHOUSE', 'BCAVE', 'HEX', 'SLASH,TRIANGLE,STAR',
      'All monsters in the Southside streets or locations are returned to the cup.');
  Add('CityGrippedByBlackouts', EXP_AH, HEADLINE, 'SBUILDING', 'UISLE', 'HEX', 'SLASH,TRIANGLE,STAR',
      'The General Store, Curiositie Shoppe, and Ye Olde Magick Shoppe are closed until '+
      'the end of next turn. Leave this card in play until then to indicate this. '+
      'Close: The General Store Curiositie Shoppe Ye Olde Magick Shoppe');
  Add('ConstructionCrewConundrum!', EXP_TBGOTW, HEADLINE, 'BCAVE', 'GRAVEYARD', 'DIAMOND,SQUARE', 'ROUNDEL',
      'A monster appears at the Downtown streets and the Miskatonic U. streets.');
  Add('CorpsesPreserved', EXP_COTDP, HEADLINE, 'INDSQUARE', 'HROADHOUSE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'Monster trophies come to life! Each investigator in Arkham must randomly choose '+
      'one of his collected monster trophies. That monster surprises him. If the '+
      'investigator defeats the monster, he may draw cards from the Exhibit Item deck '+
      'equal to its toughness, take one, and discard the rest. Only monsters that are '+
      'defeated may be taken as trophies again; if the investigator flees or the '+
      'monster defeats him, the monster is returned to the box.');
  Add('CurfewEnforced', EXP_AH, ENVIRONMENT, 'SBUILDING', 'UISLE', 'CROSS', 'MOON',
      'Any investigator who ends his movement in the streets must pass a Will (+0) '+
      'check or be arrested and taken to the Police Station.');
  Add('DarkesCarnivalArrives', EXP_AH, ENVIRONMENT, 'WOODS', 'TUNNAMABLE', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Investigators Who end their movement in the Northside streets gain 1 Clue token '+
      'from the sinister wonders they Witness, but must pass a Will (-1) check or lose '+
      '1 Sanity. Activity At: Northside Streets');
  Add('DisturbingTheDead', EXP_AH, RUMOR, '', 'BCAVE', 'SLASH,TRIANGLE,STAR', 'HEX',
      'Ongoing Effect: Roll a die at the end of every Mythos Phase While this card is '+
      'in play (beginning the turn after it entered play). On a 1 or 2, increase the '+
      'terror level by 1. Pass: If a single player discards 2 gate trophies during the '+
      'Arkham Encounter Phase While in the Rivertown streets, return this card to the '+
      'box. Each player draws l Spell. Fail: If the terror level reaches 10, return '+
      'this card to the box. Every investigator is Cursed.');
  Add('DreamOfASunkenCity', EXP_AH, ENVIRONMENT, 'TUNNAMABLE', 'INDSQUARE', 'CROSS', 'MOON',
      'Investigators cannot gain Sanity except by receiving psychiatric care at Arkham '+
      'Asylum (or from Carolyn Fern).');
  Add('EgyptianExhibitVisitsMiskatonicU', EXP_AH, ENVIRONMENT, 'BCAVE', 'TWHOUSE', 'CROSS', 'MOON',
      'Any investigator who ends his movement in the Miskatonic U. streets may pass a '+
      'Lore (-1) check to gain 1 Clue token by reading the strange heiroglyphies on the '+
      'artifacts in the exhibit. Activity At: Miskatonie U. Streets');
  Add('EndlesslyBreeding', EXP_TBGOTW, RUMOR, '', '', 'SQUARE,DIAMOND,MOON,HEX', 'SLASH,TRIANGLE,STAR,CROSS,ROUNDEL',
      'Ongoing Effect: At the end of each Mythos phase, draw a second Mythos card and '+
      'ignore everything on it except for its monster movement pattern. Each time an '+
      'investigator is reduced to 0 Stamina or 0 Sanity, place a Clue token on this '+
      'card. Pass: If a single investigator discards $10 while at the Riverside Docks, '+
      'return this card to the box. Starting with the first player, each player chooses '+
      'a monster in play and takes it as a monster trophy (ignoring Endless). Fail: If '+
      'there are ever 3 Clue tokens on this card, return it to the box. A monster surge '+
      'occurs, then add a doom token to the doom track for each Hex monster in play.');
  Add('EscapefromArkhamAsylum!', EXP_COTDP, HEADLINE, 'INDSQUARE', 'WOODS', 'MOON', 'CROSS',
      'Collect up to 3 Maniacs, drawing them first from the monster cup, then from the '+
      'Outskirts, then from those claimed as trophies. Place them all in the Downtown '+
      'streets. Investigators who defeat all 3 Maniacs before the end of next turn may '+
      'draw 1 Exhibit Item. Leave this card in play until then to indicate this.');
  Add('EstateSale', EXP_AH, ENVIRONMENT, 'BCAVE', 'TWHOUSE', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Investigators who end their movement in the Uptown streets may draw 2 Unique '+
      'Items and purchase one, none, or both of them at list price, discarding any that '+
      'are not purchased. Activity At: Uptown Streets');
  Add('FamilyFoundButchered', EXP_AH, HEADLINE, 'UISLE', 'GRAVEYARD', 'MOON', 'CROSS',
      'The terror level increases by 1 in light of this tragic news.');
  Add('FedsRaidArkham', EXP_AH, HEADLINE, 'HROADHOUSE', 'BCAVE', 'MOON', 'CROSS',
      'All monsters in the streets are returned to the cup.');
  Add('FiresintheNight', EXP_TBGOTW, ENVIRONMENT, 'HROADHOUSE,STLODGE', 'INDSQUARE', 'CROSS', 'MOON',
      'Monsters at the Woods do not move. Monsters in the Uptown streets who move move '+
      'to the woods.');
  Add('FourthOfJulyParade', EXP_AH, HEADLINE, 'BCAVE', 'TWHOUSE', 'MOON', 'CROSS',
      'Investigators cannot move into or out of the Merchant Dist. streets until the '+
      'end of next turn. Leave this card in play until then to indicate this. Close: '+
      'Merchant Dist. Streets');
  Add('FullMoon', EXP_TBGOTW, ENVIRONMENT, 'INDSQUARE', 'GRAVEYARD', 'MOON', 'CROSS',
      'All monsters have their Sanity damage increased by 1.');
  Add('FunnelClouds', EXP_TBGOTW, ENVIRONMENT, 'TWHOUSE', 'HSOCIETY', 'SLASH,STAR,TRIANGLE', 'HEX',
      'Any investigator who ends his movement in the streets must pass a Luck (+1) '+
      'check or be devoured. All flying monsters are returned to the monster cup.');
  Add('GangsCleanUpEasttown', EXP_AH, HEADLINE, 'BCAVE', 'TWHOUSE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'All monsters in the Easttown streets or locations are returned to the cup.');
  Add('GhostShipDocksByItself', EXP_AH, HEADLINE, 'WOODS', 'TUNNAMABLE', 'MOON', 'CROSS',
      'An ancient ghost ship arrives in Arkham releasing 2 monsters into the Merchant '+
      'Dist. streets.');
  Add('GoatlikeCreaturesSpottedInTheWood', EXP_AH, HEADLINE, 'TUNNAMABLE', 'INDSQUARE', 'HEX', 'SLASH,TRIANGLE,STAR',
      'All Dark Young in Arkham are returned to the cup. If at least one monster '+
      'returns to the cup, raise the terror level by 1.');
  Add('GoodWorkUndone', EXP_AH, RUMOR, '', 'UISLE', 'SLASH,TRIANGLE,STAR', 'HEX',
      'When this card enters play, place 6 Clue tokens on it. Any player may spend Clue '+
      'tokens during the Arkham Encounter Phase while in the Easttown streets to '+
      'discard Clue tokens from this card on a 1-for-1 basis. Ongoing Effect: Roll two '+
      'dice at the end of every Mythos Phase (beginning the turn after it entered '+
      'play). For every l or 2 rolled, place l Clue token on this card. Pass: If there '+
      'are no Clue tokens on this card, return it to the box. Each player draws l '+
      'Unique Item. Fail: If there are 10 Clue tokens on this card, return it to the '+
      'box. All elder sign tokens are removed from the board. Activity At: Eastown '+
      'Streets');
  Add('GypsyCaravan', EXP_TBGOTW, ENVIRONMENT, 'BCAVE', 'TUNNAMABLE', 'DIAMOND,SQUARE', 'ROUNDEL',
      'Investigators who end their movement in the Southside Streets may roll a die. On '+
      'a success, they gain $2. On a failure, they lose $1.');
  Add('HappyDaysAreHereAgain', EXP_AH, ENVIRONMENT, 'HSOCIETY', 'WOODS', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Due to the renewed prosperity that has come to Arkham, the terror level cannot '+
      'increase.');
  Add('HeatWave', EXP_AH, ENVIRONMENT, 'INDSQUARE', 'WOODS', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Fight checks in Arkam are made at a -1 penalty. Lore checks in Arkham are made '+
      'at a +1 bonus. Fire Vampires have their toughness increased by 1.');
  Add('HornsoftheBlackGoat', EXP_TBGOTW, ENVIRONMENT, 'TUNNAMABLE', 'UISLE', 'MOON', 'CROSS',
      'Dark Young have their toughness increased by 1.');
  Add('HorrorAtGroundbreaking', EXP_AH, HEADLINE, 'STLODGE', 'HSOCIETY', 'MOON', 'CROSS',
      'An ancient stone is disturbed by the construction, releasing 2 monsters into the '+
      'Miskatonic U. streets.');
  Add('IcyConditions', EXP_AH, ENVIRONMENT, 'STLODGE', 'HSOCIETY', 'CROSS', 'MOON',
      'Investigators receive 1 less movement point during the Movement Phase. Fast '+
      'monsters move like normal monsters.');
  Add('IllWindGripsArkham', EXP_AH, HEADLINE, 'UISLE', 'GRAVEYARD', 'HEX', 'SLASH,TRIANGLE,STAR',
      'The first player must pass a Luck (-1) check or be Cursed.');
  Add('KingofCardsCancelsShow', EXP_COTDP, HEADLINE, 'UISLE', 'TWHOUSE', 'MOON', 'CROSS',
      'All Witches and Warlocks in Arkham are returned to the cup. If any investigator '+
      'has Eric Weiss as an Ally, that investigator gains those monsters as trophies.');
  Add('LightningStrikesTwice!', EXP_TBGOTW, HEADLINE, 'TWHOUSE', 'UISLE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'Two similar rocks are shattered by lightning strikes in different parts of '+
      'Arkham, each releasing a monster. A monster appears at the French Hill streets '+
      'and the Uptown streets.');
  Add('LodgeMemberHeldForQuestioning', EXP_AH, HEADLINE, 'HROADHOUSE', 'BCAVE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'A Silver Lodge ritual lets 2 monsters loose in the French Hill streets.');
  Add('LodgeMembersWatchTheNight', EXP_AH, HEADLINE, 'SBUILDING', 'UISLE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'All monsters in the French Hill streets or locations are returned to the cup.');
  Add('ManHuntInArkham', EXP_AH, HEADLINE, 'INDSQUARE', 'WOODS', 'SLASH,TRIANGLE,STAR', 'HEX',
      'All monsters in locations are returned to the cup.');
  Add('MerchantsMarchOnCrime', EXP_AH, HEADLINE, 'TUNNAMABLE', 'INDSQUARE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'All monsters in the Merchant Dist. streets or locations are returned to the cup.');
  Add('MiskatonicArcticExpeditionReturns', EXP_AH, HEADLINE, 'INDSQUARE', 'TWHOUSE', 'MOON', 'CROSS',
      'Any Elder Things previously claimed as monster trophies by players retum to life '+
      'and are placed in the River Docks.');
  Add('MissingPeopleReturn', EXP_AH, HEADLINE, 'WOODS', 'TUNNAMABLE', 'SLASH,TRIANGLE,STAR', 'HEX',
      'All investigators currently lost in time and space immediately return to Arkham, '+
      'appearing in a street or location of their choice.');
  Add('MurderintheMuseum', EXP_COTDP, HEADLINE, '', '', 'SLASH,TRIANGLE,STAR', 'HEX',
      'Doom Tokens Added: 2. Players in Arkham with gate trophies must make a Fight '+
      'check or Lore check for each trophy they have, with a modifier equal to the '+
      'modifier printed on the gate. If a check for a gate is failed, draw monsters '+
      'from the cup until you draw a monster with a symbol that matches the one on the '+
      'gate, and place that monster in the players current location. If the check for a '+
      'gate succeeds, the player may remove one monster with that gates symbol from '+
      'Arkham, the Outskirts, or the Sky.');
  Add('MurdereratLarge;VictimsBrainsMissing', EXP_AH, HEADLINE, 'SBUILDING', '', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Doom Tokens Added: 2. The terror level increases by 1.');
  Add('MuseumArtifactsStolen', EXP_COTDP, HEADLINE, 'WOODS', 'INDSQUARE', 'HEX', 'SLASH,TRIANGLE,STAR',
      'Investigators in Arkham may pay $5 in bribe fees to make a connection with the '+
      'robbers. Those who do so may draw a number of Exhibit Items equal to their '+
      'focus, choose one, and discard the rest.');
  Add('MuseumHaunted', EXP_COTDP, HEADLINE, 'WOODS', 'SBUILDING', 'CROSS', 'MOON',
      'The ghosts of the pharaohs walk abroad! Collect up to 2 Ghosts, drawing them '+
      'first from the monster cup, then from the Outskirts, then from those claimed as '+
      'trophies. Place them in the Miskatonic U. streets. Investigators who destroy one '+
      'of these Ghosts before the end of next turn may draw one Exhibit Item. Leave '+
      'this card in play until then to indicate this. The terror level increases by 1.');
  Add('MysteriousCratesFoundEmpty!', EXP_TBGOTW, HEADLINE, 'INDSQUARE', 'WOODS', 'MOON', 'CROSS',
      'But the monsters inside them have already escaped. A monster appears at the '+
      'Riverside streets and the Northside streets.');
  Add('NoOneCanHelpYouNow', EXP_AH, ENVIRONMENT, 'WOODS', 'UISLE', 'CROSS', 'MOON',
      'Gates cannot be sealed, although they can still be closed.');
  Add('NodensFavor', EXP_AH, ENVIRONMENT, 'BCAVE', 'TWHOUSE', 'SLASH,TRIANGLE,STAR', 'HEX',
      'It costs 2 fewer Clue tokens to seal gates');
  Add('OneThousandYoung', EXP_TBGOTW, RUMOR, '', '', 'SLASH,TRIANGLE,STAR,CROSS,ROUNDEL', 'SQUARE,DIAMOND,MOON,HEX',
      'Ongoing Effect: When a monster enters Uptown Streets, place it on this card. '+
      'Monsters on this card do not count against the monster limit. [Pass: '+
      'Investigators who end their movement in the Uptown Streets may make a Lore (-1) '+
      'check to place a clue token on this card. If there are as many clue tokens on '+
      'this card as there are investigators plus one, return it to the box (and all '+
      'monsters on it to the cup) and each investigator gains a random monster trophy.] '+
      '[Fail: If there are as many monsters on this card as there are investigators '+
      'plus one, return it to the box (and all monsters on it to the cup). All '+
      'investigators are devoured.]');
  Add('ParazoologistVisitsMiskatonicU.', EXP_TBGOTW, ENVIRONMENT, 'UISLE,BCAVE', 'WOODS', 'SQUARE,DIAMOND,MOON,HEX', 'SLASH,TRIANGLE,STAR,CROSS,ROUNDEL',
      'Investigators who end their movement in the Miskatonic U. Streets may discard 5 '+
      'Toughness worth of monster trophies to gain 1 Spell.');
  Add('PetsandWildlifeMutilated!', EXP_TBGOTW, HEADLINE, 'TUNNAMABLE,HSOCIETY', 'BCAVE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'Monsters must be on the prowl. A monster appears in the Merchant District '+
      'streets and the Southside streets.');
  Add('PicknickersPanic', EXP_AH, HEADLINE, 'SBUILDING', 'UISLE', 'MOON', 'CROSS',
      'A careless picnicker unleashes 2 monsters on the Downtown streets.');
  Add('PlagueofInsects', EXP_COTDP, ENVIRONMENT, 'TWHOUSE', '', 'HEX', 'SLASH,TRIANGLE,STAR',
      'Doom Tokens Added: 2. Investigators that end their turns in the street lose 1 '+
      'Stamina and 1 Sanity. The terror level increases by 1.');
  Add('PlanetaryAlignment', EXP_AH, ENVIRONMENT, 'BCAVE', 'TWHOUSE', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Thanks to the mystic energy generated by the planetary alignment, all spells '+
      'have a Sanity cost of 0.');
  Add('PoliceStepUpPatrolsInNorthside', EXP_AH, HEADLINE, 'GRAVEYARD', 'STLODGE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'All monsters in the Northside streets or locations are returned to the cup.');
  Add('PrivateSecurityHiredInUptown', EXP_AH, HEADLINE, 'HSOCIETY', 'WOODS', 'ROUNDEL', 'SQUARE,DIAMOND',
      'All monsters in the Uptown streets or locations are returned to the cup.');
  Add('RainingCatsAndDogs', EXP_AH, ENVIRONMENT, 'INDSQUARE', 'HROADHOUSE', 'CROSS', 'MOON',
      'Speed cheeks in Arkam are made at a -1 penalty, and players receive 1 less '+
      'movement point during the Movement Phase. Sneak checks in Arkham are made at a '+
       '+1 bonus. Return any Fire Vampires in play to the cup. If a Fire Vampire enters '+
      'play, return it to the cup and draw a different monster.');
  Add('RashofMissingPersons!', EXP_TBGOTW, HEADLINE, 'GRAVEYARD', 'INDSQUARE', 'CROSS', 'MOON',
      'The first player chooses an investigator to be lost in time and space');
  Add('ReturntotheOldWays', EXP_COTDP, RUMOR, '', 'TWHOUSE', 'CROSS', 'MOON',
      ' Ongoing Effect: Place 1 Clue token on this card at the end of every Mythos '+
      'Phase after the first. Any time a player attempts to use a Common Item, whether '+
      'by applying its bonuses to combat, exhausting it, or discarding it, roll a die. '+
      'On a 1 or 2, it falls apart before it can be used and must be discarded. Pass: '+
      'If a player discards a Common Item while in an Other World, return this card to '+
      'the box. Each player gains 2 Clue tokens. Fail: If there are 5 Clue tokens on '+
      'this card, return it to the box. All Common Items in play are discarded, and the '+
      'Common Item deck is removed from the game.');
  Add('RitualsofPower', EXP_TBGOTW, ENVIRONMENT, 'GRAVEYARD', 'BLACKCAVE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'An arcane ritual increases the Stamina damage of all monsters by 1.');
  Add('RiverBreachestheLevees', EXP_COTDP, ENVIRONMENT, 'GRAVEYARD', 'STLODGE', 'SLASH,TRIANGLE,STAR', 'HEX',
      'Place 1 Exhibit Item, facedown, in each of the Merchant District and Rivertown '+
      'streets. The first investigator to reach one of these neighborhood streets may '+
      'end his turn to take the item. The terror level increases by 1.');
  Add('RivertownResidentsTakeBackStreets', EXP_AH, HEADLINE, 'BCAVE', 'TWHOUSE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'All monsters in the Rivertown streets or locations are returned to the cup.');
  Add('RlyehRising', EXP_AH, ENVIRONMENT, 'HSOCIETY', 'WOODS', 'SLASH,TRIANGLE,STAR', 'HEX',
      'Star Spawn and Maniacs have their toughness increased by 1. The difficulty to '+
      'seal or close gates to R`lyeh is increased by 1.');
  Add('ScientistWarnsOfDimensionalRift', EXP_AH, HEADLINE, 'SBUILDING', 'UISLE', 'HEX', 'SLASH,TRIANGLE,STAR',
      'Scientist Warns of Dimensional Rift! Headline All Dimensional Shamblers and '+
      'Hounds of Tindalos in Arkham are returned to the cup. If at least one monster '+
      'retums to the cup, raise the terror level by 1.');
  Add('SheldonGangTurnsToPoliceForAid', EXP_AH, HEADLINE, 'UISLE', 'GRAVEYARD', 'ROUNDEL', 'SQUARE,DIAMOND',
      'The Sheldon Gang disturbs a burial mound, releasing 2 monsters into the Uptown '+
      'streets.');
  Add('SlumMurdersContinue', EXP_AH, HEADLINE, 'HSOCIETY', 'WOODS', 'MOON', 'CROSS',
      'An old basement is opened, releasing 2 monsters into the Easttown streets.');
  Add('SolarEclipse', EXP_AH, ENVIRONMENT, 'UISLE', 'GRAVEYARD', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Due to the interference of the solar eclipse, no spells may be cast.');
  Add('SouthsideStranglerSuspected', EXP_AH, HEADLINE, 'HSOCIETY', 'WOODS', 'ROUNDEL', 'SQUARE,DIAMOND',
      'However, the press is mistaken, and the murders were caused by 2 monsters that '+
      'are released into the Southside streets.');
  Add('StrangeSightings(3)!', EXP_TBGOTW, HEADLINE, '', '', 'SQUARE,DIAMOND,MOON,HEX', 'SLASH,TRIANGLE,STAR,CROSS,ROUNDEL',
      'A monster surge occurs. However, no gates open this turn. The first player gains '+
      '1 Clue token.');
  Add('StrangeSightings(4a)!', EXP_TBGOTW, HEADLINE, '', '', 'SLASH,TRIANGLE,STAR,CROSS,ROUNDEL', 'SQUARE,DIAMOND,MOON,HEX',
      'A monster surge occurs. However, no gates open this turn. The first player gains '+
      '1 Clue token.');
  Add('StrangeSightings(4b)!', EXP_TBGOTW, HEADLINE, '', '', 'SLASH,TRIANGLE,STAR,CROSS,ROUNDEL', 'SQUARE,DIAMOND,MOON,HEX',
      'A monster surge occurs. However, no gates open this turn. The first player gains '+
      '1 Clue token.');
  Add('StrangeWhispersPromiseVengeance!', EXP_TBGOTW, HEADLINE, 'STLODGE', 'SBUILDING', 'HEX', 'SLASH,STAR,TRIANGLE',
      'A monster appears at a street location chosen by the first player.');
  Add('StrangeLightsOnCampus', EXP_AH, HEADLINE, 'HSOCIETY', 'WOODS', 'HEX', 'SLASH,TRIANGLE,STAR',
      'The Library, Administration Building, and Science Building are all closed until '+
      'the end of next turn. Leave this card in play until then to indicate this. '+
      'Close: Administration Building Library Science Building');
  Add('StrangePowerFluxPlaguesCity', EXP_AH, HEADLINE, 'TUNNAMABLE', 'INDSQUARE', 'SLASH,TRIANGLE,STAR', 'HEX',
      'All investigators in Other World areas may immediately retum to Arkham.');
  Add('StrangeTremorsCease', EXP_AH, HEADLINE, 'TUNNAMABLE', 'INDSQUARE', 'HEX', 'SLASH,TRIANGLE,STAR',
      'All Chthonians and Dholes in Arkham are returned to the cup. If at least 0ne '+
      'monster retums to the cup, raise the terror level by l');
  Add('StudentsProtestMuseumExhibit', EXP_COTDP, ENVIRONMENT, 'TUNNAMABLE', 'BCAVE', 'HEX', 'SLASH,TRIANGLE,STAR',
      'Any investigator who ends his movement in the streets must make a Fight (-1) '+
      'check or be delayed by the throngs of protestors.');
  Add('SunnyAndClear', EXP_AH, ENVIRONMENT, 'HROADHOUSE', 'BCAVE', 'CROSS', 'MOON',
      'Sneak checks in Arkham are made at a -1 penalty. Will Checks in Arkham are made '+
      'at a +1 bonus. If the Haunter in Darkness is in play, return it to the cup. If '+
      'the Haunter in Darkness enters play, return it to the cup and draw a different '+
      'monster.');
  Add('SuperstitionsAbound!', EXP_TBGOTW, HEADLINE, 'UISLE,GRAVEYARD', 'TUNNAMABLE', 'SLASH,STAR,TRIANGLE', 'HEX',
      'The first player chooses one investigator to become Blessed and another '+
      'investigator to become Cursed. (If there is only one investigator, nothing '+
      'happens).');
  Add('TemperenceFeverSweepsCity', EXP_AH, HEADLINE, 'BCAVE', 'TWHOUSE', 'HEX', 'SLASH,TRIANGLE,STAR',
      'Any investigator with Whiskey must pass a Sneak (-1) check or get arrested and '+
      'taken to the Police Station. If this occurs, they must discard their Whiskey. In '+
      'addition, Hibb`s Roadhouse is closed until the end of next turn. Leave this card '+
      'in play until then to indicate this. Close: Hibb`s Roadhouse');
  Add('TerrorAtTheTrainStation', EXP_AH, HEADLINE, 'BCAVE', 'TWHOUSE', 'MOON', 'CROSS',
      'A rusty train arrives in Arkham, disgorging 2 monsters into the Northside '+
      'streets.');
  Add('TheChillOfTheGrave', EXP_AH, ENVIRONMENT, 'SBUILDING', 'HROADHOUSE', 'CROSS', 'MOON',
      'All Undead monsters have their toughness increased by 1.');
  Add('TheFestival', EXP_AH, ENVIRONMENT, 'HSOCIETY', 'WOODS', 'CROSS', 'MOON',
      'The festival has begun! Cultists and Byakhee have their toughness increased by '+
      '1.');
  Add('TheGreatRitual', EXP_AH, RUMOR, '', 'SBUILDING', 'SLASH,TRIANGLE,STAR', 'HEX',
      'Ongoing Effect: Cultists, Witches, Warlocks, and High Priests have their '+
      'toughness increased by 2 while this card is in play. Place 1 Clue token on this '+
      'card at the end of every Mythos Phase (beginning the turn alter it entered '+
      'play). Pass: If a single player discards 3 spells (4 if there are 5 or more '+
      'players) While in the French Hill streets during the Arkham Encounter Phase, '+
      'return this card to the box. Each player gains 2 Clue tokens. Fail: If there are '+
      'ever 5 Clue tokens on this card, return it to the box. From now on, draw 2 '+
      'mythos cards each Mythos Phase. Ignore everything on the first card except for '+
      'the gate opening. Activity At: French Hill Streets');
  Add('TheManInBlack', EXP_AH, ENVIRONMENT, 'BCAVE', 'TWHOUSE', 'CROSS', 'MOON',
      'Investigators who end their movement in the French Hill streets may deal with '+
      'the Man in Black to gain power. They roll dice equal to their current Sanity, '+
      'and for every failed die, they lose l Sanity. If this reduces them to O Sanity, '+
      'they are devoured and the player must start a new character. Otherwise, they '+
      'gain l Clue token and draw 1 Spell. Activity At: French Hill Streets');
  Add('TheSouthsideStranglerStrikes', EXP_AH, RUMOR, '', 'INDSQUARE', 'SLASH,TRIANGLE,STAR', 'HEX',
      'Ongoing Effect: Return one Ally from the Ally deck to the box at random at the '+
      'end of every Mythos Phase while this card is in play (beginning the turn after '+
      'it entered play). The Southside Strangler has struck again! Pass: If a single '+
      'player discards 5 Clue tokens While in Ma`s Boarding House during the Arkham '+
      'Encounter Phase, return this card to the box. Each player gains $5 as a reward '+
      'from the police. Fail: If there are no Allies to return to the box at the end of '+
      'the Mythos Phase, return this card to the box. Each player must lower either '+
      'their maximum Sanity or Stamina (their choice) by 1 for the rest of the game. '+
      'Activity At Srouthsiede Streets');
  Add('TheStarsAreRight', EXP_AH, RUMOR, '', 'SBUILDING', 'SLASH,TRIANGLE,STAR', 'HEX',
      'Ongoing Effect: Roll a die at the end of every Mythos Phase while this card is '+
      'in play (beginning the turn after it entered play). On a 1 or 2, place one doom '+
      'token on the ancient one`s doom track. Pass: If a player discards an Ally card '+
      'while in the Downtown streets during the Arkham Encounter Phase, return this '+
      'card to the box. Each player draws 2 Common Items. Fail: If the Ancient One '+
      'awakens, retum this card to the box. Activity At: Downtown Streets');
  Add('TheTerribleExperiment', EXP_AH, RUMOR, '', 'UISLE', 'CROSS', 'MOON',
      'When this card enters play, place 5 monsters from the cup on it. Any player may '+
      'choose to fight one or more of these monsters while in the Miskatonic U. streets '+
      'during the Arkham Encounter Phase. If defeated, they are claimed as monster '+
      'trophies. These monsters do not move, are not considered to be on the board, and '+
      'do not count against the monster limit. Ongoing Effect: Place a monster on this '+
      'card at the end of every Mythos Phase (beginning the turn after it entered '+
      'play). Pass: If there are no monsters on this card, return it to the box. Each '+
      'player draws l Skill. Fail: If there are 8 monsters on this card, return it to '+
      'the box. Raise the terror level to 10 and place the monsters that were on it '+
      'into play in the Miskatonic U. streets.');
  Add('ThingsOfDarkness', EXP_AH, ENVIRONMENT, 'GRAVEYARD', 'STLODGE', 'SQUARE,DIAMOND', 'ROUNDEL',
      'Ghouls, Formless Spawns, Shoggoths, and Flying Polyps have their toughness '+
      'increased by l.');
  Add('Tongue-TiedTeacherTaunted!', EXP_TBGOTW, HEADLINE, 'SBUILDING', 'STLODGE', 'SLASH,TRIANGLE,STAR,CROSS,ROUNDEL', 'SQUARE,DIAMOND,MOON,HEX',
      'Each investigator with the most Clue tokens loses 1 Clue token. Each '+
      'investigator with the fewest Clue tokens gains 1 Clue token.');
  Add('VigilanteGuardsTheNight', EXP_AH, HEADLINE, 'WOODS', 'TUNNAMABLE', 'ROUNDEL', 'SQUARE,DIAMOND',
      'All monsters in the Downtown streets or locations are returned to the cup.');
  Add('VivisectionVictim!', EXP_TBGOTW, HEADLINE, 'HSOCIETY,SBUILDING', 'TWHOUSE', 'CROSS', 'MOON',
      'The first player may choose a monster in Arkham and move it to the Science '+
      'Building.');
  Add('WitchBurningAnniversary', EXP_AH, HEADLINE, 'SBUILDING', 'UISLE', 'MOON', 'CROSS',
      'All Dimensional Shamblers and Hounds of Tindalos in Arkham are returned to the '+
      'cup. If at least one monster retums to the cup, raise the terror level by 1.');
end;
             
initialization
  Mythoss := TStringList.Create;
  LoadMythoses;
  Mythoss.Sort;
end.

