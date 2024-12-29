# Test cases for Gilded Rose where we test the results of the original function against the refactored_files function.
from itertools import product

from src.starting_files.gilded_rose import Item
from src.refactored_files.ref_gilded_rose import Item as RefactoredItem

from src.starting_files.gilded_rose import GildedRose
from src.refactored_files.ref_gilded_rose import GildedRose as RefactoredGildedRose

# List of inputs found in the assignment

name_list = ["Aged Brie",
             "Backstage passes to a TAFKAL80ETC concert",
             "Sulfuras, Hand of Ragnaros",
             "+5 Dexterity Vest",
             "Elixir of the Mongoose",
             "Conjured Mana Cake"]

# Range of inputs which could be troublesome

sell_in_list = [100, 5,6,7,9,10,11,0, -100]
quality_list = [100, 0, 47,48,49,50,51,52,-100]

def test_item():
    """
    Test to check if items are equal. Strictly speaking you don't have to refactor Item as
    part of the challenge but seeing as I want to add type hints I do need to check the results.
    :return:
    """
    for name, sell_in, quality in product(name_list, sell_in_list, quality_list):
        item = Item(name, sell_in, quality)
        refactored_item = RefactoredItem(name, sell_in, quality)

        assert item.name == refactored_item.name
        assert item.sell_in == refactored_item.sell_in
        assert item.quality == refactored_item.quality

def test_gilded_rose():
    """
    Test to check if the results of the gilded rose are equal.
    :return:
    """
    item_list = list(Item(*i) for i in product(name_list, sell_in_list, quality_list))
    gildedrose = GildedRose(item_list).items
    refactoredgildedrose = RefactoredGildedRose(item_list).items

    assert gildedrose == refactoredgildedrose

    for item, ref_item in zip(gildedrose, refactoredgildedrose):
        assert item.name == ref_item.name
        assert item.sell_in == ref_item.sell_in
        assert item.quality == ref_item.quality
