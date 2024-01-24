unit AHEncounters;
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
  Encounters      : TStringList;

implementation

procedure Add(const aName          : string;
              const aExpansion     : EExpansion;
              const aNo            : integer;
              const aDescription   : string);
var
  Encounter : TEncounter;
begin
  Encounter := TEncounter.Create;
  with Encounter do begin
    name          := aName;
    expansion     := aExpansion;
    no            := aNo;
    description   := aDescription;
  end;
  Encounters.AddObject(Encounter.GetKey, Encounter);
end;

procedure LoadEncounters();
begin
  Add('ABUILDING',  EXP_AH,     1, 'Discuss the opportunity to sell a monograph with the President of the University. '+
                                   'Pass a Lore (-1) check to make the sale and gain $5.');
  Add('ABUILDING',  EXP_AH,     2, 'The Dean introduces you to an anthropology professor who gives you some insight into your '+
                                   'investigation. Gain 1 Clue token.');
  Add('ABUILDING',  EXP_AH,     3, 'You may choose to help an anthropology professor and his students decipher an ancient stone '+
                                   'tablet. If so, make a Lore (-2) check. '+
                                   'If you pass, you correctly interpret it, draw 1 Spell. If you fail, you mispronounce a word and you are cursed.');
  Add('ABUILDING',  EXP_AH,     4, 'Administration Building Your discussions on the Mythos lead campus security to conclude that you '+
                                   'are off your rocker, and they escort you off campus. '+
                                   'Move to Arkham Asylum and immediately have an encounter there.');
  Add('ABUILDING',  EXP_AH,     5, 'Pass a Will (-1) check to get the Dean to offer you a retainer to write a manuscript '+
                                   'for the college. Gain a Retainer card.');
  Add('ABUILDING',  EXP_AH,     6, 'Discuss the opportunity to sell a monograph with the President of the University. '+
                                   'Pass a Lore (-1) check to make the sale and gain $5.');
  Add('ABUILDING',  EXP_AH,     7, 'A student mistakes you for the bursar. If you want to carry on the deception, make a Will (-2) check. If you pass, gain $8 in ill-gotten tuition money. '+
                                   'If you fail, you,re arrested and taken to the Police Station.');
  Add('ABUILDING',  EXP_COTDP,  8, '"You there. Friend. You are from this town, yes?" A poor foreign student wants to enroll at the university and asks if he can use your name because '+
                                   'tuition is cheaper for local residents. If you agree, gain $10, but place a Patrol marker on the street area of Miskatonic U. '+
                                   'The neighbors find it suspicious to have two people with the same name.');
  Add('ABUILDING',  EXP_COTDP,  9, 'A Miskatonic entomologist has heard rumors of an exotic species of beetle, previously only found along the Nile, that has been spotted in the campus hedgerows. '+
                                   'Make a Luck (-1)|2| check to find it for her. If you pass, she gives you a $5 stipend for your work.');
  Add('ABUILDING',  EXP_COTDP, 10, 'The Dean would like you to escort the visiting Dr. Ali Kafour around Arkham and show him the sights. '+
                                   'If you agree, you gain $3 as spending money, but must take the Local Guide card.');
  Add('ABUILDING',  EXP_COTDP, 11, 'You meet a research assistant who is quite taken with you. Roll a die. '+
                                   'You gain that many free movement points, to be used immediately on any Tome or '+
                                   'other item that requires an expenditure of movement points to use.');
  Add('ABUILDING',  EXP_COTDP, 12, 'You overhear a history student complaining to his friend about a lack of materials for his Civil War thesis. '+
                                   'If you attempt to enlighten him, he pays $1 for each Clue token you are willing to discard. '+
                                   'Also, if you have the Cavalry Saber, Ancient Tome, or Old Journal Common Items, he will pay you double the listed cost for them.');
  Add('ARKASYLUM',  EXP_AH,     1, 'In the Doctor''s study, you find a book of helpful notes gathered from inmate interviews. '+
                                   'Make a Lore (+0) check and consult the following chart: Successes:] '+
                                   '[0) Their stories fill you with horror even as you learn a few bits of knowledge. Lose 1 Sanity and gain 1 Clue token.] '+
                                   '[1-2) You find several pieces of useful information. Gain 2 Clue tokens.] '+
                                   '[3+) One of the interviews contains vital information. Gain 3 Clue tokens.]');
  Add('ARKASYLUM',  EXP_AH,     2, 'You hear screaming. When you open a heavy cell door to investigate, a dark shape leaps out at you! '+
                                   'It''s an insane man in a straight jacket babbling about invisible horrors. '+
                                   'Make a Lore (-2) check to gleam some useful infomation from him. If you pass, gain 2 Clue tokens. '+
                                   'If you fail, lose 1 Stamina as he attacks you.');
  Add('ARKASYLUM',  EXP_AH,     3, 'You find some strange medicine labeled "Dream Enhancers" in a dusty cabinet. If you choose to take it, make a Lore(-1) check. '+
                                   'If you pass, your visions show you how to perform a ritual. Draw 1 Spell. Otherwise, nothing happens.');
  Add('ARKASYLUM',  EXP_AH,     4, 'The guards of the sanitarium are aware that there is an intruder. Make a Sneak (-1) check to escape. '+
                                   'If you pass, move to the street. If you fail, you are arrested and taken to the Police Station.');
  Add('ARKASYLUM',  EXP_AH,     5, 'Nurse Heather accidentally injects you with a sleeping draught. You may make a Fight (-2) check to resist. '+
                                   'If you fail or choose not to resist, lose your next turn and gain 2 Sanity from the prolonged rest. If you pass, nothing happens.');
  Add('ARKASYLUM',  EXP_AH,     6, 'You are mistaken for an inmate. Doctor Mintz has the guards subdue you and conducts an experiment. '+
                                   'Make a Will (-1)|2| check to discover the results. If you pass, the injections seem to increase your capacity for learning. '+
                                   'Draw 1 Skill. If you fail, his memory drug fails miserably, resulting in lost knowledge. '+
                                   'You must discard one of the following (your choice), if able: 4 Clue tokens, or 2 Spells, or 1 Skill.');
  Add('ARKASYLUM',  EXP_AH,     7, 'Nurse Heather is coming! Make a Speed (-1) check to hide in time. If you pass, you see her drop something as she walks by. '+
                                   'Draw 1 Unique Item. If you fail, she throws you out. Move to the street.');
  Add('ARKASYLUM',  EXP_COTDP,  8, '"This one''s got some wisdom to him," one of the orderlies says as he shows you a withered old Egyptian scholar who was recently committed. '+
                                   '"It''s like he seen somethin'', and if you look close in his eyes, you can see it too." If you look into the patient''s eyes, make a Will (-2) check. '+
                                   'If you pass, you gain 4 Clue tokens. If you fail, you immediately go insane.');
  Add('ARKASYLUM',  EXP_COTDP,  9, 'A doctor working on dream therapy asks if you''d be willing to venture into a patient''s nightmares; '+
                                   'he seems to be beset by dreams of animal-headed men, blinding sand, and strange pyramids. If you agree, you gain 3 Clue tokens but immediately move to the Dreamlands.');
  Add('ARKASYLUM',  EXP_COTDP, 10, 'All of the Asylum''s patients begin speaking in the same strange tounge at once. Make a Lore (-1) check. '+
                                   'If you pass, gain 1 Clue token as you realize that they''re all speaking ancient Sumerian, a language that only a few scholars in the world know!');
  Add('ARKASYLUM',  EXP_COTDP, 11, 'The inmates begin to chant in unison, screaming about the "black Kem of Re and Amen, Isis, and Osiris!" '+
                                   'It nearly drives you mad - but that which doesn''t kill you only makes you stronger. If your Will is 1 or lower, '+
                                   'you may search the Skill deck and take the Will card.');
  Add('ARKASYLUM',  EXP_COTDP, 12, 'The screams of the insane seem to permeate the Asylum... and you realize that you are hearing the voices in your mind! '+
                                   'You cry out to silence voices only you can hear. Passers-by stare at you suspiciously. '+
                                   'Place a Patrol marker on the street area of Downtown Then take the Psychic card, if it is available.');
  Add('BCAVE',      EXP_AH,     1, 'The moaning winds in the cave whisper your name. Lose 1 Sanity.');
  Add('BCAVE',      EXP_AH,     2, 'You are in a maze of twisty passages, all alike. Pass a Lore (-2) check or become lost. If you fail, lose 1 Stamina and stay here next turn.');
  Add('BCAVE',      EXP_AH,     3, 'You find an old book. If you read it, make a Luck (+0) check and consult the chart below. Successes:] '+
                                   '[0) Evil forces assault you. Lose 1 Sanity and 1 Stamina.] '+
                                   '[1) You find the diary of a lost soul who died in the caves long ago. Lose 1 Sanity and gain 1 Clue token as you read his horrible tale.] '+
                                   '[2+) The book is a spellbook. Take the first Tome from the Unique Item deck.]');
  Add('BCAVE',      EXP_AH,     4, 'Bats! Hundreds of them! Pass a Speed (-1) check to get out of the cave safely. If you fail, lose 1 Stamina.');
  Add('BCAVE',      EXP_AH,     5, 'You are attacked by a shadowy being, but a large man leaps out of the darkness and drives it off. He introduces himself as Tom "Mountain" Murphy. '+
                                   'Make a Luck (-2) check, or discard a Whiskey card to pass it automatically. If you pass, he joins your investigation. '+
                                   'Take his Ally card if it''s available, otherwise he gives you something to protect yourself with. '+
                                   'Search the Common Item deck and take the first Weapon you find. If you fail, nothing happens.');
  Add('BCAVE',      EXP_AH,     6, 'In the darkness you happen upon the remains of a previous spelunker. Make a Luck (+0) check and consult the chart below: [Successes:] '+
                                   '[0) The body begins to bloat and splits open, releasing the horror within. Lose 1 Sanity and a monster appears!] '+
                                   '[1) The body has been ripped apart as if shredded by a powerful monster. Lose 1 Sanity.] '+
                                   '[2+) Searching the body you find something interesting. Draw 1 Common Item.]');
  Add('BCAVE',      EXP_AH,     7, 'A monster appears!');
  Add('BCAVE',      EXP_COTDP,  8, 'A monster surprises you! After the battle, if you passed a Horror Check, draw Spells equal to the monster''s Horror damage. '+
                                   'If you failed a Horror check, you emerge with resolve: You may search the Skill deck for the Bravery card and take it.');
  Add('BCAVE',      EXP_COTDP,  9, 'This is a mystic place, where meditation may have strange effects. If you wish to try to meditate, make a Will (+0) check. '+
                                   'If you pass, draw 1 Spell. If you fail, lose 1 Sanity and take the Tainted card.');
  Add('BCAVE',      EXP_COTDP, 10, 'You agree to map out the caves for the local land grant office. Pass a Speed (-2) check to find a cache of stolen goods. Draw 2 Common Items.');
  Add('BCAVE',      EXP_COTDP, 11, 'You find the remains of a fire where someone attempted to burn incriminating evidence, but didn''t finish the job. '+
                                   'You may search the Common Item deck for the Research Materials card and take it.');
  Add('BCAVE',      EXP_COTDP, 12, 'You hear a child''s cries for help from deep within the cave. If you ignore them, a witness recalls seeing you in the area where the youngster disappeared. '+
                                   'Place a Patrol marker on the street area of Rivertown. If you try to rescue the child, make a Luck (-1) check. '+
                                   'If you pass, you find her in a chamber covered with strange occult inscriptions and may draw 2 Spells. If you fail, you are lost in time and space.');
  Add('BOARKHAM',   EXP_AH,     1, 'One of the other customers in the bank recognizes you and offers you a lift. Move to any location or street area in Arkham. '+
                                   'If you move to a location, immediately have an encounter there.');
  Add('BOARKHAM',   EXP_AH,     2, 'A little old lady stands in front of you in line counting out a bag of pennies to deposit. Lose 1 Sanity.');
  Add('BOARKHAM',   EXP_AH,     3, 'You find a penny with a strange sigil carved into it. '+
                                   'Amused, you flip it in the air, then gasp as you feel the sudden gathering of magical forces around you. '+
                                   'Make a Luck (-2) check. If you pass, the penny comes up heads. You are Blessed. If you fail, it comes up tails. You are Cursed.');
  Add('BOARKHAM',   EXP_AH,     4, '"This is a stick-up, see? Nobody move!" '+
                                   'Three men armed with tommy guns rob the bank while you''re standing in line. '+
                                   'Make a Combat (-1) check. If you pass, you drive them off. Nothing happens. If you fail, lose all of your money.');
  Add('BOARKHAM',   EXP_AH,     5, 'A teller you,ve never seen before insists that she just saw you come in and make a deposit the day before. '+
                                   'She proves it by showing you your signature. Gain $5, but lose 1 Sanity.');
  Add('BOARKHAM',   EXP_AH,     6, 'You see a richly dressed man making a large withdrawal. '+
                                   'On the way out, he lights his cigar with a piece of green paper which he then drops on the ground. '+
                                   'Pass a Speed (-1) click to stub it out with your toe before it burns up. '+
                                   'You discover it to be a slightly singed two dollar bill. Gain $2.');
  Add('BOARKHAM',   EXP_AH,     7, 'A man wearing dirty and tattered clothing is loitering outside the bank. '+
                                   'He offers to sell you his last possession to get some food money for him and his family. '+
                                   'If you accept, pay $2 and make a Luck (-1) check If you pass, draw 1 Unique Item. If you fail, draw 1 Common Item.');
  Add('BOARKHAM',   EXP_COTDP,  8, 'A dirty, bedraggled man in Egyptian robes stops you on your way into the bank, and intones, '+
                                   '"It is easier for a camel to pass through the eye of a needle than it is for a rich man to enter heaven!" '+
                                   'If you discard all of your money, you are Blessed.');
  Add('BOARKHAM',   EXP_COTDP,  9, 'Father Michael is hesitant to walk back to South Church alone, saying that the "Legacy of the Pharaohs" exhibit has cast a pall upon Arkham. '+
                                   'If you escort him, move immediately to South Church. '+
                                   'Do not have an encounter there, but you may trade in monster and gate trophies to be Blessed as described at that location. '+
                                   'If you escort him and have the Motorcycle or Map item or the Mists of Releh spell, you are Blessed for free.');
  Add('BOARKHAM',   EXP_COTDP, 10, 'You are retrieving some papers from the safety deposit vault when a portal to another '+
                                   'place and time suddenly opens, nearly sucking the guard in! If you push him out of the '+
                                   'way, you are Blessed, but must immediately move to the Plateau of Leng.');
  Add('BOARKHAM',   EXP_COTDP, 11, 'You head up the steps as a bank robber in a mask dashes out, running into you and dropping '+
                                   'a sack full of money. If you would like to return the money, gain 1 Sanity. If you want to '+
                                   'keep it and run away, gain $10 but lose 1 Sanity and take the Wanted card.');
  Add('BOARKHAM',   EXP_COTDP, 12, 'You see a customer going into seizures. If you want to try to help, make a '+
                                   'Fight (-2) check to restrain him and keep him from hurting himself or a Lore '+
                                   '(-2) check to correctly sedate him. If you fail, lose 2 Stamina as he lashes '+
                                   'out. If you pass, the convulsions subside and a nun rushes to you side, saying, '+
                                   '"Bless you, good sir, for helping." You are Blessed.');
  Add('CSHOPPE',    EXP_AH,     1, 'Jackpot! You find just what you,ve been looking for. Search either the Common '+
                                   'or Unique Item deck and purchase any one item of your choice at list price.');
  Add('CSHOPPE',    EXP_AH,     2, 'Pass a Luck (-1) check or you accidentally drop an item. Discard 1 item of your '+
                                   'choice. If you have no items to drop, then draw again for a different '+
                                   'encounter.');
  Add('CSHOPPE',    EXP_AH,     3, 'A pulsing void gapes behind a bookshelf, sending out waves of heat. Pass a '+
                                   'Fight (-1) check or it sucks you in, hurling you into the Abyss. Have one '+
                                   'encounter there, then immediately return.');
  Add('CSHOPPE',    EXP_AH,     4, 'As you wander into the back of the shop, you hear a noise. Pass a Speed (-1) '+
                                   'check or you look up just in time to see a descending club. Everything goes '+
                                   'black. When you awaken, you are somewhere else. Draw a mythos card and move to '+
                                   'the gate location shown on it, then immediately have an encounter there.');
  Add('CSHOPPE',    EXP_AH,     5, 'You examine an obscene statue. Pass a Luck (-2) check or else you feel a cold '+
                                   'dread spread through your body as you hold it. You are Cursed.');
  Add('CSHOPPE',    EXP_AH,     6, 'You weed through piles of junk looking for something useful. Make a Luck (-1) '+
                                   'check to see what you find. If you pass, your search has resulted in success. '+
                                   'You may look at the top cards of both the Common and Unique Items decks. You may '+
                                   'purchase one, both, or neither at list price. If you fail, there is little of '+
                                   'interest here, but you may look at the top card of the Common Item deck and '+
                                   'purchase it for its list price.');
  Add('CSHOPPE',    EXP_AH,     7, 'A sale takes place. All players may participate. Turn over the top 3 Common '+
                                   'Item cards and the top Unique Item card. Any player may buy one or more of these '+
                                   'cards for their list price. If there  disagreement over who gets to buy a '+
                                   'certain card, you decide. Any items not sold are discarded.');
  Add('CSHOPPE',    EXP_COTDP,  8, '"Durn roof keeps leakin''... ruinin'' my wares!" If you offer to fix the roof '+
                                   'for the shopkeeper, make a Speed (-1) check. If you fail, you fall and lose 2 '+
                                   'Stamina. If you pass, he is grateful, and offers to give you any Common Item in '+
                                   'the deck with a value equal to or lower than your number of successes.');
  Add('CSHOPPE',    EXP_COTDP,  9, 'If you look hard, you can find some real bargains here! Draw a number of cards '+
                                   'from the Common Item deck equal to your focus (maximum 3). You may purchase any '+
                                   'of the drawn items for $1 less than the list price, and must discard the rest.');
  Add('CSHOPPE',    EXP_COTDP, 10, 'The shop seems to be closed early. You peer through the windows and see... '+
                                   'something your mind cannot comprehend! Lose 1 Sanity.');
  Add('CSHOPPE',    EXP_COTDP, 11, 'The shopkeeper has purchased a display of kitschy Egyptian items to drum up '+
                                   'business. Make a Lore (+0) check. If you fail, it looks realistic to you. If you '+
                                   'pass, you point out a few items that are set up improperly, and help him '+
                                   'rearrange the display. In return, he offers you any one non-Weapon Common Item '+
                                   'at half price.');
  Add('CSHOPPE',    EXP_COTDP, 12, 'You get into a debate with the shopkeeper regarding the value of material '+
                                   'wealth vs. knowledge, and he challenges you to prove your point. If you pass a '+
                                   'Will (-1) check, you may discard a Common Item or any number of Clue tokens. If '+
                                   'you discard a Common Item, draw a number of Clue tokens equal to its value. If '+
                                   'you discard Clue tokens, search the Common Item deck and take any number of '+
                                   'items with a total value equal to or less than the number of Clue tokens '+
                                   'discarded.');
  Add('GENSTORE',   EXP_AH,     1, 'You try talking to the elderly locals gathered around the potbellied stove '+
                                   'playing checkers, but you gain nothing but stares and a few befuddled grunts for '+
                                   'your trouble. Apparently they don,t like outsiders. No encounter.');
  Add('GENSTORE',   EXP_AH,     2, 'Make a Will (-2) check. If you pass, you gain the ear of the shopkeeper. Seeing '+
                                   'your valiant cause, he takes you into the back room and offers you some special '+
                                   'equipment. Draw 3 Common Items. You may take 1 of them for free as a gift to '+
                                   'help thwart the evil in Arkham! Discard the other 2. If you fail, nothing '+
                                   'happens.');
  Add('GENSTORE',   EXP_AH,     3, '"Hey, you dropped this!" A young street urchin hands you an item and then '+
                                   'scampers off. You don,t recognize the item, but the boy is already gone. Draw 1 '+
                                   'Common Item.');
  Add('GENSTORE',   EXP_AH,     4, 'The shopkeeper notices one of the items you,re carrying and his face Lights up. '+
                                   '"Say, 1,ve been looking for one of those. You wouldn,t mind parting with it, '+
                                   'would ya? I can pay well." You may sell any one of your Common Items for twice '+
                                   'its listed price.');
  Add('GENSTORE',   EXP_AH,     5, 'A jar on the counter bears a sign proclaiming, "Guess how many marbles are in '+
                                   'the jar and win a prize! $I entry fee." If you want, you may pay $1 to make a '+
                                   'Lore (-2) check. If you pass, you gain $5. If you fail, nothing happens.');
  Add('GENSTORE',   EXP_AH,     6, 'You notice that some of the locals have an odd, fish-like quality to them that '+
                                   'sets your teeth on edge. The shopkeeper notices your gaze and nods, "Marsh '+
                                   'stock, from over in Innsmouth. Watch yourself around them." Shivering, you lose '+
                                   '1 Sanity.');
  Add('GENSTORE',   EXP_AH,     7, 'Noticing a glint on the floor, you discover a silver dollar someone must have '+
                                   'dropped. Gain $1.');
  Add('GENSTORE',   EXP_COTDP,  8, 'A pickpocket grabs your money and runs. Pass a Fight (-2) check to grab and '+
                                   'regain not only your money, but other stolen cash as well. Gain $3. If you fail, '+
                                   'discard all your money.');
  Add('GENSTORE',   EXP_COTDP,  9, 'If you wish, you may stay here next turn and make a Speed (+1) check. You gain '+
                                   '$1 per success rolled.');
  Add('GENSTORE',   EXP_COTDP, 10, 'Mail order! Each investigator may give you money to purchase a single Common '+
                                   'Item of his or her choice at list price. Place the items facedown in front of '+
                                   'you. If you enter the same location as the investigator who requested the item, '+
                                   'give it to him and receive $1 from the bank as a delivery fee.');
  Add('GENSTORE',   EXP_COTDP, 11, 'The shopkeeper has a terrible headache, and yells at you for stepping on all of '+
                                   'the squeaky floorboards. Make a Sneak (+1) check. If you pass, he accidentally '+
                                   'rings you up with a credit, and you gain $2. If you fail, you may search the '+
                                   'Skill deck and take the Sneak card.');
  Add('GENSTORE',   EXP_COTDP, 12, 'You find the shopkeeper dead on the floor! Make a Luck (+0) check. [Successes:] '+
                                   '[0) The Sheriff walks in and finds you at the scene. Take the Wanted card.] '+
                                   '[1-2) Lose 1 Sanity.] [3) There''s an invitation to the Silver Twilight Lodge in '+
                                   'his pocket. Take a Silver Twilight Lodge Membership card.]');
  Add('GRAVEYARD',  EXP_AH,     1, '"Testifying" Cooter Falwell latches onto you and rambles on about his spiritual '+
                                   'beliefs. Make a Lore (-1) check. If you pass, then somewhere in Cooter,s words '+
                                   'you find a clue to the Mythos threat. Gain 1 Clue token, but lose 1 Sanity. If '+
                                   'you fail, move to the street while you listen to Cooter ramble on about pure '+
                                   'nonsense.');
  Add('GRAVEYARD',  EXP_AH,     2, 'Pass a Luck (-2) check to find a valuable clue within your tombstone rubbings. '+
                                   'Gain 2 Clue tokens and you may move to any location or street area in Arkham. If '+
                                   'you move to a location, immediately have an encounter there.');
  Add('GRAVEYARD',  EXP_AH,     3, 'You find the half-buried corpse of a strange being. Draw a monster from the cup '+
                                   'and take it as a monster trophy, even if it has the Endless ability;');
  Add('GRAVEYARD',  EXP_AH,     4, 'Descending into a dark mausoleum, you discover a vampire rising to feed. You '+
                                   'quickly find yourself fighting for your life. Make a Combat (-2) check. If you '+
                                   'pass, you defeat the vampire, gaining 1 Clue token and drawing 1 Unique Item. If '+
                                   'you fail, roll a die and lose that much Stamina.');
  Add('GRAVEYARD',  EXP_AH,     5, 'Entering a stone crypt, you are surprised to find a beautiful fresco and some '+
                                   'inspirational words upon the wall. There is an almost magical peace within the '+
                                   'chamber. Gain 2 Sanity.');
  Add('GRAVEYARD',  EXP_AH,     6, 'You find a man painting a picture of one of the horrible gargoyles lining the '+
                                   'walls of the graveyard. Seeing you, he introduces himself as Richard Upton '+
                                   'Pickman, a painter visiting from Boston. If you spend monster trophies that have '+
                                   'a total of 5 toughness, Pickman takes a liking to you. Take his Ally card. If it '+
                                   'is not available, he teaches you an incantation instead. Draw 1 Spell.');
  Add('GRAVEYARD',  EXP_AH,     7, 'A monster appears!');
  Add('GRAVEYARD',  EXP_AH,      8, '"The thief went this way!" someone shouts, coming from the direction of the '+
                                   'museum exhibit. Make a Speed (-1) check. If you pass, you follow the thief into '+
                                   'the graveyard and watch where he hides the stolen item. Draw 1 Unique Item or '+
                                   'Exhibit Item.');
  Add('GRAVEYARD',  EXP_AH,      9, 'A priest kneels at the gravestone of one Walter Gilman. Hearing you approach, '+
                                   'he rises up out of his prayer and brushes off his knees. "A shame, a perfect '+
                                   'shame." If you are Cursed or either your Stamina or Sanity is 2 or lower, he '+
                                   'introduces himself as Father Iwanicki, and says "And yet, perhaps the good Lord '+
                                   'led you here so I could save you, whereas I could not save him." Take his Ally '+
                                   'card or, if it is not available, you may search the Unique Item deck for the '+
                                   'Holy Water card and take it.');
  Add('GRAVEYARD',  EXP_AH,     10, 'If you have any Ghoul, Vampire, or Zombie monster trophies, you may exchange '+
                                   'any of them for Clue tokens equal to their toughness. If you have none of those '+
                                   'trophies, the groundskeeper suspects you are a grave robber. Place a Patrol '+
                                   'marker on the street area of Rivertown.');
  Add('GRAVEYARD',  EXP_AH,     11, 'In the dead of night, you see a figure lurking in the graveyard, carrying an '+
                                   'ancient artifact. If you investigate, a monster appears, and you suffer a -1 on '+
                                   'both Horror checks and Combat checks. If you defeat the monster with your first '+
                                   'Combat check, draw 1 Unique Item or Exhibit Item. If you defeat the monster '+
                                   'after multiple Combat checks, the artifact falls to the ground, and its pieces '+
                                   'hint at a diabolical scheme: Gain 2 Clue tokens.');
  Add('GRAVEYARD',  EXP_AH,     12, 'You notice that the graveyard is in terrible disrepair and consider donating '+
                                   'money for its upkeep. For each $1 you donate, you may roll one die. Count the '+
                                   'number of successes and consult the chart below: [Successes:] '+
                                   '[0) You are thanked profusely.] '+
                                   '[1-2) You gain a number of Clue tokens equal to your number of successes.] '+
                                   '[3+) You gain 2 Clue tokens and may take the Anointed card.]');
  Add('HROADHOUSE', EXP_AH,     1, 'You enter a "friendly" card game. Make a Luck (-1) check. If you pass, you win '+
                                   'S5. If you fail, you lose $3. If you lose and can,t pay, the boys tough you up '+
                                   'and throw you outside. Lose 1 Stamina and move to the street.');
  Add('HROADHOUSE', EXP_AH,     2, 'Joey "the Rat" Vigil slips into an empty chair at your table and whispers, '+
                                   '"Psssst! Wanna buy something?" Look at the top 3 cards ofthe Common Item deck. '+
                                   'You may purchase any or all of them for $1 above list price. "Hey, I,ve got '+
                                   'overheads the Rat explains."');
  Add('HROADHOUSE', EXP_AH,     3, 'A horrible monster appears!');
  Add('HROADHOUSE', EXP_AH,     4, 'A stranger buys you a drink, You may search the Common Item deck for a Whiskey '+
                                   'card and take it.');
  Add('HROADHOUSE', EXP_AH,     5, 'Prohibition failed to influence the proprietor of Hibb,s. You drink heavily '+
                                   'while quizzing the locals about the strange goings-on in Arkham. Make a Will '+
                                   '(-1) check. If you pass, you hold your liquor and learn something. Gain 2 Clue '+
                                   'tokens. If you fail, you pass out. Move to the street and either have 1 item '+
                                   '(your choice) or all of your money stolen.');
  Add('HROADHOUSE', EXP_AH,     6, '"So, what,s your story, friend?" A smiling man inquires about your adventures '+
                                   'over a glass of gin. You tell him your story. If you spend 3 Clue tokens, he '+
                                   'introduces himself as Ryan Dean and asks to join you. Take his Ally card. if '+
                                   'it,s not available, he gives you some useful items instead. Draw 2 Common '+
                                   'Items.');
  Add('HROADHOUSE', EXP_AH,     7, 'Pass a Luck (-1) check or a pickpocket cleans you out! Lose all your money.');
  Add('HROADHOUSE', EXP_COTDP,  8, '"Friendly game of pool?" Make a Speed (+0) check and consult the chart below. '+
                                   '[Successes:] '+
                                   '[0) You lose $3.] '+
                                   '[1-2) You notice that your opponent is cheating! '+
                                   'If you confront him, place a Patrol marker on the street area of Easttown and '+
                                   'gain $3. As he shoves the money at you, he scowls, telling you you''d better not '+
                                   'come back here.] '+
                                   '[3) You gain $3.]');
  Add('HROADHOUSE', EXP_COTDP,  9, 'A man sets down a briefcase, muttering furtively. "Have you seen the yellow '+
                                   'sign?" Pass a Lore (-3) check to draw the yellow sign in a pool of beer on the '+
                                   'counter, at which he nods and leaves the briefcase. Search the Common Item deck '+
                                   'and take the first Weapon you find, and gain $10!');
  Add('HROADHOUSE', EXP_COTDP, 10, 'A truck driver at the bar has a flat tire and needs help changing it. If you '+
                                   'pass a Fight (-1) check, you help him out and he offers you some of his cargo '+
                                   'for free. Search the Common Item deck for your choice of a Lantern, Map of '+
                                   'Arkham, or Dark Cloak, and take that card.');
  Add('HROADHOUSE', EXP_COTDP, 11, 'Erica Carlyle is slumming it, and seems intrigued by your tales of mystery. If '+
                                   'you have $3 or less, she agrees to join you and help pay your way. Take her Ally '+
                                   'card or, if it is not available, gain a Retainer card.');
  Add('HROADHOUSE', EXP_COTDP, 12, 'The man at the bar next to you is deep in his cups. Pass a Luck (+0) check to '+
                                   'realize that he''s a loan officer from the Bank. He is so drunk that he barely '+
                                   'remembers his name. You may gain a Bank Loan from him, or if you have a Bank '+
                                   'Loan already, may convince him that you have paid it off, and may discard the '+
                                   'Bank Loan card.');
  Add('HSOCIETY',   EXP_AH,     1, 'Perusing the county records, you discover something horrifying about your '+
                                   'family tree. Lose 1 Sanity.');
  Add('HSOCIETY',   EXP_AH,     2, 'You encounter a friendly old professor from Miskatonic University. If you spend '+
                                   '1 gate trophy, he introduces himself as Professor Armitage and offers to join '+
                                   'forces with you. Take his Ally card if it is available, otherwise draw 1 Unique '+
                                   'Item.');
  Add('HSOCIETY',   EXP_AH,     3, 'The Society members are bird watching in the woods. The janitor offers you a '+
                                   'ride there. If you accept, move to the Woods and draw 2 cards, encountering one '+
                                   'card of your choice and discarding the other.');
  Add('HSOCIETY',   EXP_AH,     4, 'Pass a Luck (-1)|2| check to gain insight into a skill while studying the old '+
                                   'volumes of books. Draw 1 Skill, but stay here next turn.');
  Add('HSOCIETY',   EXP_AH,     5, 'You meet Cindy Fleming, a young geology professor at the University. She offers '+
                                   'to show you some interesting formations at the Black Cave. If you accept, move '+
                                   'to the Black Cave and draw 2 cards, encountering one card of your choice and '+
                                   'discarding the other.');
  Add('HSOCIETY',   EXP_AH,     6, 'Pay a $3 fee to gain access to the private library. If you refuse, move to the '+
                                   'street. If you pay, make a Luck (-1) check If you pass, you learn an ancient '+
                                   'spell from a dusty ledger. Draw 1 Spell. If you fail, you doze off and enter The '+
                                   'Dreamlands. Have one encounter there, then immediately return here.');
  Add('HSOCIETY',   EXP_AH,     7, 'You notice a creepy man watching you as you peruse the books. With a feeling of '+
                                   'dread you try to slip out without being followed. Make a Sneak (-1) check. If '+
                                   'you pass, you lose the man, gaining 1 Sanity in the process. If you fail, you '+
                                   'are accosted by the man in the street. He is a wizard and he casts a dark spell '+
                                   'on you as you flee. Lose 2 Stamina, move to the street, and you are Cursed.');
  Add('HSOCIETY',   EXP_COTDP,  8, 'A past-life believer offers to channel the spirits of the ancients. You may '+
                                   'join in and make a Will (+0) check to draw Spells until you draw one with a '+
                                   'Sanity cost of 0; keep that Spell and discard the rest. Alternatively, you may '+
                                   'watch her technique, and make a Luck (-1) check. If you pass, you may take the '+
                                   'Psychic card.');
  Add('HSOCIETY',   EXP_COTDP,  9, 'A weary old man holds out a stack of paper and says "It''s a memoir of my '+
                                   'travels along the Nile, but I doubt the world will last long enough for it to be '+
                                   'published." If you wish to read it, remain here next turn and make a Will (+0) '+
                                   'check. You may draw cards from the Skill deck equal to your number of successes, '+
                                   'and may keep one of them.');
  Add('HSOCIETY',   EXP_COTDP, 10, 'Make a Lore (-1) check to dig up inspirational travel journals penned by '+
                                   'residents of Arkham who traveled to the mysterious and dangerous Nile. If you '+
                                   'pass, you may search the Skill deck and take the Bravery card.');
  Add('HSOCIETY',   EXP_COTDP, 11, 'You find a cipher for interpreting old texts and hieroglyphics! You may '+
                                   'immediately use any Tome or other item that requires an expenditure of movement '+
                                   'points to use.');
  Add('HSOCIETY',   EXP_COTDP, 12, 'You find a painting of your grandparents wearing strange occult pendants. You '+
                                   'may search the Skill deck for the Expert Occultist or Lore card and take it, but '+
                                   'if you do so you must also take the Tainted card.');
  Add('INDSQUARE',  EXP_AH,     1, 'A pair of friendly picnickers share their lunch with you. Gain 1 Stamina.');
  Add('INDSQUARE',  EXP_AH,     2, 'There are gypsies camped in the park. Make a Luck (-1) check if you wish to '+
                                   'interact with them. If you pass, an old man has spread several items on a '+
                                   'blanket for sale. Draw 1 Unique Item and you may buy it for $1 less than the '+
                                   'list price. If you fail, a hag comes up to you and tells you that death shadows '+
                                   'you. You scoff at her and she cuts the side of your face with her fingernail, '+
                                   'drawing blood. Lose 1 Stamina and you are Cursed.');
  Add('INDSQUARE',  EXP_AH,     3, 'There are gypsies camped in the park. They are master thieves amd you are their '+
                                   'target; Pass a Luck (-2) check or lose 1 item of your choice.');
  Add('INDSQUARE',  EXP_AH,     4, 'A shadow falls across you from no apparent source and you shiver with more than '+
                                   'just cold. Pass a Will (-1) check or lose 1 Stamina and 1 Sanity.');
  Add('INDSQUARE',  EXP_AH,     5, 'You touch Founder`s Rock. Make a Luck (-1) check. If you pass, there is an '+
                                   'electrifying shock that opens your mind to the elder things of eons past. Lose 1 '+
                                   'Stamina, but gain 2 Clue tokens and draw 1 Spell. If you fail, you find a '+
                                   'strange carving. As you finger the grooves, a gate opens here and you are drawn '+
                                   'through it.');
  Add('INDSQUARE',  EXP_AH,     6, 'Pass a Fight (-1) check to intimidate a policeman or he rousts you from the '+
                                   'park. Move to the street.');
  Add('INDSQUARE',  EXP_AH,     7, 'Make a Will (-1) check. If you pass it, Anna Kaslow the fortune teller offers '+
                                   'hr help in your investigation. Take her Ally card if it is still available. '+
                                   'Otherwise, gain 2 Clue tokens. If you fail, nothing happens.');
  Add('INDSQUARE',  EXP_COTDP,  8, 'A sheaf of papers with hieroglyphics translations blows past you on the wind. '+
                                   'Make a Speed (-1) check. If you fail, a young lady runs past you after them. If '+
                                   'you pass, you catch them and are thanked profusely by Sarah Danforth, an '+
                                   'archaeology student from Miskatonic. Take her Ally card. If it is not available, '+
                                   'gain 1 Clue token instead as she chats with you about the visiting museum '+
                                   'exhibit.');
  Add('INDSQUARE',  EXP_COTDP,  9, 'A well-dressed gentleman approaches a group of children and begins to lead one '+
                                   'away... and something tells you that he''s up to no good. If you confront him, '+
                                   'he transforms. A monster appears! Treat this monster as if it had the Ambush '+
                                   'special ability. If you defeat it, draw 1 Exhibit Item, but place a Patrol '+
                                   'marker on the street area of Downtown after being seen assaulting a respected '+
                                   'citizen.');
  Add('INDSQUARE',  EXP_COTDP, 10, 'From a bench in Independence Square you can watch the comings and goings of the '+
                                   'town''s major figures. Gain 1 Clue token.');
  Add('INDSQUARE',  EXP_COTDP, 11, 'The staff of the visiting museum exhibit puts on an educational show in the '+
                                   'park, but it is rather confusing. Make a Lore (-1) check. If you pass, you gain '+
                                   'Clue tokens equal to your focus (maximum 3). If you fail, you lose Clue tokens '+
                                   'equal to your focus (maximum 3).');
  Add('INDSQUARE',  EXP_COTDP, 12, 'You learn that cultists are bribing the mayor with stolen items from the '+
                                   '"Legacy of the Pharaohs" exhibit, and often drop them off on his doorstep. If '+
                                   'you would like to reappropriate them, make a Sneak (-1) check. If you fail, you '+
                                   'are arrested. If you roll 1 success, you get away, but empty-handed. If you roll '+
                                   '2 successes, you get away with the packages: Draw 1 Unique Item or Exhibit '+
                                   'Item.');
  Add('ISANCTUM',   EXP_AH,     1, 'The Order of the Silver Twilight casts a banishment spell in their monthly '+
                                   'ceremony. Spend 1 Sanity to make a Luck (-1) check. If you pass, claim any one '+
                                   'monster on the board as a trophy. If you fail, nothing happens.');
  Add('ISANCTUM',   EXP_AH,     2, 'Carl Sanford does not- trust you and at the climax of the monthly ceremony '+
                                   'spits a spell at you. Pass a Luck (-2) check or you are Cursed.');
  Add('ISANCTUM',   EXP_AH,     3, 'You are allowed into the vault of Silver Secrets. Pass a Luck (-2) cheek to '+
                                   'steal a very unusual item. Search the Unique Item deck and take any one Unique '+
                                   'ltem you want.');
  Add('ISANCTUM',   EXP_AH,     4, 'Participating in the monthly ceremony, you witness greet power and great evil. '+
                                   'Lose up to 3 Sanity and gain that many Clue tokens.');
  Add('ISANCTUM',   EXP_AH,     5, 'Pay your monthly dues of $3 or lose 2 Sanity from strange dreams sent to you by '+
                                   'Carl Sanford when he kicks you out of the Order. If you are kicked out, lose '+
                                   'your Silver Twilight Membership.');
  Add('ISANCTUM',   EXP_AH,     6, 'You attend a ceremony in which the order opens a gate and a monster bursts out '+
                                   'of it before the gate closes once more. A monster appears!');
  Add('ISANCTUM',   EXP_AH,     7, 'You,re invited to take part in a Gating ceremony. If you agree, spend 2 Clue '+
                                   'tokens and 1 Sanity to make a Lore (-2) check. If you pass, close one gate of '+
                                   'your choice. If you fail, nothing happens.');
  Add('ISANCTUM',   EXP_COTDP,  8, '"Time to pay your dues, brother. We need a champion, and you''ve been chosen." '+
                                   'You are handed a weapon and thrown through a doorway into oblivion. You may '+
                                   'search the Unique Item deck and take the first magical weapon you find, but you '+
                                   'are transported to R''lyeh.');
  Add('ISANCTUM',   EXP_COTDP,  9, 'A gorgeous youth invites you into a meditation chamber. If you go in, you must '+
                                   'lose a total of 4 Spells or Stamina, divided up as you choose, but you may '+
                                   'search the Exhibit Item deck for the Mask of the Three Fates card and take it. '+
                                   'If it is not there, gain 4 Clue tokens instead. If you do not go in, the young '+
                                   'witch casts a hex to make others mistrust you. Place a Patrol marker on the '+
                                   'street area of French Hill.');
  Add('ISANCTUM',   EXP_COTDP, 10, 'A newly ordained member of the Lodge should be seen but not heard. Pass a Sneak '+
                                   '(-1) check to gain 2 Clue tokens. If you fail, the stern glares of the higher- '+
                                   'ranking members at least give you motivation: You may search the Spell deck for '+
                                   'the Stealth card and take it.');
  Add('ISANCTUM',   EXP_COTDP, 11, 'Only the strongest of will may enter the Lodge''s prized library. Make a Will '+
                                   '(-1) check. If you pass, you gain 3 Clue tokens and may search the Spell deck '+
                                   'for any one Spell and take it. If you fail, you lose your Silver Twilight Lodge '+
                                   'Membership.');
  Add('ISANCTUM',   EXP_COTDP, 12, 'There is an inscription above an alcove. Pass a Lore (-2) check to understand '+
                                   'it. If you do, it reads "Place herein a thing mundane, it will become a thing of '+
                                   'fame." You gain 1 Clue token and may draw 1 Unique Item or Exhibit Item. If you '+
                                   'discard a Common Item of your choice, you may keep the item drawn; otherwise, '+
                                   'discard it.');
  Add('LIBRARY',    EXP_AH,     1, 'You look up to see Abigail Foreman leaning over you with hands on hips and a '+
                                   'frustrated look on her face. Make a Will (-1) check. lf you pass, she helps you '+
                                   'find the book you were looking for. Take the first Tome from the Unique Item '+
                                   'deck. If you fail, you,ve made too much noise. She escorts you out ofthe '+
                                   'library. Move to the street.');
  Add('LIBRARY',    EXP_AH,     2, 'Make a Will (+0) check and consult the chart below: [Successes:] '+
                                   '[0) Abigail tosses you out. Move to the street.] '+
                                   '[1) Abigail lets you into a private section of the library where you find an '+
                                   'ancient tome. Draw 2 Spells and keep whichever one of them you want.] '+
                                   '[2+) Abigail loans you one of the strange items in the '+
                                   'library,s display case. Draw 1 Unique item.]');
  Add('LIBRARY',    EXP_AH,     3, 'You doze off and enter The Dreamlands. Have an encounter there, then '+
                                   'immediately return here.');
  Add('LIBRARY',    EXP_AH,     4, 'A book in a shadowy corner of the library begins to whisper terrible things to '+
                                   'you. Lose I Sanity.');
  Add('LIBRARY',    EXP_AH,     5, 'You find an unusual book that radiates evil at the touch. You begin to read and '+
                                   'are drawn into it. Make a Lore (-2) check. If you pass, you obtain vast '+
                                   'knowledge of the eldritch threat. Roll a die and gain that many Clue tokens. If '+
                                   'you fail, the book consumes you - mind and soul - lose 2 Sanity and 2 Stamina.');
  Add('LIBRARY',    EXP_AH,     6, 'Overdue book Fine is $4. Pay up or move to the street.');
  Add('LIBRARY',    EXP_AH,     7, 'Pass a Luck (-2) check to Find $5 someone was using as a bookmark.');
  Add('LIBRARY',    EXP_COTDP,  8, 'A poorly shelved collection of books falls on you. Make a Speed (+1) check or '+
                                   'lose 1 Stamina. Regardless of your success or failure, a book lands open on the '+
                                   'floor to a strange passage. Draw 1 Spell.');
  Add('LIBRARY',    EXP_COTDP,  9, 'A young, shy anthropology student trips as she''s walking past you, dropping '+
                                   'the artifact she is carrying into your hands. She apologizes profusely, '+
                                   'adjusting her glasses and keeping her eyes on the floor. Make a Will (-2) check; '+
                                   'if you are a male investigator, it is a Will (+0) check. If you succeed, she is '+
                                   'so embarrassed that she dashes off without taking the artifact. You may draw 1 '+
                                   'Exhibit Item or Unique Item.');
  Add('LIBRARY',    EXP_COTDP, 10, 'A young, shy history student bumps into you, dropping the package he is '+
                                   'carrying. He apologizes profusely, stuttering as he avoids making eye contact. '+
                                   'Make a Will (-2) check; if you are a female investigator, it is a Will (+0) '+
                                   'check. If you succeed, he is so flustered that he dashes off without picking up '+
                                   'the artifact. You may draw 1 Exhibit Item or Unique Item.');
  Add('LIBRARY',    EXP_COTDP, 11, 'Two archaeology students have fallen asleep over tomes on loan from the "Legacy '+
                                   'of the Pharaohs" exhibit. Make a Sneak (+1) check. For every two successes '+
                                   '(round down), you may draw 2 Spells, select one of them, and discard the other.');
  Add('LIBRARY',    EXP_COTDP, 12, 'You overhear two men whispering about the visiting exhibit at the museum. "They '+
                                   'cannot discover our plans. We must destroy their tomes." One of them pulls out a '+
                                   'lighter and begins to burn the books! Make a Fight (-2) check. If you pass, you '+
                                   'chase them off. If you fail, they escape and you are blamed for the arson; place '+
                                   'a Patrol marker on the street area of Miskatonic U.');
  Add('MBHOUSE',    EXP_AH,     1, 'The last guest to stay in your room had to leave in a hurry and left something '+
                                   'behind. Draw 1 Common Item.');
  Add('MBHOUSE',    EXP_AH,     2, 'Chanting neighbors keep you up all night. Pass a Luck (-1) check or lose your '+
                                   'choice of 1 Stamina or 1 Sanity.');
  Add('MBHOUSE',    EXP_AH,     3, 'Staring at a painting in one of the rooms, you find yourself drawn into it. '+
                                   'Make a Luck (+0) check. If you pass, move to The Dreamlands. Have one encounter '+
                                   'there and immediately return here. If you fail. move to the Abyss. Have one '+
                                   'encounter there and immediately return here.');
  Add('MBHOUSE',    EXP_AH,     4, 'After supper while sitting on the porch you strike up a conversation with '+
                                   'another guest: Ryan Dean, a traveling salesman. You may make a Will (+0) check '+
                                   'if you want. If you pass, Ryan has a deal for you. You may draw either 1 Common '+
                                   'or 1 Unique Item and purchase it at list price. If you fail, stay here next turn '+
                                   'listening to bawdy stories and tall tales.');
  Add('MBHOUSE',    EXP_AH,     5, 'Ma Mathison tells you that the best room in the house is available for the '+
                                   'night. lf you want, pay $3 to spend the night there. Gain 4 points split between '+
                                   'Sanity and Stamina however you choose.');
  Add('MBHOUSE',    EXP_AH,     6, 'You find a poorly boarded-up passage in the basement that opens into a winding '+
                                   'tunnel. If you venture into it, you exit in the Silver Twilight Lodge. Draw 2 '+
                                   'cards and encounter one card of your choice, discarding the other.');
  Add('MBHOUSE',    EXP_AH,     7, 'Ma Mathison serves her special soup at supper. Roll a die and gain that much '+
                                   'Stamina.');
  Add('MBHOUSE',    EXP_COTDP,  8, 'Ma Mathison offers board as well as room; the bigger the boarder, the bigger '+
                                   'the lunch. Search the Common Item deck and take the Food card. Then make a Fight '+
                                   '(-1) check. For each success, you may place a token on the Food card; when you '+
                                   'use the Food, you may discard the token instead of discarding the card.');
  Add('MBHOUSE',    EXP_COTDP,  9, 'The gable room faces east and brings in clean air from the sea. You gain 1 '+
                                   'Stamina immediately, and may stay here next turn in order to gain an additional '+
                                   '2 Stamina.');
  Add('MBHOUSE',    EXP_COTDP, 10, 'You ambush several monsters emerging from a secret tunnel! Make a Sneak (-2) '+
                                   'check and consult the table below. [Successes:] [0) Three monsters appear!] [1) '+
                                   'Draw 1 monster trophy from the cup, but 2 monsters appear!] [2) Draw 2 monster '+
                                   'trophies from the cup, but 1 monster appears!] [3+) You tear aside the sub- '+
                                   'window''s curtain, revealing the dawn''s light and all of the monsters '+
                                   'disintegrate! Draw 3 monster trophies from the cup.]');
  Add('MBHOUSE',    EXP_COTDP, 11, 'You''re invited to a midnight seance. If you attend, you may commune with the '+
                                   'spirit realm: look at the top 2 cards of the Mythos deck and replace them, '+
                                   'facedown, in any order you like. However, Ma Mathison breaks up the seance and '+
                                   'says, "Yew devil worshippers better not come round no more!" Place a Patrol '+
                                   'marker on the street area of Southside.');
  Add('MBHOUSE',    EXP_COTDP, 12, 'Your room''s last occupant left a small shrine to Osiris. Make a Luck (+0) '+
                                   'check. If you pass, a monster appears. If you fail, a monster appears and you '+
                                   'must take the Harried card.');
  Add('NEWSPAPER',  EXP_AH,     1, 'Editor Doyle Jefferies offers you a Retainer in return for your fascinating '+
                                   'stories. Take a Retainer card.');
  Add('NEWSPAPER',  EXP_AH,     2, 'Editor Doyle Jefferies offers you a Retainer in return for your fascinating '+
                                   'stories. Take a Retainer card.');
  Add('NEWSPAPER',  EXP_AH,     3, 'Earn $5 for a story.');
  Add('NEWSPAPER',  EXP_AH,     4, 'You accidentally tip over a bottle of ink and are aghast at the pattern the ink '+
                                   'forms on the newsroom floor. Lose 1 Sanity.');
  Add('NEWSPAPER',  EXP_AH,     5, 'You earn a hefty fee for a story and get a ride with Doyle Jefferies, the '+
                                   'editor. Gain $2 and move to any location or street area in Arkham. If you move '+
                                   'to a location, immediately have an encounter there.');
  Add('NEWSPAPER',  EXP_AH,     6, 'Pass a Luck (-1) check to find an article that a local citizen told you would '+
                                   'shed light on the recent strange activities. Gain 1 Clue token.');
  Add('NEWSPAPER',  EXP_AH,     7, 'Flipping through the early edition, you are surprised to see that one ofthe '+
                                   'classified ads begins with your name. Reading it, you realize that it contains '+
                                   'several coded clues to the nature of the threat that faces Arkham. Pass a Lore '+
                                   '(-1) check to gain 3 Clue tokens.');
  Add('NEWSPAPER',  EXP_COTDP,  8, 'A competitor to the Arkham Advertiser offers you money to sabotage the presses. '+
                                   'If you accept, gain $5 and make a Sneak (-2) check. If you fail, you are '+
                                   'arrested. Regardless of the result, place a Patrol marker on the street area of '+
                                   'Northside.');
  Add('NEWSPAPER',  EXP_COTDP,  9, 'A reporter will pay you handsomely, whether in money or information, for an '+
                                   'expos? on the life of a monster hunter. Discard any number of monster trophies '+
                                   'to gain $1 or 2 Clue tokens (in any combination) (errata: should be $2 or 1 Clue '+
                                   'token) for each point of toughness worth of monsters discarded.');
  Add('NEWSPAPER',  EXP_COTDP, 10, 'Staring into the presses is like watching the flow of history passing by you. '+
                                   'You begin to see a strange pattern to it all. Take the Visions card.');
  Add('NEWSPAPER',  EXP_COTDP, 11, 'The editor asks you to answer phones on a busy night. You pick up one call and '+
                                   'hear nothing at first. Then you hear your name being whispered by something that '+
                                   'can''t possibly be human. Make a Will (-1) check or lose 1 Sanity. Then make a '+
                                   'Speed (-2) check to activate a call trace in time. If you pass, you learn that '+
                                   'it came from the museum exhibit. Gain 2 Clue tokens');
  Add('NEWSPAPER',  EXP_COTDP, 12, 'You call around for a story, asking about mysterious occurrences related to the '+
                                   'visiting museum exhibit. Make a Luck (+0) check. For each success, you may take '+
                                   '1 Clue token from any locations in Arkham and add it to your pool. If there are '+
                                   'not Clue tokens in Arkham, you may not gain any.');
  Add('PSTATION',   EXP_AH,     1, 'Deputy Dingby, excitedly cleaning his gun, tires a bullet from the chamber in '+
                                   'your direction. Pass a Luck (-1) check to avoid getting shot. If you fail, lose '+
                                   '2 Stamina.');
  Add('PSTATION',   EXP_AH,     2, 'If you succeed at a Luck (-1) check, then Deputy Dinghy absent mindedly leaves '+
                                   'you holding his gun. You may search the Common Item deck for a .45 Revolver card '+
                                   'and take it.');
  Add('PSTATION',   EXP_AH,     3, 'Sheriff Engle notes that you,re carrying an awful lot of weapons. Either pay '+
                                   'him $5 or discard all of your Weapons.');
  Add('PSTATION',   EXP_AH,     4, 'Pass a Will (-1) check to convince Deputy Dingby to share some files with you '+
                                   'that are very interesting. Gain 2 Clue tokens.');
  Add('PSTATION',   EXP_AH,     5, 'Sheriff Engle trusts you and asks you to step into his office to discuss the '+
                                   'recent strange events. Pass a Luck (-2) check to convince him to take you into '+
                                   'his confidence and give you something to help you out. Draw 1 Unique Item.');
  Add('PSTATION',   EXP_AH,     6, 'One of the men in the holding cells tries to intimidate you with stories about '+
                                   'the things that he,s seen. Make a Will (-1) check. If you pass, gain 1 Clue '+
                                   'token. If you fail, move to the street and lose 1 Sanity as the man laughs at '+
                                   'your retreating back.');
  Add('PSTATION',   EXP_AH,     7, 'Deputy Dingby accidentally drops a case file as he makes his way past you. Pass '+
                                   'a Sneak (+0) check to search the Common Item deck for a Research Materials card '+
                                   'and take it.');
  Add('PSTATION',   EXP_COTDP,  8, 'Make a Sneak (-1) check to listen in on an interrogation, and consult the '+
                                   'following chart. [Successes:] [0) You misunderstand what is discussed. Lose 1 '+
                                   'Clue Token.] [1-2) Deputy Dingby sees you standing by the door. Pay $2 to gain 1 '+
                                   'Clue Token.] [3+) What you overhear helps you put the pieces together. Gain 2 '+
                                   'Clue Tokens.]');
  Add('PSTATION',   EXP_COTDP,  9, 'One of the jail''s "guests" decides to end it all rather than face justice, and '+
                                   'Deputy Dingby offers you a pick of his belongings. Pass a Luck (+0) check to '+
                                   'draw a number of cards from the Common Item deck equal to the number of '+
                                   'successes rolled. Keep 1 card and discard the rest.');
  Add('PSTATION',   EXP_COTDP, 10, 'With all the strange outsiders coming to see the visiting museum exhibit, '+
                                   'Sheriff Engle worries about Arkham''s safety. If you have a Physical weapon, he '+
                                   'gives you some training, and you may search the Skill deck for the Marksman card '+
                                   'and take it. If you do not have a Physical weapon, search the Common Item deck '+
                                   'and take the first Weapon you find.');
  Add('PSTATION',   EXP_COTDP, 11, 'You are called in for questioning about missing artifacts from the "Legacy of '+
                                   'the Pharaohs" exhibit. Make a Will (-1) check. If you pass, the Sheriff believes '+
                                   'you are innocent, and his questions tip you off about a few things; Gain 1 Clue '+
                                   'Token. If you fail, he doubts your word, and accuses you of a crime! Choose '+
                                   'between being arrested and taking the Wanted card.');
  Add('PSTATION',   EXP_COTDP, 12, 'You stop by to say hello when you hear an argument from Sheriff Engle''s '+
                                   'office. "But why would a killer perfume the body with lavender and peppermint?" '+
                                   'Make a Lore (-2) check. If you pass, you recognize those herbs as being used in '+
                                   'an ancient Egyptian embalming practices. Gain 1 Clue Token and the Sheriff '+
                                   'rewards you with the Private Investigator card.');
  Add('RDOCKS',     EXP_AH,     1, 'A horrific stench draws your attention to the body of some bizarre marine '+
                                   'creature, rotting on the edge of the docks. As you move towards it, an uneasy '+
                                   'feeling grows in the pit of your stomach, as though you are meddling with '+
                                   'something best left alone. Make a Will (-1) check. if you pass, lose 1 Sanity. '+
                                   'If you fail, lose 2 Sanity. In either event, if you are not reduced to 0 Sanity, '+
                                   'you find something clutched in its webbed hands. Draw 1 Unique Item.');
  Add('RDOCKS',     EXP_AH,     2, 'Walking along the dock you see something floating in the Water near the edge of '+
                                   'the dock. You reach for it - make a Luck (-1) check. If you pass, you dredge up '+
                                   'something useful. Draw 1 Common Item. If you fail, you pull to the surface a '+
                                   'tentacle that immediately wraps around your neck and drags you under the water '+
                                   'and out to sea. Lose 1 Sanity and 3 Stamina before you can break free.');
  Add('RDOCKS',     EXP_AH,     3, 'You open some crates on the dock. Inside you Find some useful things. Draw 2 '+
                                   'Common Items. Next, make a Luck (-1) check. If you pass, you get away without '+
                                   'being seen. If you fail, you are arrested and taken to the Police Station.');
  Add('RDOCKS',     EXP_AH,     4, 'As you look out across the waves, you feel strangely compelled to throw '+
                                   'yourself into the ocean,s watery embrace. Pass a Will (+1) check or you are lost '+
                                   'in time and space.');
  Add('RDOCKS',     EXP_AH,     5, 'You notice a piece of wood floating in the water; carved into it is the name of '+
                                   'a ship long since sunk. As you touch it, visions of the drowning passengers last '+
                                   'moments of life flood through your mind. Pass a Speed (-1) check to hurl it away '+
                                   'from you. If you fail, you fall to the ground with a cry. Lose 1 Sanity.');
  Add('RDOCKS',     EXP_AH,     6, 'The dock workers are short-handed and offer you a job as a stevedore for the '+
                                   'day. Make a Fight (+0) check. If you pass, gain $3 for every success you rolled. '+
                                   'If you fail, the boss gets tired of your lollygagging and throws you out. Lose 1 '+
                                   'Stamina and move to the street.');
  Add('RDOCKS',     EXP_AH,     7, 'You bump into Abner Weems, the local drunk. You help him find a place to sleep '+
                                   'for the night, and he mumbles something to you over and over. Make a Luck (-1) '+
                                   'check. If you pass, his mumblings is a magical chant. Draw 1 Spell. if you fail, '+
                                   'it,s gibberish. Nothing happens.');
  Add('RDOCKS',     EXP_COTDP,  8, 'A load of cargo, precariously balanced on the edge of the dock, goes into the '+
                                   'river with a splash. If you dive in and try to retrieve it, a monster appears, '+
                                   'and you suffer a -1 to your Combat checks. If you evade or defeat the monster, '+
                                   'you may draw 2 Common Items.');
  Add('RDOCKS',     EXP_COTDP,  9, 'A rowdy dock hand doesn''t like the looks of you and challenges you to a '+
                                   'fistfight. Make a Fight (+1)|2| check. If you pass, lose 1 Stamina, but you may '+
                                   'search the Skill deck for the Fight card and take it. If you fail, the dock '+
                                   'workers spit on you, and you run off. Lose 2 Stamina and place a Patrol marker '+
                                   'on the street area of the Merchant District.');
  Add('RDOCKS',     EXP_COTDP, 10, 'The docks are overloaded with shipments coming in to support the museum '+
                                   'exhibit. No one will notice if something goes missing. Make a Sneak (-1) check. '+
                                   'For each success, you may draw 1 Common Item. You may keep any non-Weapon cards, '+
                                   'and must discard the rest.');
  Add('RDOCKS',     EXP_COTDP, 11, 'You see men of questionable character guiding one of the visiting museum '+
                                   'curators toward the edge of the dock...his hands are tied! He pleads to you for '+
                                   'help with silent eyes. If you aid him, make a Fight (-2) check. If you pass, you '+
                                   'wrest the weapon from one and chase them off; you may search the Common Item '+
                                   'deck and take the Tommy Gun card. If you fail, lose 2 Stamina.');
  Add('RDOCKS',     EXP_COTDP, 12, 'You stare into the river, contemplating its currents and depths. Make a Luck '+
                                   '(+0) check. If you pass, you realize that time, fate, all of reality, are like a '+
                                   'river; take the Visions card. If you fail, a pair of dock workers knock you into '+
                                   'the river as a lark, and you catch a cold. Lose 1 Stamina.');
  Add('SBUILDING',  EXP_AH,     1, 'As you enter the Department of Alchemy, a professor looks up in horror. He '+
                                   'grabs an ancient artifact from a locked drawer in his desk and holds it up '+
                                   'before your face, chanting and making symbolic motions with the item. If you are '+
                                   'Cursed, discard the Curse. If you are not Cursed, then you are Blessed.');
  Add('SBUILDING',  EXP_AH,     2, 'Assisting a professor in his research, you find a valuable Spell. Draw 1 Spell. '+
                                   'However, you must pass a Fight (-1) check or some sticky-fingered student steals '+
                                   'one of your items. Lose 1 item of your choice.');
  Add('SBUILDING',  EXP_AH,     3, 'You find a muscular, bored-looking man who challenges you to an arm wrestling '+
                                   'match. Lose 2 Stamina if you accept. If this does not knock you unconscious, Sir '+
                                   'William Brinton laughs and slaps your shoulder, offering to join your '+
                                   'investigation. Take his Ally card. If it is not available, gain $5 instead.');
  Add('SBUILDING',  EXP_AH,     4, 'A chemical brew bubbles on a nearby Bunsen burner. It smells delicious. If you '+
                                   'drink it, make a Luck (+0) check. If you pass, the strange liquid fortiiies you. '+
                                   'Roll a die and gain that many points, split between your Stamina and Sanity '+
                                   'however you like. If you fail, the liquid turns out to be coffee. Gain 1 '+
                                   'Stamina.');
  Add('SBUILDING',  EXP_AH,     5, 'An archaeology professor shows you an item he recovered in an Egyptian pyramid. '+
                                   'If you have 2 or fewer Spells, it glows in your hands and you find yourself '+
                                   'outside, still holding it. Not wanting to confront the professor again, you '+
                                   'decide to keep it. Gain 1 Unique Item and move to the street. If you have more '+
                                   'than 2 Spells, nothing happens.');
  Add('SBUILDING',  EXP_AH,     6, 'A professor of the occult asks you to hold a hideous statue that he believes to '+
                                   'have strange powers while he reads a scroll. Energy shoots through your body. '+
                                   'Make a Luck (-1) check. If you pass, your spirit rises from your body and you '+
                                   'feel that you have the power to switch bodies with another investigator. You may '+
                                   'choose another investigator from the pile of unused investigators and bring it '+
                                   'into play as a new character, discarding your current investigator (along with '+
                                   'all of his items, skills, trophies, etc,). If you fail, nothing happens.');
  Add('SBUILDING',  EXP_AH,     7, 'You find a student pounding on a strange device that he has hooked up to '+
                                   'massive machinery. He states that it is a dimensional beam machine. If you offer '+
                                   'to help him, make a Lore (-2) check. If you pass, beams shoots out in all '+
                                   'directions, disrupting the gates open throughout the board. Roll a die for each '+
                                   'open gate one at a time. On a success the gate is closed. However, you may not '+
                                   'take it as a trophy, but instead return it to the pile of gate markers. If you '+
                                   'fail, the machinery overheats and explodes. Roll a die and lose that much '+
                                   'Stamina, then move to St. Mary,s Hospital.');
  Add('SBUILDING',  EXP_COTDP,  8, 'One of the janitors receives strange gifts from the faculty every Christmas. He '+
                                   'offers to sell you " one o'' them thar kooky books ''r thingamajigs." If you pay '+
                                   'him $5, you may draw 1 Exhibit Item or Unique Item.');
  Add('SBUILDING',  EXP_COTDP,  9, 'The faculty at Miskatonic is all abuzz about rumors of an invasion of exotic '+
                                   'insect species in town. They have no time for you. You may immediately move to '+
                                   'the Administration Building or the Library and have an encounter there.');
  Add('SBUILDING',  EXP_COTDP, 10, 'Wandering the labs at night, you are surprised by a strange, winged, crab-like '+
                                   'creature. It attacks! Make a Speed (-2) check and encounter a Mi-Go from the '+
                                   'monster cup. If you fail the check, it seems to move with preternatural, and you '+
                                   'may not use any investigator cards in this encounter.');
  Add('SBUILDING',  EXP_COTDP, 11, 'You help a professor clean his classroom, and later on are shaking the chalk '+
                                   'dust out of your clothes. Make a Luck (-1) check. If you fail, you cough and gag '+
                                   'on the dust, losing 1 Stamina. If you pass, you realize that the dust is '+
                                   'actually a mystical powder! You may search the Unique Item deck and take the '+
                                   'Powder of Ibn-Ghazi card.');
  Add('SBUILDING',  EXP_COTDP, 12, 'You turn a corner and come face to face with a hideous beast! Make a Will (+0) '+
                                   'check. If you fail, you faint in horror and hit your head, suffering a mild '+
                                   'concussion. Discard 1 Spell or Skill of your choice. If you succeed, you realize '+
                                   'that it is just a statue on loan from the "Legacy of the Pharaohs" exhibit, and '+
                                   'your turn ends.');
  Add('SCHURCH',    EXP_AH,     1, 'You enter the confessional. "Bless me, Father, for I have sinned." Make a Luck '+
                                   '(+0) check and consult the chart below: [Successes:] [0) "Father? Are you '+
                                   'there?" You hear a scream in the next compartment! Lose 3 Sanity and move to the '+
                                   'street.] [1) "Father?" There is no answer. Sighing, you leave. Move to the '+
                                   'street.] [2+) "I don''t remember my last confession?" Raise your Sanity to its '+
                                   'maximum value.]');
  Add('SCHURCH',    EXP_AH,     2, 'You join in the morning mass. Spend 1 Clue token to ask for heavenly aid. If '+
                                   'you do so, roll a die. On a success, your prayers are answered. Remove 1 doom '+
                                   'token from the Ancient One,s doom track.');
  Add('SCHURCH',    EXP_AH,     3, 'You could swear an drain pipe gargoyle moved. Lose 1 Samity,');
  Add('SCHURCH',    EXP_AH,     4, 'Noticing you eying the holy water, Father Michael tells you, "Take what you '+
                                   'need, my child." You may search the Unique Item deck for a Holy Water card and '+
                                   'take it.');
  Add('SCHURCH',    EXP_AH,     5, 'Upon entering the church, you are attacked by Father Michael with a giant '+
                                   'cross, who for some reason believes you to be in league with the devil. Make a '+
                                   'Speed (-1) check. If you pass, you escape. If you fail, lose 2 Stamina. In '+
                                   'either case, move to the street.');
  Add('SCHURCH',    EXP_AH,     6, 'Knowing that you are engaged in God,s work, Father Michael Blesses you.');
  Add('SCHURCH',    EXP_AH,     7, 'Father Michael convinces you that there are members of his congregation in '+
                                   'greater need than you. Donate either half your money (rounded up) or haif your '+
                                   'items (your choice, rounded up) to the poor.');
  Add('SCHURCH',    EXP_COTDP,  8, '"Father Michael?" You look into the back office, and see the priest being '+
                                   'assaulted by a demonic servitor of Horus! If you have a Cross, Holy Water, or '+
                                   'Blessing card, you drive it off. Father Michael is shaken, and asks you to '+
                                   'assist in running the church while he atones. If you drove off the being, you '+
                                   'may take the Anointed card.');
  Add('SCHURCH',    EXP_COTDP,  9, '"Pray for Arkham, my son." Make a Will (-2) check and consult the chart below: '+
                                   '[Successes:] [0) The Dark Pharaoh hears your prayer. Each investigator must make '+
                                   'a Will (-2) check or be Cursed.] [1-2) New and old gods alike hear you. Each '+
                                   'investigator gains 1 Stamina and 1 Sanity, but add 1 doom counter to the doom '+
                                   'track.] [3+) Hope is rekindled. You gain 2 Sanity, and each investigator may '+
                                   'make a Will (-2) check in order to be Blessed.]');
  Add('SCHURCH',    EXP_COTDP, 10, 'If you have any Exhibit Items, Father Michael calls them profane works and '+
                                   'demands that you destroy them. If you refuse, place a Patrol marker on the '+
                                   'street area of Southside. If you agree, you gain 1 Sanity and 1 Clue token per '+
                                   'item discarded.');
  Add('SCHURCH',    EXP_COTDP, 11, 'The morning sun shines through the stained-glass windows, warming your spirit. '+
                                   'Gain Sanity equal to the number of locations with sealed gates.');
  Add('SCHURCH',    EXP_COTDP, 12, 'You stumble through the doors, desperately seeking peace. But then you realize '+
                                   'that the powers you face care nothing for morals, or hope, or humanity. Lose an '+
                                   'amount of Sanity equal to the number of gates currently open.');
  Add('STLODGE',    EXP_AH,     1, 'You hear the quiet sounds of an intruder. lf you investigate, you find a woman '+
                                   'dressed in black. She attacks you as soon as she sees you. Pass a Fight (-1) '+
                                   'check to subdue her long enough to explain your investigation. You find out that '+
                                   'her name is Ruby Standish and that she was robbing the Lodge. However, upon '+
                                   'hearing your tale, she agrees to join you. Take her Ally card. If it is not '+
                                   'available, draw a Unique Item instead.');
  Add('STLODGE',    EXP_AH,     2, 'Carl Sanford draws you into the study to talk and you feel the cold creep of '+
                                   'dread listening to him. Make a Lore (-1) check. If you pass, your willpovver '+
                                   'stands up to the test of the ancient wizard and you even learn something of '+
                                   'value. Gain 3 Clue tokens. If you fail, his hypnotic tones lull you into a '+
                                   'trance. The conversation seems short, but when you leave the study, much time '+
                                   'has passed and your thoughts are confused. Lose all of your Clue tokens and move '+
                                   'to the street.');
  Add('STLODGE',    EXP_AH,     3, 'You find an old parchment in the study. Pass a Lore (-1) check to draw 2 Spells '+
                                   'and keep one of your choice.');
  Add('STLODGE',    EXP_AH,     4, 'Brushing up against a strange object in the hall, you feel stretched and thin, '+
                                   'like your skin is too tight. Pass a Luck (-1) check or you are Cursed.');
  Add('STLODGE',    EXP_AH,     5, '"Care to join the Order?" Carl Sanford and several of his henchmen ask. If you '+
                                   'accept, pay $3 and take at Silver Twilight Membership. If you decline, pass a '+
                                   'Will (-1) check or lose 3 Stamina as the henchmen assist you out the door. '+
                                   'Whether you pass or not, move to the street.');
  Add('STLODGE',    EXP_AH,     6, '"Care to join the Order?" Carl Sanford and several of his henchmen ask. If you '+
                                   'accept, pay $3 and take a Silver Twilight Membership. If you decline, pass a '+
                                   'Will (-1) check or lose 3 Stamina as the henchmen assist you out the door. '+
                                   'Whether you pass or not, move to the street.');
  Add('STLODGE',    EXP_AH,     7, 'Make a Sneak (-2) check. If you pass, you slip into the temple area of the '+
                                   'Lodge and find 2 items of interest. Roll a die for each item. On a a success, '+
                                   'draw a Unique Item, otherwise draw a Common Item.');
  Add('STLODGE',    EXP_COTDP,  8, '"Certainly, we''d love to have you," Carl Sanford says, "if you can do '+
                                   'something for us." Move to the City of the Great Race and have an encounter '+
                                   'there, then immediately return. If you passed a test or defeated a monster '+
                                   'encountered there, take a Silver Twilight Membership and gain 1 Clue token.');
  Add('STLODGE',    EXP_COTDP,  9, '"You want to see what we''re really about, then?" If you accept the Order''s '+
                                   'invitation, you are introduced to the Black Man. Make a Luck (+0) check or be '+
                                   'devoured. If you pass, take a Silver Twilight Membership card and gain 2 Clue '+
                                   'tokens.');
  Add('STLODGE',    EXP_COTDP, 10, 'Make a Will (-2) check to convince the Lodge that you need one of its sacred '+
                                   'items for the good of Arkham. If you pass, draw cards equal to the number of '+
                                   'successes from the Unique Item or Exhibit Item deck, keep one, and discard the '+
                                   'rest. If you fail, place a Patrol marker on the street area of French Hill.');
  Add('STLODGE',    EXP_COTDP, 11, 'The lights go out; you hear chanting and feel a knife at your throat. You may: '+
                                   '1) Flee. Lose 1 Stamina and move to the street. 2) Allow them to cast their '+
                                   'ritual upon you. Lose 2 Stamina, but take the Visions card and gain 1 Clue '+
                                   'token. 3) Attempt to take control of the ritual with a Lore (-1) check. If you '+
                                   'pass, the Lodge offers you a Silver Twilight Membership. (errata: the following '+
                                   'was not printed) If you fail, lose 3 Stamina and all of your Spells, then move '+
                                   'to the street. Lore -1');
  Add('STLODGE',    EXP_COTDP, 12, 'The Lodge is always eager to trade lore. Discard any number of Spells. Gain a '+
                                   'number of Clue tokens equal to the total Sanity cost of the Spells discarded.');
  Add('STMHOSPITAL',EXP_AH,     1, 'You agree to undergo an experimental treatment. Roll a die. On a 1-3, gain that '+
                                   'many Stamina. On a 4-6, nothing happens.');
  Add('STMHOSPITAL',EXP_AH,     2, 'Nurse Sharon slips something into your hand when the doctor isn,t looking. Pass '+
                                   'a Sneak (-1) check to keep anyone else from noticing. If you do, you later '+
                                   'examine the object and find it to be an old parchment with a spell scratched on '+
                                   'it. Draw 1 Spell. lf you fail, an orderly takes it away from you and you gain '+
                                   'nothing.');
  Add('STMHOSPITAL',EXP_AH,     3, 'Make a Luck (-1) check. If you pass, you realize that Dr. Mortirnore is '+
                                   'sneaking up behind you with a hypodermic needle filled with a phosphorescent '+
                                   'gel. You avoid his experiment and subdue the mad doctor. The city awards you $3 '+
                                   'and you gain 2 Sanity in the process. If you fail, lose 2 Sanity, then you are '+
                                   'dumped in the street.');
  Add('STMHOSPITAL',EXP_AH,     4, 'The Doctor escorts you behind a curtain where the body of some other '+
                                   'unfortunate investigator has been laid. The corpse has been torn to shreds. Pass '+
                                   'a Will (-1) check or lose 1 Sanity. If you pass, you may also search the body '+
                                   'and find a helpful item. Draw 1 Unique Item. If you fail, you run away '+
                                   'screaming. Move to the street.');
  Add('STMHOSPITAL',EXP_AH,     5, 'One of the staff physicians talks some sense into you. You are disabused of '+
                                   'certain crazy but accurate notions. Lose 1 Clue token.');
  Add('STMHOSPITAL',EXP_AH,     6, 'You, sneak a peek at the medical records for a recent admission who was '+
                                   'involved in a cult ritual. Pass a Lore (+0) check to learn something about the '+
                                   'cult,s methods. Gain 1 Clue token.   ?');
  Add('STMHOSPITAL',EXP_AH,     7, 'The corpse you are examining isn,t quite dead yet. It reaches out and grabs you '+
                                   'by the throat. Lose 1 Sanity. Then, you must fight the corpse. If you pass a '+
                                   'Combat (-1) check, you defeat it and gain 1 Clue token. Otherwise, move to the '+
                                   'street.');
  Add('STMHOSPITAL',EXP_COTDP,  8, 'A patient appears to be choking on something. But then, horribly, a swarm of '+
                                   'locusts vomits forth from his mouth! If you flee, move to the street. If you '+
                                   'stay to try to help him, the locusts burrow into your body. Lose 1 Stamina and 1 '+
                                   'Sanity, but you may search the Spell deck for a Plague of Locusts spell and take '+
                                   'it.');
  Add('STMHOSPITAL',EXP_COTDP,  9, 'A visiting scholar, Dr. Ali Kafour, gives a lecture on the preparatory '+
                                   'procedures used to create mummies. If you watch the brain removal demonstration, '+
                                   'make a Will (+0) check. For each success you roll, you may gain 1 Clue token; '+
                                   'for every clue token you choose to gain, however, you must discard 1 Sanity.');
  Add('STMHOSPITAL',EXP_COTDP, 10, 'An old man who looks to be near death gestures you toward his bedside. If you '+
                                   'approach, he tries to hand you something as his last breath gurgles out. Make a '+
                                   'Speed (-1) check. If you pass, you catch the object; draw 1 Exhibit Item. If you '+
                                   'fail, the ancient canopic jar shatters on the ground, and you are Cursed!');
  Add('STMHOSPITAL',EXP_COTDP, 11, 'The waiting room is filled with people complaining about a cough they''ve '+
                                   'developed from a strange dust in the air. If you interview them, pass a Fight '+
                                   '(-1) check to gain 2 Clue tokens. If you fail, you develop the cough yourself. '+
                                   'People begin to fear that you are the source of the ailment. Place a Patrol '+
                                   'marker on the street area of Uptown.');
  Add('STMHOSPITAL',EXP_COTDP, 12, 'You stumble upon an autopsy room and see something on the table that looks like '+
                                   'a man... but with the head of an alligator! Pass a Lore (+1) check to gain 1 '+
                                   'Clue token, then pass a Will (-1) check or lose 1 Sanity.');
  Add('TSTATION',   EXP_AH,     1, 'The old train hand Bill Washington sits on the train platform playing his '+
                                   'guitar as he awaits the next train. As you listen to his singing you feel '+
                                   'yourself healing inside. Gain 2 points divided between Stamina and Sanity '+
                                   'however you choose.');
  Add('TSTATION',   EXP_AH,     2, 'Joey "the Rat" is huddled in the shadows of the train station and motions for '+
                                   'you to come over. He has an item for sale. Draw the top Common Item card and pay '+
                                   '$1 more than list price if you wish to purchase it.');
  Add('TSTATION',   EXP_AH,     3, 'A well-dressed man is standing on the platform. He turns and greets you by '+
                                   'name. Although he seems oddly familiar, you don,t remember ever meeting him '+
                                   'before. Then he steps off the platform into the path of a speeding train. Make a '+
                                   'Speed (-2) check. If you pass, he vanishes as you leap right through him. On the '+
                                   'ground, you find yourself clutching a scrap of paper. Gain 1 Spell. If you fail, '+
                                   'he is obliterated before your eyes. Roll a die and lose that much Sanity.');
  Add('TSTATION',   EXP_AH,     4, 'A stranger in a turban steps off the Boston local train with a crazed look on '+
                                   'his face. Make a Luck (-1) check. If you pass, the man pulls a strange object '+
                                   'from beneath his cloak and gives it to you. Draw 1 Unique Item. If you fail, he '+
                                   'pulls a poisoned blade out of his cloak and stabs you. Roll a die and lose that '+
                                   'much Stamina.');
  Add('TSTATION',   EXP_AH,     5, 'On the loading dock you investigate a large crate with strange markings. Make a '+
                                   'Sneak (-1) check. If you pass, you find a very unusual item in the crate. Gain 1 '+
                                   'Unique Item. If you fail, Deputy Dingby catches you breaking it open. You are '+
                                   'arrested and taken to the Police Station.');
  Add('TSTATION',   EXP_AH,     6, 'Bill Washington moves the last of the baggage from his cart onto a truck and '+
                                   'offers you a ride as he opens the drivers door. If you accept, move to any '+
                                   'location or street area in Arkham. If you move to a location, immediately have '+
                                   'an encounter there.');
  Add('TSTATION',   EXP_AH,     7, 'Pay $3 at the Railroad Office to claim an item left in Lost and Found. If you '+
                                   'do so, make a Luck (-2) check. If you pass, draw a Unique Item. If you fail, '+
                                   'draw a Common Item');
  Add('TSTATION',   EXP_COTDP,  8, 'A wealthy foreigner steps off the train and mistakes you for his guide, handing '+
                                   'you his baggage. Draw 1 Exhibit Item, 1 Unique Item, and 1 Common Item. Keep one '+
                                   'of them and discard the rest. You must also take the Local Guide card.');
  Add('TSTATION',   EXP_COTDP,  9, 'The railroad bulls don''t trust the influx of foreigners with the visiting '+
                                   'museum exhibit, and are distracted. If you''d like to try to jump on board a '+
                                   'freight train as it pulls out, make a Sneak (+0) check. If you pass, you may '+
                                   'move to any Arkham location and end your turn. If you fail, you are caught and '+
                                   'warned not to show your face around here again. Lose 1 Stamina and place a '+
                                   'Patrol marker on the street area of Northside.');
  Add('TSTATION',   EXP_COTDP, 10, 'The station manager offers you a job helping to clean out the storage shed '+
                                   'where lost and left-behind luggage is kept. Gain $3 and make a Luck (-2) check. '+
                                   'If you pass, you may also draw 1 Unique Item or Exhibit Item.');
  Add('TSTATION',   EXP_COTDP, 11, 'You fall asleep waiting for your train. Move to the Dreamlands and have an '+
                                   'encounter there, then (unless you are lost in time and space) return '+
                                   'immediately. When you awake, you are holding a strange artifact. Draw 1 Unique '+
                                   'Item or Exhibit Item.');
  Add('TSTATION',   EXP_COTDP, 12, 'You share a train car with a foreign visitor. When you step off and open your '+
                                   'valise, you realize you grabbed the wrong one! Discard a Common or Unique Item '+
                                   'if able, then make a Luck (+0) check. If you pass, draw a number of Unique or '+
                                   'Exhibit Items equal to the number of successes rolled, and keep one. If you '+
                                   'fail, follow the instructions as above but draw from the Common Item deck. '+
                                   '(Clarification: you will need to discard a second item before you make the '+
                                   'second Luck check. You receive nothing if you fail this second check.');
  Add('TUNNAMABLE', EXP_AH,     1, 'The ceiling beam suddenly buckles. Make a Speed (-1) check. If you pass, move '+
                                   'to the street. If you fail, lose 2 Stamina.');
  Add('TUNNAMABLE', EXP_AH,     2, 'Pass a Luck (-1) check to find a hidden cache concealed in the wall of an '+
                                   'upstairs bedroom. Draw 1 Unique Item.');
  Add('TUNNAMABLE', EXP_AH,     3, 'In a dusty and decaying roll-top desk, you find a mysterious manuscript. If you '+
                                   'read it, make a Lore (-1) check. If you pass, draw 1 Spell. If you fail, the '+
                                   'manuscript is nothing but the insane babbling of a previous renter. Stay here '+
                                   'next turn reading it, but gain 2 Clue tokens.');
  Add('TUNNAMABLE', EXP_AH,     4, 'You hear the scurrying and squeaking of a horde of rats from inside the walls. '+
                                   'Abruptly, you realize that they are moving to surround you. Pass a Speed (-1) '+
                                   'check to make it to the front door first. If you fail, you are lost in time and '+
                                   'space.');
  Add('TUNNAMABLE', EXP_AH,     5, 'You notice a glint of light in a crevice. If you reach in, make a Luck (-1) '+
                                   'check. If you pass, draw 1 Unique Item. If you fail, you feel a sharp pain as '+
                                   'teeth clamp down on your hand. You manage to pull free, but you lose 2 Stamina '+
                                   'and I Sanity.');
  Add('TUNNAMABLE', EXP_AH,     6, 'A monster and gate appear!');
  Add('TUNNAMABLE', EXP_AH,     7, 'You bump into Eric Colt. He tells you a horrible tail of the Mythos to test '+
                                   'your nerve. If you listen, lose 2 Sanity. If this doesn,t drive you insane, take '+
                                   'his Ally card if it is available. If it is not available, you may pump him for '+
                                   'information instead. Gain 3 Clue tokens.');
  Add('TUNNAMABLE', EXP_COTDP,  8, 'A group of cultists scampers through the night. If you follow them, make a '+
                                   'Sneak (+0) check to watch where they bury their prize. If you pass, you may draw '+
                                   '1 Unique Item or Exhibit Item. If you fail, they turn and smile: a monster '+
                                   'surprises you from behind!');
  Add('TUNNAMABLE', EXP_COTDP,  9, 'Luck finds those who need it. If you Luck is 1 or lower, you find a luck penny '+
                                   'between the floorboards. You may search the Skill deck and take the Luck card.');
  Add('TUNNAMABLE', EXP_COTDP, 10, 'The house calls to you. If you follow its voice, it tells you which floorboards '+
                                   'to pry up. You may draw 1 Unique item or Exhibit Item, but must also take the '+
                                   'Tainted card.');
  Add('TUNNAMABLE', EXP_COTDP, 11, 'You pass the strange house and find yourself face to face with a foreign man '+
                                   'with a penetrating gaze. If you have any Exhibit Items or your Will is 2 or '+
                                   'lower, he seems to approve of your simpering manner, and he introduces himself '+
                                   'as Dr. Ali Kafour. Take his Ally card or, if it is not available, listen to him '+
                                   'expound upon the ancient Egyptian pantheon as it compares to that of Native '+
                                   'American myths: Gain 2 Clue tokens.');
  Add('TUNNAMABLE', EXP_COTDP, 12, 'You see a warped mirror. If you look into it, you see yourself in another time '+
                                   'and place, holding an ankh in one hand and a sacrificial blade in the other. '+
                                   'Your number of Clue tokens doubles, but if you gain more than 3 Clue tokens in '+
                                   'this manner, you are Cursed.');
  Add('TWHOUSE',    EXP_AH,     1, 'Pass a Luck (-1) check to find an odd looking item in an old dusty display '+
                                   'case. Draw 1 Unique Item.');
  Add('TWHOUSE',    EXP_AH,     2, 'A gate and a monster appear!');
  Add('TWHOUSE',    EXP_AH,     3, '"Excuse me, stranger, but have you ever seen this symbol before?" A man '+
                                   'standing near the house holds up an occult symbol. Make a Lore (-1) check. If '+
                                   'you pass, the man introduces himself as Thomas F. Malone, a police detective '+
                                   'visiting Arkham on a case. He,s impressed with you and offers to join you. Take '+
                                   'his Ally card. if it,s not available, he tells you some valuable information '+
                                   'instead. Gain 2 Clue tokens. If you fail, nothing happens.');
  Add('TWHOUSE',    EXP_AH,     4, 'You find. a banquet laid out in the dining room and feel compelled to sit down '+
                                   'and eat. Make a Luck (+0) check and consult the following chart: [Successes:] '+
                                   '[0) You suddenly realize what you,ve been eating. Lose 3 Sanity.] [1) You gorge '+
                                   'yourself unable to stop eating. Stay here next turn.] [2) The food makes you '+
                                   'feel sick. Lose 1 Stamina.] [3+) The meal refreshes you. Gain 3 Stamina.]');
  Add('TWHOUSE',    EXP_AH,     5, 'You feel the house actually breathe and speak your name. Lose 1 Sanity.');
  Add('TWHOUSE',    EXP_AH,     6, 'In an old journal you leam some horrible eldritch secrets. Roll a die. Lose '+
                                   'that much Sanity and gain that many Clue tokens.');
  Add('TWHOUSE',    EXP_AH,     7, 'You are overcome by the echoing chants of the long gone witches who have lived '+
                                   'and died here and you pass out. Make a Will (-2) check. If you pass, you learn '+
                                   'an ancient spell in your dreams. Draw 1 Spell. If you fail, you are missing half '+
                                   'your items when you wake up. Discard half of your items (your choice, round '+
                                   'down).');
  Add('TWHOUSE',    EXP_COTDP,  8, 'Ever since you visited the witch house, you keep seeing a strange, rat-like '+
                                   'creature out of the corner of you eye...and sometimes it looks like its face is '+
                                   'almost human! Gain 1 Clue token, but take the Harried card.');
  Add('TWHOUSE',    EXP_COTDP,  9, 'Something about the angles in the attic room opens your mind to the myriad '+
                                   'possibilities of other, nearly identical universes. Search the Spell deck for a '+
                                   'Spell you already have, and take another copy of it. Then, as you continue to '+
                                   'stare into the impossible angle, a Hound of Tindalos appears!');
  Add('TWHOUSE',    EXP_COTDP, 10, 'The graffiti on the walls is actually Egyptian hieroglyphics. Make a Lore (+0) '+
                                   'check. You may draw cards from the Spell deck equal to the number of successes, '+
                                   'and keep one of them.');
  Add('TWHOUSE',    EXP_COTDP, 11, 'You see a prim and proper girl in puritanical attire, but there is something '+
                                   'hungry in her eyes. "Would you like to see?" she asks, demurely. If you agree, '+
                                   'she reaches forward to touch you. You feel a terrible cold, then the burning '+
                                   'heat of the pyre! You realize that she is the ghost of Keziah Mason, who was '+
                                   'burned at the stake for witchcraft over a century ago! Make a Will (-1) check. '+
                                   'You may gain 1 Clue token for each success or 1 Spell for every two successes.');
  Add('TWHOUSE',    EXP_COTDP, 12, 'You take a renowned visiting escape artist on a tour of the witch house. If you '+
                                   'give him 2 of your Spells (discarding them), he introduces himself as Erich '+
                                   'Weiss; take his Ally card if it''s available. If it''s not available, he shows '+
                                   'you a trick instead, and you gain 2 Clue tokens.');
  Add('UISLE',      EXP_AH,     1, 'As you start to climb back into your canoe and row to shore, you see a huge, '+
                                   'shadowy shape disturb the water near the island. Waves of intense dread grip '+
                                   'you, and you must pass a Will (-1) check or be Cursed.');
  Add('UISLE',      EXP_AH,     2, 'A group of hooded cultists are having a meeting among the standing stones on '+
                                   'the island. Pass a Sneak (-1) check to overhear some of what they have to say. '+
                                   'Gain 2 Clue tokens.');
  Add('UISLE',      EXP_AH,     3, 'You come across a man examining some old bones. Pass a Sneak (-1) check to get '+
                                   'close enough to see what he,s doing. He finally notices you and is impressed '+
                                   'with your skills, introducing himself as John Legrasse. Take his Ally card if '+
                                   'it,s available, otherwise he shares a meal with you. Restore your Sanity and '+
                                   'Stamina to their maximum values.');
  Add('UISLE',      EXP_AH,     4, 'Looking up at the night sky from the island, you see constellations that you,ve '+
                                   'never seen before.The entire night sky is different here! Lose 1 Sanity and gain '+
                                   '1 Clue token.');
  Add('UISLE',      EXP_AH,     5, 'The willows sway in a wind that you cannot hear or feel, and for a moment, the '+
                                   'hatred of these ancient trees for the invader who has come to their island '+
                                   'drives you to your knees. Pass a Will (-2) check or lose 3 Sanity.');
  Add('UISLE',      EXP_AH,     6, 'A silent man brushes past you on the trail. Your arm goes numb with cold from '+
                                   'the brief contact, and you whirl around to look at him, but he has disappeared. '+
                                   'Lose 1 Stamina and pass a Will (-1) check or lose 1 Sanity as well.');
  Add('UISLE',      EXP_AH,     7, 'You come across a large pile of human bones under the boughs of one of the '+
                                   'willows on the isle. Lose 1 Sanity, but find a scroll among the bones. Draw 1 '+
                                   'Spell.');
  Add('UISLE',      EXP_COTDP,  8, 'A man wearing exotic robes and a strange hat sits in a shaded clearing, '+
                                   'seemingly in a trance. As you approach, he says, "Come sit with me," without '+
                                   'looking at you. If you are Cursed or have any Mask items, he tells you that he '+
                                   'is called The Messenger and is meant to aid you. Take his Ally card or, if it is '+
                                   'not available, gain 2 Clue Tokens.');
  Add('UISLE',      EXP_COTDP,  9, 'As you row along the island''s shore, a tree branch cracks and falls toward '+
                                   'you. Make a Speed (+0) check. If you fail, you are knocked out and wake up far '+
                                   'downstream; move to the Graveyard and you turn ends.');
  Add('UISLE',      EXP_COTDP, 10, 'Something calls to you from the island''s heart... if only you could find it! '+
                                   'Make a Luck (-2) check or exhaust the Find Gate spell, Dynamite item, or Gate '+
                                   'Box item to automatically pass. If you pass, you manage to create a tunnel down '+
                                   'into the earth. Gain 1d6 Clue tokens. If you exhausted an item or spell to pass '+
                                   'the check and gained more that 3 Clue tokens, you must discard the item or spell '+
                                   'used.');
  Add('UISLE',      EXP_COTDP, 11, 'You come upon a tree that has grown, cancer-like, around an ancient prayer '+
                                   'plaque. Make a Fight (-2) check or exhaust the Wither spell, Shrivelling spell, '+
                                   'or the Axe item to automatically pass. If you pass, draw Spells equal to your '+
                                   'focus.');
  Add('UISLE',      EXP_COTDP, 12, 'You see a group of masked Egyptian cultists performing a hideous ritual in a '+
                                   'clearing. If you wish to get closer and listen, make a Sneak (+0) check. If you '+
                                   'pass, draw 1 Spell. If you fail, the look up as one and point at you, and you '+
                                   'know that you are marked. Place a Patrol marker on the street area of the '+
                                   'Merchant District, as an aura of unnaturalness surrounds you.');
  Add('VDINER',     EXP_AH,     1, 'Velma conmments on how skinny you look and gives you a sandwich on the house. '+
                                   'You may search the Common Item deck for a Food card and take it.');
  Add('VDINER',     EXP_AH,     2, 'You spot a rat leaving the kitchen. Pass a Will (-2) check to convince Velma to '+
                                   'bribe you $5 not to tell anyone.');
  Add('VDINER',     EXP_AH,     3, 'Velma reads the tea leaves left in your cup. Make a Luck (-1) check. If you '+
                                   'pass, the formation of the leaves indicates hope, you are Blessed. If you fail, '+
                                   'the future looks bleak, you are Cursed.');
  Add('VDINER',     EXP_AH,     4, '"This must be where pies go when they die." If you want, pay $1 to enjoy a fine '+
                                   'slice of cherry pie. If you do, gain 2 Stamina.');
  Add('VDINER',     EXP_AH,     5, 'You get food poisoning! Pass a Luck (-1) check or lose 2 Stamina.');
  Add('VDINER',     EXP_AH,     6, '"What,ll it be, hon?" Velma takes your order. Pay up to $6 to gain that many '+
                                   'points split between Sanity and Stamina however you like.');
  Add('VDINER',     EXP_AH,     7, 'You find some money on ther floor under the back booth. If you take it, make a '+
                                   'Sneak (-1) check. If you pass, roll a die and gain that much money. If you fail, '+
                                   'Velma sees you pick up the money. She comes over and swipes it out of your hands '+
                                   'screaming, "Stealing my tips!" so loudly that you flee the diner. Move to the '+
                                   'street.');
  Add('VDINER',     EXP_COTDP,  8, 'A reporter from the Arkham Advertiser offers you money to plant a dead scarab '+
                                   'beetle in your soup bowl so he can get a story. If you do so, gain $3 but place '+
                                   'a Patrol marker on the street area of Easttown.');
  Add('VDINER',     EXP_COTDP,  9, 'Free Egyptian grain bread to make the newcomers welcome! Gain 1 Stamina.');
  Add('VDINER',     EXP_COTDP, 10, 'Velma asks you to sample her new Egyptian barley soup recipe. Pass a Luck (-2) '+
                                   'check to gain Stamina equal to your number of successes. If you fail, lose 1 '+
                                   'Stamina.');
  Add('VDINER',     EXP_COTDP, 11, 'You begin pumping the "Legacy of the Pharoahs" exhibit curator for information. '+
                                   'He of course denies that the exhibit has anything to do with the strange '+
                                   'occurrences in Arkham lately, and offers to pay for your meal to make sure you '+
                                   'tell the same to anyone you work for. If you have the Retainer, Deputy of '+
                                   'Arkham, or Silver Twilight Lodge Membership cards, you may discard one to gain 2 '+
                                   'Stamina and $5.');
  Add('VDINER',     EXP_COTDP, 12, 'You take a job working in the diner for tips, and you''ll never disparage a '+
                                   'waitress again. Make a Speed (-1) check. If you succeed, gain $2. If you fail, '+
                                   'lose 1 Stamina but you may search the Skill deck for the Speed card and take '+
                                   'it.');
  Add('WOODS',      EXP_AH,     1, 'You find a sleeping Sheldon Gang member near the still. Make a Sneak (-2) check '+
                                   'to try to swipe the shotgun he has dropped on the ground. If you pass, take a '+
                                   'Shotgun hom the Common Item deck if there is one. Ifyou. fail, the guard '+
                                   'awakens. You are caught and beaten, losing-2 Stamina, but you escape with your '+
                                   'life. Move to the street.');
  Add('WOODS',      EXP_AH,     2, 'You come across a cringing dog. Pass a Speed (-2) cheek to catch and calm him. '+
                                   'If you have Food, you can discard that to automatically pass the check instead '+
                                   'of rolling. You see by his collar that he is ? named Duke. Take his Ally card. '+
                                   'If it is available, gain $3 as a reward for returning. him to his owner, '+
                                   'instead.');
  Add('WOODS',      EXP_AH,     3, 'You are bushwhecked by the Sheldon Gang. Pass an Luck (-1) check to avoid their '+
                                   'trap. If you fail, lose 2 items of your choice. ?');
  Add('WOODS',      EXP_AH,     4, 'A gate and a monster appear!');
  Add('WOODS',      EXP_AH,     5, 'You trip over an object which turns out to be a rusty lockbox. If you open it, '+
                                   'make a Luck (+0) check and consult the following ? chart: [Successes:] [0) A '+
                                   'rotted human foot. Lose 1 Sanity.] [1) Draw 1 Common Item] [2) Draw 1 Unique '+
                                   'Item] [3+) $10 in jewelry.]');
  Add('WOODS',      EXP_AH,     6, 'You meet an old wise man in the grove who offers to share his wisdom with you. '+
                                   'If you accept, lose your next turn and make a Lore (-2) check. If you pass, you '+
                                   'may draw 1 Skill, or draw 2 Spells, or gain 4 Clue tokens. If you fail, nothing '+
                                   'happens.');
  Add('WOODS',      EXP_AH,     7, 'You have stumbled onto a still owned by the Sheldon Gang. Make a Sneak (-1) '+
                                   'check. If you pass, sneak away without being seen, if you fail, lose 2 Stamina '+
                                   'as the Sheldon Gang works you over while escorting you from the woods. In either '+
                                   'ease, move to the street.');
  Add('WOODS',      EXP_COTDP,  8, 'It''s not safe this close to the edge of town. You encounter all monsters '+
                                   'currently in the Outskirts, in the order of your choice. If you successfully '+
                                   'evade any monster, you may choose to move to the street and your turn ends.');
  Add('WOODS',      EXP_COTDP,  9, 'The Sheldon Gang needs someone to distribute the "product" from their hidden '+
                                   'still. Make a Sneak (-1) check. If you fail, you are arrested. If you pass, you '+
                                   'gain $3 and may search the Common Item deck for the Whiskey card and take it.');
  Add('WOODS',      EXP_COTDP, 10, 'You find the rotting body of a foreign grifter that followed the museum exhibit '+
                                   'into town. Pass a Fight (-1) check or become nauseous and move to the street. If '+
                                   'you pass, you find his wallet and gun nearby. Gain $2 and you may search the '+
                                   'Common Item deck for the .45 Automatic card and take it.');
  Add('WOODS',      EXP_COTDP, 11, 'You see a man being pursued across by hideous half-human, half-bestial '+
                                   'creatures. If you help him fight them off, lose 3 Stamina. Even if you are '+
                                   'knocked unconscious, the man, David Packard, owes you his life and intends to '+
                                   'pay his debt. Take his Ally card or, if it is not available, he gives you '+
                                   'something "for protection." You may search the Common Item deck for Dynamite and '+
                                   'take it.');
  Add('WOODS',      EXP_COTDP, 12, 'You trip over a bloodstained axe that had lain hidden beneath a tangle of '+
                                   'brush. If you pass a Luck (+1) check, it isn''t too badly rusted: You may search '+
                                   'the Common Item deck for the Axe card and take it.?');
  Add('YOMSHOPPE',  EXP_AH,     1, 'There is an old, locked trunk for sale for $5. If you buy it, make a Luck (+0) '+
                                   'check and consult thc chart below: [Successes:] [0) Empty!] [1) Gold coins! Roll '+
                                   '2 dice, add them together, and gain that much money] [2+) Jackpot! Draw 2 Unique '+
                                   'Items]');
  Add('YOMSHOPPE',  EXP_AH,     2, 'Miriam Beecher talks to you for a while explaining some very interesting '+
                                   'theories she has concerning the Mythos. Gain 1 Clue token.');
  Add('YOMSHOPPE',  EXP_AH,     3, 'You see an interesting book sitting open on Miriam Beechers desk. Pass a Lore '+
                                   '(-1) check or you peer closely at its pages only to realize too late that the '+
                                   'book is Cursed ... and now, so are you.');
  Add('YOMSHOPPE',  EXP_AH,     4, 'Pass a Lore (-1) check to recognize an item that Miriam Beecher has '+
                                   'underpriced. If you do so, draw 1 Unique Item. You may purchase it for half its '+
                                   'list price (rounded up).');
  Add('YOMSHOPPE',  EXP_AH,     5, 'Looking closely at a mummified head in the shop, you are horrified to find it '+
                                   'looking back at you! Lose 1 Sanity.');
  Add('YOMSHOPPE',  EXP_AH,     6, 'Miriam Beecher, the shopkeeper, peers closely at your face, then screams, '+
                                   '"They`ve marked?you! Get out! Get out!" and throws you out. Move to the street '+
                                   'and lose 1 Sanity from this unsettling incident.');
  Add('YOMSHOPPE',  EXP_AH,     7, 'Looking into a glass ball, you receive a vision of things to come. Turn the top '+
                                   'card of one location deck of your choice face up. The next investigator to have '+
                                   'an encounter at that location draws that encounter card.');
  Add('YOMSHOPPE',  EXP_COTDP,  8, 'A strange man roams the aisles looking desperately for something, muttering to '+
                                   'himself. Make a Speed (-1) check, or he catches you watching him and attacks! '+
                                   'Pass a Fight (+0) check to fend him off, or lose 1 Stamina.');
  Add('YOMSHOPPE',  EXP_COTDP,  9, 'As you wait in line to buy something, a swindler with scars on his face and a '+
                                   'strange accent gives you a wink, then steps in front of you and begins to '+
                                   'distract the shopkeeper. If you leave without paying, draw 1 Exhibit Item or '+
                                   'Unique Item, but you are Cursed.');
  Add('YOMSHOPPE',  EXP_COTDP, 10, 'Water damage! In order to unload damaged books, the shop is holding a sale. For '+
                                   'every $1 you pay, you may draw 1 Unique Item. You may keep any Tomes that you '+
                                   'draw, and must discard the rest. You must pay the total up front, before you '+
                                   'draw.');
  Add('YOMSHOPPE',  EXP_COTDP, 11, 'With the "Legacy of the Pharaohs" exhibit in town, folks are crazy for faux- '+
                                   'Egyptian trinkets. Pay $3 if you''d like to buy one, then make a Luck (-1) '+
                                   'check. If you pass, it''s actually a real item! Draw 1 Exhibit Item or Unique '+
                                   'Item.');
  Add('YOMSHOPPE',  EXP_COTDP, 12, 'You peek into the back room and see Miriam Beecher, the shopkeeper, unwrapping '+
                                   'a mummy stolen from the visiting museum exhibit! If you turn her in, the Sheriff '+
                                   'rewards you with a license to investigate as you see fit; take the Private '+
                                   'Investigator card, if it is available. However, Miriam''s neighbors think you '+
                                   'betrayed her. Place a Patrol marker in the street area of Uptown.');
  Add('ABUILDING',  EXP_TBGOTW,13, 'A familiar name appears as you pore over the student files. Make a Lore (-2) '+
                                   'check and gain 1 Clue token for each success.');
  Add('ABUILDING',  EXP_TBGOTW,14, 'Pass a Will (-1) check to get the Dean to offer you a retainer to write a '+
                                   'manuscript for the college. Gain a Retainer card.');
  Add('ABUILDING',  EXP_TBGOTW,15, 'The University is hosting their annual fundraising gala. It costs $3 to attend. '+
                                   'If you do, make a Luck (+0) check and consult the chart below. [Successes:] [0) '+
                                   'A pleasant, but uneventful evening.] [1) The Head of the Anthropology Dept. is '+
                                   'feeling chatty. Gain 1 Clue token as he elaborates on his recent work.] [2+) '+
                                   'You''ve won the door prize! Draw a Common Item.] Luck +0');
  Add('ABUILDING',  EXP_TBGOTW,16, 'You find it difficult to navigate the University''s bureaucracy. You are '+
                                   'delayed.');
  Add('ARKASYLUM',  EXP_TBGOTW,13, 'A voice on the other side of a locked door sounds familiar. It seems like '+
                                   'someone from your childhood, maybe a teacher or a friend of your parents. The '+
                                   'voice calls out your name and promises you a slow, painful death. Lose 1 '+
                                   'Sanity.');
  Add('ARKASYLUM',  EXP_TBGOTW,14, 'An inmate confides in you that he is actually a reporter, investigating the '+
                                   'conditions at the asylum. He fears he will not keep his sanity much longer and '+
                                   'begs you to smuggle his notes to Editor Doyle Jeffries. Pass a Sneak (-1) check '+
                                   'to receive $3 for your troubles. If not, the nursing staff confiscates the notes '+
                                   'and burns them. You must move to the street.');
  Add('ARKASYLUM',  EXP_TBGOTW,15, 'Doctor Mintz says that one of the patients has been specifically asking for '+
                                   'you. The lunatic calmly offers to put you in touch with unearthly power in '+
                                   'exchange for information. For each Clue token you spend, you may draw 1 Spell. '+
                                   'Choose 1 Spell to keep from among those you draw and discard the others.');
  Add('ARKASYLUM',  EXP_TBGOTW,16, 'You discover two men struggling, each claiming that he is a doctor and that the '+
                                   'other is an inmate. Make a Luck (-2) check. If you succeed, you assist the real '+
                                   'doctor in subduing the patient and regain 2 Sanity as you reaffirm your ability '+
                                   'to discern between the rational and the mad. If you do not succeed, lose 2 '+
                                   'Stamina as the real maniac stabs you in the back.');
  Add('BOARKHAM',   EXP_TBGOTW,13, 'A group of women are collecting charitable donations on behalf of orphans and '+
                                   'widows. If you contribute $3, regain 1 Sanity as they thank you profusely.');
  Add('BOARKHAM',   EXP_TBGOTW,14, 'A man approaches you with a business proposition. "The Bank won''t give me any '+
                                   'money, but I know I can make us a fortune!" If you''re interested in investing, '+
                                   'give him $5 and take a Retainer card.');
  Add('BOARKHAM',   EXP_TBGOTW,15, 'The bank guard starts making friendly conversation with you about the people he '+
                                   'sees every day. Make a Luck (+0) check. If you pass, gain 1 Clue token. If you '+
                                   'fail, his manager interrupts him before he can share anything useful.');
  Add('BOARKHAM',   EXP_TBGOTW,16, 'The strange events have prompted a mob of people to empty their accounts and '+
                                   'leave town. Pass a Will (-2) check to change their minds or the bank closes for '+
                                   'the rest of the game. Move to the street.');
  Add('BCAVE',      EXP_TBGOTW,13, 'A monster appears!');
  Add('BCAVE',      EXP_TBGOTW,14, 'You are attacked by a shadowy being, but a large man leaps out of the darkness '+
                                   'and drives it off. He introduces himself as Tom "Mountain" Murphy. Make a Luck '+
                                   '(-2) check, or discard a Whiskey card to pass it automatically. If you pass, he '+
                                   'joins your investigation. Take his Ally card if it''s available. If it is not, '+
                                   'he gives you something to protect yourself with. Take the first Weapon from the '+
                                   'Common Item deck. If you fail, nothing happens.');
  Add('BCAVE',      EXP_TBGOTW,15, 'You feel the darkness pulling at your very soul. Resist the effects by passing '+
                                   'a Will (-1) check or draw a Corruption card.');
  Add('BCAVE',      EXP_TBGOTW,16, 'You''ve stumbled upon the Cult of the Black Goat! You may join them if you '+
                                   'wish. To do so, you must discard at least 2 toughness worth of monster trophies, '+
                                   'lose 3 Stamina, or an ally. Take a "One of the Thousand" Membership Card. If you '+
                                   'cannot or choose not to join, pass a Speed (-2) check or lose 2 Stamina.');
  Add('CSHOPPE',    EXP_TBGOTW,13, 'A sale takes place. All players may participate. Turn over the top 2 Common '+
                                   'Item cards and the top 2 Unique Item cards. Any player may buy one or more of '+
                                   'these cards for their list price. If there is a disagreement over who gets to '+
                                   'buy a certain card, you decide. Any items not sold are discarded.');
  Add('CSHOPPE',    EXP_TBGOTW,14, 'Examining a fragile vase, it slips out of your hands. Pass a Speed (-1) check '+
                                   'to catch it or Oliver Thomas makes you buy it for $3. If you fail to catch it '+
                                   'and don''t have $3, move to the street.');
  Add('CSHOPPE',    EXP_TBGOTW,15, 'There''s an inscription on the back of this mirror! If you spend $3 to purchase '+
                                   'it, you can attempt to translate it. Pass a Lore (-1) check and draw 1 Spell if '+
                                   'you pass.');
  Add('CSHOPPE',    EXP_TBGOTW,16, 'You don''t see anyone in the shop, and yet a small army of wind-up toys wheel '+
                                   'their way across the floor towards you. Lose 1 Sanity.');
  Add('GENSTORE',   EXP_TBGOTW,13, '"Care for a pickled egg?" If you accept the shopkeeper''s offer, make a Luck '+
                                   '(+1) check. Gain 1 Stamina per success. If you do not roll any successes, lose 2 '+
                                   'Stamina.');
  Add('GENSTORE',   EXP_TBGOTW,14, 'The shopkeeper notices one of the items you''re carrying and his face lights '+
                                   'up. "Say, I''ve been looking for one of those. You wouldn''t mind parting with '+
                                   'it, would ya? I can pay well." You may sell any of your Common Items for twice '+
                                   'its listed price.');
  Add('GENSTORE',   EXP_TBGOTW,15, 'The shopkeeper opens a fresh barrel of flour only to have thousands of beetles '+
                                   'crawl out an quickly cover the floor. Pass a Will (+0) check or lose 1 Sanity.');
  Add('GENSTORE',   EXP_TBGOTW,16, 'You try talking to the elderly locals gathered around the potbellied stove '+
                                   'playing checkers, but you gain nothing but stares and few befuddled grunts for '+
                                   'your trouble. Apparently they don''t like outsiders. No encounter.');
  Add('GRAVEYARD',  EXP_TBGOTW,13, 'A gate and a monster appear!');
  Add('GRAVEYARD',  EXP_TBGOTW,14, 'Someone was here the night before and left behind smoldering ashes, candles, '+
                                   'and a few drops of blood. If you pass a Luck (-2) check, you stumble upon '+
                                   'something important and may draw 1 Unique Item.');
  Add('GRAVEYARD',  EXP_TBGOTW,15, 'You find a half-buried corpse of a strange being. Draw a monster from the cup '+
                                   'and take it as a monster trophy, even if it has the Endless ability.');
  Add('GRAVEYARD',  EXP_TBGOTW,16, 'You get caught in an unexpected downpour of freezing rain. Make a Speed (+0) '+
                                   'check to find shelter or lose 1 Stamina.');
  Add('HROADHOUSE', EXP_TBGOTW,13, '"So, what''s your story, friend?" A smiling man inquires about your adventures '+
                                   'over a glass of gin. You tell him your story. If you spend 3 Clue Tokens, he '+
                                   'introduces himself as Ryan Dean and asks to join you. Take his Ally card. If '+
                                   'it''s not available, he gives you some useful items instead. Gain 2 Common '+
                                   'Items.');
  Add('HROADHOUSE', EXP_TBGOTW,14, 'A horrible Monster appears!');
  Add('HROADHOUSE', EXP_TBGOTW,15, 'An old-timer sits down next to you and offers to teach you a trick in exchange '+
                                   'for a drink. If you agree, gain 1 Spell for the price of $3.');
  Add('HROADHOUSE', EXP_TBGOTW,16, 'You find that tipping well gets the proprietor talking. For every $1 you spend, '+
                                   'gain 1 Clue Token, to a maximum of $3.');
  Add('HSOCIETY',   EXP_TBGOTW,13, 'A monster appears and attacks you as you approach the front door!');
  Add('HSOCIETY',   EXP_TBGOTW,14, 'A large stone disc is on display which bears ancient pictograms. As you examine '+
                                   'it, the room seems to fill with whispering voices. Pass a Will (-1) check to '+
                                   'resist being overcome by its power or you are lost in time and space.');
  Add('HSOCIETY',   EXP_TBGOTW,15, 'A representative of the society is visiting a historic Arkham home to pick up '+
                                   'old photos of the neighborhoods and invites you to tag along. If you accept, '+
                                   'move to the Unnamable and draw 2 cards, encountering one card of your choice and '+
                                   'discarding the other.');
  Add('HSOCIETY',   EXP_TBGOTW,16, 'The diary of an early immigrant settler in Arkham mentions a band of pagans '+
                                   'that resided in the Woods, worshipping a vile Black Goat. If you currently '+
                                   'possess a "One of the Thousand" Cult Membership, gain 3 Clue tokens and lose 1 '+
                                   'Sanity. If not, simply gain 1 Clue token.');
  Add('INDSQUARE',  EXP_TBGOTW,13, 'A gate and a monster appear!');
  Add('INDSQUARE',  EXP_TBGOTW,14, 'As you pass by a game of horseshoes, a bad throw sends one straight at you. '+
                                   'Pass a Speed (+0) check or lose 1 Stamina.');
  Add('INDSQUARE',  EXP_TBGOTW,15, 'You find the remains of a small fire. Among the ashes you find a few scraps of '+
                                   'paper that didn''t completely burn. Make a Luck (+0) check and consult the chart '+
                                   'below. [Successes:] [0) You are Cursed.] [1) Gain 1 Clue token.] [2+) Gain 1 '+
                                   'Spell.]');
  Add('INDSQUARE',  EXP_TBGOTW,16, 'You meet Anna Kaslow, a fortune teller who may have some insight into your '+
                                   'investigation. Make a Will (-1) check. If you pass, you persuade her to help '+
                                   'you. Take her Ally card if it is available. Otherwise, gain 2 Clue tokens. If '+
                                   'you fail, nothing happens.');
  Add('ISANCTUM',   EXP_TBGOTW,13, 'A fellow Lodge member helps you perform a ritual designed to protect you and '+
                                   'your friends. Make a Lore (+0) check to see the deeper meanings. Gain 1 Clue '+
                                   'token for each success.');
  Add('ISANCTUM',   EXP_TBGOTW,14, 'An executive at the Bank of Arkham is also a member and offers to pull a few '+
                                   'strings. You may choose any one player who currently has a Bank Loan and discard '+
                                   'it without paying.');
  Add('ISANCTUM',   EXP_TBGOTW,15, 'If you currently posses a "One of the Thousand" Cult Membership, the Inner '+
                                   'Sanctum has found out about your double life! You must immediately lose either '+
                                   'your Inner Sanctum* of "One of the Thousand" card. Either way, you lose 2 '+
                                   'Stamina. If you are not One of the Thousand, you have no encounter.');
  Add('ISANCTUM',   EXP_TBGOTW,16, 'The Lodge has decided to clean up the town. Choose one dimension symbol other '+
                                   'than the moon and return all non-Spawn monsters in Arkham with that symbol to '+
                                   'the cup.');
  Add('LIBRARY',    EXP_TBGOTW,13, 'Abigail Foreman set aside a book for you, but someone seems to have moved it. '+
                                   'You are delayed while she searches for it. Search the Unique Item deck and take '+
                                   'the first Tome you find.');
  Add('LIBRARY',    EXP_TBGOTW,14, 'Engrossed in your reading, you suddenly notice the Library is locking up for '+
                                   'the evening. Make a Speed (+0) check. If you succeed, move to the street. If '+
                                   'not, you are delayed.');
  Add('LIBRARY',    EXP_TBGOTW,15, 'The text you are reading is accompanied by a gruesome collection of medieval '+
                                   'illustrations. Lose 1 Sanity.');
  Add('LIBRARY',    EXP_TBGOTW,16, 'You spy a suspicious-looking man attempting to sneak a rare book out of the '+
                                   'building. Make a Fight (+1) check to stop him. If you succeed, a grateful '+
                                   'Abigail Foreman offers you $3 as reward. If you fail, lose 1 Stamina.');
  Add('MBHOUSE',    EXP_TBGOTW,13, 'An elderly woman walks up to the porch and strikes up a conversation with you. '+
                                   'She tells you that this had been her home during a very difficult time in her '+
                                   'life. You spend the afternoon in nostalgic conversation about Arkham history. '+
                                   'Gain 1 Clue token.');
  Add('MBHOUSE',    EXP_TBGOTW,14, 'Ma asks you to give her a hand moving a piano into the house. If you agree to '+
                                   'help, make a Fight (-1) check. If you pass, Ma gratefully tucks $3 into your '+
                                   'pocket. If you pass (errata: should say "fail"), you lose 1 Stamina and are '+
                                   'delayed by the frustrating struggle.');
  Add('MBHOUSE',    EXP_TBGOTW,15, 'Ma sends you up to tell Mr. Ahrens that supper is ready. His door is ajar and '+
                                   'as you push it open, you find that he has tied a noose to the rafters and taken '+
                                   'his own life. Lose 1 Sanity.');
  Add('MBHOUSE',    EXP_TBGOTW,16, 'You recognize the man asking after a room as a wanted murderer. Pass a Speed '+
                                   '(-2) check to stop him from getting away and to collect a $5 reward from the '+
                                   'police. If you fail, he fights his way free and you lose 1 Stamina.');
  Add('PSTATION',   EXP_TBGOTW,13, 'A brawl breaks out at the front desk and you get swept up into the fray. Make a '+
                                   'Fight (+0) check or lose 1 Stamina.');
  Add('PSTATION',   EXP_TBGOTW,14, 'On the wall is a map of the city with pins marking the places where incidents '+
                                   'have occured. Imagining lines between these points, an unnerving symbol is '+
                                   'revealed to you. Pass a Will (-1) check or lose 2 Sanity.');
  Add('PSTATION',   EXP_TBGOTW,15, 'Sheriff Engle listens to your tale. He''s ready to take action, assuming that '+
                                   'he believes you. Pass a Will (-3) check to convince him. If you do, choose one '+
                                   'location or street area and return all monsters in it to the cup as armed law '+
                                   'enforcement officers storm in.');
  Add('PSTATION',   EXP_TBGOTW,16, 'The police are desperate for leads and are offering a reward for information. '+
                                   'Gain $1 for each Clue Token in your possession.');
  Add('RDOCKS',     EXP_TBGOTW,13, 'A woman stands on the docks waiting for her husband to return, six years after '+
                                   'his boat sank. As she tells you her sad tale, she hears her name called out by a '+
                                   'familiar voice. Her husband has survived and returned at last! She calls you her '+
                                   'lucky charm and Blesses you from the bottom of her heart.');
  Add('RDOCKS',     EXP_TBGOTW,14, 'A young man is anxiously trying to arrange passage out of the city. Upon '+
                                   'questioning him, he admits to horrific and revealing dreams of an impending '+
                                   'doom. Gain 1 Clue Token.');
  Add('RDOCKS',     EXP_TBGOTW,15, 'An unruly gang has descended upon Abner Weems, the local drunk. Pass a Fight '+
                                   '(-1) check to chase them off. If you succeed, Abner gives you the object he took '+
                                   'which got him in trouble in the first place. Gain 1 Common Item. If you do not '+
                                   'succeed, lose 1 Stamina.');
  Add('RDOCKS',     EXP_TBGOTW,16, 'Rising from the watery depths, the corpse of a murder victim floats to the '+
                                   'surface. Lose 1 Sanity, but gain $3 from the grateful police who are working on '+
                                   'the case.');
  Add('SBUILDING',  EXP_TBGOTW,13, 'An experiment on dogs has gone horribly awry and now a student is willing to '+
                                   'pay to get rid of the evidence. If you agree to help, pass a Sneak (+0) check to '+
                                   'gain $3.');
  Add('SBUILDING',  EXP_TBGOTW,14, 'Despite your sense of larger forces influencing your actions, more rational '+
                                   'minds convince you that there is no such thing as blessings or curses. Discard '+
                                   'any Blessing or Curse cards you have.');
  Add('SBUILDING',  EXP_TBGOTW,15, 'The professors are willing to try some radical procedures for your condition. '+
                                   'For every $3 you spend you may return one of your Corruption cards to the box.');
  Add('SBUILDING',  EXP_TBGOTW,16, 'You discover a mutilated corpse, the victim of some creature that seems to have '+
                                   'escaped. Lose 1 Sanity, and a monster appears in the Miskatonic U. street!');
  Add('STLODGE',    EXP_TBGOTW,13, '"Care to join the Order?" Carl Sanford and several of his henchmen ask. If you '+
                                   'accept, pay $3 and take a Silver Twilight Membership. If you decline, pass a '+
                                   'Will (-1) check or lose 3 Stamina as the henchmen assist you out the door. '+
                                   'Whether you pass or not, move to the street.');
  Add('STLODGE',    EXP_TBGOTW,14, 'From the darkest shadows, a monster appears!');
  Add('STLODGE',    EXP_TBGOTW,15, 'The Lodge has a strange and compelling oil painting on display. Its alien '+
                                   'landscape both fascinates and nauseates you. Pass a Will (+0) check or lose 1 '+
                                   'Sanity.');
  Add('STLODGE',    EXP_TBGOTW,16, 'The wind has pinned an odd piece of paper against the fence surrounding the '+
                                   'Lodge. Gain 1 Clue token.');
  Add('SCHURCH',    EXP_TBGOTW,13, 'A terrified young man staggers into the church seeking sanctuary. He tries to '+
                                   'explain what has traumatized him, but it is difficult to interpret his ravings. '+
                                   'Pass a Lore (-1) check to gain 1 Clue token.');
  Add('SCHURCH',    EXP_TBGOTW,14, 'The church is having a bake sale! Everything smells delicious. Spend $1 on '+
                                   'treats to regain 1 Stamina.');
  Add('SCHURCH',    EXP_TBGOTW,15, 'The Cult of the Black Goat has vandalized the church, and Father Michael asks '+
                                   'for your help in painting over the blasphemous graffiti and cleaning up the '+
                                   'damage. If you wish to help, you are delayed by the effort, but Father Michael '+
                                   'Blesses you for your hard work.');
  Add('SCHURCH',    EXP_TBGOTW,16, 'You light a candle in prayers for those souls believed to be lost. You may '+
                                   'choose one Ally card that has been returned to the box and reshuffle it back '+
                                   'into the Ally deck. If no Ally cards have been returned to the box, gain 1 '+
                                   'Sanity instead.');
  Add('STMHOSPITAL',EXP_TBGOTW,13, 'Someone has left a package unattended in the waiting room. Pass a Luck (-2) '+
                                   'check to draw 1 Unique Item before the hospital staff finds it.');
  Add('STMHOSPITAL',EXP_TBGOTW,14, 'The cafeteria food, while tasteless, is quite nutritious. Gain 1 Stamina.');
  Add('STMHOSPITAL',EXP_TBGOTW,15, 'You enter the chapel, unnoticed by a stranger who prays aloud for the health of '+
                                   'her husband. Some of her words contain shocking information. Pass a Sneak (-1) '+
                                   'check to gain 1 Clue token for each success.');
  Add('STMHOSPITAL',EXP_TBGOTW,16, 'You scrounge up some painkillers. Regain 2 Stamina.');
  Add('TUNNAMABLE', EXP_TBGOTW,13, 'A hideous monster appears!');
  Add('TUNNAMABLE', EXP_TBGOTW,14, 'A stranger approaches and struggles to explain the nature of the creature '+
                                   'inside the house. Pass a Lore (+0) check to understand his words and gain 1 Clue '+
                                   'token.');
  Add('TUNNAMABLE', EXP_TBGOTW,15, 'The door slams shut behind you! Spend a turn delayed as you search for another '+
                                   'way out.');
  Add('TUNNAMABLE', EXP_TBGOTW,16, 'You are attacked by some unseen force. Lose 2 Stamina.');
  Add('TWHOUSE',    EXP_TBGOTW,13, '"Excuse me, stranger, but have you ever seen this symbol before?" A man '+
                                   'standing near the house holds up an occult symbol. Make a Lore (-1) check. If '+
                                   'you pass, the man introduces himself as Thomas F. Malone, a police detective '+
                                   'visiting Arkham on a case. He''s impressed with you and offers to join you. Take '+
                                   'his Ally card. If it''s not available, he tells you some valuable information '+
                                   'instead. Gain 2 Clue tokens. If you fail, nothing happens.');
  Add('TWHOUSE',    EXP_TBGOTW,14, 'On the front lawn a group of children hold hands and circle around a dead bird, '+
                                   'chanting words you don''t recognize. Make a Lore (-2) check. If you pass draw 1 '+
                                   'Spell.');
  Add('TWHOUSE',    EXP_TBGOTW,15, 'Someone has left their mathematics homework lying on the dining room table. '+
                                   'Pass a Lore (-1) check to see the deeper meanings. Gain 1 Clue token for each '+
                                   'success.');
  Add('TWHOUSE',    EXP_TBGOTW,16, 'You find a terrible collection of human remains with the walls. Pass a Will '+
                                   '(-1) check or lose 2 Sanity.');
  Add('TSTATION',   EXP_TBGOTW,13, 'Bill Washington moves the last of the baggage from his cart onto a truck and '+
                                   'offers you a ride as he opens the driver''s door. If you accept, move to any '+
                                   'location or street area in Arkham. If you move to a location, immediately have '+
                                   'an encounter there.');
  Add('TSTATION',   EXP_TBGOTW,14, 'There''s been a rash of pickpocketing in the train station. Pass a Luck (-1) '+
                                   'check or lose all your money!');
  Add('TSTATION',   EXP_TBGOTW,15, 'You bump into a friend who''s returned from London with his financ?e. They''ve '+
                                   'brought back the most delightful souvenirs! Draw 3 Unique Items, keep 1, and '+
                                   'discard the others.');
  Add('TSTATION',   EXP_TBGOTW,16, 'You overhear the engineer talking. "I swear to you we hit something just '+
                                   'outside of town. Something unnatural. And it weren''t dead when we left it!" '+
                                   'Draw a monster and place it in the Outskirts.');
  Add('UISLE',      EXP_TBGOTW,13, 'Pass a Luck (-1) check to notice an unusual shape in the reeds. Gain 1 Common '+
                                   'Item.');
  Add('UISLE',      EXP_TBGOTW,14, 'The fog fills your lungs, trying to change you. Pass a Will (-1) check to '+
                                   'resist or gain one Corruption card.');
  Add('UISLE',      EXP_TBGOTW,15, 'You come across a man examining some old bones. Pass a Sneak (-1) check to get '+
                                   'close enough to see what he''s doing. He finally notices you and is impressed '+
                                   'with your skills, introducing himself as John Legrasse. Take his Ally card if '+
                                   'it''s available, otherwise he shares a meal with you. Restore your Sanity and '+
                                   'Stamina to their maximum value.');
  Add('UISLE',      EXP_TBGOTW,16, 'You''ve stumbled upon the Cult of the Black Goat! You may join them if you '+
                                   'wish. To do so, you must discard at least 2 toughness worth of monster trophies, '+
                                   'lose 3 Stamina, or an Ally. Take a "One of the Thousand" Cult Membership card. '+
                                   'If you cannot or choose not to join, you must pass a Speed (-2) check or lose 2 '+
                                   'Stamina.');
  Add('VDINER',     EXP_TBGOTW,13, 'An old man sitting alone starts choking on his meatloaf. Pass a Speed (-1) '+
                                   'check to slap him on the back and dislodge the food in time. If you succeed, he '+
                                   'tearfully thanks you and offers you his fondest possession as a reward. Draw one '+
                                   'Unique Item. If you fail, lose 1 Sanity as you watch him pass away.');
  Add('VDINER',     EXP_TBGOTW,14, 'While eating your pork chops, a pale stranger comes out from the kitchen and '+
                                   'whispers in your ear what you are actually eating. The stranger disappears into '+
                                   'the night and you lose 1 Sanity.');
  Add('VDINER',     EXP_TBGOTW,15, 'Whoever is sitting at the table behind you is having a fascinating '+
                                   'conversation. Pass a Sneak (-1) check to eavesdrop, gaining one Clue token for '+
                                   'each success.');
  Add('VDINER',     EXP_TBGOTW,16, 'You don''t notice right away, but Velma has accidentally given you too much '+
                                   'change. Gain $1.');
  Add('WOODS',      EXP_TBGOTW,13, 'A gate and a monster appear!');
  Add('WOODS',      EXP_TBGOTW,14, 'The sound of chanting fills the night air, poisoning your soul. you may resist '+
                                   'the effect by passing a Will (-1) check. If you fail, draw a Corruption card.');
  Add('WOODS',      EXP_TBGOTW,15, 'You''ve stumbled upon the Cult of the Black Goat! You may join them if you '+
                                   'wish. To do so, you must discard at least 2 toughness worth of monster trophies, '+
                                   'lose 3 Stamina, or an Ally. Take a "One of the Thousand" Cult Membership card. '+
                                   'If you cannot or choose not to join, pass a Speed (-2) check or lose 2 Stamina.');
  Add('WOODS',      EXP_TBGOTW,16, 'You''ve stumbled upon the Cult of the Black Goat! You may join them if you '+
                                   'wish. To do so, you must discard at least 2 toughness worth of monster trophies, '+
                                   'lose 3 Stamina, or an Ally. Take a "One of the Thousand" Cult Membership card. '+
                                   'If you cannot or choose not to join, pass a Speed (-2) check or lose 2 Stamina.');
  Add('YOMSHOPPE',  EXP_TBGOTW,13, 'A famous occultist is in town giving a lecture. As part of his demonstration he '+
                                   'offers to place you in a trance. If you agree, make a Will (-2) check. Gain 1 '+
                                   'Clue token for each success. if you fail the check, lose 1 Sanity as you are '+
                                   'assailed by traumatic visions from your subconscious.');
  Add('YOMSHOPPE',  EXP_TBGOTW,14, 'A smiling man greets you warmly. "It''s nice to see you again!" You believe he '+
                                   'has you mistaken for someone else, but he responds, "Nonsense! I''ve been '+
                                   'meaning to return this to you." He hands you a package and leaves. Gain 1 Common '+
                                   'Item.');
  Add('YOMSHOPPE',  EXP_TBGOTW,15, 'Miriam Beecher claims to have a healing salve in stock and offers to sell you '+
                                   'some. You may spend $3 to recover up to 2 Stamina.');
  Add('YOMSHOPPE',  EXP_TBGOTW,16, 'Miriam Beecher offers to teach you the spell you need. You may pay $5 to search '+
                                   'the Spell deck and take any one Spell you want. If you turn down her offer, '+
                                   'nothing happens.');
  Add('ABUILDING',  EXP_TKIY,  17, 'A professor of the occult pays you to post signs throughout the campus that '+
                                   'he claims will ward off danger. However, the signs carry their own danger '+
                                   'Gain $4, but pass a Will (-2) check or lose 2 Sanity.');
  Add('ABUILDING',  EXP_TKIY,  18, 'As students start leaving town in fear of their safety, the University '+
                                   'begins to offer discounts on tuition and services. You may pay $5 to draw 2 '+
                                   'Skills, keeping one and discarding the other.');
  Add('ABUILDING',  EXP_TKIY,  19, 'Make a Luck (+0) check. If you pass, your request for a stipend came '+
                                   'through and you gain $2. If you fail, the processing fees come due, and you '+
                                   'lose $1.');
  Add('ABUILDING',  EXP_TKIY,  20, 'You are asked to speak to the students regarding Lost Carcosa. Pass a Lore '+
                                   '(-1) check to gain $1 for each success you roll.');
  Add('ARKASYLUM',  EXP_TKIY,  17, 'A surprising number of society''s elite have checked in lately, and they '+
                                   'need assistants to represent their interests during their "time abroad." '+
                                   'Pass a Will (-2) check to gain a Retainer card.');
  Add('ARKASYLUM',  EXP_TKIY,  18, 'The more time you spend with them, the more their ramblings make sense. '+
                                   'Gain up to 3 Clue tokens, but for every Clue token you take, you lose 2 '+
                                   'Sanity.');
  Add('ARKASYLUM',  EXP_TKIY,  19, 'Volunteers for art therapy are requested. The inmates'' paintings are a '+
                                   'window into their madness. Pass a Will (-1) check to gain 2 Clue tokens. If '+
                                   'you fail, lose 1 Sanity.');
  Add('ARKASYLUM',  EXP_TKIY,  20, 'You hear a strange singsong voice that says, "The way of an eagle in the '+
                                   'air; the way of a serpent upon the rock." Pass a Lore (-1) check to gain 1 '+
                                   'Clue token');
  Add('BOARKHAM',   EXP_TKIY,  17, 'The bank hosts a fund drive for the arts. If you spend $1 to make a '+
                                   'donation, you are entered in a lottery. Pass a Luck (-2) check to draw 1 '+
                                   'Unique Item.');
  Add('BOARKHAM',   EXP_TKIY,  18, 'The bank offers a special incentive to anyone who opens an account: Take '+
                                   'out a loan and get free tickets to the next performance of "The King in '+
                                   'Yellow." You may take out a Bank Loan if you don''t already have one, '+
                                   'gaining $12 from the loan instead of $10. However, if you do so, you also '+
                                   'lose 1 Sanity.');
  Add('BOARKHAM',   EXP_TKIY,  19, 'The lines of businessmen. The tellers at their alters. The communion of the '+
                                   'safety deposit room. In a flash of insight, or perhaps madness, you realize '+
                                   'that a bank is simply another form of church and that whatever god it is '+
                                   'consecrated to is watching you. You may spend any or all of your Sanity. '+
                                   'After spending the Sanity, roll 1 die for each point you spent. If you '+
                                   'rolled any successes, you are Blessed.');
  Add('BOARKHAM',   EXP_TKIY,  20, 'You wander past the bank after hours, and see the night watchman convulsing '+
                                   'on the floor! Make a Fight (-2) check to restrain him. If you fail, you lose '+
                                   '1 Stamina. If you pass, he begins speaking in tongues, and some unknown '+
                                   'power Blesses you.');
  Add('BCAVE',      EXP_TKIY,  17, 'A collapsed side passage looks like it was once a smugglers'' hideout. Make '+
                                   'a Fight (-2) check. If you pass, search the Common Item deck and take the '+
                                   'first item with a list price of $4 or more.');
  Add('BCAVE',      EXP_TKIY,  18, 'The shopkeeper at the General Store thinks that transients living in the '+
                                   'caves are scaring his customers. He asks you to chase them off. Make a Fight '+
                                   '(-1) check to intimidate them. If you pass, the shopkeeper gives you a free '+
                                   'Common Item. If you fail, they pelt you with rocks, and you lose 1 Stamina.');
  Add('BCAVE',      EXP_TKIY,  19, 'You come upon the ashes of an old fire. Someone camped here and scrawled '+
                                   'runes with the ashes. Pass a Lore (-2) check to decipher them and draw 1 '+
                                   'Spell. If you fail, a monster appears!');
  Add('BCAVE',      EXP_TKIY,  20, 'You see runes carved on the cave wall, but then... is it a trick of the '+
                                   'light, or are the walls dripping silver? Make a Speed (-2) check to copy the '+
                                   'runes in time. If you pass, draw a number of Spells equal to the number of '+
                                   'successes rolled. You may keep one, and must discard the rest.');
  Add('CSHOPPE',    EXP_TKIY,  17, '"Free. Help yourself." Make a Lore (-1) check to repair the item you find '+
                                   'beneath the sign. If you pass, draw 1 Common Item. If you fail, lose 1 '+
                                   'Stamina as you injure yourself.');
  Add('CSHOPPE',    EXP_TKIY,  18, 'There are some amusing games at the Shoppe to celebrate the opening night '+
                                   'of "The King in Yellow." Correctly guess the cost of the next Common Item in '+
                                   'the deck, and you get to keep that item! Otherwise, discard it.');
  Add('CSHOPPE',    EXP_TKIY,  19, 'You find a dead cat on the front stoop of the shop. Pass a Luck (-1) check '+
                                   'to find the weapon that killed it in the grass nearby. Search the Common '+
                                   'Item deck and take the first Weapon you find.');
  Add('CSHOPPE',    EXP_TKIY,  20, 'You never know what you''ll find in the lost and found box. Spend up to $5. '+
                                   'For each $1 you pay, draw one card from the Common Item deck. You may keep '+
                                   'one card, but you must discard the rest.');
  Add('GENSTORE',   EXP_TKIY,  17, '"The King in Yellow" director is looking for old junk to use as props, and '+
                                   'the best junk is in the garbage. Make a Will (+0) check. For each success, '+
                                   'draw 1 card from the Common Item deck and note its cost. Then, discard all '+
                                   'the cards drawn, but gain money equal to the list price of the most '+
                                   'expensive item.');
  Add('GENSTORE',   EXP_TKIY,  18, 'Pass a Lore (-2) check to interpret the meaning in the strange stars '+
                                   'overhead. If you fail, you must pass a Luck (-2) check or be arrested for '+
                                   'loitering. If you pass, you find $1 for each success you rolled.');
  Add('GENSTORE',   EXP_TKIY,  19, 'The shopkeeper has heard of your recent exploits and is terrified that '+
                                   'you''ll bring bad luck down on his store! Make a Luck (-1) check. If you '+
                                   'pass, he throws money from the till at you, and begs you to leave. Gain $2. '+
                                   'If you fail, you are moved to the street.');
  Add('GENSTORE',   EXP_TKIY,  20, 'The shopkeeper opens up the secondhand section of the store. You may sell '+
                                   'any Common Items or Unique Items you have for half list price (round up).');
  Add('GRAVEYARD',  EXP_TKIY,  17, 'An old-fashioned horse-drawn hearse creaks past on the road, and you just '+
                                   'know that something wicked is coming. All Undead monsters in Arkham, the '+
                                   'Outskirts, and the Sky move to this location. You must immediately evade or '+
                                   'fight them.');
  Add('GRAVEYARD',  EXP_TKIY,  18, 'Pass a Sneak (-2) check to catch a glimpse of the actors rehearsing for '+
                                   '"The King in Yellow," and gain 2 Clue tokens. If you fail, they notice your '+
                                   'hiding spot and you are blinded by a flash of yellow light. You are '+
                                   'delayed.');
  Add('GRAVEYARD',  EXP_TKIY,  19, 'Walking through the graveyard, you see a faint glow ahead. Following it, '+
                                   'you discover an ancient tombstone covered in luminescent wormwood. Reading '+
                                   'the tombstone by the light of the strange fungus, you discover an important '+
                                   'fact. Gain 1 Clue token.');
  Add('GRAVEYARD',  EXP_TKIY,  20, 'You see a horrid shape descend from the sky, carrying a body. Pass a Will '+
                                   '(-2) check or lose 2 Sanity. If you pass, you watch it descend toward the '+
                                   'Black Cave. If you follow it, gain 2 Clue tokens and move to the Black Cave, '+
                                   'where you immediately have another encounter.');
  Add('HROADHOUSE', EXP_TKIY,  17, 'A regular needs funds to get out of town, fast. He offers to sell you '+
                                   'whatever is in his trunk. Make a Will (+0) check to convince him to show you '+
                                   'his best goods. If you pass, draw a number of Common Items equal to the '+
                                   'number of successes you rolled, and purchase any that you wish for their '+
                                   'list price. Discard the rest.');
  Add('HROADHOUSE', EXP_TKIY,  18, 'Make a Speed (-1) check to complete a transaction. If you pass, you make $2 '+
                                   'out of the deal. If you fail, someone catches you doing something you '+
                                   'shouldn''t, and blackmails you. You either lose $5 or, if you either cannot '+
                                   'or will not pay, you are reduced to 1 Stamina.');
  Add('HROADHOUSE', EXP_TKIY,  19, 'The only empty seat is next to a strange, diminutive man. He has no ears, '+
                                   'and is missing all of the fingers on his left hand. If you pass a Luck (+0) '+
                                   'check, he cackles, says "You did well, though you knew it not," and hands '+
                                   'you $2.');
  Add('HROADHOUSE', EXP_TKIY,  20, 'The proprietor asks you to clean out the old shed and offers you your '+
                                   'choice of money or whatever you find inside. You may either gain $1 or draw '+
                                   '2 Common Items, keeping one and discarding the other.');
  Add('HSOCIETY',   EXP_TKIY,  17, 'A retired actor, once the favorite of European theater, gestures to you. '+
                                   '"Take this, my young friend," he says. "You''ll need it against what''s '+
                                   'coming." He hands you a collection of news articles regarding the run of '+
                                   '"The King in Yellow" in Paris. Pass a Lore (-1) check to sense an arcane '+
                                   'pattern to them and draw a Spell. If you fail, you must discard 2 Clue '+
                                   'tokens, if able.');
  Add('HSOCIETY',   EXP_TKIY,  18, 'An actor from "The King in Yellow" leads a theater course. It''s amazing '+
                                   'what skills an actor needs to master in order to look like the real thing. '+
                                   'Pass a Will (-2) check to draw Skill cards equal to the number of successes '+
                                   'rolled. Keep one, and discard the rest. If you fail, you learn something you '+
                                   'wish you hadn''t in the theater exercises, and are Cursed.');
  Add('HSOCIETY',   EXP_TKIY,  19, 'The Historical Society is holding more educational discussion groups than '+
                                   'normal, thanks to the buzz of the "King in Yellow" performances. Make a (+0) '+
                                   'check in your lowest current skill. If you pass, draw 1 Skill.');
  Add('HSOCIETY',   EXP_TKIY,  20, 'The society''s latest treasure, an ancient cask from Europe, is not '+
                                   'altogether harmless. A monster appears when it is opened, attacking you. If '+
                                   'you pass a Combat check against the monster, you find it was entombed with '+
                                   'an ancient scroll. Draw 1 Spell.');
  Add('INDSQUARE',  EXP_TKIY,  17, 'A fluttering yellow leaf falls from the old oak in the center of the '+
                                   'square, and you glimpse a design on its surface. Make a Speed (-1) check to '+
                                   'catch it before it falls among the other leaves. If you pass, you see that '+
                                   'the leaf''s veins form the shape of the Yellow Sign: Gain 1 Clue token.');
  Add('INDSQUARE',  EXP_TKIY,  18, 'A storm strikes in the midst of rehearsals, and the actors flee for cover, '+
                                   'leaving some of their props behind. Pass a Lore (-2) check to realize that '+
                                   'one of the props is real, and draw a Unique Item.');
  Add('INDSQUARE',  EXP_TKIY,  19, 'Pass a Sneak (-2) check to catch a glimpse of the actors rehearsing for the '+
                                   'play, gaining 2 Clue tokens. If you fail, no sooner do they notice you than '+
                                   'a monster appears!');
  Add('INDSQUARE',  EXP_TKIY,  20, 'You see someone battling a monster and rush to help. A monster appears! If '+
                                   'you fight and defeat it, you may roll a number of dice equal to its '+
                                   'toughness. If you roll a success, you may draw a random Ally. If you do not '+
                                   'roll any successes, you may draw a Unique Item.');
  Add('ISANCTUM',   EXP_TKIY,  17, 'A strange maze-like symbol has been carved in the wall. Do you dare to '+
                                   'follow it with your eyes? If so, pass a Will (+0) check to gain a Clue '+
                                   'token. If you fail, you lose 1 Sanity.');
  Add('ISANCTUM',   EXP_TKIY,  18, 'Entering the workroom, you see a smith working on an ancient heirloom. He '+
                                   'says "Your piece is finished, you vulture," and throws it at you in disgust. '+
                                   'Make a Speed (-2) check. If you pass, you may search the Unique Item deck '+
                                   'and take the first Weapon you find. If you fail, you lose 2 Stamina.');
  Add('ISANCTUM',   EXP_TKIY,  19, 'Membership has it privileges. Pass a Will (-1) check to draw Unique Items '+
                                   'equal to the number of successes. You may purchase any of the items drawn, '+
                                   'using any combination of money, Clue tokens (1 Clue token = $2), or Spells '+
                                   '(1 Spell = $3).');
  Add('ISANCTUM',   EXP_TKIY,  20, 'The members are extremely concerned about the celestial bodies being '+
                                   '"changed" by some outside force, ask you to investigate. Make a Lore (-1) '+
                                   'check. If you pass, you gain 2 Clue tokens and draw a Spell to aid you on '+
                                   'your mission.');
  Add('LIBRARY',    EXP_TKIY,  17, 'Some archaeology professors seem to be having a wager, and they call you '+
                                   'into the room to have fun at your expense. "Be a good sport, and try to pick '+
                                   'out the antique from these fakes we made up, will you?" If you pass a Lore '+
                                   '(-1) check, you may draw and keep 1 Unique Item.');
  Add('LIBRARY',    EXP_TKIY,  18, 'The door closes with a bang! You bolt upright from the book you fell asleep '+
                                   'over. The library is closed for the night, and you are locked in. You are '+
                                   'delayed. However, you may search the Unique Item deck and take the first '+
                                   'Tome you find.');
  Add('LIBRARY',    EXP_TKIY,  19, 'You aren''t the only one interested in "The King in Yellow." All Maniacs '+
                                   'and Cultists in Arkham, the Sky, and the Outskirts move to your location. '+
                                   'You must immediately evade or defeat them.');
  Add('LIBRARY',    EXP_TKIY,  20, 'You check out a book of essays on the infamous "The King in Yellow." Make a '+
                                   'Will (+0) check. If you pass, you find a Spell scribbled in the margins. If '+
                                   'you fail, you lose 1 Sanity.');
  Add('MBHOUSE',    EXP_TKIY,  17, 'Ma Mathison comments that you look pallid, and suggests some yard work to '+
                                   'get you feeling fit. Pass a Sneak (-1) check to sneak a nap in the shed '+
                                   'instead and gain 2 Stamina. If you fail, lose 1 Stamina from Ma''s "tough '+
                                   'love" prescription.');
  Add('MBHOUSE',    EXP_TKIY,  18, 'Ma Mathison offers you a free night''s stay so that she doesn''t have open '+
                                   'rooms in case "one o'' them actor types looks to board here." You regain 1 '+
                                   'Stamina, but pass a Luck (-1) check or you lose 1 Sanity due to bad dreams.');
  Add('MBHOUSE',    EXP_TKIY,  19, 'You black out somewhere in Southside and wake up to find yourself in the '+
                                   'Boarding House. Regain 1 Stamina, then make a Fight (+1) check. If you fail, '+
                                   'you regain another Stamina, but you fall back asleep and are delayed.');
  Add('MBHOUSE',    EXP_TKIY,  20, 'You wake up to find your bed burning! Pass a Speed (+0) check to escape. If '+
                                   'you fail, you are lost in time and space. In any event, there is no sign of '+
                                   'the fire afterwards.');
  Add('PSTATION',   EXP_TKIY,  17, 'A protestor was arrested outside a performance of "The King in Yellow," and '+
                                   'his ranting can be heard from the cells. Pass a Lore (-1) check to gain a '+
                                   'Clue Token.');
  Add('PSTATION',   EXP_TKIY,  18, 'Sheriff Engle is training security guards for performances of "The King in '+
                                   'Yellow," but the training is rigorous. Make a Fight (-1) check to qualify. '+
                                   'If you pass, you may search the Common Item deck and take the first Weapon '+
                                   'you find. If you fail, you lose 1 Stamina.');
  Add('PSTATION',   EXP_TKIY,  19, 'The police department is decommissioning one of its paddy wagons and '+
                                   'empties its trunk into the garbage. Pass a Luck (+1) check to draw a number '+
                                   'of Common Items equal to the successes rolled. Choose one Item and discard '+
                                   'the rest.');
  Add('PSTATION',   EXP_TKIY,  20, 'You''re called in for your expertise in the unusual to help examine a '+
                                   'violent man who attacked cast members of "The King in Yellow." Make a Lore '+
                                   '(-1) check. If you pass, gain 2 Clue Tokens. If you fail, Sheriff Engle '+
                                   'demands that you stay and sort out the case. Stay here next turn.');
  Add('RDOCKS',     EXP_TKIY,  17, 'A crate bobs by the dock. Pass a Fight (-2) check to pull it from the river '+
                                   'and draw 1 Common Item.');
  Add('RDOCKS',     EXP_TKIY,  18, 'A shambling heap clambers from the river and engulfs you. If you pass a '+
                                   'Fight (-2) check, you find a Common Item in the aftermath. Otherwise, lose 1 '+
                                   'Stamina.');
  Add('RDOCKS',     EXP_TKIY,  19, 'If you have any Tomes but no Weapons, a crew of roustabouts mocks you for '+
                                   'your "book learning" and begins to push you around. Lose 2 Stamina.');
  Add('RDOCKS',     EXP_TKIY,  20, 'The leading lady of "The King in Yellow" arrives via a steamer packet from '+
                                   'the coast. She confuses you for a porter and hands you her bags to carry. '+
                                   'Make a Luck (-1) check. If you pass, she leaves one of them with you as a '+
                                   'souvenir. Draw 1 Common Item. If you fail, she accuses you of trying to '+
                                   'steal it and you are arrested.');
  Add('SBUILDING',  EXP_TKIY,  17, '"It''s a simple transference principle, really," the professor explains. '+
                                   '"Simply place an everyday item on this platform..." If you discard a Common '+
                                   'Item, you may roll a number of dice equal to the item''s cost. You may draw '+
                                   'a number of cards from the Unique Item deck equal to the number of successes '+
                                   'rolled, keeping one and discarding the rest.');
  Add('SBUILDING',  EXP_TKIY,  18, 'A lab fire breaks out and the students are trapped inside! If you force '+
                                   'your way in and save them, make a Fight (-2) check. If you pass, you rescue '+
                                   'the students and one of the rewards you with a family heirloom. Draw 1 '+
                                   'Unique Item. If you fail, lose 2 Stamina.');
  Add('SBUILDING',  EXP_TKIY,  19, 'When paranoia and fear set in, accidents are more common. Make a Speed '+
                                   'check with a penalty equal to the current terror level. If you fail, your '+
                                   'Stamina is reduced to 0 in a lab accident.');
  Add('SBUILDING',  EXP_TKIY,  20, 'You watch, disturbed, as two students immerse a live rabbit in fluid, '+
                                   'instantly transforming it to marble! Make a Sneak (-1) check to take the '+
                                   'fluid before they can do anything dangerous with it. If you pass, search the '+
                                   'Unique Item deck for Petrifying Solution and take it. If you fail, they '+
                                   'catch you in the act and splash some of the fluid on you. You are delayed.');
  Add('STLODGE',    EXP_TKIY,  17, '"Tut-tut," says Carl Sanford. "A sound mind is essential for membership, '+
                                   'I''m afraid." For each point of Sanity you have, you may roll a die. If you '+
                                   'roll any successes, you may draw a Twilight Lodge Membership card. For each '+
                                   'unsuccessful die you roll, you lose 1 Sanity.');
  Add('STLODGE',    EXP_TKIY,  18, 'A lovely young woman stumbles into you as you''re searching for the '+
                                   'library. "Pardon me," she says, "my name is Constance Hawberk. Have you seen '+
                                   'my father?" Pass a Luck (-1) check to point her in the right direction. In '+
                                   'return, she points you to the library and you gain 2 Clue tokens.');
  Add('STLODGE',    EXP_TKIY,  19, 'The members are extremely concerned about something regarding the celestial '+
                                   'bodies being "changed" by some outside force. Pass a Sneak (-2) check to '+
                                   'gain 2 Clue tokens. If you fail, you are pushed out into the street.');
  Add('STLODGE',    EXP_TKIY,  20, 'When you inquire about membership, the lodge members get a gleam in their '+
                                   'eyes. If you have an Ally, you may discard it to take both a Silver Twilight '+
                                   'Membership card and a Unique Item, but you are Cursed. If you do not have an '+
                                   'Ally or do not wish to discard one, pass a Fight (-3) check or you are lost '+
                                   'in time and space.');
  Add('SCHURCH',    EXP_TKIY,  17, '"A strong soul must be willing to make sacrifices," Father Michael says. '+
                                   'You may discard a single beneficial Investigator card (a Spell, Item, Ally, '+
                                   'etc.) to make a Luck (+1) check. If you pass, you are restored to full '+
                                   'Sanity. If you fail, you gain only 1 Sanity.');
  Add('SCHURCH',    EXP_TKIY,  18, 'A man attacks Father Michael as he tends to the grounds! Pass a Fight (-1) '+
                                   'check to drive the man off. If you fail, you are Cursed.');
  Add('SCHURCH',    EXP_TKIY,  19, 'An esteemed organist from the Church of St. Barnabe in France has been '+
                                   'haunting South Church, disturbing the flock with his otherworldly playing. '+
                                   'Father Michael asks you to convince him to leave. Pass a Fight (-2) check to '+
                                   'intimidate him into leaving and gain 2 Sanity. If you fail, he troubles your '+
                                   'dreams, and you are reduced to 1 Sanity.');
  Add('SCHURCH',    EXP_TKIY,  20, 'You admire a new stained-glass window from the pews, but if you could peer '+
                                   'directly through it, how illuminated life would seem! Make a Fight (-2) '+
                                   'check to climb up to it safely. If you pass, gain 1 Sanity. If you fail. '+
                                   'lose 2 Stamina.');
  Add('STMHOSPITAL',EXP_TKIY,  17, 'Nurse Sharon asks for your help in organizing some records that were '+
                                   'accidentally dropped and scattered. Pass a Lore (+0) check to gain 1 Clue '+
                                   'token.');
  Add('STMHOSPITAL',EXP_TKIY,  18, 'The doctors know that something strange is going on, but don''t have time '+
                                   'to talk. If you want to question them, you''ll need to look like you need '+
                                   'medical aid. For each point of Stamina you are below you maximum, you may '+
                                   'roll 1 die. Gain 1 Clue token for each success.');
  Add('STMHOSPITAL',EXP_TKIY,  19, 'The hospital has a ward for special cases, but it is off-limits to the '+
                                   'public. Make a Sneak (-3) check and gain 1 Clue token for each success you '+
                                   'roll.');
  Add('STMHOSPITAL',EXP_TKIY,  20, 'You stumble upon an autopsy room. Make a Will (-2) check to stay calm while '+
                                   'you investigate. If you pass, gain 2 Clue tokens. If you fail, lose 1 '+
                                   'Stamina as you cut yourself on one of the autopsy implements.');
  Add('TUNNAMABLE', EXP_TKIY,  17, 'A gleam of metal draws your attention to the fireplace, which suddenly '+
                                   'ignites! You may attempt a Speed (-3) check to pull an item from the fire '+
                                   'before it is destroyed. If you pass, draw 1 Unique Item. If you attempt it '+
                                   'and fail, lose 1 Stamina.');
  Add('TUNNAMABLE', EXP_TKIY,  18, 'A useful weapon sits here in the center of a pentagram. Search the Unique '+
                                   'Item deck and look at the first Weapon you find. You may either keep it and '+
                                   'be Cursed or discard it and gain 1 Clue token.');
  Add('TUNNAMABLE', EXP_TKIY,  19, 'A voice - perhaps the house itself - begins whispering to you. Make a Will '+
                                   '(-2) check. Gain 1 Clue token for each success, but lose either 1 Stamina or '+
                                   '1 Sanity if you fail.');
  Add('TUNNAMABLE', EXP_TKIY,  20, 'As you look out of an upstairs window, you see an unfamiliar cityscape with '+
                                   'twin suns setting over strange towers. Gain 1 Clue token, but you must pass '+
                                   'a Will (-2) check or lose 1 Sanity.');
  Add('TWHOUSE',    EXP_TKIY,  17, '"What a shame," a voice whispers, "such unused potential." Search the '+
                                   'Unique Item deck and take the first Tome you find. If it requires a skill '+
                                   'check to read, then you may immediately make a check to read it, without '+
                                   'spending any movement points to do so.');
  Add('TWHOUSE',    EXP_TKIY,  18, 'A muffled cry and some thumping comes from a nearby closet. Pass a Fight '+
                                   '(-2) check to open it and rescue whoever is inside, drawing a random Ally. '+
                                   'If you fail, whatever trapped him attacks you too: A monster appears.');
  Add('TWHOUSE',    EXP_TKIY,  19, 'A woman poses by a window; the dim light revealing the outline of her '+
                                   'beautiful figure, but hiding her face. "Will you paint me?" she asks. Make a '+
                                   'Luck (-2) check. If you pass, you find a painting of the woman where she was '+
                                   'standing. It has a Spell scribed on the back. Draw one Spell. If you fail, a '+
                                   'monster appears!');
  Add('TWHOUSE',    EXP_TKIY,  20, 'An artist''s address book lies on a table with a list of names: Lizzie '+
                                   'Burke, Pinkie McCormick, Tessie. You feel like you know them all, or knew '+
                                   'them, and feel a stab of sadness. Gain 1 Clue token, but pass a Will (+0) '+
                                   'check or lose 1 Sanity.');
  Add('TSTATION',   EXP_TKIY,  17, 'A porter drops what looks like an ancient relic on the tracks. If you want '+
                                   'to try and grab it, make a Speed (-3) check. If you pass, you may draw 1 '+
                                   'Unique Item. If you fail, you are reduced to 0 Stamina by the oncoming '+
                                   'train.');
  Add('TSTATION',   EXP_TKIY,  18, 'Make a Fight (-2) [2] check as you help unload the set materials for "The '+
                                   'King in Yellow." If you pass, you are rewarded. Draw 1 Unique Item. If you '+
                                   'roll only one success, you are given 1 Common Item. If you fail, you overdo '+
                                   'it, and lose 1 Stamina.');
  Add('TSTATION',   EXP_TKIY,  19, 'Pass a Luck (+1) check to find an unlabeled crate and draw both 1 Unique '+
                                   'Item and 1 Common Item. You must either purchase both of them at list price '+
                                   'or discard them both.');
  Add('TSTATION',   EXP_TKIY,  20, 'The porter went into that train car half an hour ago, and he hasn''t come '+
                                   'out. If you investigate, you find his mutilated corpse clutching an item! '+
                                   'Lose 2 Sanity but draw 1 Common Item.');
  Add('UISLE',      EXP_TKIY,  17, 'A monster appears! If you pass a Combat check against it, you find its skin '+
                                   'is covered with the scrawl of archaic runes, and may draw 1 Spell.');
  Add('UISLE',      EXP_TKIY,  18, 'A monster is attacking a huddled figure in the shadows. If you pass the '+
                                   'first Combat check you make against the monster, you may draw a random Ally '+
                                   'or Spell.');
  Add('UISLE',      EXP_TKIY,  19, 'The clouds overhead begin to spiral. Pass a Lore (-1) check to make out the '+
                                   'symbol of the Yellow Sign and gain 1 Clue token.');
  Add('UISLE',      EXP_TKIY,  20, 'You watch two women walk the island while they speak of the Hyades, Hali, '+
                                   'and Lost Carcosa. Gain 1 Clue token, then make a Sneak (-2) check. If you '+
                                   'pass, you hear further details, gaining 1 more Clue token. If you fail, they '+
                                   'see you and call upon protection. A monster appears!');
  Add('VDINER',     EXP_TKIY,  17, 'Velma decides to treat you to a hero''s feast. Roll a die for each gate or '+
                                   'monster trophy you have. For each success you roll, gain 1 Stamina.');
  Add('VDINER',     EXP_TKIY,  18, 'You bite into a biscuit and find a plump, white grave worm writhing inside! '+
                                   'Make a Fight (+1) check to keep your lunch down. If you fail, lose 1 '+
                                   'Stamina.');
  Add('VDINER',     EXP_TKIY,  19, 'You forgot to pay for your meal. Make a Luck (+0) check. If you pass, you '+
                                   'realize it later and Velma tells you not to worry about it, so nothing '+
                                   'happens. If you fail, she sends Deputy Dingby after you. You are taken to '+
                                   'the Police Station and arrested, unless you''re the Deputy.');
  Add('VDINER',     EXP_TKIY,  20, 'You overhear a man threatening an elderly woman with blackmail. He shows '+
                                   'her an envelope, smiles, then returns it to his pocket and heads for the '+
                                   'door. Make a Sneak (-1) check to lift the envelope from his pocket. If you '+
                                   'pass, you may either look inside to gain a Clue token or sell it back to the '+
                                   'woman for $1.');
  Add('WOODS',      EXP_TKIY,  17, 'An easel and paints have been left here, abandoned by the artist. Not far '+
                                   'away is the still life he was painting. Draw a card from the Common Item '+
                                   'deck. If it is a Weapon, discard it. Otherwise, keep it.');
  Add('WOODS',      EXP_TKIY,  18, 'Strange coins have been strewn about the glade, forming an odd symbol that '+
                                   'pains you to see. Pass a Will (+0) check to gain $1. You may continue '+
                                   'checking until you fail, gaining $1 each time, but with the modifier '+
                                   'decreasing by -1 with each check. If you fail, you lose 1 Sanity for every '+
                                   '$1 you''ve gained from this encounter.');
  Add('WOODS',      EXP_TKIY,  19, 'Yellow-robed actors are re-enacting some sort of battle in the woods... or '+
                                   'are they rehearsing for a battle yet to come? Pass a Sneak (-1) check to '+
                                   'search the Common Item deck and take the first Weapon you find. If you fail, '+
                                   'you are attacked and lose 2 Stamina.');
  Add('WOODS',      EXP_TKIY,  20, 'You see a woman pouring blood on a field of flowers. When you move closer, '+
                                   'she is gone. Make a Luck (+1) check. If you pass, she left her jewelry among '+
                                   'the blood, and you gain $3. If you fail, the strange combination of blood '+
                                   'and flowers is toxic and you lose 2 Stamina.');
  Add('YOMSHOPPE',  EXP_TKIY,  17, '"Ah, there you are. That item you ordered has come in." Oddly enough, you '+
                                   'ordered no such item. If you wish, you may make a Will (-2) check to '+
                                   'impersonate the rightful owner. If you pass, you may draw 1 Unique Item. If '+
                                   'you fail, you are arrested.');
  Add('YOMSHOPPE',  EXP_TKIY,  18, 'Behind a bookshelf, you hear a woman whisper, "I have killed him I loved; '+
                                   'the world''s athirst, now let it drink." When you look down that aisle, '+
                                   'there''s no one there, but there is an item resting on the floor. Draw 1 '+
                                   'Unique Item. You may purchase it for half list price (round up).');
  Add('YOMSHOPPE',  EXP_TKIY,  19, 'Miriam Beecher eyes you carefully. "Hmm, if we''re going to survive, I''d '+
                                   'better teach you this." Draw 2 Spells, keeping 1 and discarding the other.');
  Add('YOMSHOPPE',  EXP_TKIY,  20, 'No one is manning the shop, but an intriguing item is sitting on the '+
                                   'counter. Draw 1 Unique Item. You may either discard it, keep it and pay its '+
                                   'list price, or keep it without paying for it and be Cursed.');
  Add('ABUILDING',  EXP_TKIY,  21, 'A student is angrily complaining about his research being called "too '+
                                   'radical". He needs funds badly and would be willing to sell you his work. '+
                                   'You may pay $5 to draw 1 Spell.');
  Add('ABUILDING',  EXP_TLATT, 22, 'You catch sight of one of the professors chanting quietly over talismans '+
                                   'she had hidden in her desk. Make a Sneak (-1) check or she Curses you!');
  Add('ABUILDING',  EXP_TLATT, 23, 'You encounter a student trying unsuccessfully to get a refund on tuition he '+
                                   'overpaid. He''s having a hard time getting anyone to listen to him. Make a '+
                                   'Will (-2) check to help him out. If you pass, he gets his refund and '+
                                   'gratefull gives you $2.');
  Add('ABUILDING',  EXP_TLATT, 24, 'You own copies of some of the books being used this semester. Make a Luck '+
                                   '(+1) check to find students willing to purchase your used copies of the '+
                                   'texts. If you pass, gain $2.');
  Add('ARKASYLUM',  EXP_TKIY,  21, 'A patient becomes irrationally possessive over one of your belongings. Make '+
                                   'a Fight (-3) check. If you fail choose 1 Common Item or Unique Item and '+
                                   'discard it.');
  Add('ARKASYLUM',  EXP_TLATT, 22, 'A seemingly-sane inmate is willing to pay you to help him escape. If you '+
                                   'agree to help, you may make a Sneak (-1) check. If you succeed, gain $3. If '+
                                   'you fail, you are arrested.');
  Add('ARKASYLUM',  EXP_TLATT, 23, 'The doctors allow you to observe the therapy session of one of the '+
                                   'asylum''s most disturbed patients. Make a Will (-1) check to maintain your '+
                                   'wits enough to garner useful information from his story. If you pass, gain 2 '+
                                   'Clue tokens. Then, whether you pass or not, lose 1 Sanity after learning of '+
                                   'his bone-chilling experiences.');
  Add('ARKASYLUM',  EXP_TLATT, 24, 'You discover that the patient you''ve been looking for has been '+
                                   'lobotomized. He can''t answer your questions now. Draw one Ally card from '+
                                   'the Ally deck and return it to the box.');
  Add('BOARKHAM',   EXP_TKIY,  21, 'A child is struggling to bring an enormous jar of pennies to the teller. '+
                                   'You may make a Fight (-1) check to help him out. If you pass, gain 1 Sanity '+
                                   'and $1 for your efforts. If you fail, lose 1 Stamina.');
  Add('BOARKHAM',   EXP_TLATT, 22, 'A large painting of historic Arkham hangs in the bank lobby. Examining it, '+
                                   'you notice an unnerving circle of stones barely visible on the edge of the '+
                                   'city. Lose 1 Sanity.');
  Add('BOARKHAM',   EXP_TLATT, 23, 'A young woman is examining the contents of a safe deposit box bequethed to '+
                                   'her by her late mother. It is an ancient book written in a language she '+
                                   'doesn''t understand, and she asks you if you recognize the language. Make a '+
                                   'Lore (-1) [2] check. If you pass, gain 2 Clue tokens as you decipher the '+
                                   'text.');
  Add('BOARKHAM',   EXP_TLATT, 24, 'You find a penny with a strange sigil carved into it. Amused, you flip it '+
                                   'in the air, but then gasp as you feel the sudden gathering of magical forces '+
                                   'around you. Make a Luck (-2) check. If you pass, the penny comes up heads. '+
                                   'You are Blessed. If you fail, it comes up tails. you are Cursed.');
  Add('BCAVE',      EXP_TKIY,  21, 'Outside the cave, someone hung a package from a tree, presumably to keep it '+
                                   'safe from curious wildlife. Make a Luck (-2) check to see if the contents '+
                                   'have been left alone. If you pass, gain 1 Common Item.');
  Add('BCAVE',      EXP_TLATT, 22, 'Within the cave, you find the remains of a fire, candles, and other signs '+
                                   'that a ritual has been attempted here. Whoever it was left some handwritten '+
                                   'notes. Make a Lore (+0) [2] check. If you pass, gain 1 Spell.');
  Add('BCAVE',      EXP_TLATT, 23, 'You''ve gone so far into the cave, you fear it will take you a long time to '+
                                   'find your way back. There''s a small, difficult-to-navigate passage that may '+
                                   'be faster. Make a Fight (-2) check to squeeze through the smaller cave. If '+
                                   'you fail, stay here next turn while you go back the long way.');
  Add('BCAVE',      EXP_TLATT, 24, 'Your presence has upset a large number of bats. As they fly about you, make '+
                                   'a Will (-2) check. If you fail, you run blindly through the dark and lose 1 '+
                                   'Stamina as you knock into the cave walls.');
  Add('CSHOPPE',    EXP_TKIY,  21, '"According to legend, this mirror was once used to travel from our world '+
                                   'into the lands beyond. Does this interest you?" If you wish, you may discard '+
                                   'any Common Item, Unique Item, or Spell to move to the first area of any '+
                                   'Other World.');
  Add('CSHOPPE',    EXP_TLATT, 22, 'Oliver Thomas has an extremely rare book on display, but it is not for '+
                                   'sale. He''s willing to let you have a look at it. Make a Will (-1) check to '+
                                   'quickly memorize as much as you can of this informative text. Gain 1 Clue '+
                                   'token for each success you roll.');
  Add('CSHOPPE',    EXP_TLATT, 23, 'Oliver Thomas, the shopkeeper, greets you enthusiastically. "There was an '+
                                   'item here earlier that I just knew was meant for you. I''m not sure where it '+
                                   'went, but I imagine if it was meant to be, you''ll be able to find it." Make '+
                                   'a Will (-2) check. If you pass, gain 1 Unique Item. If you fail, gain 1 '+
                                   'Common Item.');
  Add('CSHOPPE',    EXP_TLATT, 24, 'Other customers are intrigued by your knowledge of the items in the shop. '+
                                   'The more you describe the histories of these objects, the more people '+
                                   'purchase. Make a Lore (+0) check. If you pass, Oliver Thomas is so grateful '+
                                   'for your help with sales that he offers you $3 for your efforts.');
  Add('GENSTORE',   EXP_TKIY,  21, 'A customer is angrily demanding his money back for an item he claims is '+
                                   'defective. The shopkeeper argues that there''s nothing wrong with it. The '+
                                   'customer shoves the item in your hands and storms off in a huff. Gain 1 '+
                                   'Common Item.');
  Add('GENSTORE',   EXP_TLATT, 22, 'A tall set of shelves containing hardware suddenly tips over! Make a Speed '+
                                   '(-1) check. If you fail, lose 2 Stamina.');
  Add('GENSTORE',   EXP_TLATT, 23, 'Something has turned all the food in the store rancid. The shopkeeper '+
                                   'offers to pay if you help him throw it all away. You may make a Will (-2) '+
                                   'check to give it a try. If you pass, gain $2. If you fail, lose 1 Stamina.');
  Add('GENSTORE',   EXP_TLATT, 24, 'Sometime in the middle of the night, someone broke into the store and '+
                                   'created arcane designs on the floor with lines of salt. Make a Lore (-1) '+
                                   'check to recognize the significance. If you pass, gain 1 Clue token.');
  Add('GRAVEYARD',  EXP_TKIY,  21, 'Miriam Beecher is kneeling by a grave, apparently talking to someone you '+
                                   'can neither see nor hear. Make a Sneak (-2) check to hear her half of the '+
                                   'conversation. If you pass, gain 2 Clue tokens.');
  Add('GRAVEYARD',  EXP_TLATT, 22, 'One of the headstones has a strange riddle inscribed on it. Make a Lore '+
                                   '(-2) check to interpret it. If you pass, you press a button hidden among the '+
                                   'various symbols adorning the grave to reveal a secret compartment and gain 1 '+
                                   'Unique Item. If you fail, nothing happens.');
  Add('GRAVEYARD',  EXP_TLATT, 23, 'To your horror, you discover a grave bearing today''s date and the name of '+
                                   'someone you know well. Choose one of your Ally cards to discard. If you '+
                                   'don''t have any, choose a random card from the Ally deck and return it to '+
                                   'the box. If there are no Ally cards available, there is no effect.');
  Add('GRAVEYARD',  EXP_TLATT, 24, 'You strike up a conversation with a man digging a grave. He''s got a wry '+
                                   'wit that puts all the doom and gloom you''ve experienced into perspective. '+
                                   'Gain 1 Sanity.');
  Add('HROADHOUSE', EXP_TKIY,  21, '"Care to make a couple extra bucks?" The proprietor needs some help moving '+
                                   'in the new pool table. Make a Fight (-1) check and gain $2 if you pass.');
  Add('HROADHOUSE', EXP_TLATT, 22, 'A barfly sits down next to you and shares boring and incoherent stories. '+
                                   'Make a Will (-1) check to endure these dull tales until he''s finished '+
                                   'talking. If you pass, he tells you, "You''re a good sort," and offers you a '+
                                   'gift. Draw 1 Common Item.');
  Add('HROADHOUSE', EXP_TLATT, 23, 'A man with an accordian is playing tunes and everybody is singing along. If '+
                                   'you choose to stay late into the evening, gain 2 Sanity, but lose 1 '+
                                   'Stamina.');
  Add('HROADHOUSE', EXP_TLATT, 24, 'Whoever was sitting here before you used a knife to carve a horribe symbol '+
                                   'into the surface of the table. Make a Will (-1) check and lose 1 Sanity if '+
                                   'you fail. Then, whether you passed or not, search the Common Item deck for '+
                                   'the Knife and take it.');
  Add('HSOCIETY',   EXP_TKIY,  21, '"After my husband passed away, I thought the Society would be interested in '+
                                   'his documents. He was very influential in Arkham." Make a Luck (-2) check to '+
                                   'see if the curator recognizes their arcane significance. If you pass, gain 1 '+
                                   'Spell as the Society passes these papers off to you.');
  Add('HSOCIETY',   EXP_TLATT, 22, 'A guest lecturer provides a lengthy but informative presentation about his '+
                                   'explorations of ancient sites. You may make a Lore (-1) [2] check and stay '+
                                   'here next turn. If you pass, gain 1 Skill.');
  Add('HSOCIETY',   EXP_TLATT, 23, 'While researching, you find a story about a series of disappearances that '+
                                   'occurred in the earliest days of Arkham. Coincidentally, you notice a '+
                                   'newspaper reporting a similar disappearance just last week. Return 1 Ally at '+
                                   'random from the Ally deck to the box. Then gain 3 Clue tokens.');
  Add('HSOCIETY',   EXP_TLATT, 24, 'You encounter a friendly old professor from Miskatonic University. If you '+
                                   'spend 1 Gate trophy, he introduces himself as Professor Armitage and offers '+
                                   'to join forces with you. Take his Ally card if it is available; otherwise, '+
                                   'draw 1 Unique Item.');
  Add('INDSQUARE',  EXP_TKIY,  21, 'A bronze plate near Founder''s Rock commemorates the establishing of the '+
                                   'city. You notice that a line of odd symbols runs along the border of the '+
                                   'marker. Make a Lore (-1) check to interpret their meaning. If you pass, gain '+
                                   '1 Spell.');
  Add('INDSQUARE',  EXP_TLATT, 22, 'An old gypsy man is being attacked by a mysterious robed figure. Make a '+
                                   'Fight (-2) check to help fend off the assailant. If you pass, the gypsy '+
                                   'insists you accept a token of his gratitude. Gain 1 Unique Item.');
  Add('INDSQUARE',  EXP_TLATT, 23, 'You hoped to get near enough to the gypsy camp to eavesdrop, but a dog bark '+
                                   'has alerted them that there is an intruder. Make a Sneak (-1) check to '+
                                   'escape! If you fail, you are Cursed.');
  Add('INDSQUARE',  EXP_TLATT, 24, 'You start digging in a patch of grond where, as long as you can recall, no '+
                                   'grass has ever grown. Make a Luck (-2) check. If you pass, gain 2 Clue '+
                                   'tokens as you unearth a pocket watch inscribed with the name of a man who '+
                                   'went missing decades ago. If you fail, lose 1 Stamina for exhausting '+
                                   'yourself fruitlessly.');
  Add('ISANCTUM',   EXP_TKIY,  21, '"Admiring our library?" Carl Sanford asks you. "Membership has privileges. '+
                                   'Borrow one of our texts if you wish." Search Unique Item deck and take the '+
                                   'first Tome you find.');
  Add('ISANCTUM',   EXP_TLATT, 22, 'Carl Sanford accuses you of stealing from the Lodge. Make a Will (-1) check '+
                                   'to prove that you''ve been framed. If you fail, lose 1 Stamina and your '+
                                   'Silver Twilight Membership, and then move to the streets. If you pass, there '+
                                   'is no effect.');
  Add('ISANCTUM',   EXP_TLATT, 23, 'The Lodge Members have gathered to perform a powerful banishment ritual. '+
                                   'Make a Lore (-2) check. If you pass, you may either gain 2 Clue tokens or '+
                                   'choose one monster in the same location as an open Gate and return that '+
                                   'monster to the monster cup.');
  Add('ISANCTUM',   EXP_TLATT, 24, 'Within this spiritually attuned chamber, you find that if you open your '+
                                   'mind to the spirit world, the spirits will bestow eldritch knowledge upon '+
                                   'you. Gain up to 3 Spells and then lose 1 Sanity for each spell chosen.');
  Add('LIBRARY',    EXP_TKIY,  21, 'A particularly ancient and tattered text provides vital information. Make a '+
                                   'Lore (-2) check and gain 1 Clue token for each success. Regardless of the '+
                                   'result, lose 1 Stamina as the mold infiltrates your lungs.');
  Add('LIBRARY',    EXP_TLATT, 22, 'Someone left the door to the basement unlocked! There''s an abundance of '+
                                   'texts and artifacts hidden away down here, but most of it is useless to you. '+
                                   'Make a Luck (-1) [2] check. If you pass, gain 1 Unique Item.');
  Add('LIBRARY',    EXP_TLATT, 23, 'The library has come into possession of an unidentified gramophone record. '+
                                   'It is a recording of a strange language no one on the staff can interpret. '+
                                   'Make a Lore (-2) check to see if you can make sense of the message. If you '+
                                   'pass, you gain 1 Spell.');
  Add('LIBRARY',    EXP_TLATT, 24, 'You think you''ve found valuable information in this reference book, but a '+
                                   'loud conversation near you is making it hard to concentrate. Make a Will '+
                                   '(-2) check and gain 2 Clue tokens if you pass.');
  Add('MBHOUSE',    EXP_TKIY,  21, 'A portrait of one of Arkham''s founding fathers hangs in Ma''s sitting '+
                                   'room. On the back of the painting is a series of symbols and numbers. Pass a '+
                                   'Lore (-1) check to interpret their meaning and gain a Clue token for each '+
                                   'success.');
  Add('MBHOUSE',    EXP_TLATT, 22, 'As a favor, you volunteer to head to the basement to have a look at the '+
                                   'pipes. The steps are mostly rotten and are starting to fall apart under your '+
                                   'weight. Make a Speed (+0) check to avoid injury. If you fail, lose 1 '+
                                   'Stamina.');
  Add('MBHOUSE',    EXP_TLATT, 23, 'If you''re healthy enough, Ma could sure use some help rebuilding the '+
                                   'porch. If you have 3 or more Stamina, take a Retainer card.');
  Add('MBHOUSE',    EXP_TLATT, 24, 'You sneak down to Ma''s kitchen for a midnight snack. Make a Luck (+0) '+
                                   'check to see if there''s any leftovers waiting for you. Gain 1 Stamina per '+
                                   'success.');
  Add('PSTATION',   EXP_TKIY,  21, '"Please! My husband is innocent! He could never commit those atrocities!" '+
                                   'Deputy Dingby refuses to listen to the woman, but her story explains much of '+
                                   'what has been going on. Gain 1 Clue token.');
  Add('PSTATION',   EXP_TLATT, 22, '"You okay, fella? You''re not making sense." Sheriff Engle wants to keep '+
                                   'you out of trouble. If you currently have 2 or less Sanity, make a Fight '+
                                   '(+0) check. If you fail, lose all your Weapons and lose 1 Stamina.');
  Add('PSTATION',   EXP_TLATT, 23, 'Deputy Dingby forgot to bring his lunch today, and if you help him out, '+
                                   'he''ll become very friendly and chatty. You may give the Deputy either the '+
                                   'Food Common Item card or $1 to gain 1 Clue token in return.');
  Add('PSTATION',   EXP_TLATT, 24, 'Sheriff Engle wrestles a prisoner into the lobby of the Police Station. The '+
                                   'handcuffed man bumps into you and whispers, "I can''t be found with this." '+
                                   'Make a Sneak (-1) check. If you pass, draw 1 Common item.');
  Add('RDOCKS',     EXP_TKIY,  21, 'A terrified young student from Miskatonic University seems to have wound up '+
                                   'here by accident. Make a Will (+1) check to keep him calm enough to safely '+
                                   'guide him back to more familiar streets. If you pass, he gratefully offers '+
                                   'you $2 for your assistance.');
  Add('RDOCKS',     EXP_TLATT, 22, 'As a truck is driving away from the warehouse, you see a crate fall off the '+
                                   'back. Unfortuneately, Joey "the Rat" saw it too. Make a Speed (+1) check to '+
                                   'beat him to the crate. If you pass, gain 1 Common Item.');
  Add('RDOCKS',     EXP_TLATT, 23, 'Items in an abandoned warehouse are being auctioned off. The selection is '+
                                   'quite good, but prices are running high. Draw the top three Common Items '+
                                   'from their deck. You may purchase 1 of them for $1 more than the listed '+
                                   'price. Discard any items that are not purchased.');
  Add('RDOCKS',     EXP_TLATT, 24, 'This area has always smelled foul, but today something in the river smells '+
                                   'absolutely noxious. Make a Speed (-2) check to reach fresher air. If you '+
                                   'fail, lose 1 Stamina. Whether you pass or not, move to the street.');
  Add('SBUILDING',  EXP_TKIY,  21, 'A loud roaring noise emanates from a laboratory. Rushing to investigate, '+
                                   'you see a swirling vortex collapsing in on itself, giving you a quick '+
                                   'glimpse of the worlds beyond. Make a Will (-2) check. If you fail, lose 2 '+
                                   'Sanity. Whether you succeed or not, if you are not driven insane, gain 1 '+
                                   'Unique Item that the spiralling anomaly transports into the room.');
  Add('SBUILDING',  EXP_TLATT, 22, 'Baffled scientists show you a wax cylinder which has apparently recorded '+
                                   'the voices of people in the future, warning of what is to come. Make a Lore '+
                                   '(-2) check. If you pass, you may look at the top three cards of the Mythos '+
                                   'deck and then return them to the top of the deck in any order you choose.');
  Add('SBUILDING',  EXP_TLATT, 23, 'The Psychology Department would like to perform some deep hypnosis '+
                                   'experiments on you. If you agree, make a Will (-1) check. If you pass, you '+
                                   'make contact with a strange alien intelligence and gain 1 Spell. If you '+
                                   'fail, the incident traumatizes you and you lose 1 Sanity.');
  Add('SBUILDING',  EXP_TLATT, 24, 'The staff is looking for exhausted or unhealthy subjects for medical '+
                                   'experiments. If you are currently at less than your maximum Stamina, you may '+
                                   'choose to gain $3. You must then make a Luck (+0) [2] check. If you succeed, '+
                                   'you are restored to full Stamina. If you fail, lose 1 Stamina.');
  Add('STLODGE',    EXP_TKIY,  21, '"Care to join the order?" asks Carl Sanford and his henchmen. If you '+
                                   'accept, pay $3 and take a Silver Twilight Membership. If you decline, pass a '+
                                   'Will (-1) check or lose 3 Stamina as the henchmen assist you to the door. '+
                                   'Whether you pass or not, move to the street.');
  Add('STLODGE',    EXP_TLATT, 22, 'Carl Sanford sits in the center of the room chanting while books and other '+
                                   'small objects appear to be flying around the room of their own accord! Make '+
                                   'a Fight (-1) check to avoid being clobbered by these items and to understand '+
                                   'what Sanford is saying. If you pass, gain 2 Clue tokens. If you fail, you '+
                                   'awaken bruised and sore. Lose 1 Stamina.');
  Add('STLODGE',    EXP_TLATT, 23, 'You hear the quiet sounds of an intruder. If you investigate, you find a '+
                                   'woman dress in black. Pass a Fight (-1) check to subdue her long enough to '+
                                   'explain your investigation. You find out that her name is Ruby Standish and '+
                                   'that she was robbing the Lodge. However, upon hearing your tale, she agrees '+
                                   'to join you. Take her Ally card. If it is not available, draw a Unique Item '+
                                   'instead.');
  Add('STLODGE',    EXP_TLATT, 24, 'You recognize one of the Lodge Members as a friend from years ago. Make a '+
                                   'Will (-2) check to convince him to help you in some way. If you pass, draw 1 '+
                                   'Unique Item. Whether you pass or not, move to the street.');
  Add('SCHURCH',    EXP_TKIY,  21, '"You! You are the one who has stood against the evil that plagues this '+
                                   'town. We are all so grateful!" A crowd surrounds you, expressing gratitude '+
                                   'and adoration. Gain 2 Sanity.');
  Add('SCHURCH',    EXP_TLATT, 22, 'Father Michael''s sermon is comforting, but a little dull, and you''ve '+
                                   'dozed off. Stay here next turn and restore your Sanity to its maximum.');
  Add('SCHURCH',    EXP_TLATT, 23, 'If you can show Father Michael proof of the doom that threatens Arkham, he '+
                                   'will agree to lead the congregation in a prayer to purge the streets of '+
                                   'evil. If you spend 1 Gate trophy, you may remove all monsters from the '+
                                   'Southside neighborhood.');
  Add('SCHURCH',    EXP_TLATT, 24, 'Someone left a box of donation items at the Church''s doorstep. You notice '+
                                   'an odd, grotesque idol. Make a Will (+0) check. If you fail, you are '+
                                   'Cursed.');
  Add('STMHOSPITAL',EXP_TKIY,  21, 'The doctors insist on treating you! Ignoring any protests, they anesthetize '+
                                   'you and start patching you up. When you come to, you''re physically fine but '+
                                   'your thoughts are pretty foggy. Gain 2 Stamina but lose a Clue token if you '+
                                   'have any.');
  Add('STMHOSPITAL',EXP_TLATT, 22, 'You find a doctor''s bag sitting unattended. Inside, there''s bandages, '+
                                   'rubbing alcohol, and medicines. Gain 2 Stamina.');
  Add('STMHOSPITAL',EXP_TLATT, 23, 'You sit next to a small boy in the waiting room while his mother is in '+
                                   'surgery. He tells you that his mommy protected him from a big monster with '+
                                   'scary fangs. You tell him everything will be fine. Gain 1 Clue token and '+
                                   'lose 1 Sanity.');
  Add('STMHOSPITAL',EXP_TLATT, 24, 'You think a man in the waiting room is having a more serious emergency than '+
                                   'he realizes. Make a Lore (-2) check to make a correct diagnosis. If you '+
                                   'pass, gain 1 Sanity. If you fail, move to the streets as you are curtly '+
                                   'asked to leave.');
  Add('TUNNAMABLE', EXP_TKIY,  21, 'A box full of documents in the closet has grown damp and moldy. Make a Luck '+
                                   '(+1) check to see if anything of value has been spared. If you pass, gain 1 '+
                                   'Clue token.');
  Add('TUNNAMABLE', EXP_TLATT, 22, 'A pen and paper rest on a table next to your chair. Picking up the pen, you '+
                                   'black out for an uncertain amount of time. When you regain your senses, the '+
                                   'paper is covered with strange messages, not written in your handwriting. '+
                                   'Make a Lore (-1) check and gain 1 Clue token for each success. Then, whether '+
                                   'you pass or not, lose 1 Sanity.');
  Add('TUNNAMABLE', EXP_TLATT, 23, 'A repellent, tar-like appendage is dragging an item of interest quickly '+
                                   'through the halls. Make a Speed (-2) check. If you pass, draw 2 Unique Items '+
                                   'and keep 1. If you fail, lose 2 Stamina as you are dragged across the '+
                                   'floor.');
  Add('TUNNAMABLE', EXP_TLATT, 24, 'Things seem to just disappear here. Choose 1 Common Item and discard it. If '+
                                   'you do not have a Common Item, lose 1 Sanity.');
  Add('TWHOUSE',    EXP_TKIY,  21, 'In the attic, you feel a force in your mind, trying to replace your '+
                                   'thoughts with those of another. Make a Speed (-1) check to escape. If you '+
                                   'pass, move to the streets. If you fail, lose 1 Spell, or if you have no '+
                                   'Spells, lose 2 Sanity.');
  Add('TWHOUSE',    EXP_TLATT, 22, 'In the middle of the night, something in the dark is clutching at your '+
                                   'chest! Make a Fight (+0) check and lose 2 Stamina if you fail.');
  Add('TWHOUSE',    EXP_TLATT, 23, 'The room is filled with glowing bubbles! You are having a hard time gaining '+
                                   'your bearings and finding the door. Lose 1 Sanity and you are delayed, but '+
                                   'then gain 3 Clue tokens.');
  Add('TWHOUSE',    EXP_TLATT, 24, 'You find an old journal, largely devoured by vermin. Make a Luck (-3) check '+
                                   'to see if certain vital pages remain intact. If you pass, draw 2 Spells and '+
                                   'keep 1.');
  Add('TSTATION',   EXP_TKIY,  21, 'A nervous-looking man is moving quickly through the crowd, with Sheriff '+
                                   'Engle in pursuit. The anxious man bumps into you, falls to the ground, and '+
                                   'drops a package. Make a Speed (-2) check to grab the package and escape '+
                                   'before the sheriff arrives. If you pass, gain 1 Unique Item.');
  Add('TSTATION',   EXP_TLATT, 22, 'Hot peanuts are for sale at a pushcart. You may pay up to $3 and gain 1 '+
                                   'Stamina for each $1 you spend.');
  Add('TSTATION',   EXP_TLATT, 23, 'You find a key to a locker on the ground, but the tag that shows its number '+
                                   'has been removed. Make a Luck (-2) check to find the right locker. If you '+
                                   'pass, gain 1 Common Item.');
  Add('TSTATION',   EXP_TLATT, 24, 'You see a familiar face about to get on a train leaving Arkham. Draw an '+
                                   'Ally card and then make a Will (-2) [2] check. If you pass, you''ve '+
                                   'convinced your friend to stay and may take the Ally card. If you fail, the '+
                                   'Ally card is returned to the box.');
  Add('UISLE',      EXP_TKIY,  21, 'The ground is covered with a strange luminescent substance. Make a Lore '+
                                   '(+0) check to keep yourself safe from its damaging effects. If you fail, you '+
                                   'are Cursed.');
  Add('UISLE',      EXP_TLATT, 22, 'The seclusion on the island is making you more withdrawn and paranoid. Make '+
                                   'a Will (+0) check to keep your wits. If you fail, lose 2 Sanity.');
  Add('UISLE',      EXP_TLATT, 23, 'You must have fallen into the water. A passerby managed to pull you out and '+
                                   'resusitate you. He claims you were dead for a brief time. Perhaps you did go '+
                                   'to the other side and returned with new knowledge. Make a Will (-2) check to '+
                                   'recollect your experience. If you pass, gain 2 Spells. If you fail, lose 2 '+
                                   'Sanity.');
  Add('UISLE',      EXP_TLATT, 24, 'You see Carl Sanford covertly trying to find a place on the island to '+
                                   'recite a ritual. Make a Sneak (-2) check. If you pass, you get close enough '+
                                   'to hear what he is saying and gain 3 Clue tokens.');
  Add('VDINER',     EXP_TKIY,  21, 'Two businessmen are arguing over who will pay the bill, and both have put '+
                                   'several dollars on the table. If you can sneak one of the payments off the '+
                                   'table, each of the businessmen will think the other relented and will drop '+
                                   'the argument. Plus, you''ll make a little money. Make a Sneak (-2) check and '+
                                   'gain $3 if you pass.');
  Add('VDINER',     EXP_TLATT, 22, 'Velma''s got a fire in the kitchen! Make a Speed (-2) check to extinguish '+
                                   'it before any damage is done. If you pass, Velma''s grateful expression '+
                                   'inspires you and you recover 1 Sanity. If you fail, lose 1 Stamina from some '+
                                   'bad burns.');
  Add('VDINER',     EXP_TLATT, 23, 'Velma''s hot turkey sandwich with potatoes and gravy hits the spot! Gain 1 '+
                                   'Stamina.');
  Add('VDINER',     EXP_TLATT, 24, 'You see a veteran, blinded by gas during the Great War, come into the '+
                                   'diner. Spend $2 to buy him dinner or lose 1 Sanity.');
  Add('WOODS',      EXP_TKIY,  21, 'A car has smashed into a tree. The driver, a member of the Sheldon Gang, is '+
                                   'unconscious and a bag of stolen valuables sits next to him. You can hear '+
                                   'other members of the gang coming through the woods looking for him. Make a '+
                                   'Sneak (-2) check. If you pass, gain $3. If you fail, you are delayed While '+
                                   'hiding from the gang.');
  Add('WOODS',      EXP_TLATT, 22, 'A sudden clearing reveals a prehistoric circle of carved stones. Standing '+
                                   'here, your thoughts are filled with the angry and fearful voices of those '+
                                   'who perished or were taken to other worlds here. Make a Will (+0) check. If '+
                                   'you fail, you are Cursed.');
  Add('WOODS',      EXP_TLATT, 23, 'You notice an odd symbol carved into a tree. It leads you to another tree '+
                                   'with a symbol carved into it. Make a Lore (-1) check to follow the path of '+
                                   'symbols. If you pass, you discover it leads to an unusual object hidden '+
                                   'under a rock. Gain 1 Unique Item. If you fail, lose 1 Stamina as you become '+
                                   'increasingly exhausted.');
  Add('WOODS',      EXP_TLATT, 24, 'You stumble upon an old shack, but it looks like animals got inside and '+
                                   'have torn up just about everything. Make a Luck (-2) check to see if any '+
                                   'reading material survived. If you pass, search the Common Item deck for the '+
                                   'first Tome you find and take it.');
  Add('YOMSHOPPE',  EXP_TKIY,  21, 'Miriam Beecher offers to cleanse your aura and restore your mental well- '+
                                   'being, for a price. If you discard 1 Unique Item and pay $3, you are '+
                                   'Blessed.');
  Add('YOMSHOPPE',  EXP_TLATT, 22, 'Speaking with Miriam Beecher, she tells you she would be willing to trade '+
                                   'for items, if you have anything of interest. Look at the top card of the '+
                                   'Unique Item deck. If you want to keep it, discard one of your Unique Items '+
                                   'or Spells.');
  Add('YOMSHOPPE',  EXP_TLATT, 23, 'The item you have been hoping to purchase has already been sold. Make a '+
                                   'Sneak (-1) check to sneak a peek at the ledger to see who purchased it. If '+
                                   'you pass, gain 2 Clue tokens.');
  Add('YOMSHOPPE',  EXP_TLATT, 24, 'You accidentally bump into a glass bottle filled with a strange grey '+
                                   'powder. Make a Speed (-2) check to catch it before it breaks. If you fail, '+
                                   'lose 1 Stamina as you break out into a fit of unexplained sneezing and '+
                                   'itching.');

end;

initialization
  Encounters := TStringList.Create;
  LoadEncounters;
  Encounters.Sort;
end.

