import os, os.path, shutil, glob, mutagen.mp4, stat, sys

start_in   = '/firstfour/Audible'

def do_album(ofile, data):
    global bookname
    data = data.replace(' (Unabridged)','')
    ofile.write(f'_bk = _obj()\n')
    ofile.write(f'_bk.album = {data}\n')
    bookname = data.replace('(Unabridged)','').replace(' ','').replace(',','').replace("'",'').replace('"','')

def do_name(ofile, data):
    data = data.replace(' (Unabridged)','')
    ofile.write(f'_bk.name = {data}\n')

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
    ofile.write(f'_bk.genre: {data}\n')

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
    with open('/firstfour/Audible/aaxlist.py', 'wt') as ofile:
        ofile.write(f'class _obj: pass\n')
        ofile.write(f'books = dict()\n')
        sys.stdout = open('/firstfour/Audible/aaxlist.txt', 'wt')
        mask = '%s/*/*.aax' % (start_in)
        print ('start %s' % (mask))
        count = 0
        for file in sorted(glob.glob(mask)):
            _, filename = os.path.split(file)
            print (file)
            count = count + 1
            try:
                props = mutagen.mp4.MP4(file)
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
            ofile.write(f'_bk.filename={repr(filename)}\n')
            ofile.write(f'books["{authorname}-{bookname}"] = _bk\n')
            
        print (count)    

main()