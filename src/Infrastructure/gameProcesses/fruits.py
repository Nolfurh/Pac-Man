from src.Core.Abstract import item


class PacDot(item.FruitEntity):
    def __int__(self):
        super().__init__()
        self.score = 5


class Cherry(item.FruitEntity):
    def __int__(self):
        super().__init__()
        self.score = 100
