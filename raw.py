import _mysql

db = _mysql.connect('localhost', 'root', db='test')

db.query('select * from table1')
res = db.use_result()
print(res.fetch_row())

db.close()

import MySQLdb

db = MySQLdb.connect('localhost', 'root', db='test')

c = db.cursor()
c.execute('select * from table1 where id < %s', (100,))

print(c.fetchone())

c.close()

c = db.cursor()
c.executemany(
      'insert into table1 (name) values (%s)',
      [
          ('name2',),
          ('name3',),
          ('name4',),
          ('name5',),
          ('name6',),
      ])
db.commit()
c.close()
db.close()