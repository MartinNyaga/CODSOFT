from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String,Date,Boolean,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime



engine = create_engine('sqlite:///todo.db')



Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer(), primary_key=True)
    todo_name = Column(String())
    description = Column(String())
    due_date = Column(Date())
    completed = Column(Boolean())
    created_at = Column(DateTime(), default=datetime.utcnow())
    updated_at = Column(DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __repr__(self):
        return f"id {self.id}: " \
            + f"todo_name {self.todo_name}, " \
            + f"descrition {self.description}, " \
            + f"due_date {self.due_date}, " \
            + f"completed {self.completed} ," \
            + f"created_at {self.created_at} ," \
            + f"updated_at {self.updated_at}"