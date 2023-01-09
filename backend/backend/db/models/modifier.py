from .base import BaseModel
from peewee import TextField


class Modifier(BaseModel):
    name = TextField()
