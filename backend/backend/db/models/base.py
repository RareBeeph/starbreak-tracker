from backend.db import conn
from peewee import Model


class BaseModel(Model):
    class Meta:
        database = conn
