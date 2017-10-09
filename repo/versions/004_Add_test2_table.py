from sqlalchemy import *
from migrate import *

meta = MetaData()

table2 = Table('table2', meta,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('table1', Integer, ForeignKey('table1.id'))
              )


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    Table('table1', meta, autoload=True)
    table2.create()



def downgrade(migrate_engine):
    meta.bind = migrate_engine
    Table('table1', meta, autoload=True)
    table2.drop()
