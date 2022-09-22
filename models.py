from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from config import DB_URL

engine = create_engine(DB_URL, echo=False)
base = declarative_base()


class Item(base):

    __tablename__ = 'Item'
    id = Column(Integer, primary_key=True)
    image = Column(String)
    title = Column(String)
    date = Column(String)
    location = Column(String)
    beds = Column(String)
    description = Column(String)
    price = Column(String)

