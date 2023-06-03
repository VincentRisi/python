import sys, os, os.path
from datetime import date

def main():
    for dirpath,dirnames,filenames in os.walk(r"d:\vlab\python"):
        if r'\vlab\jportal' in dirpath: continue
        if r'\jtools\out' in dirpath: continue
        for file in filenames:
            _, ext = os.path.splitext(file)
            if ext in ['.cpp','.java','.py','.h']:
                file = rf'{dirpath}\{file}'
                date_of = str(date.fromtimestamp(os.path.getmtime(file)))
                if date_of >= '2022-06-01':
                    print (date_of, file)

main()