import sys
import pygame as pg
from src.Infrastructure.gameCore import GameSettings
from src.Infrastructure.gameMaps import Level_1
from src.Infrastructure.inputController import Events


class PackManWorld():

    def __init__(self):
        pg.init()

        self.settings = GameSettings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.game_map = Level_1()
        self.events = Events()

    # main game loop
    def run_game(self):
        while True:
            self._update_screen()
            self.events.check_events()


    # here on-screen objects will be
    def _update_screen(self):
        self.screen.fill(self.settings.map_background)
        self.game_map.draw_map()

        pg.display.flip() # [last function] to redraw last frames on screen