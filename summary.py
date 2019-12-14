datetime.today().minute
os.getcwd()
sys.platform
sys.version
os.environ
os.getenv('HOME')
datetime.date.isoformat(datetime.date.today())
time.strftime("%I: %M")
time.strftime("%A %p")
html.escape("")
html.unescape("")
for i in range(4):
time.sleep(5)
dir(random)
help(random.randint)
random.randint(1, 60)
for i in range(99, 0, -1):
len()
[list].append()
if a not in [list]
[list].remove()
[list].pop
[list].extend
[list].insert(i, v)
list()
str = '',join(list)
[list].copy
'str' * 3
for k in {dist}:
  {dist}[k]
sorted()
for k, v in sorted({dist}.items()):
{dist}.setdefault(k, v)
set('aio')
{many}.union{many}
{many}.difference{many}
{many}.intersection{many}
type()
("tuple",)
pprint.pprint({dict})
def function(a:srt, b:int) -> set:
def function(a:srt, b:str='aeio') -> set:
###
def func(a:str, b:str='asdf') -> set:
func(b='qwe', a='zxcv')
###
dict(name = "John", age = 36, country = "Norway")
tuple("asdf")
###
todos = open('todos.txt', 'a')
print('Put out the reash.', file=todos)
todos.close
###
print(line, end='')
###
with open('todos.txt') as tasks:
  for chore in tasks:
    print(chore, end='')
###
escape('This is a <Request>')
print('asd', '123', sep='\t')
#####
dbconfig = {'host': '127.0.0.1', 'user': 'vsearch', 'password': 'vsearchpasswd', 'database': 'vsearchlogDB',}
import mysql.connector
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """desc log"""
cursor.execute(_SQL)
res = cursor.fetchall()
#fetchone
#fetchmany
for row in res:
  print(row)
_SQL = """insert into log
  (phrase, letters, ip, browser_string, results)
    values
      ('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""
cursor.execute(_SQL)
_SQL = """insert into log
  (phrase, letters, ip, browser_string, results)
    values
      (%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()'))
conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
  print(row)
cursor.close()
conn.close()
#####
import mysql.connector
class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

##
from DBcm import UseDatabase
    dbconfig = {
      'host': '127.0.0.1',
      'user': 'vsearch',
      'password': 'vsearchpasswd',
      'database': 'vsearchlogDB',
    }
with UseDatabase(dbconfig) as cursor:
    _SQL = """show tables"""
    cursor.execute(_SQL)
    data = cursor.fetchall()
###
