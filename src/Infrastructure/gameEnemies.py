import pygame as pg
from src.Infrastructure.gameProcesses.statistics import Statistics

class PositionCheck():
    def check_position(self, var):
        x_pos = var.settings.screen_width // 30
        y_pos = (var.settings.screen_height - 50) // 32
        tweaker = 15
        center_x = var.x + 17
        center_y = var.y + 17
        var.turns = [False, False, False, False]
        if 0 < center_x // 30 < 29:
            if var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] == 9:
                var.turns[2] = True
            if var.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] < 3 \
                    or (var.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] == 9 and (
                    var.in_box or var.eaten)):
                var.turns[1] = True
            if var.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] < 3 \
                    or (var.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] == 9 and (
                    var.in_box or var.eaten)):
                var.turns[0] = True
            if var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                    or (var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                    var.in_box or var.eaten)):
                var.turns[3] = True
            if var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                    or (var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                    var.in_box or var.eaten)):
                var.turns[2] = True

            if var.moving_up or var.moving_down:
                if 1 <= center_x % x_pos <= 25:
                    if var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (var.map_matrix[int((center_y + tweaker) // y_pos)][
                                    int(center_x // x_pos)] == 9 and (
                                        var.in_box or var.eaten)):
                        var.turns[3] = True
                    if var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (var.map_matrix[int((center_y - tweaker) // y_pos)][
                                    int(center_x // x_pos)] == 9 and (
                                        var.in_box or var.eaten)):
                        var.turns[2] = True
                if 1 <= center_y % y_pos <= 25:
                    if var.map_matrix[int(center_y // y_pos)][int((center_x - x_pos) // x_pos)] < 3 \
                            or (
                            var.map_matrix[int(center_y // y_pos)][int((center_x - x_pos) // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[1] = True
                    if var.map_matrix[int(center_y // y_pos)][int((center_x + x_pos) // x_pos)] < 3 \
                            or (
                            var.map_matrix[int(center_y // y_pos)][int((center_x + x_pos) // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[0] = True

            if var.moving_right or var.moving_left:
                if 1 <= center_x % x_pos <= 25:
                    if var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[3] = True
                    if var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[2] = True
                if 1 <= center_y % y_pos <= 25:
                    if var.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] < 3 \
                            or (var.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[1] = True
                    if var.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] < 3 \
                            or (var.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[0] = True
        else:
            var.turns[0] = True
            var.turns[1] = True
        if 350 < var.x < 550 and 370 < var.y < 480:
            var.in_box = True
        else:
            var.in_box = False
        return var.turns, var.in_box

class Blinky():
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/blinky.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.turns = [False, False, False, False]

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.blinky_x
        self.rect.centery = self.settings.blinky_y

        self.cooldown = 250

        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[0]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # self.ghost_set = GhostSet(self)

    def update(self, var):
        self.ghost_targets = var.ghost_targets[0]
        self.eaten_ghost = var.eaten_ghost

        self.player_x, self.player_y = var.player_x, var.player_y
        self.player = var.player

        self.draw()
        PositionCheck().check_position(self)
        self.move_blinky()
        self.result_collision()

    def result_collision(self):
        player_circle = pg.draw.circle(self.screen, 'gray', (self.player_x, self.player_y), 21, 2)
        if not Statistics().activatedBonuses:
            if (player_circle.colliderect(self.rect)) and not self.eaten:
                if Statistics.lives > 0:
                    Statistics.lives -= 1
                    Statistics.activatedBonuses = []
                    self.x = 300
                    self.y = 300
                    self.rect.x = self.x
                    self.rect.y = self.y
                    self.player.x = 50
                    self.player.y = 50
                    self.moving_right = True
                    self.moving_left = False
                    self.moving_up = False
                    self.moving_down = False
                    self.eaten_ghost = [False, False, False, False]
                    self.eaten = False
                else:
                    Statistics.lose = True
        if Statistics().activatedBonuses and player_circle.colliderect(self.rect) and not self.eaten:
            if Statistics.lives > 0:
                Statistics.activatedBonuses = []
                power_counter = 50
                power_counter -= 1
                self.x = 300
                self.y = 300
                self.rect.x = self.x
                self.rect.y = self.y
                self.moving_right = False
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
                self.eaten_ghost = [True, False, False, False]
                self.eaten = True
                if power_counter == 1:
                    self.eaten = False
            else:
                Statistics.lose = True
        if self.eaten:
            self.cooldown -= 1
            if self.cooldown == 1:
                self.eaten = False
                self.moving_right = True
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
                self.cooldown = 250

    def draw(self):
        center_x = self.rect.x + 17
        center_y = self.rect.y + 17
        if not Statistics().activatedBonuses and not self.eaten:
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
        elif Statistics().activatedBonuses and not self.eaten:
            self.screen.blit(self.vulnerable, (self.x, self.y))
        else:
            self.screen.blit(self.spunky, (self.x, self.y))
        ghost_rect = pg.rect.Rect((center_x - 17, center_y - 17), (35, 35))
        return ghost_rect

    def move_blinky(self):
        if self.moving_right:
            if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                self.x += self.speed
            elif not self.turns[0]:
                self.moving_right = False
                if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
            elif self.turns[0]:
                if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                    self.moving_right = False
                if self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                    self.moving_right = False
                else:
                    self.x += self.speed
        elif self.moving_left:
            if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                self.moving_down = True
                self.moving_left = False
            elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                self.x -= self.speed
            elif not self.turns[1]:
                self.moving_left = False
                if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
            elif self.turns[1]:
                if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                    self.moving_left = False
                if self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                    self.moving_left = False
                else:
                    self.x -= self.speed
        elif self.moving_up:
            if self.ghost_targets[0] < self.rect.x and self.turns[1]:
                self.moving_left = True
                self.x -= self.speed
                self.moving_up = False
            elif self.ghost_targets[1] < self.rect.y and self.turns[2]:
                self.moving_up = True
                self.y -= self.speed
            elif not self.turns[2]:
                self.moving_up = False
                if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
            elif self.turns[2]:
                if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                    self.moving_up = False
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                    self.moving_up = False
                else:
                    self.y -= self.speed
        elif self.moving_down:
            if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                self.y += self.speed
            elif not self.turns[3]:
                self.moving_down = False
                if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
            elif self.turns[3]:
                if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                    self.moving_down = False
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                    self.moving_down = False
                else:
                    self.y += self.speed
        if self.rect.x > 700:
            self.x = -10
            self.rect.x = self.x
        elif self.rect.x < -10:
            self.x = 700
            self.rect.x = self.x
        self.rect.x = self.x
        self.rect.y = self.y
        #return self.rect.x, self.rect.y, self.moving_left, self.moving_right, self.moving_up, self.moving_down

class Inky():
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/inky.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.turns = [False, False, False, False]

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.inky_x
        self.rect.centery = self.settings.inky_y

        self.cooldown = 250

        self.moving_right = False
        self.moving_left = True
        self.moving_up = False
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[0]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # self.ghost_set = GhostSet(self)

    def update(self, var):
        self.ghost_targets = var.ghost_targets[0]
        self.eaten_ghost = var.eaten_ghost

        self.player_x, self.player_y = var.player_x, var.player_y
        self.player = var.player

        self.draw()
        PositionCheck().check_position(self)
        self.move_inky()
        self.result_collision()

    def result_collision(self):
        player_circle = pg.draw.circle(self.screen, 'black', (self.player_x, self.player_y), 21, 2)
        if not Statistics().activatedBonuses:
            if (player_circle.colliderect(self.rect)) and not self.eaten:
                if Statistics.lives > 0:
                    Statistics.lives -= 1
                    Statistics.activatedBonuses = []
                    self.x = 300
                    self.y = 300
                    self.rect.x = self.x
                    self.rect.y = self.y
                    self.player.x = 50
                    self.player.y = 50
                    self.moving_right = True
                    self.moving_left = False
                    self.moving_up = False
                    self.moving_down = False
                    self.eaten_ghost = [False, False, False, False]
                    self.eaten = False
                else:
                    Statistics.lose = True
        if Statistics().activatedBonuses and player_circle.colliderect(self.rect) and not self.eaten:
            if Statistics.lives > 0:
                Statistics.activatedBonuses = []
                power_counter = 50
                power_counter -= 1
                self.x = 300
                self.y = 300
                self.rect.x = self.x
                self.rect.y = self.y
                self.moving_right = False
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
                self.eaten_ghost = [True, False, False, False]
                self.eaten = True
                if power_counter == 1:
                    self.eaten = False
            else:
                Statistics.lose = True
        if self.eaten:
            self.cooldown -= 1
            if self.cooldown == 1:
                self.eaten = False
                self.moving_right = True
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
                self.cooldown = 250

    def draw(self):
        center_x = self.rect.x + 17
        center_y = self.rect.y + 17
        if not Statistics().activatedBonuses and not self.eaten:
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
        elif Statistics().activatedBonuses and not self.eaten:
            self.screen.blit(self.vulnerable, (self.x, self.y))
        else:
            self.screen.blit(self.spunky, (self.x, self.y))
        ghost_rect = pg.rect.Rect((center_x - 17, center_y - 17), (35, 35))
        return ghost_rect

    def move_inky(self):
        # blinky is going to turn whenever colliding with walls, otherwise continue straight
        if self.moving_right:
            if self.ghost_targets[0] > self.x and self.turns[0]:
                self.x += self.speed
            elif not self.turns[0]:
                self.moving_right = False
                if self.ghost_targets[1] > self.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.ghost_targets[1] < self.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.ghost_targets[0] < self.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
            elif self.turns[0]:
                self.x += self.speed
        elif self.moving_left:
            if self.ghost_targets[0] < self.x and self.turns[1]:
                self.x -= self.speed
            elif not self.turns[1]:
                self.moving_left = False
                if self.ghost_targets[1] > self.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.ghost_targets[1] < self.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.ghost_targets[0] > self.x and self.turns[0]:
                    self.moving_up = True
                    self.x += self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[0]:
                    self.moving_up = True
                    self.x += self.speed
            elif self.turns[1]:
                self.x -= self.speed
        elif self.moving_up:
            if self.ghost_targets[1] < self.y and self.turns[2]:
                self.moving_up = True
                self.y -= self.speed
            elif not self.turns[2]:
                self.moving_up = False
                if self.ghost_targets[0] > self.x and self.turns[0]:
                    self.moving_up = True
                    self.x += self.speed
                elif self.ghost_targets[0] < self.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.ghost_targets[1] > self.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[0]:
                    self.moving_up = True
                    self.x += self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
            elif self.turns[2]:
                self.y -= self.speed
        elif self.moving_down:
            if self.ghost_targets[1] > self.y and self.turns[3]:
                self.y += self.speed
            elif not self.turns[3]:
                self.moving_down = False
                if self.ghost_targets[0] > self.x and self.turns[0]:
                    self.moving_up = True
                    self.x += self.speed
                elif self.ghost_targets[0] < self.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.ghost_targets[1] < self.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[0]:
                    self.moving_up = True
                    self.x += self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
            elif self.turns[3]:
                self.y += self.speed
        if self.rect.x > 700:
            self.x = -10
            self.rect.x = self.x
        elif self.rect.x < -10:
            self.x = 700
            self.rect.x = self.x
        self.rect.x = self.x
        self.rect.y = self.y
        return self.rect.x, self.rect.y, self.moving_left, self.moving_right, self.moving_up, self.moving_down

class Pinky():
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/pinky.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.turns = [False, False, False, False]

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.pinky_x
        self.rect.centery = self.settings.pinky_y

        self.cooldown = 250

        self.moving_right = True
        self.moving_left = False
        self.moving_up = True
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[0]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # self.ghost_set = GhostSet(self)

    def update(self, var):
        self.ghost_targets = var.ghost_targets[0]
        self.eaten_ghost = var.eaten_ghost

        self.player_x, self.player_y = var.player_x, var.player_y
        self.player = var.player

        self.draw()
        PositionCheck().check_position(self)
        self.move_pinky()
        self.result_collision()

    def result_collision(self):
        player_circle = pg.draw.circle(self.screen, 'black', (self.player_x, self.player_y), 21, 2)
        if not Statistics().activatedBonuses:
            if (player_circle.colliderect(self.rect)) and not self.eaten:
                if Statistics.lives > 0:
                    Statistics.lives -= 1
                    Statistics.activatedBonuses = []
                    self.x = 300
                    self.y = 300
                    self.rect.x = self.x
                    self.rect.y = self.y
                    self.player.x = 50
                    self.player.y = 50
                    self.moving_right = True
                    self.moving_left = False
                    self.moving_up = False
                    self.moving_down = False
                    self.eaten_ghost = [False, False, False, False]
                    self.eaten = False
                else:
                    Statistics.lose = True
        if Statistics().activatedBonuses and player_circle.colliderect(self.rect) and not self.eaten:
            if Statistics.lives > 0:
                Statistics.activatedBonuses = []
                power_counter = 50
                power_counter -= 1
                self.x = 300
                self.y = 300
                self.rect.x = self.x
                self.rect.y = self.y
                self.moving_right = False
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
                self.eaten_ghost = [True, False, False, False]
                self.eaten = True
                if power_counter == 1:
                    self.eaten = False
            else:
                Statistics.lose = True
        if self.eaten:
            self.cooldown -= 1
            if self.cooldown == 1:
                self.eaten = False
                self.moving_right = True
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
                self.cooldown = 250

    def draw(self):
        center_x = self.rect.x + 17
        center_y = self.rect.y + 17
        if not Statistics().activatedBonuses and not self.eaten:
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
        elif Statistics().activatedBonuses and not self.eaten:
            self.screen.blit(self.vulnerable, (self.x, self.y))
        else:
            self.screen.blit(self.spunky, (self.x, self.y))
        ghost_rect = pg.rect.Rect((center_x - 17, center_y - 17), (35, 35))
        return ghost_rect

    def move_pinky(self):
        # inky turns up or down at any point to pursue, but left and right only on collision
        if self.moving_right:
            if self.ghost_targets[0] > self.x and self.turns[0]:
                self.x += self.speed
            elif not self.turns[0]:
                self.moving_right = False
                if self.ghost_targets[1] > self.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.ghost_targets[1] < self.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.ghost_targets[0] < self.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
            elif self.turns[0]:
                if self.ghost_targets[1] > self.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                if self.ghost_targets[1] < self.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                else:
                    self.x += self.speed
        elif self.moving_left:
            if self.ghost_targets[1] > self.y and self.turns[3]:
                self.moving_down = True
            elif self.ghost_targets[0] < self.x and self.turns[1]:
                self.x -= self.speed
            elif not self.turns[1]:
                self.moving_left = False
                if self.ghost_targets[1] > self.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.ghost_targets[1] < self.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.ghost_targets[0] > self.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
            elif self.turns[1]:
                if self.ghost_targets[1] > self.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                if self.ghost_targets[1] < self.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                else:
                    self.x -= self.speed
        elif self.moving_up:
            if self.ghost_targets[1] < self.y and self.turns[2]:
                self.moving_up = True
                self.y -= self.speed
            elif not self.turns[2]:
                self.moving_up = False
                if self.ghost_targets[0] > self.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                elif self.ghost_targets[0] < self.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.ghost_targets[1] > self.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
            elif self.turns[2]:
                self.y -= self.speed
        elif self.moving_down:
            if self.ghost_targets[1] > self.y and self.turns[3]:
                self.y += self.speed
            elif not self.turns[3]:
                self.moving_down = False
                if self.ghost_targets[0] > self.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                elif self.ghost_targets[0] < self.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.ghost_targets[1] < self.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
            elif self.turns[3]:
                self.y += self.speed
        if self.rect.x > 700:
            self.x = -10
            self.rect.x = self.x
        elif self.rect.x < -10:
            self.x = 700
            self.rect.x = self.x
        self.rect.x = self.x
        self.rect.y = self.y
        return self.rect.x, self.rect.y, self.moving_left, self.moving_right, self.moving_up, self.moving_down

class Clyde():
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/clyde.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.turns = [False, False, False, False]

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.clyde_x
        self.rect.centery = self.settings.clyde_y

        self.cooldown = 250

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = True

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[0]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # self.ghost_set = GhostSet(self)

    def update(self, var):
        self.ghost_targets = var.ghost_targets[0]
        self.eaten_ghost = var.eaten_ghost

        self.player_x, self.player_y = var.player_x, var.player_y
        self.player = var.player

        self.draw()
        PositionCheck().check_position(self)
        self.move_clyde()
        self.result_collision()

    def result_collision(self):
        player_circle = pg.draw.circle(self.screen, 'black', (self.player_x, self.player_y), 21, 2)
        if not Statistics().activatedBonuses:
            if (player_circle.colliderect(self.rect)) and not self.eaten:
                if Statistics.lives > 0:
                    Statistics.lives -= 1
                    Statistics.activatedBonuses = []
                    self.x = 300
                    self.y = 300
                    self.rect.x = self.x
                    self.rect.y = self.y
                    self.player.x = 50
                    self.player.y = 50
                    self.moving_right = True
                    self.moving_left = False
                    self.moving_up = False
                    self.moving_down = False
                    self.eaten_ghost = [False, False, False, False]
                    self.eaten = False
                else:
                    Statistics.lose = True
        if Statistics().activatedBonuses and player_circle.colliderect(self.rect) and not self.eaten:
            if Statistics.lives > 0:
                Statistics.activatedBonuses = []
                power_counter = 50
                power_counter -= 1
                self.x = 300
                self.y = 300
                self.rect.x = self.x
                self.rect.y = self.y
                self.moving_right = False
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
                self.eaten_ghost = [True, False, False, False]
                self.eaten = True
                if power_counter == 1:
                    self.eaten = False
            else:
                Statistics.lose = True
        if self.eaten:
            self.cooldown -= 1
            if self.cooldown == 1:
                self.eaten = False
                self.moving_right = True
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False
                self.cooldown = 250

    def draw(self):
        center_x = self.rect.x + 17
        center_y = self.rect.y + 17
        if not Statistics().activatedBonuses and not self.eaten:
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
        elif Statistics().activatedBonuses and not self.eaten:
            self.screen.blit(self.vulnerable, (self.x, self.y))
        else:
            self.screen.blit(self.spunky, (self.x, self.y))
        ghost_rect = pg.rect.Rect((center_x - 17, center_y - 17), (35, 35))
        return ghost_rect

    def move_clyde(self):
        if self.moving_right:
            if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                self.x += self.speed
            elif not self.turns[0]:
                self.moving_right = False
                if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
            elif self.turns[0]:
                if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                    self.moving_right = False
                if self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                    self.moving_right = False
                else:
                    self.x += self.speed
        elif self.moving_left:
            if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                self.moving_down = True
                self.moving_left = False
            elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                self.x -= self.speed
            elif not self.turns[1]:
                self.moving_left = False
                if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
            elif self.turns[1]:
                if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                    self.moving_left = False
                if self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                    self.moving_left = False
                else:
                    self.x -= self.speed
        elif self.moving_up:
            if self.ghost_targets[0] < self.rect.x and self.turns[1]:
                self.moving_left = True
                self.x -= self.speed
                self.moving_up = False
            elif self.ghost_targets[1] < self.rect.y and self.turns[2]:
                self.moving_up = True
                self.y -= self.speed
            elif not self.turns[2]:
                self.moving_up = False
                if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.ghost_targets[1] > self.rect.y and self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[3]:
                    self.moving_down = True
                    self.y += self.speed
                elif self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
            elif self.turns[2]:
                if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                    self.moving_up = False
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                    self.moving_up = False
                else:
                    self.y -= self.speed
        elif self.moving_down:
            if self.ghost_targets[1] > self.rect.y and self.turns[3]:
                self.y += self.speed
            elif not self.turns[3]:
                self.moving_down = False
                if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.ghost_targets[1] < self.rect.y and self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[2]:
                    self.moving_up = True
                    self.y -= self.speed
                elif self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                elif self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
            elif self.turns[3]:
                if self.ghost_targets[0] > self.rect.x and self.turns[0]:
                    self.moving_right = True
                    self.x += self.speed
                    self.moving_down = False
                elif self.ghost_targets[0] < self.rect.x and self.turns[1]:
                    self.moving_left = True
                    self.x -= self.speed
                    self.moving_down = False
                else:
                    self.y += self.speed
        if self.rect.x > 700:
            self.x = -10
            self.rect.x = self.x
        elif self.rect.x < -10:
            self.x = 700
            self.rect.x = self.x
        self.rect.x = self.x
        self.rect.y = self.y
        # return self.rect.x, self.rect.y, self.moving_left, self.moving_right, self.moving_up, self.moving_down
