class ConjuredItem:
    def update_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 2
        item.sell_in = item.sell_in - 2
        if item.sell_in < 0:
            if item.quality > 0:
                item.quality = item.quality - 4