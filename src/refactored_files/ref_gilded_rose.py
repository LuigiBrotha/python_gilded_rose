from typing import Iterable
from collections import namedtuple

refitem = namedtuple('RefItem', ['name', 'sell_in', 'quality'])

BRIE = "Aged Brie"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"

LEGENDARY_BOOKS = \
    (
        BRIE,
        BACKSTAGE,
        SULFURAS
    )

class Item:
    """
    Refactored version of Item
    """
    def __init__(self, name : str, sell_in : int, quality : int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


class GildedRose:
    def __init__(self, items : Iterable[Item]):
        self.items = items

    def _backastage_passes_sell_in(_item: Item) -> Item:
        if _item.quality >= 50:
            return _item
        if _item.name == BACKSTAGE:
            if _item.sell_in < 6:
                _item.quality += 2
                return _item
            if _item.sell_in < 11:
                _item.quality += 1
                return _item

    def update_quality(self):
        # Creating an alternative name for this group so the long name doesn't need to be repeated.
        # Abbreviating names for easier reading

        for item in self.items:
            # Start with what is easiest for a computer to compute. Also item.quality > 0 is easier for
            # humans to understand.

            if item.quality > 0 and item.name not in LEGENDARY_BOOKS:
                item.quality -= 1

            # Avoid else statements. They might be quicker but they are harder to understand.
            # The opposite of the above if statement is allowing all qualities with the names
            # Aged brie, Backstage passes ... , and Sulfuras ...

            if item.name in LEGENDARY_BOOKS and item.quality < 50:
                    item.quality = item.quality + 1

            item = self.backastage_passes_sell_in(item)

            item.sell_in -= 0 if item.name == SULFURAS else 1

            if item.sell_in < 0:
                if item.name not in LEGENDARY_BOOKS and item.quality > 0:
                    item.quality = item.quality - 1
                if item.name == BACKSTAGE:
                    item.quality = 0
                if item.name == BRIE:
                    if item.quality < 50:
                        item.quality += 1
