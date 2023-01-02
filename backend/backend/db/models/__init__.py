from .weapon import Weapon
from backend.db import conn

all_models = [Weapon]

conn.create_tables(all_models)
