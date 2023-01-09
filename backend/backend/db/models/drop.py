from .base import BaseModel
from peewee import BigBitField, BooleanField


class Drop(BaseModel):
    modifiers = BigBitField()  # Include repeats separate from unrepeated forms
    is_elite_boss_drop = BooleanField()  # Distinguishes 0-3 mod and 1-4 mod samples
