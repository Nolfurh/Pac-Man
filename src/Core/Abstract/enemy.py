from src.Infrastructure.gameEnemies import Blinky, Inky, Pinky, Clyde
import pygame as pg

class Ghosts:

    def __init__(self, var):
        self.vulnerable = pg.transform.scale(pg.image.load('src/Core/images/vulnerable-ghost.bmp'), (35, 35))
        self.spunky = pg.transform.scale(pg.image.load('src/Core/images/spunky.bmp'), (35, 35))

        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.game_map.map_matrix
        self.eaten_ghost = [False, False, False, False]
        self.powerup = var.powerup

        self.player_x = var.playerx
        self.player_y = var.playery

        self.ghost_targets = [(self.player_x, self.player_y), (self.player_x, self.player_y),
                              (self.player_x, self.player_y), (self.player_x, self.player_y)]

        self.blinky = Blinky(self)
        self.inky = Inky(self)
        self.pinky = Pinky(self)
        self.clyde = Clyde(self)


    def update(self, var):
        self.player_x = var.playerx
        self.player_y = var.playery
        self.powerup = var.powerup
        self.ghost_targets = self.get_targets(self.settings.blinky_x, self.settings.blinky_y,
                                              self.settings.inky_x, self.settings.inky_y,
                                              self.settings.pinky_x, self.settings.pinky_y,
                                              self.settings.clyde_x, self.settings.clyde_y,
                                              self.player_x, self.player_y)
        self.blinky.update(self)
        self.inky.update(self)
        self.clyde.update(self)
        self.pinky.update(self)


    def get_targets(self, blink_x, blink_y, ink_x, ink_y, pink_x, pink_y, clyd_x, clyd_y, player_x, player_y):
        if player_x < 450:
            runaway_x = 900
        else:
            runaway_x = 0
        if player_y < 450:
            runaway_y = 900
        else:
            runaway_y = 0
        return_target = (380, 400)
        if self.powerup:
            if not self.blinky.eaten and not self.eaten_ghost[0]:
                blink_target = (runaway_x, runaway_y)
            elif not self.blinky.eaten and self.eaten_ghost[0]:
                if 340 < blink_x < 560 and 340 < blink_y < 500:
                    blink_target = (400, 100)
                else:
                    blink_target = (player_x, player_y)
            else:
                blink_target = return_target
            if not self.inky.eaten and not self.eaten_ghost[1]:
                ink_target = (runaway_x, player_y)
            elif not self.inky.eaten and self.eaten_ghost[1]:
                if 340 < ink_x < 560 and 340 < ink_y < 500:
                    ink_target = (400, 100)
                else:
                    ink_target = (player_x, player_y)
            else:
                ink_target = return_target
            if not self.pinky.eaten:
                pink_target = (player_x, runaway_y)
            elif not self.pinky.eaten and self.eaten_ghost[2]:
                if 340 < pink_x < 560 and 340 < pink_y < 500:
                    pink_target = (400, 100)
                else:
                    pink_target = (player_x, player_y)
            else:
                pink_target = return_target
            if not self.clyde.eaten and not self.eaten_ghost[3]:
                clyde_target = (450, 450)
            elif not self.clyde.eaten and self.eaten_ghost[3]:
                if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                    clyde_target = (400, 100)
                else:
                    clyde_target = (player_x, player_y)
            else:
                clyde_target = return_target
        else:
            if not self.blinky.eaten:
                if 340 < blink_x < 560 and 340 < blink_y < 500:
                    blink_target = (400, 100)
                else:
                    blink_target = (player_x, player_y)
            else:
                blink_target = return_target
            if not self.inky.eaten:
                if 340 < ink_x < 560 and 340 < ink_y < 500:
                    ink_target = (400, 100)
                else:
                    ink_target = (player_x, player_y)
            else:
                ink_target = return_target
            if not self.pinky.eaten:
                if 340 < pink_x < 560 and 340 < pink_y < 500:
                    pink_target = (400, 100)
                else:
                    pink_target = (player_x, player_y)
            else:
                pink_target = return_target
            if not self.clyde.eaten:
                if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                    clyde_target = (400, 100)
                else:
                    clyde_target = (player_x, player_y)
            else:
                clyde_target = return_target
        return [blink_target, ink_target, pink_target, clyde_target]
