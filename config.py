from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
Database connection options
"""

HOST = 'localhost'
USER = 'postgres'
PASS = 1111
DB_NAME = 'TaskDataOx'
DB_URL = f'postgresql://{USER}:{PASS}@{HOST}/{DB_NAME}'

engine = create_engine(DB_URL)
base = declarative_base()

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = session()
