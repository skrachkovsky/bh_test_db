from sqlalchemy import *
from migrate import *

meta = MetaData()

table = Table('table1', meta,
              Column('id', Integer, primary_key=True, autoincrement=True)
              )


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
