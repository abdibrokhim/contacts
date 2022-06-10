from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///./contact.db', echo=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
Base = declarative_base()


def update_table():
    pass


class Contact(Base):
    __tablename__ = 'CONTACT'
    ID = Column(Integer, primary_key=True)
    FULLNAME = Column(String(50))
    NICKNAME = Column(String(50))
    OCCUPATION = Column(String(50))
    PHONE_NUMBER = Column(String(50))
    EMAIL = Column(String(50))
    ADDRESS = Column(String(50))

    def __repr__(self):
        return "<Contact(FULLNAME='%s', NICKNAME='%s', OCCUPATION='%s', " \
               "PHONE_NUMBER='%s', EMAIL='%s', ADDRESS='%s')>" % (
                   self.FULLNAME, self.NICKNAME, self.OCCUPATION, self.PHONE_NUMBER, self.EMAIL, self.ADDRESS)

# Base.metadata.create_all(engine)