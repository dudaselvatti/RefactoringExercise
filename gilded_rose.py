# -*- coding: utf-8 -*-

from updaters.AgedBrie import AgedBrie
from updaters.NormalItem import NormalItem
from updaters.Sulfuras import Sulfuras
from updaters.BackstagePass import BackstagePass
from updaters.Conjured import ConjuredItem

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                updater = Sulfuras()
                updater.update_quality(item)
            elif item.name == "Aged Brie":
                updater = AgedBrie()
                updater.update_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                updater = BackstagePass()
                updater.update_quality(item)
            elif item.name.startswith("Conjured Mana Cake"):
                updater = ConjuredItem()
                updater.update_quality(item)
            else:
                updater = NormalItem()
                updater.update_quality(item)
            


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
