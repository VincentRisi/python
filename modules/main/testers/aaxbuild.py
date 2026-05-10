from aaxlist import books
print (len(books))
delim = '|'
use_fields = []
for book in books:
    for field in vars(book):
        if field not in use_fields:
            use_fields.append(field)

with open('aaxlist.input', 'w') as ofile:
    with open('aaxlist.h', 'w') as hfile:
        hfile.write('#pragma once\n\n')
        hfile.write('struct Book\n{\n')
        line = ''
        separator = ''
        enum_list = []
        for field in use_fields:
            if field in ['description']:
                continue
            enum_list.append(field)
            hfile.write(f'    const char* {field};\n')
            line += f'{separator}{field}'
            separator = delim
        hfile.write('};\n')
        hfile.write(f'const char* book_fields = "{line}";\n')
        hfile.write('enum BookFields\n{\n')
        for field in enum_list:
            hfile.write(f'    {field},\n')
        hfile.write('    BookFieldsCount\n')
        hfile.write('};\n')
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
            if field in ['description']:
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
