import pygame as pg
import sys

class Events():

    def __init__(self, var):
        self.player = var.player

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pg.K_LEFT:
            self.player.moving_left = True
        elif event.key == pg.K_UP:
            self.player.moving_up = True
        elif event.key == pg.K_DOWN:
            self.player.moving_down = True
        elif event.key == pg.K_q:
            sys.exit()
