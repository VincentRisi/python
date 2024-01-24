unit AHInvestigators;
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
  Investigators      : TStringList;
  BackStories        : TStringList;
  FixedPossessions   : array of TFixedPossession;
  
implementation

procedure Add(const aName        : string;
              const aExpansion   : EExpansion;
              const aProfession  : string;
              const aHome        : string;
              const aStatus      : EGraceType;
              const aSanity      : integer;
              const aStamina     : integer;
              const aClues       : integer;
              const aCash        : integer;
              const aFocus       : integer;
              const aSpeed       : integer;
              const aSneak       : integer;
              const aFight       : integer;
              const aWill        : integer;
              const aLore        : integer;
              const aLuck        : integer;
              const aCommon      : integer;
              const aUnique      : integer;
              const aSpell       : integer;
              const aSkill       : integer;
              const aAbility     : string);
var
  Investigator : TInvestigator;
begin
  Investigator := TInvestigator.Create;
  with Investigator do begin
    name        := aName;
    expansion   := aExpansion;
    profession  := aProfession;
    home        := aHome;
    status      := aStatus;
    sanity      := aSanity;
    stamina     := aStamina;   
    clues       := aClues;     
    cash        := aCash;      
    focus       := aFocus;     
    speed       := aSpeed;     
    sneak       := aSneak;     
    fight       := aFight;     
    will        := aWill;      
    lore        := aLore;      
    luck        := aLuck;      
    common      := aCommon;
    unique      := aUnique;
    spell       := aSpell;
    skill       := aSkill;
    ability     := aAbility;   
  end;
  Investigators.AddObject(aName, Investigator);
end;

procedure AddBackStory(const aName        : string;
                       const aExpansion   : EExpansion;
                       const aDescription : string);
var
  BackStory : TBackStory;
begin
  BackStory := TBackStory.Create;
  BackStory.name := aName;
  BackStory.expansion   := aExpansion;
  BackStory.description := aDescription;
  BackStories.AddObject(aName, BackStory);
end; 

procedure AddFixedPossession(const aName        : string;
                             const aExpansion   : EExpansion;
                             const aItem        : string);
var
  FixedPossession : TFixedPossession;
  i               : integer;
begin
  FixedPossession := TFixedPossession.Create;
  FixedPossession.name        := aName;
  FixedPossession.expansion   := aExpansion;
  FixedPossession.item        := aItem;
  i := Length(FixedPossessions);
  setLength(FixedPossessions, i+1);
  FixedPossessions[i] := FixedPossession;
end;

