from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('table1', meta, autoload=True)
    table.c.name.alter(String(200))


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('table1', meta, autoload=True)
    table.c.name.alter(String(100))
