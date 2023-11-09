# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    registration_date = Column(DateTime, server_default='NOW()')
    
    workouts = relationship("Workout", back_populates="user")

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
   
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="workouts")
   
    exercises = relationship("Exercise", back_populates="workout")

    UniqueConstraint('user_id', 'date', name='unique_user_workout_date')

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    weight = Column(Integer)
    
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    workout = relationship("Workout", back_populates="exercises")

# Set up the SQLAlchemy engine and session
DB_URL = 'sqlite:///fitlife_log.db'
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