procedure LoadInvestigators();
begin
  Add('AmandaSharpe',  EXP_AH, 'Studious',      'BOARKHAM',    NORMAL,  5, 5, 1,  1, 3, 1, 4, 1, 4, 1, 4, 1, 1, 1, 2, 'Any Phase: Whenever Amanda draws one or '+
                                                                                                               'more cards from Skill deck, she draws '+
                                                                                                               'one extra and then discards one of the '+
                                                                                                               'cards.');
  Add('AshcanPete',    EXP_AH, 'Scrounger',     'RDOCKS',      NORMAL,  4, 6, 3,  1, 1, 0, 6, 2, 5, 0, 3, 1, 1, 0, 1, 'When Pete draws from the Common Item, '+
                                                                                                               'Unique Item, or Spell deck, he may draw '+
                                                                                                               'from either the top or the bottom of '+
                                                                                                               'that deck, his choice. Pete may look at '+
                                                                                                               'the bottom card of those decks at any '+
                                                                                                               'time.');
  Add('BobJenkins',    EXP_AH, 'Dealer',        'GENSTORE',    NORMAL,  4, 6, 0,  9, 1, 2, 3, 1, 6, 0, 4, 2, 2, 0, 1, 'Shrewd Dealer - Any Phase: Whenever Bob '+
                                                                                                               'draws one or more '+
                                                                                                               'cards from the Common Item deck, he '+
                                                                                                               'draws one extra and then discards one of '+
                                                                                                               'the cards.');
  Add('CarolynFern',   EXP_AH, 'Phychologist',  'ARKASYLUM',   NORMAL,  6, 4, 1,  7, 2, 0, 3, 1, 4, 2, 5, 2, 2, 0, 1, 'Upkeep: Dr. Fern may restore 1 Sanity '+
                                                                                                               'to herself or another character in her '+
                                                                                                               'location. She cannot raise a Sanity '+
                                                                                                               'higher than that character''s maximum '+
                                                                                                               'Sanity.');
  Add('DarrellSimmons', EXP_AH, 'Journalist',    'NEWSPAPER',   NORMAL,  4, 6, 1,  4, 2, 2, 3, 2, 4, 0, 4, 1, 2, 0, 1, 'Town Encounter: When drawing location '+
                                                                                                               'encounters in Arkham, Darrell draws two '+
                                                                                                               'cards and may choose whichever one of '+
                                                                                                               'the two he wants. This ability does not '+
                                                                                                               'work when drawing gate encounters in '+
                                                                                                               'Other Worlds.');
  Add('DexterDrake',   EXP_AH,  'Magician',      'YOMSHOPPE',   NORMAL,  5, 5, 0,  5, 2, 2, 4, 1, 3, 2, 3, 1, 1, 2, 1, 'Any Phase: Whenever "The Great" Drake '+
                                                                                                               'draws one or more cards from the Spell '+
                                                                                                               'deck, he draws one extra card and then '+
                                                                                                               'discards one of the cards.');
  Add('GloriaGoldberg', EXP_AH, 'Psychic',       'VDINER',      NORMAL,  6, 4, 2,  7, 2, 1, 3, 0, 5, 1, 5, 2, 0, 2, 1, 'Other World Encounter: When drawing '+
                                                                                                               'gate encounters in Other Worlds, Gloria '+
                                                                                                               'draws two cards that match the color of '+
                                                                                                               'one of the World''s encounter symbols, '+
                                                                                                               'then chooses whichever one of the two '+
                                                                                                               'she wants. This ability does not work '+
                                                                                                               'when drawing location encounters in '+
                                                                                                               'Arkham.');
  Add('HarveyWalters',  EXP_AH, 'Strong Minded', 'ABUILDING',   NORMAL,  7, 3, 1,  5, 2, 0, 5, 0, 3, 3, 4, 0, 2, 2, 1, 'Any Phase: Harvey reduces all Sanity '+
                                                                                                               'losses he suffers by 1, to a minimum of '+
                                                                                                               '0.');
  Add('JennyBarnes',    EXP_AH, 'Trust Fund',    'TSTATION',    NORMAL,  6, 4, 0, 10, 1, 0, 4, 1, 5, 1, 5, 2, 1, 1, 1, 'Upkeep: Jenny gains $1');
  Add('JoeDiamond',     EXP_AH, 'Hunches',       'PSTATION',    NORMAL,  4, 6, 3,  8, 3, 3, 4, 2, 3, 0, 3, 2, 0, 0, 1, 'Any Phase: Joe rolls one extra bonus '+
                                                                                                               'die when he spends a Clue token to add '+
                                                                                                               'to a roll.');
  Add('KateWinthrop',   EXP_AH, 'Scientist',     'SBUILDING',   NORMAL,  6, 4, 1,  7, 1, 1, 5, 1, 3, 2, 4, 1, 1, 2, 1, 'Any Phase: Gates and monsters cannot '+
                                                                                                               'appear in Kate''s location due to her '+
                                                                                                               'flux stabilizer. Monsters and gates do '+
                                                                                                               'not disappear if she enters their '+
                                                                                                               'location, however, and monsters can move '+
                                                                                                               'into her location as usual. * Do not '+
                                                                                                               'place a Clue token on the Science '+
                                                                                                               'Building to start the game.');
  Add('MandyThompson',  EXP_AH, 'Researcher',    'LIBRARY',     NORMAL,  5, 5, 4,  6, 2, 1, 5, 0, 5, 1, 3, 2, 1, 0, 1, 'Any Phase: Once per turn, Mandy can '+
                                                                                                               'activate this ability after any '+
                                                                                                               'investigator (including herself) makes a '+
                                                                                                               'skill check. That investigator then re- '+
                                                                                                               'rolls all of the dice rolled for that '+
                                                                                                               'check that did not result in successes.');
  Add('MichaelMcGlen',  EXP_AH, 'Strong Body',   'MBHOUSE',     NORMAL,  3, 7, 0,  8, 1, 2, 4, 3, 4, 0, 3, 1, 0, 0, 1, 'Any Phase: Michael reduces all Stamina '+
                                                                                                               'losses he suffers by 1, to a minimum of '+
                                                                                                               '0.');
  Add('MontereyJack',   EXP_AH, 'Archaeologist', 'CSHOPPE',     NORMAL,  3, 7, 1,  7, 2, 1, 3, 2, 3, 1, 5, 2, 0, 0, 1, 'Any Phase: Whenever Monterey draws one '+
                                                                                                               'or more cards from the Unique Item deck, '+
                                                                                                               'he draws one extra card and then '+
                                                                                                               'discards one of the cards.');
  Add('SisterMary',     EXP_AH, 'Guardian Angel','SCHURCH',     BLESSED, 7, 3, 0,  0, 1, 1, 4, 0, 4, 1, 6, 0, 0, 2, 1, 'Any Phase: Sister Mary is never Lost in '+
                                                                                                               'Time and Space. Instead, if her Sanity '+
                                                                                                               'is O, she returns to Arkham Asylum. If '+
                                                                                                               'her Stamina is 0, she returns to '+
                                                                                                               'St.Mary''s Hospital. If neither her '+
                                                                                                               'Sanity nor her Stamina are 0, she '+
                                                                                                               'returns to South Church.');
  Add('VincentLee',     EXP_AH, 'Physician',     'STMHOSPITAL', NORMAL,  5, 5, 1,  9, 2, 0, 5, 0, 4, 2, 4, 2, 0, 2, 1, 'Upkeep: Dr. Lee may restore 1 Stamina '+
                                                                                                               'to himself or another character in his '+
                                                                                                               'location. He cannot raise a character''s '+
                                                                                                               'Stamina higher than that character''s '+
                                                                                                               'maximum Stamina.');
  AddBackStory('AmandaSharpe', EXP_AH,
    'Amanda has been a student at Miskatonic University for 2 years now. On her Way '+
    'to talk to one of her professors last month, she saw a painting in the hallway '+
    'that captured her attention with its hazy depiction of some horrible creature '+
    'rising up out of the ocean. Ever since, Amanda has heard strange Whispers in a '+
    'foreign language Whenever her attention drifts. More disturbingly, she has begun '+
    'to dream of the vast green depths of the ocean and terrible alien cities that '+
    'lie in its darkest crevasses. This evening, as she finishes her shift as a bank '+
    'teller at the First Bank of Arkham, something out in the night calls to her -- '+
    'something dark and sinister that leaves the feel of sea foam in her mind and '+
    'makes her gasp with the effort of resisting it. Leaning against the brick Wall '+
    'of the bank, Amanda realizes that she has to find out Whats happening to her or '+
    'shes going to fall prey to whatever alien presence is invading her mind.');
  AddBackStory('AshcanPete', EXP_AH,
    'When youve lived on the streets as long as Pete has, you see things. Things that '+
    'would drive braver men screaming into the night. But you also learn to be quiet, '+
    'to stay hidden, and to play stupid if all else fails. It also helps to have a '+
    'good dog, like Duke, to scare away the meaner elements of the street. '+
    'Unfortunately, this time, Pete cant hide, and theres nothing Duke can do to '+
    'protect him. His nightmares have been growing steadily Worse over the last '+
    'month, driving him all the way here...to Arkham. Even the whiskey isnt helping '+
    'mueh anymore. Soon, he Wont be able to sleep at all. Still, there are always '+
    'opportunities for a man who knows how to stay quiet...as long as he isnt too '+
    'picky.');
  AddBackStory('BobJenkins', EXP_AH,
    'As a traveling salesman, Bob is always on the go. But yesterday, he saw '+
    'something that made him decide to stay in Arkham and miss his train. While he '+
    'was in the General Store selling his Wares, a robed man came in and bought '+
    'several items, paying with old gold coins. Astounded, Bob tumed to the '+
    'shopkeeper for an explanation, but the man just ignored his questions, simply '+
    'saying, "That happens, sometimes." Now, Bob isnt leaving until he figures out '+
    'where those gold coins came from. If he plays his cards right, maybe this will '+
    'be the big score. Maybe hell finally be able to retire and buy that boat hes had '+
    'his eye on and spend the rest of his days fishing in a tropical paradise. Then '+
    'again, maybe Bob will finally come to see that all that glitters is not gold.');
  AddBackStory('CarolynFern', EXP_AH,
    'Carolyn is a first year resident at a sanitarium in Providence. Over the past '+
    'six months, she has been studying the dreams of her patients using hypnosis. One '+
    'patient in particular gave her vivid and disturbing descriptions of his dreams, '+
    'right up until he was murdered With a strange knife that closely resembled '+
    'something from one of his nightmares. Disturbed and frightened by his murder, '+
    'Carolyn dug back through her notes, poring over them late into the night. '+
    'Finally, she found some subtle clues that led her here, to Arkham, where he was '+
    'previously an inmate in Arkham Asylum. Someone here has to know why a harmless '+
    'man was murdered for talking about his dreams to his psychologist.');
  AddBackStory('DarrellSimmons', EXP_AH,
    'Even while growing up in Arkham, Darrell always knew that there was something '+
    'not quite right about the strange little town. After graduating from high '+
    'school, he went to work for the Arkham Advertiser as a photographer, and in the '+
    'years since, hes crawled over every square inch of the city. Last night, '+
    'however, Darrell saw something horrible -- something that has shaken his world '+
    'to its core and torn away the safe illusions we all foster to protect our minds '+
    'and our souls. His editor says he was just seeing things, but as he leaves the '+
    'newspaper building, he knows just what he saw and he intends to show the world! '+
    'This time hell be more careful. This time hell take pictures and prove that '+
    'things are not normal in Arkham.');
  AddBackStory('DexterDrake', EXP_AH,
    'After returning from from his stint in the army during WWI, Dexter became a '+
    'stage magician, and proved to be very successful at his trade, but he always '+
    'longed to find real magic. As they say, be careful what you wish for. Years '+
    'later, in a rundown store, Dexter came across a burnt and torn fragment of the '+
    'Necronomicon itself. Intrigued by this ancient piece of occult knowledge, Dexter '+
    'began to use his wealth in search of the truth about the ancient lore, and what '+
    'he found horrified him. Now, the more he learns, the less he wants to know, but '+
    'his studies have led him to believe that a great evil will soon rise in Arkham. '+
    'He knows that he may well be the only person with the ability to stop this evil '+
    'from swallowing the world, so he has come to that sleepy town to speak with the '+
    'proprietor of Ye Olde Magick Shoppe, one of the few magic shops that contain '+
    'true lore, and not merely the stage tricks he once studied.');
  AddBackStory('GloriaGoldberg', EXP_AH,
    'As a young girl, Gloria was haunted by terrible visions. After years of visiting '+
    'doctors and some therapy, she learned to control her visions somewhat by writing '+
    'stories. Her weird and disturbing fiction somehow spoke to the public in these '+
    'troubled times, and has made her a bestselling writer. This evening, while '+
    'leaving a book signing shes attending in Arkham, she was knocked to the ground '+
    'by the most powerful vision shes ever experienced. Gloria saw the sky tear open, '+
    'and a huge and monstrous form pour out of the very air itself, wreaking untold '+
    'havoc and killing thousands. As she sat on the ground with her arms wrapped '+
    'around herself, Gloria knew, somehow, that this vision was real, and that it '+
    'would come to pass unless she did something about it. Now, she finds herself in '+
    'a run-down diner, sipping coffee and trying to decide what to do.');
  AddBackStory('HarveyWalters', EXP_AH,
    'Harvey is a visiting Professor at Miskatonic University. With Doctorates in '+
    'History and Archeology, he has uncovered several interesting artifacts over the '+
    'years and learned a little of the arcane arts. Recently, by carefully studying '+
    'the papers and talking to people in the streets, he has begun to detect a '+
    'disturbance in the city - something that could potentially herald the arrival of '+
    'something unthinkable from beyond space and time. Checking his notes, Professor '+
    'Walters prepares himself for one last trip into the streets of Arkham to confirm '+
    'his theory. If hes right, it could spell the end of everything.');
  AddBackStory('JennyBarnes', EXP_AH,
    'Several months ago, Jenny was visiting Paris when she received a letter from her '+
    'sister, Isabelle. In it, Isabelle rambled incoherently, writing about men in '+
    'dark cloaks following her Wherever she went, and of hoofprints in the woods, '+
    'left by an enormous goat. The outside of the envelope was partially stained with '+
    'blood, and it Was mailed from Arkham. That was the last letter from Isabelle she '+
    'received. Jenny has since returned to the States, coming to Arkham to find her '+
    'missing sister. Stepping off the train from Boston into the dark autumn night, '+
    'she believes that her sister was abducted by a strange cult, and is determined '+
    'to find her and thwart the plans of those that took her...even if she has to '+
    'save all of Arkham in the process.');
  AddBackStory('JoeDiamond', EXP_AH,
    'The job sounded simple enough -- pick up a statue at the Providence Museum and '+
    'deliver it to a guy at the Silver Twilight Lodge. The money Was good, and the '+
    'dame Who gave him the job seemed sincere. Sadly, things never seem to Work out '+
    'that easily for Joe. Now the statue is missing, two people are dead, strange '+
    'cultists are on his tail, and all the clues lead to Arkham. Lady Luck can be '+
    'funny that Way. Hes already tried talking to the Sheriff, but that flatfoot '+
    'proved to he worse than useless. Looks like its once again going to he up to Joe '+
    'Diamond to solve the case.');
  AddBackStory('KateWinthrop', EXP_AH,
    'A brilliant researcher, but a shy, lonely person, Kate Winthrop has been working '+
    'at the Miskatonic Science Labs for 4 years now and her supervisor still doesnt '+
    'know her name. That doesnt matter to her though, as she has been working to '+
    'complete a private quest for most of that time. Almost 3 years ago, she watched '+
    'as a device malfunctioned, and Professor Young, her long-time mentor and friend, '+
    'was torn apart by an indistinct creature that shrieked and gibbered before '+
    'vanishing into the night. Since then, she has delved into darker scientific '+
    'studies, always hoping to find something that would allow her to ?nd and defeat '+
    'that creature along with the others of its kind. Tonight, her research has '+
    'finally paid off, allowing her to create a device that can defeat the alien '+
    'beings she has detected in Arkham!');
  AddBackStory('MandyThompson', EXP_AH,
    'Mandy came to Arkham several years ago looking for work as a researcher for '+
    'Miskatonic University. Since then, she has worked with many of the University '+
    'professors, delving into esoteric tomes filled with scientific information, '+
    'historical reports, and sometimes even occult ramblings. It was while reading an '+
    'old book of prophecies last week that she first felt that she had stumbled onto '+
    'something big. Mandy came to believe that certain signs and portents described '+
    'in the book were taking place in Arkham right now -- omens that indicated the '+
    'return of a terrible being referred to as an Ancient One, which would grind the '+
    'cities of Man beneath its loathsome tread. Tonight, the full moon has turned '+
    'blood red, which is the ?nal omen of the return of the Ancient One. Slipping '+
    'into the night, and armed with her knowledge of the prophecy, Mandy has decided '+
    'to see if she can defy fate and stop these events from taking place.');
  AddBackStory('MichaelMcGlen', EXP_AH,
    'As a soldier in the OBannion gang, Michael didnt really believe in all this '+
    'voodoo mumbo jumbo around town. Or at least, he didnt until the night of the '+
    'Foreman job, When he saw Fast Louie Farrell pulled screaming into the river by a '+
    'scaly green creature. As they say, seeing is believing and Michael is starting '+
    'to believe. Now, he has gathered his belongings together in the room that he '+
    'rents at Mas Boarding House. Louie was a friend of his, and he wont rest until '+
    'he finds out whats happening in this town and avenges his buddy. . . .');
  AddBackStory('MontereyJack', EXP_AH,
    'Monterey has been a globe-trotting treasure hunter and adventurer for many '+
    'years. Following in his fathers footsteps, hes always tried to ensure that the '+
    'scientific value of his finds is preserved. Recently, he followed a lead on an '+
    'odd prehistoric statue to Arkham. However, when he arrived, the man he came to '+
    'buy the statue from was locked up in the asylum. Monterey was just about to give '+
    'up and go home in disgust when a robed figure pushed past him. For just an '+
    'instant, there was a flash of a silver pendant with a symbol on it that Monterey '+
    'would never forget. That symbol had been carved into his murdered fathers '+
    'forehead, and had haunted his dreams for years. Chasing after the mysterious '+
    'figure, he turned a corner only to discover that he had lost his quarry. '+
    'However, Monterey knows that somewhere in Arkham may lie the answer to the '+
    'mystery of his fathers murder, and hes not leaving until he finds it.');
  AddBackStory('SisterMary', EXP_AH,
    'Sister Mary has served the Church faithfully for many years, so when she was '+
    'sent to Arkham to work with Father Michael, a man whose writings she had admired '+
    'for many years, she felt that she was truly blessed. Now, after witnessing '+
    'Father Michaels strange mood swings and seeing some of the bizarre practices '+
    'that go on in this town, shes beginning to feel that she may have been a bit too '+
    'hasty... For instance, last night, there was a knock on the door of the church, '+
    'and when she answered it, there was nothing but a handwritten joumal laying on '+
    'the steps outside. Reading it, she learned of strange cults and terrible '+
    'creatures that lurk in the darkness. Worse, when she laughingly showed it to '+
    'Father Michael, he turned pale and threw it into the fire, yelling at her to '+
    'forget what shed seen. Now, gathering her things and quietly leaving South '+
    'Church, Sister Mary has decided to investigate this town, and in so doing, '+
    'reaffirm her faith.');
  AddBackStory('VincentLee', EXP_AH,
    'A Yale graduate of Medicine, Vincent has recently moved to Arkham from Boston to '+
    'practice at St.Marys Hospital. Since his coming to Arkham, he has seen far too '+
    'many horrible and unexplained deaths -- an elderly victim torn apart by unknown '+
    'wild animals, a healthy young man Whose heart exploded, and so many others. '+
    'Their faces haunt his dreams, especially the young mans terrified expression. '+
    'After all this, small Wonder that Vincent has begun to Wonder if theres '+
    'something sinister going on in this quiet Massachusetts town. Tonight, Dr. Lee '+
    'made the decision to investigate the mysteries of Arkham and stop the strange '+
    'deaths. He is determined to see this through, even if in so doing he becomes '+
    'another puzzle for the next doctor who comes to Arkham.');
  AddFixedPossession('AshcanPete',     EXP_AH,  'DUKE');
  AddFixedPossession('DarrellSimmons', EXP_AH,  'RETAINER');
  AddFixedPossession('DexterDrake',    EXP_AH,  'SHRIVELLING');
  AddFixedPossession('JoeDiamond',     EXP_AH,  '.45AUTOMATIC');
  AddFixedPossession('MichaelMcGlen',  EXP_AH,  'DYNAMITE');
  AddFixedPossession('MichaelMcGlen',  EXP_AH,  'TOMMYGUN');
  AddFixedPossession('MontereyJack',   EXP_AH,  'BULLWHIP');
  AddFixedPossession('MontereyJack',   EXP_AH,  '.38REVOLVER');
  AddFixedPossession('SisterMary',     EXP_AH,  'BLESSING');
  AddFixedPossession('SisterMary',     EXP_AH,  'CROSS');
  AddFixedPossession('SisterMary',     EXP_AH,  'HOLYWATER');
end;
             
initialization
  Investigators    := TStringList.Create;
  BackStories      := TStringList.Create;
  setLength(FixedPossessions, 0);
  LoadInvestigators;
  Investigators.Sort;
  BackStories.Sort;
end.

