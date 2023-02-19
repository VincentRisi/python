import os, os.path, shutil, glob, mutagen.mp4, stat, sys, re, base64

start_in   = '/media/vince/Audible/source'

biggest = 0

def do_aacr(ofile, data):
    ofile.write(f'_bk.aacr = {data}\n')

def do_aart(ofile, data):
    ofile.write(f'_bk.aart = {data}\n')

def do_album(ofile, data):
    ofile.write(f'_bk.album = {data}\n')

def do_atday(ofile, data):
    ofile.write(f'_bk.atday = {data}\n')

def do_atnu(ofile, data):
    ofile.write(f'_bk.atnu = {data}\n')

def do_atppi(ofile, data):
    ofile.write(f'_bk.atppi = {data}\n')

def do_atpst(ofile, data):
    ofile.write(f'_bk.atpst = {data}\n')

def do_atpti(ofile, data):
    ofile.write(f'_bk.atpti = {data}\n')

def do_author(ofile, data):
    ofile.write(f'_bk.author = {data}\n')

def do_cdek(ofile, data):
    ofile.write(f'_bk.cdek = {data}\n')

def do_cdet(ofile, data):
    ofile.write(f'_bk.cdet = {data}\n')

def do_comment(ofile, data):
    ofile.write(f'_bk.comment = {data}\n')

def do_cprt(ofile, data):
    ofile.write(f'_bk.cprt = {data}\n')

def do_description(ofile, data):
    global biggest
    n=len(data)
    if n > biggest:
        biggest = n
    ofile.write(f'_bk.description = {data}\n')

def do_genre(ofile, data):
    ofile.write(f'_bk.genre = {data}\n')

def do_guid(ofile, data):
    ofile.write(f'_bk.guid = {data}\n')

def do_name(ofile, data):
    ofile.write(f'_bk.name = {data}\n')

def do_narrator(ofile, data):
    ofile.write(f'_bk.narrator = {data}\n')

def do_prid(ofile, data):
    ofile.write(f'_bk.prid = {data}\n')

def do_publisher(ofile, data):
    ofile.write(f'_bk.publisher = {data}\n')

def do_released(ofile, data):
    ofile.write(f'_bk.released = {data}\n')

def do_sti(ofile, data):
    ofile.write(f'_bk.sti = {data}\n')

def do_trkn(ofile, data):
    ofile.write(f'_bk.trkn = {data}\n')

def do_vers(ofile, data):
    ofile.write(f'_bk.vers = {data}\n')

#-- '@ppi'
#-- '@PST'
#-- '@pti'
#-- '@sti'
#-- 'AACR'
#-- 'aART'
#-- 'atnu'
#-- 'CDEK'
#-- 'CDET'
#-- 'covr'
#-- 'cprt'
#-- 'GUID'
#-- 'PASN'
#-- 'prID'
#-- 'rldt'
#-- 'trkn'
#-- 'VERS'
#-- '©alb'
#-- '©ART'
#-- '©cmt'
#-- '©day'
#-- '©des'
#-- '©gen'
#-- '©nam'
#-- '©nrt'
#-- '©pub'

names = dict()
names['@ppi'] = 'atppi', do_atppi             
names['@PST'] = 'atpst', do_atpst             
names['@pti'] = 'atpti', do_atpti             
names['@sti'] = 'sti', do_sti                 
names['AACR'] = 'aacr', do_aacr               
names['aART'] = 'aart', do_aart               
names['atnu'] = 'atnu', do_atnu               
names['CDEK'] = 'cdek', do_cdek               
names['CDET'] = 'cdet', do_cdet               
names['cprt'] = 'cprt', do_cprt               
names['GUID'] = 'guid', do_guid               
names['prID'] = 'prid', do_prid               
names['rldt'] = 'released', do_released       
names['trkn'] = 'trkn', do_trkn               
names['VERS'] = 'vers', do_vers               
names['©alb'] = 'album', do_album             
names['©ART'] = 'author', do_author           
names['©cmt'] = 'comment', do_comment         
names['©day'] = 'atday', do_atday             
names['©des'] = 'description', do_description 
names['©gen'] = 'genre', do_genre             
names['©nam'] = 'name', do_name               
names['©nrt'] = 'narrator', do_narrator       
names['©pub'] = 'publisher', do_publisher     

taglist = list()

def main():
    global filename
    with open('/media/vince/Audible/aaxlist.py', 'wt') as ofile:
        ofile.write(f'class _obj: pass\n')
        ofile.write(f'books = list()\n')
        sys.stdout = open('/media/vince/Audible/aaxlist.txt', 'wt')
        mask = '%s/*.aax' % (start_in)
        print ('start %s' % (mask))
        count = 0
        for file in sorted(glob.glob(mask)):
            _, filext = os.path.split(file)
            filename, _ = os.path.splitext(filext)
            ofile.write(f'_bk = _obj()\n')
            ofile.write(f'books.append(_bk)\n')
            ofile.write(f'_bk.filename = {repr(filename)}\n')
            count = count + 1
            try:
                props = mutagen.mp4.MP4(file)
                for key in props:
                    if not key in taglist:
                        taglist.append(key)
                for tag in names:
                    name, func = names[tag]
                    if tag in props:
                        try:
                            data = props[tag]
                            if tag != 'covr':
                               print('%s: %s' % (name, data[0]))
                               func(ofile, repr(data[0]))
                            else:
                               data = base64.a85encode(data[0])
                               print('%s(%d): %s' % (name, len(data), data))
                               func(ofile, data)

                        except:
                            print('{%s error}' % (name))  
            except:
                print('{%s error}' % (file))
            #ofile.write(f'books["{authorname}-{bookname}"] = _bk\n')
    
        print (count)    
    print (taglist)
    print (biggest)


main()