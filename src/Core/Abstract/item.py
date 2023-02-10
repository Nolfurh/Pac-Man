import abc


class ItemEntity(abc.ABC):
    def use(self):
        pass


class BonusEntity(ItemEntity):
    pass


class FruitEntity(ItemEntity):
    pass
