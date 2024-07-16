# database.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker,declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///projects.db')
Session = sessionmaker(bind=engine)

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    create_user=Column(String)
    create_time=Column(DateTime)

Base.metadata.create_all(engine)

def get_session():
    return Session()
