xxx='''
("class OciSqlReturning():");
(1, "def __init__(self, table, field):");
(2, "self.head = ''");
(2, "self.output = ''");
(2, "self.sequence = f'  {table}Seq.nextval'");
(2, "self.tail = 'returning {field} into :{field} '");
(2, "self.dropField = ''");
(2, "self.usesPlSql = True");
(1, "def check_use(self, value):");
(2, "return value");
("dbapi_util.returning = OciSqlReturning");
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
(2, "_command = f'select {self.tableSeq}.nextval from dual'");
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
("dbapi_util.get_sequence = get_sequence");
();
'''.splitlines()
for line in xxx:
    if line[:2] == '()': print ()
    elif line[:2] == '("': print(f'{line[2:-3]}')
    elif line[:2] == '(1': print(f'    {line[5:-3]}')
    elif line[:2] == '(2': print(f'        {line[5:-3]}')
    elif line[:2] == '(3': print(f'            {line[5:-3]}')
    else: print(f'#{line}')

