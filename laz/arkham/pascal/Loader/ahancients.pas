unit AHAncients;
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
  Ancients: TStringList;
 
implementation

procedure Add(const aName          : string;
              const aExpansion     : EExpansion;
              const aCombatRating  : string;
              const aDefences      : string;
              const aWorshippers   : string;
              const aPower         : string;
              const aStartOfBattle : string;
              const aAttack        : string;
              const aDoomTrack     : integer;
              const aUseMasks      : integer);
var
  Ancient : TAncient;
begin
  Ancient := TAncient.Create;
  with Ancient do begin
    name          := aName;
    expansion     := aExpansion;
    combatRating  := aCombatRating;
    defences      := aDefences;
    worshippers   := aWorshippers;
    power         := aPower; 
    startOfBattle := aStartOfBattle;
    attack        := aAttack;
    doomTrack     := aDoomTrack;
    usemasks      := aUseMasks;
  end;
  Ancients.AddObject(aName, Ancient);
end;

procedure LoadAncients;
begin
  Add('Azathoth', EXP_AH
    , '-oo'
    , ''
    , 'Since Azathoth promises nothing except destruction, only the insane worship him. However, their fanaticism gives them strength. '+
      'Maniacs have their toughness increased by 1.'
    , 'Absolute Destruction - If Azathoth awakens, the game is over and the investigators lose.'
    , ''
    , 'The end is here! Azathoth destroys the world.'
    , 14, 0
    );
  Add('Cthulhu', EXP_AH
    , '-6'
    , 'Attack'
    , 'Cthulhu''s worshippers often have the Innsmouth Look, a sign of monstrous ancestors. '+
      'Cultists have a horror rating of -2 and a horror damage of 2 Sanity.'
    , 'Dreams of Madness - While Cthulhu stirs in his slumber, investigators have their maximum Sanity and maximum Stamina reduced by 1.'
    , ''
    , 'Each investigator lowers either his maximum Sanity or Maximum Stamina by 1 (his choice). '+
      'After Cthulhu attacks 1 doom token is placed back on Cthulhu''s doom track if it isn''t already full.'
    , 13, 0
    );
  Add('Hastur', EXP_AH
    , '-X'
    , 'Physical Resistance'
    , 'Hastur''s worshippers ride byakhee mounts that they call with enchanted whistles. Cultists are flying monsters and their combat rating is -2.'
    , 'The King in Yellow - While Hastur stirs in his slumber, the cost to seal a gate is 8 Clue tokens instead of 5.'
    , 'X is set to the current terror level.'
    , 'Each investigator lowers either his maximum Sanity or Maximum Stamina by 1 (his choice). '+
      'After Hastur attacks 1 doom token is placed back on Hastur''s doom track if it isn''t already full.'
    , 13, 0
    );
  Add('Ithaqua', EXP_AH
    , '-3'
    , ''
    , 'Ithaqua''s worshippers eat the flesh of their fellow men, gaining supernatural power through their dark practice. '+
      'Cultists have their toughness increased by 2.'
    , 'Icy Winds - While Ithaqua stirs in his slumber, any investigator in a street area at the end of the Mythos phase '+
      'loses 1 Stamina. In addition, all Weather cards are discarded without their special effects taking place.'
    , 'Investigators must roll a die for every item they have, discarding the item on a failure.'
    , 'Each investigator must pass a Fight (+1) check or lose 2 Stamina. This check''s modifier decreases by 1 each turn '+
      '(+0 the 2nd turn, -1 the 3rd turn, etc.)'
    , 11, 0
    );
  Add('Nyarlathotep', EXP_AH
    , '-4'
    , 'Magical Resistance'
    , 'Nyarlathotep has innumerable cults all over the world. Cultists have the Endless ability.'
    , 'A Thousand Masks - At the start of the game add the 5 Mask monsters to the cup. Multiple Mask monsters can be in play at once.'
    , 'Any investigator with no Clue tokens is devoured.'
    , 'Each investigator must pass a Lore (+1) check or lose 1 Clue token. Any investigator with no Clue tokens left '+
      'is devoured. This check''s modifier decreases by 1 each turn (+0 the 2nd turn, -1 the 3rd turn, etc.)'
    , 11, 1
    );
  Add('Shub-Niggurath', EXP_AH
    , '-5'
    , 'Physical Immunity'
    , 'Shub-Niggurath''s young are numberless. Dark Young have the Endless ability.'
    , 'Black Goat of the Woods - While Shub-Niggurath stirs in her slumber, all monsters have their toughness increased by 1.'
    , 'Any investigator with no monster trophies is devoured.'
    , 'Each investigator must pass a Sneak (+1) check or lose 1 monster trophy. Any investigator with no monster trophies left is devoured. The check''s modifier decreases by 1 each turn (+0 the 2nd turn, -1 the 3rd turn, etc.)'
    , 12, 0
    );
  Add('Yig', EXP_AH
    , '-3'
    , ''
    , 'Yig''s worshippers are actually disguised serpent people. Their bite is highly poisonous. Cultists have a combat rating of +0 and a combat damage of 4 Stamina.'
    , 'Yig''s Anger - While Yig stirs in his slumber, he gains a doom token whenever a Cultist is defeated or an investigator is Lost in Time and Space.'
    , 'Every investigator is Cursed. Any investigator that already has a Curse is devoured.'
    , 'Each investigator must pass a Speed (+1) check or lose 1 Sanity and 1 Stamina. This check''s modifier decreases by 1 each turn (+0 the 2nd turn, -1 the 3rd turn, etc.)'
    , 10, 0
    );
  Add('Yog-Sothoth', EXP_AH
    , '-5'
    , 'Magical Immunity'
    , 'Yog-Sothoth''s worshippers have powerful magical abilities. Cultists have Magical Immunity and a combat rating of -1.'
    , 'The Key and the Gate - While Yog-Sothoth stirs in his slumber, the difficulty to close or seal a gate increases by 1. In addition, any investigator Lost in Time and Space is devoured.'
    , 'Any investigator with no gate trophies is devoured.'
    , 'Each investigator must pass a Will (+1) check or lose 1 gate trophy. Any investigator with no gate trophies left is devoured. This check''s modifier decreases by 1 each turn (+0 the 2nd turn, -1 the 3rd turn, etc.)'
    , 12, 0
    );
end;

initialization
  Ancients := TStringList.Create;
  LoadAncients;
  Ancients.sort;
end.

