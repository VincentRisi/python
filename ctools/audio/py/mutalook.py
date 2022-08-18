import os, os.path, shutil, glob, mutagen.mp4, stat, sys, re

start_in   = '/media/vince/Audible/source'

def do_album(ofile, data):
    global bookname, album
    data = data.replace(' (Unabridged)','')
    album = data
    ofile.write(f'_bk.album = {data}\n')
    bookname = data.replace('(Unabridged)','').replace(' ','').replace(',','').replace("'",'').replace('"','')

repl_list = [
  (' (Unabridged)',''),
  ('Dragonlance: Chronicles', 'Dragonlance Chronicles'),
  ('High Mage','High Mage: Spellmonger, Book 5'),
  ('Blood of Dragons: The Rain Wild Chronicles 4', 'Blood of Dragons: The Rain Wild Chronicles, Book 4'),
  ('WWW: Wake', 'Wake: WWW, Book 1'),
  ('WWW: Watch', 'Watch: WWW, Book 2'),
  ('WWW: Wonder', 'Wonder: WWW, Book 3'),
  ('Crossroads of Twilight: Book Ten of The Wheel of Time', 'Crossroads of Twilight: Wheel of Time, Book 10'),
  ('Knife of Dreams: Book Eleven of The Wheel of Time', 'Knife of Dreams: Wheel of Time, Book 11'),
  ('The Eye of the World: Book One of The Wheel of Time', 'The Eye of the World: Wheel of Time, Book 1'),
  ('The Fires of Heaven: Book Five of The Wheel of Time', 'The Fires of Heaven: Wheel of Time, Book 5'),
  ('The Shadow Rising: Book Four of The Wheel of Time', 'The Shadow Rising: Wheel of Time, Book 4'),
  ('The Stone Man -', 'A Science Fiction Thriller:'),
  ('A Science Fiction Thriller:', 'The Stone Man:'),
  ('A Christmas Carol','A Christmas Carol HG'),
  ('White Lies','White Lies: Dan Shepherd, Book 11'),
  ('The 13th Spider Shepherd Thriller','Dan Shepherd, Book 13'),
  ('The 14th Spider Shepherd Thriller','Dan Shepherd, Book 14'),
  ('The 15th Spider Shepherd Thriller','Dan Shepherd, Book 15'),
  ('The 16th Spider Shepherd Thriller','Dan Shepherd, Book 16'),
  ('The 17th Spider Shepherd Thriller','Dan Shepherd, Book 17'),
  ('Midnight','Midnight: A Jack Nightingale Supernatural Thriller, Book 2'),
  ('San Francisco Night','San Francisco Night: A Jack Nightingale Supernatural Thriller, Book 6'),
  ('New York Night','New York Night: A Jack Nightingale Supernatural Thriller, Book 7'),
  ('Nightfall: A Jack Nightingale Supernatural Thriller','Nightfall: A Jack Nightingale Supernatural Thriller, Book 1'),
  # 

]
def do_name(ofile, data):
    global album
    ofile.write(f'# original name = {data}\n')
    if album.find('Sandman') >= 0:
        print('   album:', album)
    if data.find('WWW') == 0:
        data = album
    elif album.find('The Sandman: Act II') >= 0:
        data = "'The Sandman Act 2: Sandman Audio Graphic, Book 2'"  
    elif album.find('The Sandman') >= 0:
        data = "'The Sandman Act 1: Sandman Audio Graphic, Book 1'"
    for a, b in repl_list:
        data = data.replace(a,b)
    #ofile.write(f'# {data} {album} {filename}\n')    
    #if album == "'Black Ops'":    
    #    data = data.replace('Black Ops','Black Ops: Dan Shepherd, Book 12')
    arr = data[1:-1].split(':')
    if len(arr) == 2:
        name = repr(arr[0]) 
        extra = arr[1].strip().replace('(','').replace(')','')
        arr2 = extra.split(',')
        if len(arr2) == 2:
            series = repr(arr2[0].strip())
            book = repr(arr2[1].strip())
            ofile.write(f'_bk.series = {series}\n')
            ofile.write(f'_bk.book = {book}\n')
        elif len(arr2) == 1:
            result = re.search(r'(Book )([0-9]+)( of )(.*)', extra)
            if result != None:
                series = repr(result.group(4))
                book = repr(f'Book {result.group(2)}')
                ofile.write(f'_bk.series = {series}\n')
                ofile.write(f'_bk.book = {book}\n')
        else:    
            name = data    
    else:
        name = data    
    ofile.write(f'_bk.name = {name}\n')

def get_author(data):
    data = data.replace(' and ', ',')
    arr = data.split(',')
    if len(arr) > 1:
        return arr[0].replace(' ','').replace("'",'')
    return data.replace(' ','')    

def do_author(ofile, data):
    global authorname
    ofile.write(f'_bk.author = {data}\n')
    authorname = get_author(data.replace("'",''))

def do_genre(ofile, data):
    ofile.write(f'_bk.genre = {data}\n')

def do_comment(ofile, data):
    ofile.write(f'_bk.comment = {data}\n')

def do_description(ofile, data):
    ofile.write(f'_bk.description = {data}\n')

def do_publisher(ofile, data):
    ofile.write(f'_bk.publisher = {data}\n')

def do_narrator(ofile, data):
    ofile.write(f'_bk.narrator = {data}\n')

def do_released(ofile, data):
    ofile.write(f'_bk.released = {data}\n')

def do_sti(ofile, data):
    data = data.replace(' (Unabridged)','')
    ofile.write(f'_bk.sti = {data}\n')

names = dict()
names['©alb'] = 'album', do_album
names['©nam'] = 'name', do_name
names['©ART'] = 'author', do_author
names['©gen'] = 'genre', do_genre
names['©cmt'] = 'comment', do_comment
names['©des'] = 'description', do_description
names['©pub'] = 'publisher', do_publisher
names['©nrt'] = 'narrator', do_narrator
names['rldt'] = 'released', do_released
names['@sti'] = 'sti', do_sti

def main():
    with open('/media/vince/Audible/aaxlist.py', 'wt') as ofile:
        ofile.write(f'class _obj: pass\n')
        ofile.write(f'books = dict()\n')
        sys.stdout = open('//media/vince/Audible/aaxlist.txt', 'wt')
        mask = '%s/*.aax' % (start_in)
        print ('start %s' % (mask))
        count = 0
        for file in sorted(glob.glob(mask)):
            _, filext = os.path.split(file)
            filename, _ = os.path.splitext(filext)
            ofile.write(f'_bk = _obj()\n')
            ofile.write(f'_bk.filename = {repr(filename)}\n')
            count = count + 1
            try:
                props = mutagen.mp4.MP4(file)
                print (file, props.keys())
                for tag in names:
                    name, func = names[tag]
                    if tag in props:
                        try:
                            data = props[tag]
                            print('%s: %s' % (name, data[0]))
                            func(ofile, repr(data[0]))
                        except:
                            print('{%s error}' % (name))  
            except:
                print('{%s error}' % (file))
            ofile.write(f'books["{authorname}-{bookname}"] = _bk\n')
            
        print (count)    

main()