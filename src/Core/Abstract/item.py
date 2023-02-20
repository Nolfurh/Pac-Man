import abc
import os

import pygame


class ItemEntity(abc.ABC):
    def __init__(self):
        self.eat_sound = pygame.mixer.Sound(os.path.join('src', os.path.join('Core',
                                                                             os.path.join('sounds',
                                                                                          'pacman_eatfruit.wav'))))

    @staticmethod
    def use(statistics):
        pass


class BonusEntity(ItemEntity):
    statistics = None



class FruitEntity(ItemEntity):
    def __init__(self):
        super().__init__()
        self.score = 0
