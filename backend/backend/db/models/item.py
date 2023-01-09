from .base import BaseModel
from peewee import BigBitField, TextField


class Item(BaseModel):
    equip_slot = TextField()  # Might be better as an enum
    name = TextField()
    supported_modifiers = BigBitField()  # Include repeats separate from unrepeated forms
