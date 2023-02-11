import pygame as pg
import math
from src.Infrastructure.gameCore import GameSettings
from src.Infrastructure.gameMaps import Level_1


class GameMap:
    def __init__(self):
        self.settings = GameSettings()
        self.map_1 = Level_1()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))


    def draw_map(self):
        x_pos = self.settings.screen_width // 30
        y_pos = (self.settings.screen_height - 50) // 32
        for i in range(len(self.map_1.map_1_matrix)):
            for j in range(len(self.map_1.map_1_matrix[i])):
                if self.map_1.map_1_matrix[i][j] == 1:
                    pg.draw.circle(self.screen, self.settings.map_dots_color,
                                   (j * x_pos + (0.5 * x_pos), i * y_pos + (0.5 * y_pos)), 4)
                if self.map_1.map_1_matrix[i][j] == 2:
                    pg.draw.circle(self.screen, self.settings.map_dots_color,
                                   (j * x_pos + (0.5 * x_pos), i * y_pos + (0.5 * y_pos)), 10)
                if self.map_1.map_1_matrix[i][j] == 3:
                    pg.draw.line(self.screen, self.settings.map_lines_color, (j * x_pos + (0.5 * x_pos), i * y_pos),
                                 (j * x_pos + (0.5 * x_pos), i * y_pos + y_pos), 3)
                if self.map_1.map_1_matrix[i][j] == 4:
                    pg.draw.line(self.screen, self.settings.map_lines_color, (j * x_pos, i * y_pos + (0.5 * y_pos)),
                                 (j * x_pos + x_pos, i * y_pos + (0.5 * y_pos)), 3)
                if self.map_1.map_1_matrix[i][j] == 5:
                    pg.draw.arc(self.screen, self.settings.map_lines_color, [(j * x_pos - (x_pos * 0.4)) - 2,
                                                                             (i * y_pos + (0.5 * y_pos)), x_pos,
                                                                             y_pos], 0, math.pi / 2, 3)
                if self.map_1.map_1_matrix[i][j] == 6:
                    pg.draw.arc(self.screen, self.settings.map_lines_color, [(j * x_pos + (x_pos * 0.5)),
                                                                             (i * y_pos + (0.5 * y_pos)), x_pos,
                                                                             y_pos], math.pi / 2, math.pi, 3)
                if self.map_1.map_1_matrix[i][j] == 7:
                    pg.draw.arc(self.screen, self.settings.map_lines_color, [(j * x_pos + (x_pos * 0.5)),
                                                                             (i * y_pos - (0.4 * y_pos)), x_pos,
                                                                             y_pos], math.pi, 3 * math.pi / 2, 3)
                if self.map_1.map_1_matrix[i][j] == 8:
                    pg.draw.arc(self.screen, self.settings.map_lines_color, [(j * x_pos - (x_pos * 0.4)) - 2,
                                                                             (i * y_pos - (0.4 * y_pos)), x_pos,
                                                                             y_pos], 3 * math.pi / 2, 2 * math.pi, 3)
                if self.map_1.map_1_matrix[i][j] == 9:
                    pg.draw.line(self.screen, self.settings.map_lines_door, (j * x_pos, i * y_pos + (0.5 * y_pos)),
                                 (j * x_pos + x_pos, i * y_pos + (0.5 * y_pos)), 3)