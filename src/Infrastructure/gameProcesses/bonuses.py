import time
from src.Core.Abstract import item
from src.Infrastructure.gameProcesses.statistics import Statistics
import threading


class PowerPellet(item.BonusEntity):
    """
    A class that representing the power pellet, concrete realisation of bonus

    Methods:
    --------
    activate():
        Activating the Power pellet bonus power.
    use():
        Defines a logic when bonus can be picked up, but not activated.
    """
    def activate(self):
        """
        Activates the power pellet bonus ability and then automatically deactivates it.
        :return:
        """
        Statistics.activatedBonuses.append(self)
        time.sleep(10)
        Statistics.activatedBonuses.remove(self)
        
    @staticmethod
    def use():
        """
        Not implemented
        :param statistics: A statistics object containing information about the game statistics.
        """
        pass

    def __init__(self):
        """
        Initializes the Power pellet object.
        """
        task = threading.Thread(target=self.activate)
        task.start()
