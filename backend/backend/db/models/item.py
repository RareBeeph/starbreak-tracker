from .base import BaseModel
from peewee import BitField
from peewee import TextField


class Item(BaseModel):
    equip_slot = TextField()  # Might be better as an enum
    name = TextField()
    supported_modifiers = BitField()  # Include repeats separate from unrepeated forms
