import pygame
from src.Infrastructure.gameProcesses.statistics import Statistics


class StatisticsView:
    def __init__(self, statistics, screen):
        self.statistics = statistics
        self.screen = screen
        self.font = pygame.font.SysFont('timesnewroman',  38)

    def ShowStatistics(self):

        game_score_render = self.font.render(f"Score: {self.statistics.score}", True, 'blue', 'black')
        self.screen.blit(game_score_render, (self.screen.get_rect().right - game_score_render.get_rect().right,
                                             self.screen.get_rect().bottom - game_score_render.get_rect().bottom))

        player_lives_render = self.font.render(f"☻: {self.statistics.lives}", True, 'yellow', 'black')
        self.screen.blit(player_lives_render, (self.screen.get_rect().left,
                                               self.screen.get_rect().bottom - player_lives_render.get_rect().bottom))
