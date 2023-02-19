import abc


class ItemEntity(abc.ABC):

    @staticmethod
    def use(statistics):
        pass


class BonusEntity(ItemEntity):
    statistics = None



class FruitEntity(ItemEntity):
    def __init__(self):
        super().__init__()
        self.score = 0
