from .base import BaseModel
from peewee import BitField
from peewee import TextField


class Item(BaseModel):
    equipSlot = TextField()  # Might be better as an enum
    name = TextField()
    supportedModifiers = BitField()  # Include repeats separate from unrepeated forms
