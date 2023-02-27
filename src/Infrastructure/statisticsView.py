import pygame
from src.Infrastructure.gameProcesses.statistics import Statistics


class StatisticsView:
    """
    This class is responsible for displaying game statistics on the screen.

    Parameters:
    -----------
    statistics : object
        Object that stores game statistics data.
    screen : object
        Object that represents the game screen.
    player : object
        Object that represents the game player.

    Attributes:
    -----------
    statistics : object
        Object that stores game statistics data.
    screen : object
        Object that represents the game screen.
    player : object
        Object that represents the game player.
    font : object
        Object that represents the font used to display game statistics.

    Methods:
    --------
    ShowStatistics()
        Method that displays game statistics on the screen.
    """
    def __init__(self, statistics, screen, player):
        """
        Initializes StatisticsView class.

        Parameters:
        -----------
        statistics : object
            Object that stores game statistics data.
        screen : object
            Object that represents the game screen.
        player : object
            Object that represents the game player.
        """
        self.statistics = statistics
        self.screen = screen
        self.player = player
        self.font = pygame.font.SysFont('timesnewroman',  38)

    def ShowStatistics(self):
        """
        Method that displays game statistics on the screen.
        """
        game_score_render = self.font.render(f"Score: {self.statistics.score}", True, 'blue', 'black')
        self.screen.blit(game_score_render, (self.screen.get_rect().right - game_score_render.get_rect().right,
                                             self.screen.get_rect().bottom - game_score_render.get_rect().bottom))

        player_lives_render = self.font.render(f"☻: {self.statistics.lives}", True, 'yellow', 'black')
        self.screen.blit(player_lives_render, (self.screen.get_rect().left,
                                               self.screen.get_rect().bottom - player_lives_render.get_rect().bottom))

        if self.statistics.win:
            win_font = pygame.font.SysFont('timesnewroman',  60)
            win_render = win_font.render(f"Вітаємо, Ви перемогли!", True, 'green')
            self.screen.blit(win_render, win_render.get_rect(center = self.screen.get_rect().center))

        if self.statistics.lose:
            lose_font = pygame.font.SysFont('timesnewroman',  60)
            lose_render = lose_font.render(f"Програш", True, 'white', 'black')
            self.screen.blit(lose_render, lose_render.get_rect(center = self.screen.get_rect().center))