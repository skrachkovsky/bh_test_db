from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('table1', meta, autoload=True)
    name_col = Column('name', String(100), nullable=False)
    name_col.create(table)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    table = Table('table1', meta, autoload=True)
    table.c.name.drop()
