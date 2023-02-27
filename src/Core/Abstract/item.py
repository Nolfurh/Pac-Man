import abc
import os

import pygame


class ItemEntity(abc.ABC):
    """
    An abstract base class representing an item entity.

    Attributes
    ----------
    eat_sound : Sound
        A Pygame Sound object representing the sound made when an item is eaten.

    Methods
    -------
    use(statistics)
        Abstract method that is implemented by subclasses to define the effect of using an item.
    """
    def __init__(self):
        """
        Constructs a new ItemEntity object.
        """
        self.eat_sound = pygame.mixer.Sound(os.path.join('src', os.path.join('Core',
                                                                             os.path.join('sounds',
                                                                                          'pacman_eatfruit.wav'))))

    @staticmethod
    def use(statistics):
        """
        Abstract method that is implemented by subclasses to define the effect of using an item.

        Parameters
        ----------
        statistics : Statistics
            A statistics object containing information about the game statistics.
        """
        pass


class BonusEntity(ItemEntity):
    """
    A class representing a bonus item entity.

    Attributes
    ----------
    statistics : Statistics
        A statistics object containing information about the game statistics.
    """
    statistics = None



class FruitEntity(ItemEntity):
    """
    A class representing a fruit item entity.

    Attributes
    ----------
    score : int
        The score gained by eating the fruit.
    """
    def __init__(self):
        """
        Constructs a new FruitEntity object.
        """
        super().__init__()
        self.score = 0
