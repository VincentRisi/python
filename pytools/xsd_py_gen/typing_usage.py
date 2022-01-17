from typing import NewType, List, Tuple
ATTRIB = NewType('ATTRIB', int)
PSEUDO = NewType('PSEUDO', int)
ASIS   = NewType('ASIS', int)

class RecordType:
    column: Tuple[str,ATTRIB]
    whizz: Tuple[str,PSEUDO]
    def __init__(self):
        self.isNew = ''
        self.whizz = ''
        self.column = ''

class MsgTableType:
    record: List[RecordType]
    def __init__(self):
        self.record = []

rt = RecordType()
print ('RecordType', rt.__annotations__)

mtt = MsgTableType()
print ('MsgTableType', mtt.__annotations__)
