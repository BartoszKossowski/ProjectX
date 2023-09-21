import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def shickPhick(ip, url, username, password, fu, lu):

    Base = declarative_base()

    class Person(Base):
        __tablename__ = ip

        url = Column("Url", String, primary_key=True)
        username = Column("Username", String)
        password = Column("Password", String)
        fu = Column("first_usage", String)
        lu = Column('last_usage', String)

        def __init__(self, url, username, password, fu, lu):
            self.url = url
            self.username = username
            self.password = password
            self.fu = fu
            self.lu = lu

        def __repr__(self):
            return f"({self.url}) {self.username} {self.password} {self.fu} {self.lu}"

    engine = create_engine("sqlite:///mydb.db", echo=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    person = Person(url, username, password, fu, lu)
    session.add(person)
    session.commit()


