class BackstagePass:
    def update_quality(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = item.quality + 3
        elif item.sell_in <= 10:
            item.quality = item.quality + 2
        else:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0
        if item.quality > 50:
            item.quality = 50