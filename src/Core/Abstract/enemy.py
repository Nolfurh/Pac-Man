import inspect

from src.Infrastructure.gameEnemies import Blinky, Inky, Pinky, Clyde
import pygame as pg
from src.Infrastructure.gameProcesses.statistics import Statistics

class Ghosts:
    """
    A class representing the Ghost object.

    Parameters
    ----------
    var : object
        An object containing the variables needed for the Ghost object.

    Attributes
    ----------
    vulnerable : object
        A scaled image object representing the Ghost when vulnerable.
    spunky : object
        A scaled image object representing the Ghost when spunky.
    screen : object
        A screen object to display the Ghost on.
    settings : object
        An object containing the game's settings.
    map_matrix : list
        A list containing the game's map matrix.
    eaten_ghost : list
        A list containing boolean values indicating whether each Ghost has been eaten.
    player_x : int
        An integer representing the x-coordinate of the player.
    player_y : int
        An integer representing the y-coordinate of the player.
    ghost_targets : list
        A list containing tuples representing the target coordinates for each Ghost.
    blinky : object
        An object representing the Ghost named Blinky.
    inky : object
        An object representing the Ghost named Inky.
    pinky : object
        An object representing the Ghost named Pinky.
    clyde : object
        An object representing the Ghost named Clyde.

    Methods
    -------
    update(var)
        Updates the Ghost object with the current player coordinates and calls the update method for each Ghost object.
        get_targets(blink_x, blink_y, ink_x, ink_y, pink_x, pink_y, clyd_x, clyd_y, player_x, player_y)
        Returns a list containing the target coordinates for each Ghost based on their current position and the player's position.
    """
    def __init__(self, var):
        """
        Initialize the Ghost object.

        Parameters
        ----------
        var : object
            An object containing the variables needed for the Ghost object.
        """
        self.vulnerable = pg.transform.scale(pg.image.load('src/Core/images/vulnerable-ghost.bmp'), (35, 35))
        self.spunky = pg.transform.scale(pg.image.load('src/Core/images/spunky.bmp'), (35, 35))

        self.screen = var.screen


        self.settings = var.settings
        self.map_matrix = var.game_map.map_matrix
        self.eaten_ghost = [False, False, False, False]

        self.player_x = var.playerx
        self.player_y = var.playery

        self.ghost_targets = [(self.player_x, self.player_y), (self.player_x, self.player_y),
                              (self.player_x, self.player_y), (self.player_x, self.player_y)]

        self.blinky = Blinky(self)
        self.inky = Inky(self)
        self.pinky = Pinky(self)
        self.clyde = Clyde(self)

    def update(self, var):
        """
        Update the Ghost object with the current player coordinates and call the update method for each Ghost object.

        Parameters
        ----------
        var : object
            An object containing the variables needed for the Ghost object.
        """
        self.player_x = var.playerx
        self.player_y = var.playery
        self.player = var.player

        self.ghost_targets = self.get_targets(self.blinky.x, self.blinky.y,
                                              self.inky.x, self.inky.y,
                                              self.pinky.x, self.pinky.y,
                                              self.clyde.x, self.clyde.y,
                                              self.player_x, self.player_y)
        self.blinky.update(self)
        self.inky.update(self)
        self.clyde.update(self)
        self.pinky.update(self)


    def get_targets(self, blink_x, blink_y, ink_x, ink_y, pink_x, pink_y, clyd_x, clyd_y, player_x, player_y):
        """
        Returns a list containing the target coordinates for each Ghost based on their current position and the player's position.

        Parameters
        ----------
        blink_x : int
            An integer representing the x-coordinate of the Ghost named Blinky.
        blink_y : int
            An integer representing the y-coordinate of the Ghost named Blinky.
        ink_x : int
            An integer representing the x-coordinate of the Ghost named Inky.
        ink_y : int
            An integer representing the y-coordinate of the Ghost named Inky.
        pink_x : int
            An integer representing the x-coordinate of the Ghost named Pinky.
        pink_y : int
            An integer representing the y-coordinate of the Ghost named Pinky.
        clyd_x : int
            An integer representing the x-coordinate of the Ghost named Clyde.
        clyd_y : int
            An integer representing the y-coordinate of the Ghost named Clyde.
        player_x : int
            An integer representing the x-coordinate of the player.
        player_y : int
            An integer representing the y-coordinate of the player.

        Returns
        -------
        list
            A list containing tuples representing the target coordinates for each Ghost.
        """
        if player_x < 450:
            runaway_x = 900
        else:
            runaway_x = 0
        if player_y < 450:
            runaway_y = 900
        else:
            runaway_y = 0
        return_target = (380, 400)
        if Statistics().activatedBonuses:
            if not self.blinky.eaten:
                if 305 < blink_x < 445 and 290 < blink_y < 385:
                    blink_target = (375, 100)
                else:
                    blink_target = (runaway_x, runaway_y)
            else:
                blink_target = return_target
            if not self.inky.eaten:
                if 305 < ink_x < 445 and 290 < ink_y < 385:
                    ink_target = (375, 100)
                else:
                    ink_target = (runaway_x, player_y)
            else:
                ink_target = return_target
            if not not self.pinky.eaten:
                if 305 < pink_x < 445 and 290 < pink_y < 385:
                    pink_target = (375, 100)
                else:
                    pink_target = (player_x, runaway_y)
            else:
                pink_target = return_target
            if not self.clyde.eaten:
                if 305 < clyd_x < 445 and 290 < clyd_y < 385:
                    clyde_target = (375, 100)
                else:
                    clyde_target = (450, 450)
            else:
                clyde_target = return_target
        else:
            if not self.blinky.eaten:
                if 305 < blink_x < 445 and 290 < blink_y < 385:
                    blink_target = (375, 100)
                else:
                    blink_target = (player_x, player_y)
            else:
                blink_target = return_target
            if not self.inky.eaten:
                if 305 < ink_x < 450 and 290 < ink_y < 380:
                    ink_target = (400, 100)
                else:
                    ink_target = (player_x, player_y)
            else:
                ink_target = return_target
            if not self.pinky.eaten:
                if 305 < pink_x < 445 and 290 < pink_y < 385:
                    pink_target = (400, 100)
                else:
                    pink_target = (player_x, player_y)
            else:
                pink_target = return_target
            if not self.clyde.eaten:
                if 305 < clyd_x < 445 and 290 < clyd_y < 385:
                    clyde_target = (400, 100)
                else:
                    clyde_target = (player_x, player_y)
            else:
                clyde_target = return_target
        return [blink_target, ink_target, pink_target, clyde_target]
