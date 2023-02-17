import time
from src.Core.Abstract import item
from src.Infrastructure.gameProcesses.statistics import Statistics
import threading


class PowerPellet(item.BonusEntity):
    def activate(self):
        Statistics.activatedBonuses.append(self)
        time.sleep(10)
        Statistics.activatedBonuses.remove(self)
        
    @staticmethod
    def use():
        pass

    def __init__(self):
        task = threading.Thread(target=self.activate)
        task.start()
