import glob, shutil, os.path

def do_copy(a, b):
    if os.path.exists(b): return
    try:
        print (a, b)
        shutil.copyfile(a, b)
    except:
        print (failed)	    


targetdir = '/media/vince/Audible/source'

aaxfiles = list()
for file in glob.glob('/firstfour/Audible/*/*.aax'):
    aaxfiles.append(file)
    dir, namext = os.path.split(file)
    name, ext = os.path.splitext(namext)
    mp3file = f'{dir}/mp3/{name}.mp3'
    targetaax = f'{targetdir}/{namext}'
    do_copy(file, targetaax)
    if os.path.exists(mp3file):
        targetmp3 = f'{targetdir}/{name}.mp3'
        do_copy(mp3file, targetmp3)
    