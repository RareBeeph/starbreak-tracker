from .item import Item


class Drop(Item):
    modifiers = None  # List containing modifier instances, possibly including duplicates
    isEliteBossDrop = None  # Boolean keeping track of whether the weapon was expected to drop with 0-3 modifiers, or 1-4, so as to not mix samples with different odds
