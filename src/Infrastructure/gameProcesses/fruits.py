import os

import pygame
from src.Core.Abstract import item


class PacDot(item.FruitEntity):
    def __init__(self):
        super().__init__()
        self.score = 5
        self.eat_sound = pygame.mixer.Sound(os.path.join('src', os.path.join('Core',
                                                         os.path.join('sounds', 'pacman_chomp.wav'))))
        self.eat_sound.play()


class Cherry(item.FruitEntity):
    def __init__(self):
        super().__init__()
        self.score = 100
        self.time_until_disappear = 10

        self.image = pygame.transform.scale(pygame.image.load('src/Core/images/Cherry.webp'), (35, 35))
        self.rect = self.image.get_rect()
