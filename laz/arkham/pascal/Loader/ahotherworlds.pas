unit AHOtherWorlds;
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
  OtherWorlds    : TStringList;

implementation

procedure AddCard(const aGroupId       : EOWorldGroup;
                  const aExpansion     : EExpansion;
                  const aPlace         : EOWorldPlace;
                  const aNo            : integer;
                  const aDescription   : string);
var
  OtherWorld : TOtherWorld;
begin
  OtherWorld := TOtherWorld.Create;
  with OtherWorld do begin
    groupId     := aGroupId;
    expansion   := aExpansion;
    place       := aPlace;
    no          := aNo;
    description := aDescription;
  end;
  OtherWorlds.AddObject(OtherWorld.GetKey, OtherWorld);
end;

procedure Load;
begin
  AddCard(GROUPB, EXP_AH, ABYSS, 1,
         'You rest a bit beside a small, glowing pool filled with black, blind fish. Pass '+
         'a Luck (-1) check to notice an unusual object in the Water. Fishing it out, you '+
         'draw l Unique Item and gain $3.');
  AddCard(GROUPB, EXP_AH, ABYSS, 2,
         'A glowing light ahead draws you towards it. Make a Luck (-1) check. If you pass, '+
         'the glow is a way home. Return to Arkham. If you fail, the light is a trap set '+
         'by one of the creatures that lives here A monster appears!');
  AddCard(GROUPB, EXP_AH, ABYSS, 3,
         'You are bewildered. Pass a Lore (-1) check or stay here next turn.');
  AddCard(GROUPB, EXP_AH, ABYSS, 4,
         'The caverns split. Make a Luck (+1) check and consult the chart below: '+
         'Successes: 0-1: Move to the Black Cave. 2: Move to The Dreamlands. 3+: You enter '+
         'a dark temple. Pass a Luck (-1) check to draw a Unique Item.');
  AddCard(GROUPB, EXP_AH, ABYSS, 5,
         'The feeble glow and Warmth of the candle is enough to restore you a bit. Gain 1 '+
         'Stamina.');
  AddCard(GROUPB, EXP_COTDP, ABYSS, 6,
         'You are lost in the darkness. Pass a Luck (-2) check or lose 1 Sanity and stay '+
         'here next turn.');
  AddCard(GROUPB, EXP_COTDP, ABYSS, 7,
         'Something impossibly huge and ominous lurches across the horizon, Pass a Luck '+
         '(-1) check or its gaze with eyes the size of planets fall upon you, and you lose '+
         '2 Sanity.');
  AddCard(GROUPB, EXP_COTDP, ABYSS, 8,
         'A horrible scene capturers your gaze. Creatures that mortals would call angels '+
         'and devils cavort together, their bodies and laughter mingling in an unholy '+
         'fusion. If you join their dance, take both the Tainted card and the Anointed '+
         'card.');
  AddCard(GROUPB, EXP_COTDP, ABYSS, 9,
         'You look into a pool of water and see someone! Choose another investigator and '+
         'make a Will (-2) check. Successes: [0) He is drawn into the Abyss.] [1-2) You '+
         'and he switch places.] [3+) You move to his location, and the gate through which '+
         'you entered the Abyss is sealed.]');
  AddCard(GROUPB, EXP_COTDP, ABYSS, 9,
         'Your journey through the darkness is slow but restful. You are restored to your '+
         'maximutn Stamina, but are delayed.');
  AddCard(GROUPB, EXP_COTDP, ABYSS, 10,
         'You discover a large chamber filled with hideous creatures, in numbers too vast '+
         'to count. Your only hope is to pass undetected. Pass a Sneak (+1) check or be '+
         'devoured.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 1,
         'Luck is With you. You stumble on a cache of supplies. Draw 1 Common Item.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 2,
         'Pass a Luck (-1) check to discover a cache of ancient papers containing valuable '+
         'information about the Mythos. Gain 1 Clue token for every success you rolled on '+
         'your Luck check.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 3,
         'Monsters lurk everywhere. Pass a Sneak (-2) check or stay here next turn.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 4,
         'Pass a Luck (-1) check to find something to defend yourself with. Take the first '+
         'Weapon from the Common Item deck.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 5,
         'Pass a Fight (-2) check to lever back the lid of the stone chest. Inside, you '+
         'find $8. If you fail, lose 1 Stamina.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 6,
         'Pass a Fight (-1) check to hang on to your prize despite the wind Draw 1 Spell.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 7,
         'The insanity of this place really hits you. Lose 1 Sanity.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 8,
         'A monster appears!');
  AddCard(GROUPB, EXP_AH, ANOTHER, 9,
         'A hideous monster appears!');
  AddCard(GROUPB, EXP_AH, ANOTHER, 10,
         'You`ve completed your task, but now you must escape before the portal closes! '+
         'Pass a Speed (-2) check to return to Arkham. If you fail, you are lost in time '+
         'and space. In either event, you automatically close the gate you entered '+
         'through.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 11,
         'You are lost in a labyrinth of high walls. Pass a Lore (-1) check or stay here '+
         'next turn.');
  AddCard(GROUPB, EXP_AH, ANOTHER, 12,
         'The strain is too much for your mind. Lose 1 Sanity.');
  AddCard(GROUPB, EXP_COTDP, ANOTHER, 13,
         'The stench of fecundity and blood surrounds you. A monster appears! If you do '+
         'not evade it or defeat it on the first round of combat, it replicates, and you '+
         'must evade or defeat a second one!');
  AddCard(GROUPB, EXP_COTDP, ANOTHER, 14,
         'Something followed you here...if there are any monsters in the same location as '+
         'the gate you entered, they appear. If they are not defeated, they remain in '+
         'their original location.');
  AddCard(GROUPB, EXP_COTDP, ANOTHER, 15,
         'A scrap of paper flutters into your hands, with the words "this world was '+
         'inhabited at one time by another race who, in practising black magic, lost their '+
         'foothold and were expelled from the allegorical garden...." Lose. up to 2 Clue '+
         'tokens due to this misleading information, if able.');
  AddCard(GROUPB, EXP_COTDP, ANOTHER, 16,
         'Make a Luck (-1) check. If you fail, a monster appears! If you pass, you may '+
         'draw 2 monsters from the cup and choose which one appears.');
  AddCard(GROUPB, EXP_COTDP, ANOTHER, 17,
         'Make a Fight (+0) or Will (+0) check. If you pass, you push through the walls of '+
         'fatigue and confusion and realize what must be done. You may seal the gate '+
         'through which you entered, but only by sacrificing yourself. If you choose to '+
         'seal the gate, you are devoured.');
  AddCard(GROUPB, EXP_COTDP, ANOTHER, 18,
         'You find the body of a long-dead explorer. Make a Luck (-2) check. For each '+
         'success, you may draw and keep one card from the Common Item deck.');
  AddCard(GROUPB, EXP_TBGOTW, ANOTHER, 19,
         'A monster appears!');
  AddCard(GROUPB, EXP_TBGOTW, ANOTHER, 20,
         'You encounter a stranger who looks like a much older version of yourself. You '+
         'are told, "Press on, you will succeed." Gain 2 Sanity.');
  AddCard(GROUPB, EXP_TBGOTW, ANOTHER, 21,
         'A ghostly ship captain offers you passage home, for a price. Return to Arkham, '+
         'but you are Cursed.');
  AddCard(GROUPB, EXP_TBGOTW, ANOTHER, 22,
         'At the top of a hill is an old stone well. You may toss $1 inside and pass a '+
         'Luck (-2) check to be Blessed. If you fail, nothing happens.');
  AddCard(GROUPB, EXP_TBGOTW, ANOTHER, 23,
         'A terrible monster appears!');
  AddCard(GROUPB, EXP_TBGOTW, ANOTHER, 24,
         'You are unsure if you are back in Arkham or not. Make a Will (-2) check. If you '+
         'succeed, return to Arkham. If not, lose 2 Sanity as the landscape twists and '+
         'warps in a nightmarish way.');
  AddCard(GROUPB, EXP_TBGOTW, ANOTHER, 25,
         'A ghastly monster appears!');
  AddCard(GROUPB, EXP_AH, CELEANO, 1,
         'A lurking monster appears!');
  AddCard(GROUPB, EXP_AH, CELEANO, 2,
         'Pass a Luck (-1) check or the book is a prison. If you fail, roll a die. On a '+
         'failure, a monster appears from the book. On a success, you are drawn into the '+
         'book for a time. Stay here next turn.');
  AddCard(GROUPB, EXP_AH, CELEANO, 3,
         'The symbol above the doorway glows. Make a Luck (-1) check. If you pass, gain 2 '+
         'Stamina and 2 Sanity. If you fail, discard 2 items of your choice.');
  AddCard(GROUPB, EXP_AH, CELEANO, 4,
         'That`s it! That`s the document you need! Quietly, you reach for it, trying not '+
         'to disturb its guardian. Make a Sneak (-2) check. If you pass, search the Spell '+
         'deck and take 1 Spell of your choice. If you fail, lose 2 Stamina.');
  AddCard(GROUPB, EXP_AH, CELEANO, 5,
         'The huge book opens noiselessly at your approach. If you choose, you may read '+
         'it, in which case you must pass a Fight (-1) [2] check to defeat its guardian. '+
         'If you do, draw 3 Spells and keep 2 of them. If you fail, lose 3 Stamina.');
  AddCard(GROUPB, EXP_COTDP, CELEANO, 6,
         'As you read the page, you realize that you have stumbled into a Written trap. '+
         'Pass a Lore (-1) check or you are Cursed.');
  AddCard(GROUPB, EXP_COTDP, CELEANO, 7,
         'You wander endless rows of tablets, scrolls, and tomes. If you wish, you may '+
         'spend 1 Sanity and 1 Stamina to make a Luck (+0) check. If you pass, you may '+
         'search the Common Item. Unique Item, or Exhibit Item deck forany single Tome '+
         'card and take that card.');
  AddCard(GROUPB, EXP_COTDP, CELEANO, 8,
         'The unwelcome are shown no mercy. Make a Lore (-1) check or you are expelled '+
         'from the great library, where a monster surprises you.');
  AddCard(GROUPB, EXP_COTDP, CELEANO, 9,
         'No sound is allowed in the great library but the rustling of pages and the '+
         'whisper of thoughts. Make a Sneak (-2) check or you are delayed.');
  AddCard(GROUPB, EXP_COTDP, CELEANO, 10,
         'You discover a copy of your favorite childhood story book. Gain 2 Sanity.');
  AddCard(GROUPB, EXP_COTDP, CELEANO, 11,
         'A book that you thought contained useful information has suddenly turned into a '+
         'vivid description of methods of torture. Lose 1 Sanity.');
  AddCard(GROUPB, EXP_AH, DREAMLAND, 1,
         'Humans are not the only creatures to dream. Make a Speed (-1) check. If you '+
         'pass, a monster appears. If you fail, a monster surprises you.');
  AddCard(GROUPB, EXP_AH, DREAMLAND, 2,
         'You stumble upon a nightmare, and must relive your past battles with horrible '+
         'creatures. One of your monster trophies, chosen at random, returns to life and '+
         'surprises you!');
  AddCard(GROUPB, EXP_AH, DREAMLAND, 3,
         'If humans dream of monsters, do monsters dream of us? A monster surprises you, '+
         'but seems terrified by your very humanity. Make a Will (-1) check. For each '+
         'success you roll, you gain a +1 to all checks during this combat.');
  AddCard(GROUPB, EXP_AH, DREAMLAND, 4,
         'King Kuranes would like a souvenir. If you have a Common Item, you may trade it '+
         'to him for 2 Clue tokens. If not, nothing happens.');
  AddCard(GROUPB, EXP_AH, DREAMLAND, 5,
         'Ghouls have feasted here and left behind a grisly mess. Pass a Will (-2) check '+
         'or lose 2 Sanity.');
  AddCard(GROUPB, EXP_COTDP, DREAMLAND, 6,
         'You must face the guardian to claim your prize. A monster appears! If you defeat '+
         'it, you do not collect it as a monster trophy, but you do gain 1 Unique Item.');
  AddCard(GROUPB, EXP_COTDP, DREAMLAND, 7,
         'A terrible storm strikes the ship which carries you. Pass a Fight (-2) check or '+
         'lose 2 Stamina.');
  AddCard(GROUPB, EXP_COTDP, PLATLENG, 8,
         'The villagers offer you a little sustenance. Gain 1 Stamina.');
  AddCard(GROUPB, EXP_AH, RLYEH, 1,
         'You hear distant chants. You feel you may learn more if you stop to listen. If '+
         'you wish, you may gain 1 Spell, but you will be delayed.');
  AddCard(GROUPB, EXP_AH, RLYEH, 2,
         'A massive wave crashes over you and washes one of your items out to sea. Choose '+
         '1 of your Common or Unique Items and discard it. If you have none, nothing '+
         'happens.');
  AddCard(GROUPB, EXP_AH, YUGGOTH, 1,
         'The stone creature pursues you. Pass a Speed (-1) check to escape with the '+
         'statue, gaining $5 and 2 Clue tokens. If you fail, the creature smashes you off '+
         'the cliff. You are lost in time and space.');
  AddCard(GROUPB, EXP_AH, YUGGOTH, 2,
         'Exposure and fear Weaken your mind. Pass a Will (-2) check or you must either '+
         'lose 2 Spells of your choice or lose 2 Sanity.');
  AddCard(GROUPB, EXP_AH, YUGGOTH, 3,
         'A monster appears from the darkness!');
  AddCard(GROUPB, EXP_AH, YUGGOTH, 4,
         'Pass a Sneak (-1) check or the creatures capture and experiment on you. Lose '+
         'half of your items, then immediately return to Arkham with no memory of the '+
         'experiments.');
  AddCard(GROUPB, EXP_AH, YUGGOTH, 5,
         'The creature`s grip is like steel! Pass a Fight (-2) check to break free and '+
         'escape. If you fail, the creature`s grip tightens with a sickening pop. You are '+
         'lost in time and space.');
  AddCard(GROUPB, EXP_COTDP, YUGGOTH, 6,
         'You`re dizzy from the strange ray. Pass a Will (-2) check or lose 1 item of your '+
         'choice.');
  AddCard(GROUPB, EXP_COTDP, YUGGOTH, 7,
         'You peer through a strange machine of glass and stone, its lenses pointed toward '+
         'the dark, sunless sky. There, impossibly far away, you behold the Earth. Gain 2 '+
         'Clue tokens, but make a Will (-3) check or lose 1 Sanity.');
  AddCard(GROUPB, EXP_COTDP, YUGGOTH, 8,
         'Make a Lore (-1) check to realize that you have come upon the "shining '+
         'trapezohedron," and utter the proper protective spell. If you fail, lose 1 '+
         'Sanity and set you Will slider to the lowest possible number.');
  AddCard(GROUPB, EXP_COTDP, YUGGOTH, 9,
         'Scuttling surrounds you in the dark as the creatures attack. Lose 1 Stamina. '+
         'Altemafively, you may light a torch to drive them back and lose no Stamina, but '+
         'upon seeing them, your mind recoils, and you lose 2 Sanity.');
  AddCard(GROUPB, EXP_COTDP, YUGGOTH, 10,
         'Stumbling around in the dark, you tumble down a sheer cliff. Pass a Speed (-1) '+
         'check to avoid losing 1 Common or Unique Item of your choosing.');
  AddCard(GROUPB, EXP_COTDP, YUGGOTH, 11,
         'You must immediately fight Shug-Niggurath! Since there is only one player in '+
         'this combat, you need one success to remove a doom token. If you run out of '+
         'monster trophies, you are devoured. If you defeat Shub-Niggurath, she retreats '+
         'into the void and you may escape to Arkham immediately. The gate to Yuggoth is '+
         'sealed behind you, and you may take it as a trophy. If Shub-Niggurath is the '+
         'Ancient One in play, do not fill up her doom track before this combat; also, '+
         'successes allow you to temporarily flip over doom tokens to their elder sign '+
         'sides instead of removing them. Once the battle is over, regardless of the '+
         'outcome, flip all the tokens on Shub-Nigguraths doom track back to their doom '+
         'token side and continue play.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 1,
         'Carefully, you avoid the gaze of a gigantic eye Watching an altar. You may try '+
         'to pass a Sneak (-1) check to steal a scroll from the dais. Draw l Spell. If you '+
         'fail, you are wracked by pain and lose 3 Sanity.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 2,
         'Pass a Luck (-1) check to discover a vital document. Gain 2 Clue tokens.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 3,
         'You come across a sleeping horror with a tentacle draped across a small gold '+
         'idol. Silence is of the essence as you attempt to gently ease the idol out from '+
         'under the creature`s pseudopod. Make a Sneak (-1) check. If you pass, gain $3. '+
         'If you fail, lose 2 Stamina.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 4,
         'Pass a Luck (-1) check to find the gate back. If so, immediately return to '+
         'Arkham.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 5,
         'Wedged beneath a fallen stone is a scroll. Draw l Spell.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 6,
         'The rope seems to extend upwards forever, but it`s the only way out of the '+
         'crevasse you ?nd yourself in. Pass a Fight (-1) check to climb it and return to '+
         'Arkham. If you fail, you fall, losing 2 Stamina and staying here next turn.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 7,
         'Pass a Fight (-2) check to pry open a grate you find built into the wall. '+
         'Inside, you find something fascinating. Draw 1 Unique Item.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 8,
         'A glimpse of home gives you hope. Gain 1 Sanity.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 9,
         'You come across a slaughtered creature. Pass a Luck (-1) check to claim a '+
         'monster trophy from the cup (even if it is Endless) and gain 2 Clue tokens.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 10,
         'You find some valuable items that you can sell back in Arkham. Gain $3.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 11,
         'You find a quiet spot to rest and recuperate. Gain 1 Stamina.');
  AddCard(GROUPG, EXP_AH, ANOTHER, 12,
         'You are beginning to understand the strange creatures here. Gain 1 Clue token.');
  AddCard(GROUPG, EXP_COTDP, ANOTHER, 13,
         'The monsters corpse lies before you, and to your horror, you find your mouth '+
         'watering. If you consume it, make a Fight (-2) check. If you fail lose Stamina '+
         'equal to the number of dice rolled. If you pass, gain Stamina equal to the '+
         'number of dice rolled.');
  AddCard(GROUPG, EXP_COTDP, ANOTHER, 14,
         'You approach a tunnel only to feel a terrible tromping shake the ground from '+
         'below...and then an unearthly screech rends the sky. Make a Sneak (-1) check. If '+
         'you pass, 1 monster appears! If you fail, 2 monsters appear!');
  AddCard(GROUPG, EXP_COTDP, ANOTHER, 15,
         'Pass a Speed (-2) check to jump the fissure. If you fail, lose 1 Stamina and you '+
         'are delayed.');
  AddCard(GROUPG, EXP_COTDP, ANOTHER, 16,
         'A man in a coat and hat takes your arm, and you find yourself leading the '+
         'shadowy presence forward. All the reward you seem to need is his '+
         'reassurance...perhaps you are being mystically controlled, but its hard to care. '+
         'Gain 1 Sanity, but take the Local Guide card.');
  AddCard(GROUPG, EXP_COTDP, ANOTHER, 17,
         'A dark ocean laps at your feet, and you see the gables of old-fashioned '+
         'buildings across the water. Could that be Innsmouth? Your Luck slider is reset '+
         'to the lowest possible number, but you gain 1 Clue token.');
  AddCard(GROUPG, EXP_COTDP, ANOTHER, 18,
         'A strange song conjures up images of a life you could have lived. Gain Clue '+
         'tokens equal to your focus.');
  AddCard(GROUPG, EXP_TBGOTW, ANOTHER, 19,
         'A monster appears!');
  AddCard(GROUPG, EXP_TBGOTW, ANOTHER, 20,
         'An enormous stone marker covered with arcane markings stands before you. Its '+
         'true purpose is unclear, but you think you may be able to translate a small '+
         'portion. Pass a Lore (-1) check to gain I Spell.');
  AddCard(GROUPG, EXP_TBGOTW, ANOTHER, 21,
         'Your feet begin to sink into a repulsive goo. Pass a Fight (-2) check to pull '+
         'yourself out. If you fail, you are sucked into the unknown and are Iost in time '+
         'and space.');
  AddCard(GROUPG, EXP_TBGOTW, ANOTHER, 22,
         'Its a dead end. You are delayed as you must retrace your path and try something '+
         'different.');
  AddCard(GROUPG, EXP_TBGOTW, ANOTHER, 23,
         'The air here is too noxious. You dont think you can make it. Pass a Speed (-1) '+
         'check or lose 1 Stamina.');
  AddCard(GROUPG, EXP_TBGOTW, ANOTHER, 24,
         'You find a fresh water source that replenishes you. Gain 1 Stamina.');
  AddCard(GROUPG, EXP_TBGOTW, ANOTHER, 25,
         'You feel a powerful pulse of malevolent intelligence. It wants to tell you '+
         'secrets. For each point of Sanity you sacrifice. you may gain 1 Clue token.');
  AddCard(GROUPG, EXP_AH, CELEANO, 1,
         'An old professor from Earth teaches you a thing or two. Pass a Luck (-1) [2] '+
         'check to draw 1 Skill.');
  AddCard(GROUPG, EXP_AH, CELEANO, 2,
         'Pass a Luck (-2) check to find a valuable book. If so, search the Unique Item '+
         'deck and take the first Tome you find.');
  AddCard(GROUPG, EXP_AH, CELEANO, 3,
         'Your red-eyed reflection in the mirror captures your attention. Stay here next '+
         'turn.');
  AddCard(GROUPG, EXP_AH, CELEANO, 4,
         'You come across a Wizened old creature who debates with you for some time. If '+
         'you pass a Lore (-1) check, the creature is amused by your discussion and you '+
         'are Blessed.');
  AddCard(GROUPG, EXP_AH, CELEANO, 5,
         'You find secret lore hidden in the mosaics on the wall. Make a Lore (+2) check '+
         'and gain Clue tokens equal to your successes.');
  AddCard(GROUPG, EXP_COTDP, CELEANO, 6,
         'Pass a Luck (-2) check to find a book small enough to carry. Search the Unique '+
         'Item deck and take the first Tome you find.');
  AddCard(GROUPG, EXP_COTDP, CELEANO, 7,
         'The book you are reading is a vacuous tome of oblivion, and it begins to suck '+
         'you into its pages! Make a Fight (+1) check or you are devoured. Spells may be '+
         'discarded as if they were Clue tokens for this check.');
  AddCard(GROUPG, EXP_COTDP, CELEANO, 8,
         'You find a journal so compelling that its author seems to live in your mind! '+
         'Make a Luck (+1) check. If you fail, lose 2 Sanity. If you pass, draw an Ally '+
         'and place tokens on it equal to the number of successes rolled. Discard 1 token '+
         'from it during each Upkeep Phase. If it has no tokens at the beginning of the '+
         'Upkeep Phase, discard the Ally instead.');
  AddCard(GROUPG, EXP_COTDP, CELEANO, 9,
         'Words are the nourishment of the mind. You lose 1 Stamina, but make a Speed (-1) '+
         'check. If you pass, gain 2 Sanity.');
  AddCard(GROUPG, EXP_COTDP, CELEANO, 9,
         'Youve found a most amazing book, filled with everything you could ever want to '+
         'know provided you can endure reading it. For each point of Sanity you are '+
         'willing to lose, you may draw a Spell; choose one to keep and discard the '+
         'others.');
  AddCard(GROUPG, EXP_COTDP, CELEANO, 10,
         'It is recommended to you to simply open a book at random to find the answers you '+
         'seek. If you would like to give it a try, make a Luck (-2) check. If you pass, '+
         'gain 2 Clue tokens. If not, you still gain 2 Clue tokens but you are delayed.');
  AddCard(GROUPG, EXP_AH, DREAMLAND, 1,
         'Touring the perfumed jungles of Kied, you come across an ancient ivory palace. '+
         'Pass a Luck (-1) check to explore it Without getting caught. Draw l Spell. If '+
         'you fail the check, lose l item of your choice.');
  AddCard(GROUPG, EXP_AH, DREAMLAND, 2,
         'Pass a Will (-1) check to convince the Rulers of Rokol to share their Wealth '+
         'with you. If so, roll two dice and add them together. Gain that much money.');
  AddCard(GROUPG, EXP_AH, DREAMLAND, 3,
         'Pass a Luck (-1) check to chance across one of the little red singing birds of '+
         'Celephais. Its song brings solace and strength to your heart. Restore your '+
         'Sanity and Stamina to their maximum values.');
  AddCard(GROUPG, EXP_AH, DREAMLAND, 4,
         'You encounter the talking cats of Ulthar. Pass a Will (+0) check to draw l '+
         'Spell.');
  AddCard(GROUPG, EXP_AH, DREAMLAND, 5,
         'Pass a Luck (-1) check to come across a riding zebra and save some traveling '+
         'time. If you are in the first area of The Dreamlands, move to the second area. '+
         'If you are in the second area, return to Arkham.');
  AddCard(GROUPG, EXP_COTDP, DREAMLAND, 6,
         'Make a Luck (-1) check. If you pass, then, waving goodbye, the happy villagers '+
         'bestow a gift upon you. Draw 1 Common Item.');
  AddCard(GROUPG, EXP_COTDP, DREAMLAND, 7,
         'Have an encounter at a location of your choice in Arkham, then return here. If '+
         'you wish, you may pass a Luck (-1) check to realize that it was all a dream, and '+
         'negate any Sanity or Stamina loss as a result of that encounter.');
  AddCard(GROUPG, EXP_COTDP, DREAMLAND, 8,
         'A powerful wind scours away your memories, good and bad. Discard all of the '+
         'following, Blessing, Curse, Detriment cards, and Benefit cards.');
  AddCard(GROUPG, EXP_COTDP, DREAMLAND, 9,
         'A strange man in a turban tells you, "In Dylath-Leen, they will exchange '+
         'anything for a ruby such as this." If you take the ruby, search the Unique Item '+
         'deck for a card of your choice, but then you lose 3 Sanity and are Cursed.');
  AddCard(GROUPG, EXP_COTDP, DREAMLAND, 9,
         'You find the corpses of a party of cultists. Make a Fight (-1) check to drag '+
         'their bodies from the pit. If you pass, take a number of Cultists as trophies '+
         'from the monster cup equal to the number of successes you rolled.');
  AddCard(GROUPG, EXP_COTDP, DREAMLAND, 10,
         'Your zebra has run off without you. Now, you are delayed.');
  AddCard(GROUPG, EXP_COTDP, DREAMLAND, 11,
         'Make a Will (-2) check to whisper to a sleeper in his dreams. If you pass, one '+
         'investigator in Arkham of your choice gains Clue tokens equal to the number of '+
         'successes you rolled.');
  AddCard(GROUPG, EXP_AH, GREATRACE, 1,
         'Sometimes, violence is the answer. Pass a Fight (-1) check to break free of your '+
         'captors and return to Arkham.');
  AddCard(GROUPG, EXP_AH, GREATRACE, 2,
         'You must have that device if you are to escape from this accursed city. Pass a '+
         'Sneak (-1) [2] check to draw 1 Unique Item and return to Arkham. If you fail, '+
         'your captors are none too kind. Lose 3 Sanity and 1 Stamina.');
  AddCard(GROUPG, EXP_AH, GREATRACE, 3,
         'You find yourself in an ancient and abandoned temple. Pass a Luck (-1) check to '+
         'find a golden statue worth $10. However, if you take it, you are Cursed.');
  AddCard(GROUPG, EXP_AH, GREATRACE, 4,
         'Pass a Luck (-1) check to find something useful among the incomprehensible '+
         'artifacts. If so, draw 1 Unique Item.');
  AddCard(GROUPG, EXP_AH, GREATRACE, 5,
         'The conical entity tries to teach you some magic. Pass a Lore (-2) [2] check to '+
         'draw 2 Spells.');
  AddCard(GROUPG, EXP_COTDP, GREATRACE, 6,
         'You may choose to try and infiltrate one of the angled structures. If so, make a '+
         'Sneak (-1) check. If you pass, draw 2 Unique Items and keep 1 of them If you '+
         'fail, you are lost in time and space.');
  AddCard(GROUPG, EXP_COTDP, GREATRACE, 7,
         'The conical beings here try to speak to you. Make a Lore (-2) check. If you '+
         'fail. you are delayed. If you pass you learn that they are enemies of the '+
         'Ancient Ones; gain 3 Clue token.');
  AddCard(GROUPG, EXP_COTDP, GREATRACE, 8,
         'These beings knew of senses beyond the five you possess. If your maximum Sanity '+
         'is higher than your maximum Stamina, take the Psychic card. If your maximum '+
         'Stamina is higher than your maximum Sanity, take the Visions card.');
  AddCard(GROUPG, EXP_COTDP, GREATRACE, 9,
         'Theyve been collecting people! Make a Lore (-2) |2| cheek to determine how to '+
         'release the victims. If you pass, you may search the Ally deck and take any Ally '+
         'of your choice. If you fail, you are taken captive yourself, and are delayed.');
  AddCard(GROUPG, EXP_COTDP, GREATRACE, 9,
         'You read a detailed description of humanitys extinction. Pass a Will (-1) check '+
         'or lose 2 Sanity.');
  AddCard(GROUPG, EXP_COTDP, GREATRACE, 10,
         'One of the strange creatures wants to take one of your items. Pass a Fight (-2) '+
         'check to hold onto it. If you do not, choose 1 Common or Unique Item and discard '+
         'it.');
  AddCard(GROUPG, EXP_COTDP, GREATRACE, 11,
         'You examine strange glyphs and begin to understand their purpose. Pass a Lore '+
         '(-2) check to gain I Spell.');
  AddCard(GROUPG, EXP_AH, PLATLENG, 1,
         'The hooved, wide-mouthed traders of this land are wealthy, but dangerous. You '+
         'may make a Lore (-2) check to trade with them. If you pass, gain $6. If you '+
         'fail, you are lost in time and space.');
  AddCard(GROUPG, EXP_AH, PLATLENG, 2,
         'You wander the frozen wastes. No encounter.');
  AddCard(GROUPG, EXP_AH, PLATLENG, 3,
         'Pass a Luck (-2) check to find some useful things among the bones. If so, draw 1 '+
         'Common Item and 1 Spell.');
  AddCard(GROUPG, EXP_AH, PLATLENG, 4,
         'The rickety bridge collapses as you cross it. Pass a Fight (-1) check to hang '+
         'on, finding a relic on the other side. Draw 1 Unique Item. If you fail, you '+
         'plummet into darkness. You are lost in time and space.');
  AddCard(GROUPG, EXP_AH, PLATLENG, 5,
         'Your mind and body are toughened by your experiences. Pass a Will (+0) [2] check '+
         'to draw l Skill.');
  AddCard(GROUPG, EXP_COTDP, PLATLENG, 6,
         'Your peril clears your mind. Pass a Will (+0) check to restore your Sanity to '+
         'its maximum value.');
  AddCard(GROUPG, EXP_COTDP, PLATLENG, 7,
         'A captive has been bound to a pole above the natives cooking fire. If you want '+
         'to try to free him, make a Fight (-3) check. If you fail, lose 2 Stamina. if you '+
         'pass, draw an Ally.');
  AddCard(GROUPG, EXP_COTDP, PLATLENG, 8,
         'The primitives are entranced by your equipment. You must discard one Common hem '+
         'worth at least S2 or lose 3 Stamina. If you pass a Will (+0) check, you convince '+
         'them to give you their idol in exchange: You may search the Unique Item deck for '+
         'the Obsidian Statue and take it.');
  AddCard(GROUPG, EXP_COTDP, PLATLENG, 9,
         'The icy winds tear at your flesh, and the plains seem endless. Pass a Fight (-1) '+
         'check or lose 1 Stamina and Pass a Will (-1) check or lose 1 Sanity. If Ithaqua '+
         'is the Ancient One the modifiers for these rolls are both reduced to -3.');
  AddCard(GROUPG, EXP_COTDP, PLATLENG, 10,
         'Something is here, frozen beneath the snow. Draw a monster from the cup and take '+
         'it as a monster trophy, even if it has the Endless ability.');
  AddCard(GROUPG, EXP_COTDP, PLATLENG, 11,
         'The icy weather has damaged one of your items beyond repair. Discard 1 Common or '+
         'Unique item of your choice. If you have no items, lose 1 Stamina.');
  AddCard(GROUPG, EXP_TBGOTW, PLATLENG, 12,
         'You must immediately fight Ithaqua! Since there is only one player in this '+
         'combat, you need one success to remove a doom token. If you reach  0 Stamina, '+
         'you are devoured. If you defeat Ithaqua, he disperses into icy wind and you may '+
         'escape to Arkham immediately. The gate to Plateua of Leng is sealed behind you, '+
         'and you may take it as a trophy. If Ithaqua is the Ancient One in play, do not '+
         'fill up his doom track before this combat; also, successes allow you to '+
         'temporarily flip over doom tokens to their elder sign sides instead of removing '+
         'them. Once the battle is over, regardless of the outcome, flip all the tokens on '+
         'Ithaquas doom track back to their doom token side and continue play.');
  AddCard(GROUPG, EXP_TBGOTW, RLYEH, 13,
         'As you stare out across the waters, a monster appears!');
  AddCard(GROUPG, EXP_TBGOTW, YUGGOTH, 14,
         'A horrid monster appears!');
  AddCard(GROUPR, EXP_AH, ABYSS, 1,
         'Pass a Luck (-1) check or you are faced with an enormous mountain with a strange '+
         'symbol carved into it, as if by the claw of a gigantic creature. The world swims '+
         'around you and you lose 3 Sanity.');
  AddCard(GROUPR, EXP_AH, ABYSS, 2,
         'You are disturbed by unsettling echoes. Pass a Sneak (-1) check to quiet them or '+
         'lose 2 Sanity.');
  AddCard(GROUPR, EXP_AH, ABYSS, 3,
         'The stone arch breaks! Pass a Speed (-1) check to dive out of the way or roll a '+
         'die and lose that much Stamina.');
  AddCard(GROUPR, EXP_AH, ABYSS, 4,
         'Starving, you consider eating some of the glowing mushrooms. If you decide to do '+
         'so, make a Luck (-1) check. If you fail, roll a die and lose that much Stamina. '+
         'If you succeed, roll a die and gain that much Stamina.');
  AddCard(GROUPR, EXP_AH, ABYSS, 5,
         'Pass a Speed (-1) check to avoid a monstrous mass. If you fail, you are lost in '+
         'time and space.');
  AddCard(GROUPR, EXP_COTDP, ABYSS, 6,
         'A monster appears!');
  AddCard(GROUPR, EXP_COTDP, ABYSS, 7,
         'This place is alive with malevolent intent. It likes it when you inflict pain '+
         'upon yourself. Discard any amount of Stamina, all at once; for each Stamina '+
         'token you discarded, pass a Will (-1) check to gain 2 Clue tokens.');
  AddCard(GROUPR, EXP_COTDP, ABYSS, 8,
         'The faces of those you have failed erupt from the earth around you, accusing, '+
         'pleading, hating. Pass a Lore (-1)|2| check to take the Psychic card. If you '+
         'roll only 1 success, you musttake either the Tainted or Harried card, and if you '+
         'roll no successes, you must take both the Harried and Tainted cards.');
  AddCard(GROUPR, EXP_COTDP, ABYSS, 9,
         'This place seduces you into madness with hints of escape. Discard any amount of '+
         'Sanity, all at once, for each Sanity token you discarded, pass a Fight (-1) '+
         'check to gain 2 Clue tokens.');
  AddCard(GROUPR, EXP_COTDP, ABYSS, 10,
         'It is the little things that comfort you in your darkest hour. You think fondly '+
         'of the mundane joys of your life. Regain 1 Sanity for each Common Item you '+
         'possess.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 1,
         'The obsidian door refuses to open.  Pass a Fight (-1) check or stay  here next '+
         'tum, struggling with it.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 2,
         'Pass a Speed (-1) check to grab the carving before it falls. Draw 1 Spell.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 3,
         'You push yourself to the limit. Roll 1 die for each point of Stamina you have. '+
         'Lose 1 Stamina for each die that does not roll a success. If you do not fall '+
         'unconscious, gain 1 Clue token for each die that rolled a success.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 4,
         'The humidity and heat is exhausting. Lose 1 Stamina.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 5,
         'The pinkish rays nearly get you. Pass a Sneak (+0) check or lose 2 Stamina.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 6,
         'The colors am blinding. Pass a Lore (-1) check or stay here next turn.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 7,
         'A lurking monster appears!');
  AddCard(GROUPR, EXP_AH, ANOTHER, 8,
         'There is nothing here but barren wastes. No encounter.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 9,
         'You sleep, fitfully, and awaken to the sound of your own voice, chanting '+
         'something. Make a Luck (-2) check. If you pass, you are able to retain what you '+
         'are saying. Draw l Spell and gain 2 Clue tokens. If you fail, the chant attracts '+
         'something unsavory. A monster appears!');
  AddCard(GROUPR, EXP_AH, ANOTHER, 10,
         'Pass a Luck (-1) check to discover a useful object in your Wanderings. Draw 1 '+
         'Unique Item.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 11,
         'Pass a Luck (-1) check to find a quiet spot to rest. Gain 2 Stamina and 2 '+
         'Sanity.');
  AddCard(GROUPR, EXP_AH, ANOTHER, 12,
         'The shadowy entity gives up the chase. Lose 1 Stamina from exhaustion.');
  AddCard(GROUPR, EXP_COTDP, ANOTHER, 13,
         'It was a diabolical trap, you suddenly realize...now that youre inside it! Make '+
         'a Lore (-1) check or you are delayed.');
  AddCard(GROUPR, EXP_COTDP, ANOTHER, 14,
         'A monster appears!');
  AddCard(GROUPR, EXP_COTDP, ANOTHER, 15,
         'What was that!? Make a Sneak (+3) check or you will find out as you are devoured '+
         'by it.');
  AddCard(GROUPR, EXP_COTDP, ANOTHER, 16,
         'You can hear it breathing...make a Will (-1) check lf fail, you scream in '+
         'terror, giving yourself away. Lose 1 Sanity and 2 Stamina.');
  AddCard(GROUPR, EXP_COTDP, ANOTHER, 17,
         'The chess game with the strange serpent seems to go on for days. Pass a Lore '+
         '(+2) check to gain $1 for each success you roll. If you fail, you are delayed.');
  AddCard(GROUPR, EXP_COTDP, ANOTHER, 18,
         'The mad scientist cackles as he pulls down on the lever of his machine. Pass a '+
         'Speed (+1) check to reach the giant gem that powers it in time and gain $4. If '+
         'you fail, you are thrown through a portal. Draw a Gate card. move to the Other '+
         'World listed first, and have another encounter there.');
  AddCard(GROUPR, EXP_TBGOTW, ANOTHER, 19,
         'A monster appears!');
  AddCard(GROUPR, EXP_TBGOTW, ANOTHER, 20,
         'A monster appears!');
  AddCard(GROUPR, EXP_TBGOTW, ANOTHER, 20,
         'You take careful notes of all of your experiences. You are certain they will '+
         'come in handy later. Gain I Clue token.');
  AddCard(GROUPR, EXP_TBGOTW, ANOTHER, 21,
         'On the horizon, you see the hazy silhouette of the Ancient One. Pass a Will (-2) '+
         'check or lose all your Sanity.');
  AddCard(GROUPR, EXP_TBGOTW, ANOTHER, 22,
         'You are not safe here. A monster appears!');
  AddCard(GROUPR, EXP_TBGOTW, ANOTHER, 23,
         'A strange rash has appeared on your skin, and youve developed a harsh, rattling '+
         'cough. Lose 1 Stamina.');
  AddCard(GROUPR, EXP_TBGOTW, ANOTHER, 24,
         'A mixed, half-dead explorer attacks you. Pass a Fight (+2) check to overcome '+
         'him. If you succeed, take 1 Common Item and lose 1 Sanity as you contemplate '+
         'this poor souls fate. If you fail, lose 1 Stamina.');
  AddCard(GROUPR, EXP_TBGOTW, ANOTHER, 25,
         'You find a small gem that you plan on selling when you get the chance. Gain $3.');
  AddCard(GROUPR, EXP_AH, CELEANO, 1,
         'A strangely dressed man accuses you of trying to steal his book. Make a Fight '+
         '(-2) check. If you succeed, you can take his book away. Take the first Tome in '+
         'the Unique Item deck. If you fail, lose I Stamina.');
  AddCard(GROUPR, EXP_AH, DREAMLAND, 1,
         'In the valley of Pnoth, where the dholes crawl and burrow nastily, you hear a '+
         'slithering among the mountains of bone. Make a Sneak (-1) check. If you fail, '+
         'you are devoured. If you pass, gain 3 Clue tokens and return immediately to '+
         'Arkham.');
  AddCard(GROUPR, EXP_AH, DREAMLAND, 2,
         'The ice bridge begins to crack, Pass a Luck (-1) check or fall into the icy '+
         'depths. If you fall, you are lost in time and space.');
  AddCard(GROUPR, EXP_AH, DREAMLAND, 3,
         'The Wind increases, and you feel your feet go numb. Pass a Fight (-1) check or '+
         'lose 2 Stamina.');
  AddCard(GROUPR, EXP_AH, DREAMLAND, 4,
         'The shantak claws at you as it swoops past overhead. Pass a Speed (-2) check or '+
         'lose 2 Stamina as its claws rake your chest.');
  AddCard(GROUPR, EXP_AH, DREAMLAND, 5,
         'While wandering the phosphorescent Woods, you are surrounded by hungry Zoogs! '+
         'Make a Luck (-2) check. If you pass, they take a liking to you and give you a '+
         'gourd of moon-tree Wine. Gain 1 Sanity and l Clue token. If you fail, the zoogs '+
         'close in around you, their teeth gleaming. You are lost in time and space.');
  AddCard(GROUPR, EXP_COTDP, DREAMLAND, 6,
         'Avalanche! Pass a Speed (-1) check or lose 3 Stamina.');
  AddCard(GROUPR, EXP_COTDP, DREAMLAND, 7,
         'Its lovely hero and perfect...so perfect you might stay forever. Make a Will '+
         '(+3) check. If you pass, gain 2 Sanity, If you fail, you are devoured.');
  AddCard(GROUPR, EXP_COTDP, DREAMLAND, 8,
         'From this strange mindscape you can see into the dreams of sleeping in Arkham. '+
         'Make a Speed (-1) check. If you pass, you catch the delicate wisps of their '+
         'thoughts, and gain 2 Clue tokens. If you fail, their slumbering minds lash out '+
         'at you, and you lose 2 Sanity.');
  AddCard(GROUPR, EXP_COTDP, DREAMLAND, 9,
         'You come upon the borderlands. Pass a Luck (-2) check to gain 1 Stamina and 1 '+
         'Sanity and return to Arkham. If you fail, move to the Plateau of Leng and your '+
         'turn ends.');
  AddCard(GROUPR, EXP_COTDP, DREAMLAND, 10,
         'You have inadvertently stumbled into a dangerous area. From the shadows, a '+
         'monster appears!');
  AddCard(GROUPR, EXP_COTDP, DREAMLAND, 11,
         'You find yourself reliving a moment in your past that you have always regretted, '+
         'only this time everything goes as well as you could over hope. Gain 2 Sanity.');
  AddCard(GROUPR, EXP_AH, GREATRACE, 1,
         'You feel other minds trying to contact you and warn you of something. Gain 2 '+
         'Clue tokens.');
  AddCard(GROUPR, EXP_AH, GREATRACE, 2,
         'The bells ring ten, eleven, then midnight. But what does time mean, here? If '+
         'your Sanity is 3 or less, you are lost in time and space.');
  AddCard(GROUPR, EXP_AH, GREATRACE, 3,
         'The conical creatures wish you to return an item to your own world. They have no '+
         'need of it Gain $3.');
  AddCard(GROUPR, EXP_AH, PLATLENG, 1,
         'The villagers leap around a bonfire on the hoary plain. Pass a Sneak (-1) check '+
         'or you are captured and subjected to terrible rites. Lose 3 Sanity and 3 '+
         'Stamina, then stay here next turn.');
  AddCard(GROUPR, EXP_AH, PLATLENG, 2,
         'The loathsome villagers send out their strongest warrior to fight you in unarmed '+
         'combat. Pass a Fight (-1) [2] check to defeat him and draw 1 Unique Item and '+
         'gain 1 Clue token. Otherwise lose l Sanity and 2 Stamina.');
  AddCard(GROUPR, EXP_AH, PLATLENG, 3,
         'A monster appears from the shadows!');
  AddCard(GROUPR, EXP_AH, PLATLENG, 4,
         'A vast stirring rumbles through the plateau. Pass a Sneak (+0) check or roll a '+
         'die and lose that much Stamina.');
  AddCard(GROUPR, EXP_AH, PLATLENG, 5,
         'You are taken to a prehistoric monastery, where a high priest in a yellow silken '+
         'mask questions you. Pass a Lore (-2) check to answer him to his satisfaction. '+
         'Gain your ?eedom and 1 Spell. Otherwise, you are lost in time and space.');
  AddCard(GROUPR, EXP_COTDP, PLATLENG, 6,
         'While you are climbing a high cliff, you begin to slip. Pass a Speed (-1) check '+
         'or crash down the mountain, losing 2 Stamina.');
  AddCard(GROUPR, EXP_COTDP, PLATLENG, 7,
         'From these alien heights, everything seems so clear...gain 1 Clue token, then '+
         'pass a Will (+1) check to snap out of your reverie and descend to a safe '+
         'elevation. If you fail, lose 1 Stamina and continue making the check until you '+
         'pass or are knocked unconscious. Each cheek after the first, the modifier '+
         'decreases by one (0 on the second check, -1 on the third, and so on).');
  AddCard(GROUPR, EXP_COTDP, PLATLENG, 8,
         'Through the haze and mist, you make out human forms and hurry toward them, '+
         'seeking rescue. Make a Luck (-2) check. If you pass, they are an expedition from '+
         'Miskatonic U. Gain 1 Stamina and 1 Sanity and return to Arkham. If you fail, '+
         'they lower their hoods and remove their goggles, revealing themselves as '+
         'something other than human! Lose 2 Sanity.');
  AddCard(GROUPR, EXP_COTDP, PLATLENG, 9,
         'Whether you are still on earth or not is impossible to say...it may be the wind '+
         'that threatens to sweep you into the sky, or it might be a lack or gravity! Make '+
         'a Fight (+0) check or your are lost in time and space.');
  AddCard(GROUPR, EXP_COTDP, PLATLENG, 10,
         'A monster appears from the shadows!');
  AddCard(GROUPR, EXP_COTDP, PLATLENG, 11,
         'One of the villagers has a prized possession of unknown origins. Pass a Sneak '+
         '(+1) check to successfully claim it as he sleeps. Draw I Common Item.');
  AddCard(GROUPR, EXP_TBGOTW, PLATLENG, 12,
         'You examine the frescoes and find them both informative and repellent. Make a '+
         'Lore (-2) check and gain I Clue token per success. After that, lose I Sanity.');
  AddCard(GROUPR, EXP_TBGOTW, PLATLENG, 13,
         'You must immediately fight Ithaqua! Since there is only one player in this '+
         'combat, you need one success to remove a doom token. If you reach  0 Stamina, '+
         'you are devoured. If you defeat Ithaqua, he disperses into icy wind and you may '+
         'escape to Arkham immediately. The gate to Plateua of Leng is sealed behind you, '+
         'and you may take it as a trophy. If Ithaqua is the Ancient One in play, do not '+
         'fill up his doom track before this combat; also, successes allow you to '+
         'temporarily flip over doom tokens to their elder sign sides instead of removing '+
         'them. Once the battle is over, regardless of the outcome, flip all the tokens on '+
         'Ithaquas doom track back to their doom token side and continue play.');
  AddCard(GROUPR, EXP_AH, RLYEH, 1,
         'Pass a Speed (-1) check or you slip and slide down a barnacled surface, slashing '+
         'your skin to ribbons. Lose 3 Stamina.');
  AddCard(GROUPR, EXP_AH, RLYEH, 2,
         'A slimy monster appears!');
  AddCard(GROUPR, EXP_AH, RLYEH, 3,
         'Hurricane Winds smash you against the cyclopean stones. Pass a Fight (-1) check '+
         'or lose 3 Stamina.');
  AddCard(GROUPR, EXP_AH, RLYEH, 4,
         'Slip on Wet stones and slide into a pit. Pass a Luck (+0) check to climb out. If '+
         'you fail, lose 1 Sanity and stay here next turn.');
  AddCard(GROUPR, EXP_AH, RLYEH, 5,
         'You become tangled in the damp seaweed. Pass a Luck (-1) check to pull free '+
         'before something finds you while you`re helpless. If you fail, roll a die and '+
         'lose that much Stamina.');
  AddCard(GROUPR, EXP_COTDP, RLYEH, 6,
         'The shadow tries to force its way between your lips. Pass a Fight (-2) check or '+
         'lose 2 Stamina and stay here next turn.');
  AddCard(GROUPR, EXP_COTDP, RLYEH, 7,
         'A miracle! A boat appears, hailing from the nearby island of Ponape. Pass a Will '+
         '(-3) check to convince them to take you back to the normal world. If you pass, '+
         'immediately return Arkham.');
  AddCard(GROUPR, EXP_COTDP, RLYEH, 8,
         'Something horrid and vast. a creature all of green and tentacles yet horribly '+
         'human, lies in state in the mausoleum before you. Creatures cast from the same '+
         'mold, yet merely man-sized, swarm over it in the hundreds. Gain 2 Clue tokens '+
         'and lose 2 Sanity, then pass a Sneak (-1) check. If you fail, a monster appears!');
  AddCard(GROUPR, EXP_COTDP, RLYEH, 9,
         'As you stumble across this inhuman isle, you feel a rumbling beneath your feet. '+
         'It has begun to sink beneath the waves! Pass a Speed (-2) check or you are lost '+
         'in time and space. If you pass, immediately return to Arkham.');
  AddCard(GROUPR, EXP_COTDP, RLYEH, 10,
         'You must immediately fight Cthulhu! Since there is only one player in this '+
         'combat, you need one success to remove a doom token. If you reach 0 Sanity or 0 '+
         'Stamina, you are devoured. If you defeat Cthulhu, he retreats back into slumber '+
         'and you may escape to Arkham immediately. The gate to Rlyeh is sealed behind '+
         'you, and you may take it as a trophy. If Cthulhu is the Ancient One in play, do '+
         'not fill up his doom track before this combat; also, successes allow you to '+
         'temporarily flip over doom tokens to their elder sign sides instead of removing '+
         'them. Once the battle is over, regardless of the outcome, flip all the tokens on '+
         'Cthulhus doom track back to their doom token side and continue play.');
  AddCard(GROUPR, EXP_COTDP, RLYEH, 11,
         'You hear a monstrous roar behind you and a voice within tells you to am and not '+
         'look back. Pass a Will (-2) check to do exactly that. Otherwise you give into '+
         'temptation and glance back at the creature, losing 2 Sanity and becoming lost in '+
         'time end space.');
  AddCard(GROUPR, EXP_AH, YUGGOTH, 1,
         'You might be smarter than the Mi-Go realize. Theyve left you alone with some '+
         'alien documents. Pass a Lore (-2) check to gain a Spell.');
  AddCard(GROUPY, EXP_AH, ABYSS, 1,
         'A monster appears!');
  AddCard(GROUPY, EXP_AH, ABYSS, 2,
         'The darkness claws at your mind, obscuring what was once so clear to you. Make a '+
         'Will (-1) check. For each success you roll, you may keep 1 Clue token, losing '+
         'the others.');
  AddCard(GROUPY, EXP_AH, ABYSS, 3,
         'You can feel bleak despair taking over your mind. Make a Will (-2) check. If you '+
         'pass, regain 1 Sanity. If you do not, you leap blindly into the yawning darkness '+
         'and are last in time and space.');
  AddCard(GROUPY, EXP_AH, ANOTHER, 1,
         'A monster appears!');
  AddCard(GROUPY, EXP_AH, ANOTHER, 2,
         'You are not safe here. A monster appears!');
  AddCard(GROUPY, EXP_AH, ANOTHER, 3,
         'A monster appears from the shadows!');
  AddCard(GROUPY, EXP_AH, ANOTHER, 4,
         'A ripple in the air passes over you. Pass a Lore (-1) check or lose 1 Spell of '+
         'your choice as it is burned from your mind.');
  AddCard(GROUPY, EXP_AH, ANOTHER, 5,
         'Your mind is flooded with knowledge. Make a Lore (-2) check. If you pass it, '+
         'draw l Spell, but lose l Sanity.');
  AddCard(GROUPY, EXP_AH, ANOTHER, 6,
         'Suddenly you notice something that you had previously missed. Gain l Clue token.');
  AddCard(GROUPY, EXP_AH, ANOTHER, 7,
         'Suddenly, the things you`ve seen make sense! Gain 1 Clue token.');
  AddCard(GROUPY, EXP_AH, ANOTHER, 8,
         'You stare into the face of madness. Roll 1 die for each point of Sanity you '+
         'have. Lose 1 Sanity for each die that does not roll a success. If you do not go '+
         'insane, gain 1 Clue token for each die that rolled a success.');
  AddCard(GROUPY, EXP_AH, ANOTHER, 9,
         'A glimmer of gold catches your eye. Gain $2.');
  AddCard(GROUPY, EXP_AH, ANOTHER, 10,
         'Time and space bend around you. Make a Luck (-1) check. If you pass, return to '+
         'Arkham. If you fail, stay here next turn.');
  AddCard(GROUPY, EXP_AH, ANOTHER, 11,
         'The sky is spinning. Pass a Will (-2) check or pass out and stay here next turn.');
  AddCard(GROUPY, EXP_AH, ANOTHER, 12,
         'The unending blackness terrifies you. Pass a Will (-1) check or lose 1 Sanity '+
         'and 1 Stamina from fear and exhaustion.');
  AddCard(GROUPY, EXP_COTDP, ANOTHER, 13,
         'The cultists thrust you forward, and the God of the Bloody Tongue surprises you! '+
         'You gain a +1 to all skill checks against this monster for each Unique Item or '+
         'Exhibit Item you have.');
  AddCard(GROUPY, EXP_COTDP, ANOTHER, 14,
         'The Bloated Woman makes you an offer. Lose 1 Sanity, then you may discard any '+
         'amount of money, all at once, then draw a number of cards from the Unique Item '+
         'deck equal to the total amount of money discarded. You may take one card from '+
         'among those drawn with a value equal to or less than the amount of money '+
         'discarded, then discard the rest.');
  AddCard(GROUPY, EXP_COTDP, ANOTHER, 15,
         'The Black Man lays his book before you. If you wish to open the book, pass a '+
         'Luck (-2) check to gain 5 Clue tokens. If you fail, you are devoured.');
  AddCard(GROUPY, EXP_COTDP, ANOTHER, 16,
         'Nephren-Ka places your soul upon the Balance of Thoth, and finds you lacking. '+
         'First discard Stamina or Sanity, whichever is higher, until your Stamina and '+
         'Sanity are equal. Then you are surprised by a monster. If you defeat it, you may '+
         'draw 1 Exhibit Item.');
  AddCard(GROUPY, EXP_COTDP, ANOTHER, 17,
         'You inadvertently summon the Haunter of the Dark to carry you through the '+
         'void.You must lose Sanity equal to your current Stamina, or Stamina equal to '+
         'your current Sanity, but gain 2 Clue tokens for each monster in the Sky.');
  AddCard(GROUPY, EXP_COTDP, ANOTHER, 18,
         '"Mr. Skins the name, investigatins my game," he says. with a friendly smile. But '+
         'theres something about him that makes you feel like a helpless child before a '+
         'ravenous beast. If you agree to let him come along, his form and face seem to '+
         'shift...you may take any Ally of your choice, but you lose 2 Stamina and 2 '+
         'Sanity.');
  AddCard(GROUPY, EXP_TBGOTW, ANOTHER, 19,
         'A monster appears!');
  AddCard(GROUPY, EXP_TBGOTW, ANOTHER, 20,
         'A monster appears!');
  AddCard(GROUPY, EXP_TBGOTW, ANOTHER, 21,
         'A revolting monster appears!');
  AddCard(GROUPY, EXP_TBGOTW, ANOTHER, 22,
         'In the dark, you stumble into a deep hole. Looking up, you see a gravestone '+
         'bearing your name. Pass a Speed (-2) check to scramble out or lose 2 Sanity and '+
         'be delayed.');
  AddCard(GROUPY, EXP_TBGOTW, ANOTHER, 23,
         'A wounded beast snarls at you, but it cant move. You dont think its going to '+
         'live much longer. If you want to wait around, you are delayed, but you may draw '+
         'a monster from the cup and take it as a monster trophy, even if it has the '+
         'Endless ability.');
  AddCard(GROUPY, EXP_TBGOTW, ANOTHER, 24,
         'A mysterious woman warns you that you would be able to see all that you need to '+
         'know if your mind were not clouded by the unnatural. Discard 2 Spells to gain 5 '+
         'Clue tokens. If you cant or choose not to, gain 1 Sanity.');
  AddCard(GROUPY, EXP_TBGOTW, ANOTHER, 25,
         'Your path ends at two identical doors. Make a Luck (+0) check. If you succeed, '+
         'return to Arkham. If not, you are lost in time and space.');
  AddCard(GROUPY, EXP_TBGOTW, ANOTHER, 26,
         'You hear the call of a hunting creature in the sky above. Pass a Sneak (-2) '+
         'check or you become its prey and lose 1 Stamina.');
  AddCard(GROUPY, EXP_AH, CELEANO, 1,
         'A lurking monster appears!');
  AddCard(GROUPY, EXP_AH, DREAMLAND, 1,
         'The meeping of the ghouls in the tunnels echoes in your ears. Pass a Will (-2) '+
         'check or lose 2 Sanity.');
  AddCard(GROUPY, EXP_AH, DREAMLAND, 2,
         'You see the mountains move. Lose 1 Sanity from terror.');
  AddCard(GROUPY, EXP_AH, DREAMLAND, 3,
         'The stone face reveals to you one of the deepest secrets of the Dreamlands, Pass '+
         'a Lore (-1) [2] check to gain 4 Clue tokens. If you fail the check, however, the '+
         'sight claims your last shred of sanity. Lose all your Sanity.');
  AddCard(GROUPY, EXP_AH, DREAMLAND, 4,
         'Pass a Luck (+0) check or stumble into a spider`s web. Lose 2 Sanity and stay '+
         'here next turn while struggling to get free.');
  AddCard(GROUPY, EXP_AH, DREAMLAND, 5,
         'The golden city of your dreams is threatening to become an obsession. Pass a '+
         'Luck (-1) check or stay here next turn to hunt for it.');
  AddCard(GROUPY, EXP_COTDP, DREAMLAND, 6,
         'You come across an abandoned onyx quarry whose chiselled vacancies are so vast '+
         'that it staggers your mind. Pass a Lore (-1) check to avoid awakening anything '+
         'here, or else lose 3 Sanity.');
  AddCard(GROUPY, EXP_COTDP, DREAMLAND, 7,
         'Have an encounter at a location of your choice in Arkham, then return to the '+
         'Dreamlands.');
  AddCard(GROUPY, EXP_COTDP, DREAMLAND, 8,
         'All things of which humanity dreams are here. Pass a Luck (+0) check to gain S1 '+
         'per success rolled. If you fail, lose 1 Sanity.');
  AddCard(GROUPY, EXP_COTDP, DREAMLAND, 9,
         'Make a Will (-1) check. If you pass, you view the dreams around you with an '+
         'objective eye: Gain 2 Clue tokens. If you fail, the dreams we not so easily '+
         'forgotten: Take the Harried card.');
  AddCard(GROUPY, EXP_COTDP, DREAMLAND, 10,
         'You have inadvertently stumbled into a dangerous area. From the shadows, a '+
         'monster appears!');
  AddCard(GROUPY, EXP_COTDP, DREAMLAND, 11,
         'Time passes differently in the Dreamlands, and youve needed to learn a few '+
         'things to survive. Gain 1 Skill.');
  AddCard(GROUPY, EXP_TBGOTW, DREAMLAND, 12,
         'Looking over the Lake of Yath and taking in the fragrant air, you find yourself '+
         'comforted. Gain 1 Sanity.');
  AddCard(GROUPY, EXP_AH, GREATRACE, 1,
         'The buzzing language of your captors begins to make sense to you. Gain 2 Clue '+
         'tokens. Then you must pass a Luck (-1) check to avoid hearing about the origins '+
         'of mankind and thereby losing 2 Sanity.');
  AddCard(GROUPY, EXP_AH, GREATRACE, 2,
         'Glancing behind you, you see that the beasts are still chasing you. Pass a Speed '+
         '(-1) check or be lost in time and space.');
  AddCard(GROUPY, EXP_AH, GREATRACE, 3,
         'The odd plant has you in its clutches. Pass a Fight (-1) check to break free. If '+
         'you fail, lose l Stamina and l Sanity as it partially digests you.');
  AddCard(GROUPY, EXP_AH, GREATRACE, 4,
         'In a flash of insight, you realize the purpose of the bladed artifact. '+
         'Shivering, you put it back where you found it. Lose 1 Sanity but gain 1 Clue '+
         'token.');
  AddCard(GROUPY, EXP_AH, GREATRACE, 5,
         'The hideous Whistling fills your ears. Pass a Will (-1) check or lose 2 Sanity.');
  AddCard(GROUPY, EXP_COTDP, GREATRACE, 6,
         'You wander the empty streets of the city. No encounter.');
  AddCard(GROUPY, EXP_COTDP, GREATRACE, 7,
         'A monster erupts from the ground and surprises you! You suffer a -2 to all '+
         'checks against this monster, but you may discard Spells during this combat as if '+
         'they were Clue tokens.');
  AddCard(GROUPY, EXP_COTDP, GREATRACE, 8,
         'Strange instruments of metal and glass surround you. Make a Will (-1) check. If '+
         'you fail, you are delayed. If you pass, you may discard any number of Clue '+
         'tokens, all at once, then draw a number of cards from the Unique Item or Exhibit '+
         'Item deck equal to the total number of Clue tokens discarded. You may take one '+
         'card from among those drawn, then discard the rest.');
  AddCard(GROUPY, EXP_COTDP, GREATRACE, 9,
         'You may take 1 Spell, but must pass a Will (-1) check or lose 1 Sanity.');
  AddCard(GROUPY, EXP_COTDP, GREATRACE, 10,
         'These creatures dont want you to leave just yet. Pass a Sneak (-3) check or be '+
         'delayed.');
  AddCard(GROUPY, EXP_AH, RLYEH, 1,
         'The city is filled with unnerving alien angles. Pass a Speed (-1) check to avoid '+
         'touching them or lose l Sanity.');
  AddCard(GROUPY, EXP_AH, RLYEH, 2,
         'You trip over a stone outcropping that shouldn`t be there. Pass a Speed (-1) '+
         'check or you are lost in time and space.');
  AddCard(GROUPY, EXP_AH, RLYEH, 3,
         'You run for the boat. Pass a Speed (-1) [2] check to reach it in time. If you '+
         'do, you escape With vital information. Gain 5 Clue tokens. If you fail, stay '+
         'here next turn, hiding from your pursuer.');
  AddCard(GROUPY, EXP_AH, RLYEH, 4,
         'A horrible visage captures your gaze. Pass a Will (+0) check to look away or '+
         'lose 1 Stamina and stay here next turn.');
  AddCard(GROUPY, EXP_AH, RLYEH, 5,
         'The stink of this place is unbearable. Pass a Wiil (-1) check or lose 1 Stamina, '+
         '1 Sanity, and your lunch.');
  AddCard(GROUPY, EXP_COTDP, RLYEH, 6,
         'The night stars change and the brazen temple doors open, pouring forth a vast, '+
         'black corpulence. Roll a die and lose that much Sanity.');
  AddCard(GROUPY, EXP_COTDP, RLYEH, 7,
         'The child is wracked with pain and begins to mutate. Pass a Speed (-1) check to '+
         'gain Sanity equal to the number of successes rolled. If you fail, a monster '+
         'surprises you and you suffer -2 to all Horror checks against it!');
  AddCard(GROUPY, EXP_COTDP, RLYEH, 8,
         'The bodies of the drowned clutch at your ankles. Make a Speed (-2) check or lose '+
         '1 Stamina.');
  AddCard(GROUPY, EXP_COTDP, RLYEH, 9,
         'You find a humaYou find a human corpse...which then sits up! Make a Lore (+1) '+
         'check. If you V. fail, lose 2 Sanity. If you pass, you realize that it is a '+
         'zombie and may draw an Ally. Place tokens on it equal to the number of successes '+
         'rolled. Discard 1 token from it during each Upkeep Phase. If it has no tokens at '+
         'the beginning of the Upkeep Phase, discard the Ally instead.n corpse...which '+
         'then sits up! Make a Lore (+1) check. If you V. fail, lose 2 Sanity. If you '+
         'pass, you realize that it is a zombie and may draw an Ally. Place tokens on it '+
         'equal to the number of successes rolled. Discard 1 token from it during each '+
         'Upkeep Phase. If it has no tokens at the beginning of the Upkeep Phase, diseard '+
         'the Ally instead.');
  AddCard(GROUPY, EXP_COTDP, RLYEH, 10,
         'You must immediately fight Cthulhu! Since there is only one player in this '+
         'combat, you need one success to remove a doom token. If you reach 0 Sanity or 0 '+
         'Stamina, you are devoured. If you defeat Cthulhu, he retreats back into slumber '+
         'and you may escape to Arkham immediately. The gate to Rlyeh is sealed behind '+
         'you, and you may take it as a trophy. If Cthulhu is the Ancient One in play, do '+
         'not fill up his doom track before this combat; also, successes allow you to '+
         'temporarily flip over doom tokens to their elder sign sides instead of removing '+
         'them. Once the battle is over, regardless of the outcome, flip all the tokens on '+
         'Cthulhus doom track back to their doom token side and continue play.');
  AddCard(GROUPY, EXP_COTDP, RLYEH, 11,
         'You stand before the massive citadel and feel baleful forces inspecting you. '+
         'Make a Lore (-2) check. If you roll no successes you have been Cursed!');
  AddCard(GROUPY, EXP_TBGOTW, RLYEH, 12,
         'To your horror, the unearthly geometry of the place is starting to make sense. '+
         'Take a number of Clue tokens equal to the difference between your current Sanity '+
         'score and your maximum.');
  AddCard(GROUPY, EXP_AH, YUGGOTH, 1,
         'The cylindered head mocks your hopes. "You`l1 never return home!" it cackles. '+
         'Pass a Will (-2) check or lose 2 Sanity.');
  AddCard(GROUPY, EXP_AH, YUGGOTH, 2,
         'A strange creature stares at you with burning eyes. It is as if its gaze were '+
         'stealing your soul. Pass a Luck (-1) check or roll a die and subtract 2 from it '+
         '(minimum O), then lose that much Stamina and Sanity.');
  AddCard(GROUPY, EXP_AH, YUGGOTH, 3,
         'Fear grabs you as the buzzing entities approach. Pass a Will (-1) check or lose '+
         '2 Sanity.');
  AddCard(GROUPY, EXP_AH, YUGGOTH, 4,
         'Breathing hard, you stay huddled against the rock until the sounds of pursuit '+
         'fade into the distance. No encounter.');
  AddCard(GROUPY, EXP_AH, YUGGOTH, 5,
         'Your only hope is to steal a byakhee and some space mead! Pass a Sneak (-2) '+
         'check to escape. Return to Arkham and gain 2 Clue tokens. If you fail, you are '+
         'lost in time and space.');
  AddCard(GROUPY, EXP_COTDP, YUGGOTH, 6,
         'An alien mind forces its way into your body. Pass a Luck (-2) check to guess a '+
         'Way to drive it out, gaining 2 Clue tokens in the process, or else stay here '+
         'next turn, serving as its host body.');
  AddCard(GROUPY, EXP_COTDP, YUGGOTH, 7,
         '"Help me!" The voice comes from a cylinder containing a human brain! You may '+
         'search the Skill deck for the Lore card. If you take it, you lose 2 Sanity.');
  AddCard(GROUPY, EXP_COTDP, YUGGOTH, 8,
         'The Mi-Go offer immortality...of a sort. If you accept, you are devoured, except '+
         'that you keep all of your Spells, Skills, and Clue tokens, to be used with your '+
         'next investigator. Then close and seal a gate to Yuggoth, if one is open.');
  AddCard(GROUPY, EXP_COTDP, YUGGOTH, 9,
         'You are swept away by a river of some dark substance. Make a Fight (-1) check or '+
         'you are lost in time and space.');
  AddCard(GROUPY, EXP_COTDP, YUGGOTH, 10,
         'You must immediately fight Shug-Niggurath! Since there is only one player in '+
         'this combat, you need one success to remove a doom token. If you run out of '+
         'monster trophies, you are devoured. If you defeat Shub-Niggurath, she retreats '+
         'into the void and you may escape to Arkham immediately. The gate to Yuggoth is '+
         'sealed behind you, and you may take it as a trophy. If Shub-Niggurath is the '+
         'Ancient One in play, do not fill up her doom track before this combat; also, '+
         'successes allow you to temporarily flip over doom tokens to their elder sign '+
         'sides instead of removing them. Once the battle is over, regardless of the '+
         'outcome, flip all the tokens on Shub-Nigguraths doom track back to their doom '+
         'token side and continue play.');
  AddCard(GROUPY, EXP_COTDP, YUGGOTH, 11,
         'You see the faint glimmer of an object poised on a precipice. Pass a Fight (-2) '+
         'check to climb your way out to it safely. If you succeed, draw one Unique Item. '+
         'If you fail, the precipice crumbles and you are last in time and space.');
  AddCard(GROUPY, EXP_TBGOTW, YUGGOTH, 12,
         'The sun is so far away. Everything seems hopeless. Lose 1 Sanity.');
  AddCard(GROUPB, EXP_TKIY, ABYSS, 41,
         'A subterranean monster appears!');
  AddCard(GROUPB, EXP_TKIY, ABYSS, 42,
         'The darkness here is absolute. Pass a Will (-1) check or lose 1 Sanity.');
  AddCard(GROUPB, EXP_TKIY, ABYSS, 43,
         'The phosphorescent fungus make this cavern appealing to rest a moment... but the '+
         'toxic spores they emit prove dangerous! Make a Will (-1) [2] check or lose 2 '+
         'Sanity and 2 Stamina.');
  AddCard(GROUPR, EXP_TKIY, ABYSS, 44,
         'You climb a long stone stair towards Sarkomand. Make a Fight (+0) [2] check. If '+
         'you pass, move to the Dreamlands. If you fail, you become exhausted and must '+
         'stay here next turn.');
  AddCard(GROUPR, EXP_TKIY, ABYSS, 45,
         'You grope blindly in the darkness, desperately avoiding razor-sharp shards of '+
         'stone. Make a Luck (+1) check. Lose 4 Stamina, reduced by 1 per success.');
  AddCard(GROUPR, EXP_TKIY, ABYSS, 46,
         'You stumble down a twisting passage and a monster appears!');
  AddCard(GROUPB, EXP_TKIY, CELEANO, 41,
         'An endless bookshelf! Make a Luck (+1) check and consult the chart below: '+
         '[Successes:] [0-1) Nothing happens.] [2) Gain 1 Spell.] [3+) Search the Unique '+
         'Item deck and take the first Tome you find.]');
  AddCard(GROUPB, EXP_TKIY, CELEANO, 42,
         'Make a Lore (+0) [2] check to decipher these cryptic runes and find a way out! '+
         'If you fail, you are delayed.');
  AddCard(GROUPB, EXP_TKIY, CELEANO, 43,
         'Make a Luck (-1) check to find a scroll containing 1 Spell.');
  AddCard(GROUPG, EXP_TKIY, CELEANO, 44,
         'The creature here demands tribute. Add to the library by discarding 1 Spell and '+
         'be rewarded with 2 Clue tokens. If you do not, the creatures anger costs you 1 '+
         'Sanity and 1 Stamina.');
  AddCard(GROUPG, EXP_TKIY, CELEANO, 45,
         'The creature that acts as librarian here is asleep. Make a Sneak (-1) check to '+
         'pilfer important documents and gain 2 Clue tokens.');
  AddCard(GROUPG, EXP_TKIY, CELEANO, 46,
         'You find a book in a familiar language. Make a Luck (-1) check. If you pass, the '+
         'book is useful! Gain 1 Skill. If you fail, its useless and poorly-written.');
  AddCard(GROUPG, EXP_TKIY, GREATRACE, 41,
         'If you can just climb this bizarre structure, you think you can reach your '+
         'destination! Make a Fight (-2) check to return to Arkham. If you fail, stay here '+
         'next turn.');
  AddCard(GROUPG, EXP_TKIY, GREATRACE, 42,
         'Its a horrible collection of impossible things! Roll 3 dice. For each success, '+
         'gain 1 Clue token. For each die that is not a success, lose 1 Sanity.');
  AddCard(GROUPG, EXP_TKIY, GREATRACE, 43,
         'Somewhere in this room is something valuable! Make a Lore (-2) check to find it '+
         'and draw 1 Unique Item. If you fail, lose 1 Sanity and 1 Stamina from what you '+
         'do find.');
  AddCard(GROUPY, EXP_TKIY, GREATRACE, 44,
         'The creature exchanges its mind with yours for a time. You may choose to lose 1 '+
         'or more Sanity, gaining an equal number of Clue tokens.');
  AddCard(GROUPY, EXP_TKIY, GREATRACE, 45,
         'The thing that enters your mind is particularly intersted in your Spells. For '+
         'each Spell you have, gain 1 Clue token but lose 1 Sanity.');
  AddCard(GROUPY, EXP_TKIY, GREATRACE, 46,
         'Your mind is not your own! Make a Will (-1) [2] check to endure the experience. '+
         'If you pass, gain 2 Clue tokens when you are restored to your body. If you fail, '+
         'the mind-wipe is successful. Lose 2 Sanity, less 1 for each Clue token you '+
         'discard.');
  AddCard(GROUPB, EXP_TKIY, ANOTHER, 41,
         'A strange serpent-face person in a hooded robe speaks at you in an ancient '+
         'tongue. Make a Lore (-2) check to decipher his words and gain 1 Clue token. If '+
         'you fail, he bites you, disgusted, and leaves. Lose 1 Stamina.');
  AddCard(GROUPB, EXP_TKIY, ANOTHER, 42,
         'A terrifying monster appears!');
  AddCard(GROUPB, EXP_TKIY, ANOTHER, 43,
         'It takes you a moment to realize that the horrible screeching noise consists of '+
         'English words spoken by something monstrous! Lose 1 Sanity, but gain 1 Clue '+
         'token.');
  AddCard(GROUPR, EXP_TKIY, ANOTHER, 44,
         'Make a Fight (-2) check to scale that sheer cliff. If you succeed, the view from '+
         'the top grants you 1 Clue token. If you fail, lose 1 Stamina.');
  AddCard(GROUPR, EXP_TKIY, ANOTHER, 45,
         'Make a Luck (+0) check and consult the chart below. [Successes:] [0-1) Thousands '+
         'of minute creatures! Lose 1 Stamina] [2) You find $2 worth of gold ingots] [3+) '+
         'Anywhere is better than here. Return to Arkham.]');
  AddCard(GROUPR, EXP_TKIY, ANOTHER, 46,
         'Make a Luck (-2) check to come across a Unique Item!');
  AddCard(GROUPB, EXP_TKIY, ANOTHER, 47,
         'Make a Luck (-2) check to make it through the twisted forest. If you pass, you '+
         'find $3 worth of precious baubles! If you fail, you are delayed.');
  AddCard(GROUPB, EXP_TKIY, ANOTHER, 48,
         'Make a Speed (-1) check to run for safety and return to Arkham. If you fail, you '+
         'are caught and are delayed.');
  AddCard(GROUPB, EXP_TKIY, ANOTHER, 49,
         'Nothing but emptiness. No encounter.');
  AddCard(GROUPG, EXP_TLATT, ANOTHER, 50,
         'One glimpse at the sky and things fall into place for you. Gain 1 Clue token.');
  AddCard(GROUPG, EXP_TLATT, ANOTHER, 51,
         'Silence and warmth, for a change. Gain 1 Sanity.');
  AddCard(GROUPG, EXP_TLATT, ANOTHER, 52,
         'Something small scurries away from you, carrying 1 of your Common Items with it.');
  AddCard(GROUPG, EXP_TLATT, ANOTHER, 53,
         'The bruising winds make movement difficult. Lose 1 Stamina.');
  AddCard(GROUPG, EXP_TLATT, ANOTHER, 54,
         'The door slams shut behind you. You are in total blackness. Pass a Luck (-2) '+
         'check, otherwise you are delayed.');
  AddCard(GROUPG, EXP_TLATT, ANOTHER, 55,
         'The floor is crumbling beneath you! Make a Speed (-1) check or be lost in time '+
         'and space.');
  AddCard(GROUPY, EXP_TLATT, ANOTHER, 56,
         'The ground is giving way! Pass a Speed (-1) check to escape; otherwise you are '+
         'delayed.');
  AddCard(GROUPY, EXP_TLATT, ANOTHER, 57,
         'There are two flasks here. You may drink one to gain 1 Sanity and lose 1 Stamina '+
         'or drink the other to gain 1 Stamina and lose 1 Sanity.');
  AddCard(GROUPY, EXP_TLATT, ANOTHER, 58,
         'These loathsome beings are certainly not friendly. Make a Sneak (-1) check to '+
         'avoid them and gain 1 Clue token. If you fail, lose 1 Sanity and 1 Stamina as '+
         'you flee!');
  AddCard(GROUPY, EXP_TLATT, ANOTHER, 59,
         'What was that? Lose 1 Sanity.');
  AddCard(GROUPY, EXP_TLATT, ANOTHER, 60,
         'Whats that? Another Gate? Hurry! Make a Speed (-1) check. If you fail, you are '+
         'lost in time and space. If you pass with 1 success, nothing happens. If you pass '+
         'with 2 or more successes, return to Arkham.');
  AddCard(GROUPY, EXP_TLATT, ANOTHER, 61,
         'Whats that behind you!? A monster appears.');
  AddCard(GROUPR, EXP_TLATT, ANOTHER, 62,
         'You find a $5 bill on the ground here, with no possible explanation for its '+
         'presence. Gain $5.');
  AddCard(GROUPR, EXP_TLATT, ANOTHER, 63,
         'You pass the night in animated conversation with an old man sucking on a clay '+
         'pipe. When you awaken, the man is gone without a trace, but you do gain 1 Clue '+
         'token from his wisdom.');
  AddCard(GROUPR, EXP_TLATT, ANOTHER, 64,
         'Youve never seen nor experienced anything so awful. Roll four dice. For each die '+
         'that is not a success, lose 1 Sanity or 1 Stamina (your choice).');
  AddCard(GROUPG, EXP_TKIY, PLATLENG, 41,
         'It seems you are in an entire forest of webs. Make a Sneak (-2) check to avoid '+
         'getting ensnared. If you fail, you are lost in time and space.');
  AddCard(GROUPG, EXP_TKIY, PLATLENG, 42,
         'Its cold, windy, and dangerous here. Fortunately, theres a ship headed for '+
         'warmer climes. If you like, you may move to the Dreamlands.');
  AddCard(GROUPG, EXP_TKIY, PLATLENG, 43,
         'Run! Run for your life! Make a Speed (-1) check and lose 3 Stamina, less 1 per '+
         'success.');
  AddCard(GROUPR, EXP_TKIY, PLATLENG, 44,
         'The road divides here. Make a Lore (-2) check to decipher the signposts. If you '+
         'succeed and are in the first area of the Plateau of Leng, move to the second '+
         'area. If you are in the second area, return to Arkham. If you fail, you are lost '+
         'in time and space.');
  AddCard(GROUPR, EXP_TKIY, PLATLENG, 45,
         'The wide-mouthed men of Leng are curious about your exotic wonders. You may '+
         'attempt to barter with them. Discard 1 Common Item and make a Will (+0) [2] '+
         'check. If you pass, draw a Unique item. If you fail, gain $2.');
  AddCard(GROUPR, EXP_TKIY, PLATLENG, 46,
         'You find yourself sliding down a shear sheet of ice! Make a Luck (-2) check. If '+
         'you pass, you land on 1 Unique Item. If you fail, lose 2 Stamina.');
  AddCard(GROUPR, EXP_TKIY, RLYEH, 41,
         '"Ia! Ia! Cthulhu Fhtagn!" Where is that chanting coming from? Make a Luck (-2) '+
         'check. If you succeed, gain 2 Clue tokens as you follow the robed figures. If '+
         'you fail, lose 2 Sanity and 2 Stamina.');
  AddCard(GROUPR, EXP_TKIY, RLYEH, 42,
         'As you turn a corner, a leering idol startles you. Pass a Will (-2) check or '+
         'jump back and fall down a steep slope. If you fail, you lose 2 Stamina and are '+
         'delayed.');
  AddCard(GROUPR, EXP_TKIY, RLYEH, 43,
         'Only brute strength will get you out of this stone trap. Make a Fight (-2) check '+
         'or you are delayed.');
  AddCard(GROUPY, EXP_TKIY, RLYEH, 44,
         'Terrible stone edifices loom above you, horrifying in their non- Euclidean '+
         'splendor. Make a Will (-1) check and lose 2 Sanity, less 1 for every success.');
  AddCard(GROUPY, EXP_TKIY, RLYEH, 45,
         'The earth shakes-- is the city sinking? Make a Luck (-1) [2] check to escape. If '+
         'you fail, you are lost in time and space.');
  AddCard(GROUPY, EXP_TKIY, RLYEH, 46,
         'The sonorous wind of a sleeping leviathan echoes around you. You rest, but you '+
         'do not rest easy. Gain 1 Stamina, but lose 1 Sanity.');
  AddCard(GROUPB, EXP_TKIY, DREAMLAND, 41,
         'A bored cat challenges you to a riddle contest. Make a Lore (+0) [2] check. If '+
         'you pass, the cat leads you to a cache containing 1 Unique Item. If you fail, '+
         'you are delayed.');
  AddCard(GROUPB, EXP_TKIY, DREAMLAND, 42,
         'A squat little creature offers to serve as your guide. Make a Luck (+1) check '+
         'and consult the chart below: [Successes:] [0) Lost in time and space] [1) Move '+
         'to the Abyss] [2) Move to the Plateau of Leng] [3+) Return to Arkham]');
  AddCard(GROUPB, EXP_TKIY, DREAMLAND, 43,
         'Bandits with hooves and horns set upon you! Make a Fight (-2) check to beat them '+
         'off or lose 2 Items of your choice.');
  AddCard(GROUPG, EXP_TKIY, DREAMLAND, 44,
         'Maybe you shouldnt have eaten that strangely-colored fruit. Lose 1 Sanity, then '+
         'make a Fight (-1) check. If you fail, lose 2 Stamina.');
  AddCard(GROUPG, EXP_TKIY, DREAMLAND, 45,
         'Pass a Luck (-2) check to meet the dreamself of a familiar face from Arkham: '+
         'Joey "the Rat". Draw 3 Common Items and purchase any of them for $1 less than '+
         'their listed prices. Discard any you dont buy.');
  AddCard(GROUPG, EXP_TKIY, DREAMLAND, 46,
         'Pass a Will (-1) check to gain 1 Common Item from traveling merchants.');
  AddCard(GROUPR, EXP_TKIY, DREAMLAND, 47,
         'Something small bites you and flies away. Lose 1 Stamina.');
  AddCard(GROUPR, EXP_TKIY, DREAMLAND, 48,
         'The zoogs and the cats are at war! You must choose. Either side with the zoogs '+
         'and make a Sneak (-1) check or side with the cats and make a Fight (-1) check. '+
         'If you fail your check, lose 2 Stamina.');
  AddCard(GROUPR, EXP_TKIY, DREAMLAND, 49,
         'You are surrounded by thousands of tiny blue men. Make a Will (-1) [2] check (or '+
         'discard a Whiskey card to pass it automatically) to talk them out of robbing '+
         'you, or lose all your Common Items. They seem oddly uninterested in your Unique '+
         'Items and money.');
  AddCard(GROUPY, EXP_TLATT, DREAMLAND, 50,
         'You find yourself on a rise overlooking an intricate hedge maze with a fabulous '+
         'temple at its center. You may enter and make a Lore (-1) [2] check to find the '+
         'center. If you pass, gain 1 Unique Item from the temple within. If you fail, '+
         'stay here next turn.');
  AddCard(GROUPY, EXP_TLATT, DREAMLAND, 51,
         'You find yourself surrounded by unblinking cats. Pass a Will (-1) check to pass '+
         'by unharmed. If you fail, lose 1 Sanity.');
  AddCard(GROUPY, EXP_TLATT, DREAMLAND, 52,
         'You wander into the Enchanted Forest. Make a Luck (-1) check. If you pass, you '+
         'find succulent fruit that restores 1 Stamina. If you fail, you get lost and are '+
         'delayed.');
  AddCard(GROUPB, EXP_TKIY, YUGGOTH, 41,
         'The buzzing speech of the natives echoes from nearby. Make a Sneak (-2) check to '+
         'remain hidden. If you fail, the creatures find you. You wake up in St. Marys '+
         'Hospital with no memory of your trip to Yuggoth; discard 2 Clue tokens.');
  AddCard(GROUPB, EXP_TKIY, YUGGOTH, 42,
         'The creatures have terrible ray guns! Make a Speed (-1) [2] check to sprint for '+
         'cover. If you fail, you are lost in time and space.');
  AddCard(GROUPB, EXP_TKIY, YUGGOTH, 43,
         'The natives capture you for medical experiments! Make a Luck (-3) check to '+
         'escape. If you fail, exchange your current Stamina and Sanity totals (any '+
         'Stamina or Sanity in excess of your maximums are lost).');
  AddCard(GROUPY, EXP_TKIY, YUGGOTH, 44,
         'The three moons confound you. Make a Will (-2) check or lose 2 Sanity.');
  AddCard(GROUPY, EXP_TKIY, YUGGOTH, 45,
         'This alien city seems recently abandoned. Make a Luck (-1) [2] check to find a '+
         'Unique Item the former inhabitants left behind. If you fail, you discover why '+
         'they abandoned the city, instead. Lose 2 Sanity.');
  AddCard(GROUPY, EXP_TKIY, YUGGOTH, 46,
         'What are these strange disks? If you pass a Luck (-1) check, they are tokl coins '+
         'worth $3! If you fail, they are hazardous Mi-Go artifacts; lose 1 Stamina.');

end;
             
initialization
  OtherWorlds := TStringList.Create;
  Load;
  OtherWorlds.Sort;
end.

