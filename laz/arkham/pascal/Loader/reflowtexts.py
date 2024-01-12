# -*- coding: iso-8859-1 -*-
import textwrap

lines ='''\
  AddDarkPact('BLOODPACT', 'Blood Pact', 'When you gain a Blood Pact, restore your Stamina to full. Any Phase: While this card is refreshed, any time you would gain any amount of Stamina, you may instead gain that amount of Power. You may spend a Power token as either a Clue token or as 1 Sanity when you suffer a Sanity loss. Upkeep: Exhaust Blood Pact and lose X Stamina to gain X Power.');
  AddDarkPact('SOULPACT',  'Soul Pact',  'When you gain a Soul Pact, restore your Sanity to full. Any Phase: While this card is refreshed, anytime you would gain any amount of Sanity, you may instead gain that amount of Power. You may spend a Power token as either a Clue token or as 1 Stamina when you suffer a Stamina loss. Upkeep: Exhaust Soul Pact and lose X Sanity to gain X Power.');
  AddDarkPact('BOUNDALLY', 'Bound Ally', 'When you gain a Bound Ally, take the top card of the Ally deck and attach it to this card. You gain the services of that Ally. When the Ancient One awakens, discard the Ally and put this card on the Ancient One. For each Bound Ally on the Ancient One, it takes one additional success to remove a doom token. You may spend a Power token as either a Clue token or as $1.');
'''.splitlines()

size = 41
length = 72

ofile = open('reformatted11.code', 'wt')
def printit2(front, back):
  ofile.write("%s\n" % (front))
  bits = textwrap.wrap(back, length)
  for i,d in enumerate(bits):
    if i == 0:
      f = ' ' * 6
    else:
      f = ' ' * 6 + "'"
    if i == len(bits)-1:
      b = ');'
    else:
      b = " '+"
    ofile.write("%s%s%s\n" % (f,d,b))

def printit(front, back):
  bits = textwrap.wrap(back, length)
  for i,d in enumerate(bits):
    if i == 0:
      f = front
    else:
      f = ' ' * size + "'"
    if i == len(bits)-1:
      b = ');'
    else:
      b = " '+"
    ofile.write("%s%s%s\n" % (f,d,b))

for line in lines:
  front = line[:size]
  back  = line[size:-2]
  printit(front, back)
ofile.close()
