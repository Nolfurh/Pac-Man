import pygame as pg
from src.Infrastructure.gameProcesses.statistics import Statistics
from  src.Infrastructure.gameProcesses import fruits, bonuses

class Pacman:
    def __init__(self, var):
        self.screen = var.screen
        self.screen_rect = var.screen.get_rect()

        self.image = pg.transform.scale(pg.image.load('src/Core/images/Pacman.png'), (35, 35))
        self.rect = self.image.get_rect()

        self.settings = var.settings
        self.map_matrix = var.game_map.map_matrix

        self.rect.centerx = self.settings.pacman_x
        self.rect.centery = self.settings.pacman_y

        self.powerup = False

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.turns = [True, True, True, True]
        self.clock = pg.time.Clock()


    def update(self):
        delta_time = self.clock.tick()
        self.check_position()
        if self.moving_right and self.turns[0]:
            self.x += self.settings.pacman_speed * (delta_time / 10)
            self.turns[0] = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

        if self.moving_left and self.turns[1]:
            self.x -= self.settings.pacman_speed * (delta_time / 10)
            self.turns[1] = False
            self.moving_right = False
            self.moving_up = False
            self.moving_down = False

        if self.moving_up and self.turns[2]:
            self.y -= self.settings.pacman_speed * (delta_time / 10)
            self.turns[2] = False
            self.moving_right = False
            self.moving_left = False
            self.moving_down = False

        if self.moving_down and self.turns[3]:
            self.y += self.settings.pacman_speed * (delta_time / 10)
            self.turns[3] = False
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False

        self.rect.x = self.x
        self.rect.y = self.y

        self.eat()

    def check_position(self):
        x_pos = self.settings.screen_width // 30
        y_pos = (self.settings.screen_height - 50) // 32
        tweaker_1 = 15
        centerx = self.x + 17
        centery = self.y + 17
        if centerx // 30 < 29:
            if self.moving_right:
                if self.map_matrix[int(centery // y_pos)][int((centerx + tweaker_1) // x_pos)] < 3:
                    self.turns[0] = True
            if self.moving_left:
                if self.map_matrix[int(centery // y_pos)][int((centerx - tweaker_1) // x_pos)] < 3:
                    self.turns[1] = True
            if self.moving_up:
                if self.map_matrix[int((self.y + tweaker_1) // y_pos)][int(self.x // x_pos)] < 3:
                    self.turns[3] = True
            if self.moving_down:
                if self.map_matrix[int((self.y - tweaker_1) // y_pos)][int(self.x // x_pos)] < 3:
                    self.turns[2] = True

            if self.moving_up or self.moving_down:
                if 1 <= centerx % x_pos <= 25:
                    if self.map_matrix[int((centery + tweaker_1) // y_pos)][int(centerx // x_pos)] < 3:
                        self.turns[3] = True
                    if self.map_matrix[int((centery - tweaker_1) // y_pos)][int(centerx // x_pos)] < 3:
                        self.turns[2] = True
                if 1 <= self.y % y_pos <= 25:
                    if self.map_matrix[int(centery // y_pos)][int((centerx - x_pos) // x_pos)] < 3:
                        self.turns[1] = True
                    if self.map_matrix[int(centery // y_pos)][int((centerx + x_pos) // x_pos)] < 3:
                        self.turns[0] = True

            if self.moving_right or self.moving_left:
                if 1 <= centerx % x_pos <= 25:
                    if self.map_matrix[int((centery + y_pos) // y_pos)][int(centerx // x_pos)] < 3:
                        self.turns[3] = True
                    if self.map_matrix[int((centery - y_pos) // y_pos)][int(centerx // x_pos)] < 3:
                        self.turns[2] = True
                if 5 <= centery % y_pos <= 25:
                    if self.map_matrix[int(centery // y_pos)][int((centerx - tweaker_1) // x_pos)] < 3:
                        self.turns[1] = True
                    if self.map_matrix[int(centery // y_pos)][int((centerx + tweaker_1) // x_pos)] < 3:
                        self.turns[0] = True

        else:
            self.turns[0] = True
            self.turns[1] = True
        return self.turns

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def eat(self):
        x_pos = self.settings.screen_width // 30
        y_pos = (self.settings.screen_height - 50) // 32
        centerx = self.x + 17
        centery = self.y + 17

        if self.map_matrix[int(centery // y_pos)][int(centerx // x_pos)] == 1:
            self.map_matrix[int(centery // y_pos)][int(centerx // x_pos)] = 0
            PacDot = fruits.PacDot()
            Statistics.score += PacDot.score
            Statistics.collectedPacDots += 1
            Statistics.check_win()

        if self.map_matrix[int(centery // y_pos)][int(centerx // x_pos)] == 2:
            self.map_matrix[int(centery // y_pos)][int(centerx // x_pos)] = 0
            PowerPellet = bonuses.PowerPellet()
            PowerPellet.use()
