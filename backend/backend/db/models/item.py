from .base import BaseModel
from peewee import CharField
from peewee import TextField


class Item(BaseModel):
    equipSlot = None  # String specifying if it's a primary weapon, etc
    name = "Test"  # String
    supportedModifiers = None  # List containing modifier instances, possibly including duplicates representing some number of times that modifier is repeatable
