# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.command import upgrade


DB_URL = 'sqlite:///fitlife_log.db'

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)

def init_db():
    from lib.models import Base  # Import the Base model from lib.models
    Base.metadata.create_all(engine)

def run_migrations():
    from alembic import command
    from alembic.config import Config
    alembic_config = Config('alembic.ini')
    command.upgrade(alembic_config, 'head')

