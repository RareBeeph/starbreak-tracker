from .item import Item
from peewee import BitField
from peewee import BooleanField


class Drop(Item):
    modifiers = BitField()  # Include repeats separate from unrepeated forms
    isEliteBossDrop = BooleanField()  # Distinguishes 0-3 mod and 1-4 mod samples
