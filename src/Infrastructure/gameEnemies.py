import pygame as pg

class GhostSet:
    def __init__(self, var):
        self.image = var.image
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.powerup = var.powerup
        self.speed = var.settings.ghosts_speed

        self.centerx = var.rect.centerx
        self.centery = var.rect.centery

        self.moving_right = var.moving_right
        self.moving_left = var.moving_left
        self.moving_up = var.moving_up
        self.moving_down = var.moving_down

        self.x = var.x
        self.y = var.y
        self.turns = [False, False, False, False]

        self.eaten = var.eaten
        self.in_box = var.in_box

        self.ghost_targets = var.ghost_targets

    def draw(self):
        center_x = self.rect.x + 17
        center_y = self.rect.y + 17
        if not self.powerup and not self.eaten_ghost[0]:
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
        elif self.powerup and not self.eaten_ghost and not self.eaten_ghost[0]:
            self.screen.blit(self.vulnerable, (self.x, self.y))
        else:
            self.screen.blit(self.spunky, (self.x, self.y))
        ghost_rect = pg.rect.Rect((center_x - 17, center_y - 17), (35, 35))
        return ghost_rect

    def move_blinky(self, var):
        self.ghost_targets = var.ghost_targets
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
        if self.x < -30:
            self.x = 900
        elif self.x > 900:
            self.x - 30
        self.rect.x = self.x
        self.rect.y = self.y
        return self.rect.x, self.rect.y, self.moving_left, self.moving_right, self.moving_up, self.moving_down

    def check_position(self):
        x_pos = self.settings.screen_width // 30
        y_pos = (self.settings.screen_height - 50) // 32
        tweaker = 15
        center_x = self.x + 17
        center_y = self.y + 17
        self.turns = [False, False, False, False]
        if 0 < center_x // 30 < 29:
            if self.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] == 9:
                self.turns[2] = True
            if self.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] < 3 \
                    or (self.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] == 9 and (
                    self.in_box or self.eaten)):
                self.turns[1] = True
            if self.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] < 3 \
                    or (self.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] == 9 and (
                    self.in_box or self.eaten)):
                self.turns[0] = True
            if self.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                    or (self.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                    self.in_box or self.eaten)):
                self.turns[3] = True
            if self.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                    or (self.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                    self.in_box or self.eaten)):
                self.turns[2] = True

            if self.moving_up or self.moving_down:
                if 1 <= center_x % x_pos <= 25:
                    if self.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (self.map_matrix[int((center_y + tweaker) // y_pos)][
                                    int(center_x // x_pos)] == 9 and (
                                        self.in_box or self.eaten)):
                        self.turns[3] = True
                    if self.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (self.map_matrix[int((center_y - tweaker) // y_pos)][
                                    int(center_x // x_pos)] == 9 and (
                                        self.in_box or self.eaten)):
                        self.turns[2] = True
                if 1 <= center_y % y_pos <= 25:
                    if self.map_matrix[int(center_y // y_pos)][int((center_x - x_pos) // x_pos)] < 3 \
                            or (
                            self.map_matrix[int(center_y // y_pos)][int((center_x - x_pos) // x_pos)] == 9 and (
                            self.in_box or self.eaten)):
                        self.turns[1] = True
                    if self.map_matrix[int(center_y // y_pos)][int((center_x + x_pos) // x_pos)] < 3 \
                            or (
                            self.map_matrix[int(center_y // y_pos)][int((center_x + x_pos) // x_pos)] == 9 and (
                            self.in_box or self.eaten)):
                        self.turns[0] = True

            if self.moving_right or self.moving_left:
                if 1 <= center_x % x_pos <= 25:
                    if self.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (self.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                            self.in_box or self.eaten)):
                        self.turns[3] = True
                    if self.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (self.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                            self.in_box or self.eaten)):
                        self.turns[2] = True
                if 1 <= center_y % y_pos <= 25:
                    if self.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] < 3 \
                            or (self.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] == 9 and (
                            self.in_box or self.eaten)):
                        self.turns[1] = True
                    if self.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] < 3 \
                            or (self.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] == 9 and (
                            self.in_box or self.eaten)):
                        self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x < 550 and 370 < self.y < 480:
            self.in_box = True
        else:
            self.in_box = False
        return self.turns, self.in_box

class Blinky():
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/blinky.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.powerup = var.powerup
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.blinky_x
        self.rect.centery = self.settings.blinky_y

        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[0]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.ghost_set = GhostSet(self)

    def update(self, var):
        self.ghost_targets = var.ghost_targets[0]
        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.powerup = var.powerup
        self.ghost_set.draw()
        self.ghost_set.check_position()
        self.ghost_set.move_blinky(self)

class Inky():
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/inky.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.powerup = var.powerup
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.inky_x
        self.rect.centery = self.settings.inky_y

        self.moving_right = False
        self.moving_left = True
        self.moving_up = False
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[1]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.ghost_set = GhostSet(self)

    def update(self, var):
        self.ghost_targets = var.ghost_targets[1]
        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.powerup = var.powerup
        self.ghost_set.draw()
        self.ghost_set.check_position()
        self.ghost_set.move_blinky(self)

class Pinky():
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/pinky.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.powerup = var.powerup
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.pinky_x
        self.rect.centery = self.settings.pinky_y

        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[2]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.ghost_set = GhostSet(self)

    def update(self, var):
        self.ghost_targets = var.ghost_targets[2]
        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.powerup = var.powerup
        self.ghost_set.draw()
        self.ghost_set.check_position()
        self.ghost_set.move_blinky(self)

class Clyde():
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/clyde.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.powerup = var.powerup
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.clyde_x
        self.rect.centery = self.settings.clyde_y

        self.moving_right = False
        self.moving_left = False
        self.moving_up = True
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[3]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.ghost_set = GhostSet(self)

    def update(self, var):
        self.ghost_targets = var.ghost_targets[3]
        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.powerup = var.powerup
        self.ghost_set.draw()
        self.ghost_set.check_position()
        self.ghost_set.move_blinky(self)
