from aaxlist import books
print (len(books))
delim = '|'
use_fields = list()
for book in books:
    for field in vars(book):
        if field not in use_fields:
            use_fields.append(field)
with open('aaxlist.input', 'w') as ofile:
    line = ''
    separator = ''
    for field in use_fields:
        if field in ['comment','description']:
            continue
        line += f'{separator}{field}'
        separator = delim
    ofile.write(f'{line}\n')
    
    def check(value, delim):
        if value is None:
            return ''
        if isinstance(value, str):
            if delim in value:  
                 return f'"{value}"'
            return value
        return ''
    
    for book in books:
        line = ''
        separator = ''
        for field in use_fields:
            if field in ['comment','description']:
                continue
            if hasattr(book, field):
                line += separator
                line += f"{check(getattr(book, field), delim)}"
                separator = delim
        try:
            ofile.write(f'{line}\n')
        except Exception as e:
            pass
        separator = ''
