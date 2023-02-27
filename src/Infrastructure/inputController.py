import pygame as pg
import sys

class Events():
    """
    A class to handle game events.
    ...

    Attributes
    ----------
    player : object
        a Player object representing the player

    Methods
    -------
    check_events():
        Checks the event queue and handles events.
    check_keydown_events(event):
        Handles keydown events.
    """

    def __init__(self, var):
        """
        Constructs all the necessary attributes for the Events object.

        Parameters
        ----------
        var : object
            a variable object containing the Player object representing the player
        """

        self.player = var.player

    def check_events(self):
        """
        Checks the event queue and handles events.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        """
        Handles keydown events.

        Parameters
        ----------
        event : event object
            an event object representing a keydown event
        """
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
