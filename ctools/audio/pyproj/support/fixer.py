xxx='''
("class ODBCReturning():");
(1, "def __init__(self, table, field):");
(2, "self.head = ''");
(2, "self.output = f'  output Inserted.{field}'");
if (table.hasSequence)
(2, "self.sequence = f'  nextval for {table}Seq'");
(2, "self.doesGeneratedKeys = False"); 
else
(2, "self.sequence = ''");
(2, "self.doesGeneratedKeys = True");
(2, "self.tail = ''");
(2, "self.dropField = ''");
(2, "self.usesPlSql = False");
(1, "def check_use(self, value):");
if (table.hasSequence)
(2, "return value");
else
(2, "return ''");
("dbapi_util.returning = ODBCReturning");
();
("class Dutil_sequence(object):");
(1, "def _make(self): return Dutil_sequence()");
(1, "__slots__ = ['seq', 'tableSeq']");
(1, "def __init__(self):");
(2, "self.seq = ''");
(2, "self.tableSeq = ''");
(1, "def _fields(self):");
(2, "return Dutil_sequence.__slots__");
();
("class util_sequence(Dutil_sequence):");
(1, "def _get_output(self, _result):");
(2, "self.seq = _result[0]");
(2, "return 1");
(1, "def _copy_input(self, record):");
(2, "record.tableSeq = self.tableSeq");
(1, "def execute(self, connect):");
(2, "_command = f'select nextval for {self.tableSeq}'");
(2, "cursor = connect.cursor()");
(2, "cursor.execute(_command)");
(2, "record = util_sequence()");
(2, "self._copy_input(record)");
(2, "result = cursor.fetchone()");
(2, "if result == None:");
(3, "return None");
(2, "record._get_output(result)");
(2, "return record");
();
("def get_sequence(connect, table):");
(1, "query = util_sequence()");
(1, "query.tableSeq = f'{table}Seq'");
(1, "query.execute(connect)");
(1, "return query.seq");
();
'''.splitlines()
for line in xxx:
    if line[:2] == '()': print ()
    elif line[:2] == '("': print(f'{line[2:-3]}')
    elif line[:2] == '(1': print(f'    {line[5:-3]}')
    elif line[:2] == '(2': print(f'        {line[5:-3]}')
    elif line[:2] == '(3': print(f'            {line[5:-3]}')
    else: print(f'#{line}')

