from .item import Item
from backend.db import conn

all_models = [Item]

conn.create_tables(all_models)
