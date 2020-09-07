import sqlite3

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

connect = sqlite3.connect('test.db')

# try:
# cursor = connect.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# finally:
#     cursor.close()
# print(cursor.rowcount)
# connect.commit()
# cursor2 = connect.cursor()
# cursor2.execute('select * from user')
# print(cursor2.fetchall())

Base = declarative_base()

class Student(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    archivement = relationship('Archivement')

    def __str__(self):
        return ('姓名:%s  学号:%s' % (studentO.name, studentO.id))

class Archivement(Base):
    __tablename__ = 'archivement'
    id = Column(String(20), primary_key=True)
    student_id = Column(String(20), ForeignKey('user.id'))
    term = Column(String(20))
    chinese = Column(String(4))
    english = Column(String(4))
    history = Column(String(4))
    mathemmatics = Column(String(4))

    def __str__(self):
        return '学年：%s \n  语文:%s  数学:%s \n  历史:%s  英语:%s' % (self.term, self.chinese, self.mathemmatics, self.history, self.english)

engine = create_engine('sqlite:///test.db')
DBSession = sessionmaker(bind=engine)

session = DBSession()
# student = Student(101, 'TianNa')
# session.add(student)
# session.commit()

studentO = session.query(Student).filter(Student.id == '1').one()
print(studentO)
print('成绩单:')

for archivement in studentO.archivement:
    print(archivement)

session.close()
