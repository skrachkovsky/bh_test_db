from sqlalchemy import Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Table1(Base):
    __tablename__ = 'table1'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))

    tables2 = relationship('Table2', remote_side='Table2.table1')


class Table2(Base):
    __tablename__ = 'table2'

    id = Column(Integer, primary_key=True, autoincrement=True)
    table1 = Column(Integer, ForeignKey('table1.id'))


engine = create_engine('mysql+mysqldb://root@localhost/test', echo=True)

Session = sessionmaker(bind=engine)

session = Session()

# session.add(Table1(name='test2'))
# session.add(Table2(table1=2))
# session.commit()
r = session.query(Table1).filter(Table1.id==1).all()
print(r[0].tables2)
