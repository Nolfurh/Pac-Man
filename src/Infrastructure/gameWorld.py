import sys
import pygame as pg
from src.Infrastructure.gameCore import GameSettings
from src.Infrastructure.gameMaps import Level_1
from src.Infrastructure.inputController import Events
from src.Infrastructure.gameProcesses.statistics import Statistics
from src.Infrastructure.statisticsView import StatisticsView
from src.Core.Abstract.item import BonusEntity
from src.Core.Abstract.player import Pacman
from src.Core.Abstract.enemy import Ghosts

class PackManWorld():

    def __init__(self):
        pg.init()

        self.settings = GameSettings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.game_map = Level_1()
        self.player = Pacman(self)
        self.events = Events(self)

        self.statistics = Statistics()
        self.statistics_view = StatisticsView(self.statistics, self.screen, self.player)
        BonusEntity.statistics = self.statistics
        Statistics.allPacDots = self.game_map.get_PacDots()

        self.vulnerable = pg.transform.scale(pg.image.load('src/Core/images/vulnerable-ghost.bmp'), (35, 35))
        self.rect = self.vulnerable.get_rect()
        self.rect.centerx = 350
        self.rect.centery = 350

        self.playerx = self.player.rect.x
        self.playery = self.player.rect.y

        self.ghosts = Ghosts(self)

    # main game loop
    def run_game(self):
        while True:
            self._update_screen()
            self.events.check_events()
            self.player.update()

            self.playerx = self.player.rect.centerx
            self.playery = self.player.rect.centery

            self.ghosts.update(self)

            pg.display.flip()  # [last function] to redraw last frames on screen

    # here on-screen objects will be
    def _update_screen(self):
        self.screen.fill(self.settings.map_background)
        self.game_map.draw_map()
        self.statistics_view.ShowStatistics()
        self.player.blitme()
