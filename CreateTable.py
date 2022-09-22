from sqlalchemy import Column, Integer, MetaData, Table, Text
from sqlalchemy import create_engine
from config import DB_URL

engine = create_engine(DB_URL, echo=False)
meta = MetaData()

Item = Table("Item", meta, Column("id", Integer, primary_key=True),
             Column("image", Text),
             Column("title", Text),
             Column("date", Text),
             Column("location", Text),
             Column("beds", Text),
             Column("description", Text),
             Column("price", Text))

meta.create_all(engine)
