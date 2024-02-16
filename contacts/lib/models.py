from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String,Date,DateTime,Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime



engine = create_engine('sqlite:///phonebook.db')



Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    number = Column(Integer())
    email = Column(String(), index=True, unique=True)
    address = Column(Text())
    created_at = Column(DateTime(), default=datetime.utcnow())
    updated_at = Column(DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())


    def __repr__(self):
        return f"id {self.id}: " \
            + f"name {self.name}, " \
            + f"number {self.number}, " \
            + f"email {self.email}, " \
            + f"address {self.address} ," \
            + f"created_at {self.created_at} ," \
            + f"updated_at {self.updated_at}"