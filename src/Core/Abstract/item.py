import abc


class ItemEntity(abc.ABC):

    @staticmethod
    def use(statistics):
        pass


class BonusEntity(ItemEntity):
    statistics = None



class FruitEntity(ItemEntity):
    pass
