from dbapi_util import *

# //      if (table.hasSequence)
# //      {
# //        writeln("class OciSqlReturning():");
# //        writeln(1, "def __init__(self, table, field):");
# //        writeln(2, "self.head = ''");
# //        writeln(2, "self.output = ''");
# //        writeln(2, "self.sequence = f'  {table}Seq.nextval'");
# //        writeln(2, "self.tail = 'returning {field} into :{field} '");
# //        writeln(2, "self.dropField = ''");
# //        writeln(2, "self.usesPlSql = True");
# //        writeln(1, "def check_use(self, value):");
# //        writeln(2, "return value");
# //        writeln("dbapi_util.returning = OciSqlReturning");
# //        writeln();
# //        writeln("class Dutil_sequence(object):");
# //        writeln(1, "def _make(self): return Dutil_sequence()");
# //        writeln(1, "__slots__ = ['seq', 'tableSeq']");
# //        writeln(1, "def __init__(self):");
# //        writeln(2, "self.seq = ''");
# //        writeln(2, "self.tableSeq = ''");
# //        writeln(1, "def _fields(self):");
# //        writeln(2, "return Dutil_sequence.__slots__");
# //        writeln();
# //        writeln("class util_sequence(Dutil_sequence):");
# //        writeln(1, "def _get_output(self, _result):");
# //        writeln(2, "self.seq = _result[0]");
# //        writeln(2, "return 1");
# //        writeln(1, "def _copy_input(self, record):");
# //        writeln(2, "record.tableSeq = self.tableSeq");
# //        writeln(1, "def execute(self, connect):");
# //        writeln(2, "_command = f'select {self.tableSeq}.nextval from dual'");
# //        writeln(2, "cursor = connect.cursor()");
# //        writeln(2, "cursor.execute(_command)");
# //        writeln(2, "record = util_sequence()");
# //        writeln(2, "self._copy_input(record)");
# //        writeln(2, "result = cursor.fetchone()");
# //        writeln(2, "if result == None:");
# //        writeln(3, "return None");
# //        writeln(2, "record._get_output(result)");
# //        writeln(2, "return record");
# //        writeln();
# //        writeln("def get_sequence(connect, table):");
# //        writeln(1, "query = util_sequence()");
# //        writeln(1, "query.tableSeq = f'{table}Seq'");
# //        writeln(1, "query.execute(connect)");
# //        writeln(1, "return query.seq");
# //        writeln("dbapi_util.get_sequence = get_sequence");
# //        writeln();
# //      }

def to_date14(data, format='%Y%m%d%H%M%S'):
    return datetime.strptime(data, format)

def to_date8(data, format='%Y%m%d'):
    return datetime.strptime(data, format)

def to_time6(data, format='%H%M%S'):
    return datetime.strptime(data, format)

def to_char14(data, format='%Y%m%d%H%M%S'):
    return datetime.strftime(data, format)

def to_char8(data, format='%Y%m%d'):
    return datetime.strftime(data, format)

def to_char6(data, format='%H%M%S'):
    return datetime.strftime(data, format)

def get_timestamp():
    return datetime
