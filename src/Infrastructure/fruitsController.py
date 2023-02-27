import pygame
import src.Infrastructure.gameProcesses.fruits as fruits
from src.Infrastructure.gameProcesses.statistics import Statistics
from src.Infrastructure.gameCore import GameSettings
import time


class FruitsController:

    def __init__(self, time_to_fruit1, time_to_fruit2, game_map, player, settings):
        """
        Initialize a new instance of the FruitsController class.

        Parameters
        ----------
        time_to_fruit1 : int
            Time after which the first fruit will appear.
        time_to_fruit2 : int
            Time after which the second fruit will appear.
        game_map : GameMap
            The current game map.
        player : Player
            The current player.
        settings : Settings
            The current game settings.

        """
        self.time_to_fruit_appearing1 = time_to_fruit1
        self.time_to_fruit_appearing2 = time_to_fruit2

        self.first_fruit_appeared = False
        self.second_fruit_appeared = False

        self.map = game_map
        self.player = player
        self.settings = settings

        self.fruit_appeared = False
        self.fruit = None
        self.time_of_fruit_creation = None
        self.start_time = time.process_time()

    def spawn_fruit(self):
        """
        Create a new instance of the Fruit class and draw it on the game screen.
        """

        self.fruit = fruits.Cherry()
        self.time_of_fruit_creation = time.process_time()
        self.draw_fruit(self.fruit)

    def draw_fruit(self, fruit):
        """
        Draw the given fruit on the game screen.
        Parameters
        ----------
        fruit : Fruit
            The fruit to draw.

        """

        self.map.screen.blit(fruit.image, (self.map.fruit_appearing[0] * (self.settings.screen_width // 30) - 5,
                                           self.map.fruit_appearing[1] * (
                                                   (self.settings.screen_height - 50) // 32) - 5))

    def fruit_controller_update(self):
        """
         Update the state of the fruit controller.
        """
        if self.fruit is not None:
            self.draw_fruit(self.fruit)

            if self.map.fruit_appearing[0] == int((self.player.x + 17) // (self.settings.screen_width // 30)) and \
                    self.map.fruit_appearing[1] == int(
                    (self.player.y + 17) // ((self.settings.screen_height - 50) // 32)):
                Statistics.score += self.fruit.score
                self.fruit.eat_sound.play()
                self.fruit = None
            else:
                if int(time.process_time()) - int(self.time_of_fruit_creation) == self.fruit.time_until_disappear:
                    self.fruit = None
                    self.time_of_fruit_creation = None
        else:
            if int(time.process_time()) - int(self.start_time) == self.time_to_fruit_appearing1 and not self.first_fruit_appeared:
                self.spawn_fruit()
                self.first_fruit_appeared = True

            if int(time.process_time()) - int(self.start_time) == self.time_to_fruit_appearing2 and not self.second_fruit_appeared:
                self.spawn_fruit()
                self.second_fruit_appeared = True
