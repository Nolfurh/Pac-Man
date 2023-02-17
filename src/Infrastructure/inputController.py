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
            if self.player.turns[0]:
                self.player.moving_left = False
                self.player.moving_up = False
                self.player.moving_down = False
                self.player.moving_right = True
        elif event.key == pg.K_LEFT:
            if self.player.turns[1]:
                self.player.moving_right = False
                self.player.moving_up = False
                self.player.moving_down = False
                self.player.moving_left = True
        elif event.key == pg.K_UP:
            if self.player.turns[2]:
                self.player.moving_right = False
                self.player.moving_left = False
                self.player.moving_down = False
                self.player.moving_up = True
        elif event.key == pg.K_DOWN:
            if self.player.turns[3]:
                self.player.moving_right = False
                self.player.moving_left = False
                self.player.moving_up = False
                self.player.moving_down = True
        elif event.key == pg.K_q:
            sys.exit()
