import pygame as pg
import sys

class Events:

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()