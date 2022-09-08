import sys, os, os.path, re
from aaxlist import books
rl = dict()
rl['TheTimePolice'] = 'TimePolice'
rl['ATimePolice'] = 'TimePolice'
rl['ADCITomDouglasla'] = 'DCITomDouglas, Book 1'
for bk in books:
    book = books[bk]
    album = book.album
    for key in rl: album = album.replace(key, rl[key])
    album = album.replace(':','|').replace(', Book','|Book').replace(' ','').replace("'",'').replace('Novel','').replace('Series','')
    numbers = 'One|Two|Three|Four|Five|Six|Seven|Eight|Nine'
    for i, num in enumerate(numbers.split('|')): album = album.replace('Book%s' % num,'Book%02d'%(i+1))
    for i, num in enumerate(numbers.upper().split('|')): album = album.replace('Book%s' % num,'Book%02d'%(i+1))
    for i, num in enumerate(numbers.lower().split('|')): album = album.replace('Book%s' % num,'Book%02d'%(i+1))
    print (book.author, album.split('|'))

