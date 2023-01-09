from .base import BaseModel
from .item import Item
from peewee import BigBitField, BooleanField, ForeignKeyField


class Drop(BaseModel):
    item = ForeignKeyField(Item, backref="drops")
    modifiers = BigBitField()  # Include repeats separate from unrepeated forms
    is_elite_boss_drop = BooleanField()  # Distinguishes 0-3 mod and 1-4 mod samples
