import os
import sys
import pygame as pg
from src.Infrastructure.gameCore import GameSettings
from src.Infrastructure.gameMaps import Level_1
from src.Infrastructure.inputController import Events
from src.Infrastructure.gameProcesses.statistics import Statistics
from src.Infrastructure.statisticsView import StatisticsView
from src.Core.Abstract.item import BonusEntity
from src.Core.Abstract.player import Pacman
from src.Infrastructure.fruitsController import FruitsController
from src.Core.Abstract.enemy import Ghosts
from src.Infrastructure.pacmanCMD import pacmd

class PackManWorld():
    """
    The main class for the Pac-Man game.

    Attributes:
    -----------
    settings : GameSettings
        The instance of GameSettings.
    pacmd : pacmd
        The instance of pacmd, which is responsible for parsing command line arguments.
    screen : Surface
        The screen on which the game will be displayed.
    game_map : Level_1
        The instance of Level_1, which is responsible for generating the map of the game.
    player : Pacman
        The instance of Pacman, which represents the player character in the game.
    events : Events
        The instance of Events, which handles the input events.
    statistics : Statistics
        The instance of Statistics, which holds the game statistics.
    statistics_view : StatisticsView
        The instance of StatisticsView, which is responsible for displaying the game statistics on the screen.
    fruitsController : FruitsController
        The instance of FruitsController, which is responsible for the fruits appearing in the game.
    vulnerable : Surface
        The image of the vulnerable ghost, which is displayed on the screen.
    rect : Rect
        The rectangle representing the vulnerable ghost on the screen.
    playerx : int
        The x-coordinate of the player.
    playery : int
        The y-coordinate of the player.
    ghosts : Ghosts
        The instance of Ghosts, which represents the enemy characters in the game.
    beginning_sound : Sound
        The sound played at the beginning of the game.

    Methods:
    --------
    run_game()
        The main game loop, responsible for running the game.
    _update_screen()
        Draws the on-screen objects of the game.
    """

    def __init__(self):
        """
        Initializes the PackManWorld class. Initializes the pygame module and sets the attributes of the class.
        """
        pg.init()

        self.settings = GameSettings()
        self.pacmd = pacmd(self.settings)
        self.pacmd.parse_cmd()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.game_map = Level_1(self.settings)
        self.player = Pacman(self)
        self.events = Events(self)

        self.statistics = Statistics()
        self.statistics_view = StatisticsView(self.statistics, self.screen, self.player)
        BonusEntity.statistics = self.statistics
        Statistics.allPacDots = self.game_map.get_PacDots()
        self.fruitsController = FruitsController(self.settings.time_to_fruit_appearing1, self.settings.time_to_fruit_appearing2, self.game_map, self.player, self.settings)

        self.vulnerable = pg.transform.scale(pg.image.load('src/Core/images/vulnerable-ghost.bmp'), (35, 35))
        self.rect = self.vulnerable.get_rect()
        self.rect.centerx = 350
        self.rect.centery = 350

        self.playerx = self.player.rect.x
        self.playery = self.player.rect.y

        self.ghosts = Ghosts(self)

        self.beginning_sound = pg.mixer.Sound(os.path.join('src', os.path.join('Core',
                                                         os.path.join('sounds', 'pacman_beginning.wav'))))
        self.beginning_sound.play()

    # main game loop
    def run_game(self):
        """
        The main game loop, responsible for running the game. Calls the _update_screen(), checks the input events
        with events.check_events(), updates the player and fruitsController with player.update() and
        fruitsController.fruit_controller_update(), updates the ghosts with ghosts.update(), and redraws the last
        frames on the screen with pg.display.flip().
        """
        while True:
            self._update_screen()
            self.events.check_events()
            self.player.update()
            self.fruitsController.fruit_controller_update()
            self.playerx = self.player.rect.centerx
            self.playery = self.player.rect.centery
            self.ghosts.update(self)

            pg.display.flip()  # [last function] to redraw last frames on screen

    # here on-screen objects will be
    def _update_screen(self):
        """
        Draws the on-screen objects of the game.
        """
        self.screen.fill(self.settings.map_background)
        self.game_map.draw_map()
        self.statistics_view.ShowStatistics()
        self.player.blitme()
