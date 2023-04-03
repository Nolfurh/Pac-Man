import pygame as pg
import pytest
import src.Infrastructure.gameEnemies
from src.Infrastructure.gameCore import GameSettings
from src.Infrastructure.gameMaps import Level_1
from src.Infrastructure.gameEnemies import GhostMovement, ConcreteMovementOne, ConcreteMovementTwo, ConcreteMovementThree, ConcreteMovementFour, Blinky, Inky, Clyde, Pinky
from src.Infrastructure.gameWorld import PackManWorld
from src.Core.Abstract.enemy import Ghosts


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


@pytest.fixture()
def for_ghost():
    settings = GameSettings()
    screen = screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    vulnerable = pg.transform.scale(pg.image.load('src/Core/images/vulnerable-ghost.bmp'), (35, 35))
    spunky = pg.transform.scale(pg.image.load('src/Core/images/spunky.bmp'), (35, 35))
    var = {"settings": settings, 
        "map_matrix": Level_1(settings),
        "ghost_targets": (450, 630), 
        "screen": screen, 
        "eaten_ghosts": [False, False, False, False],
        "speed": settings.ghosts_speed, 
        "vulnerable": vulnerable,
        "spunky": spunky}
    var = dotdict(var)
    return var


@pytest.fixture()
def for_movement_algorithm():

    settings = GameSettings()
    screen = screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    var = {"settings": settings, 
        "x": 370,
        "y": 300,
        "map_matrix": Level_1(settings).map_matrix, 
        "screen": screen, 
        "speed": settings.ghosts_speed,
        "in_box": False,
        "turns": [True, False, True, False],
        "moving_up": False,
        "moving_down": False, 
        "moving_left": False, 
        "moving_right": True,
        "ghost_targets": [375, 100]}
    var = dotdict(var)
    return var


@pytest.mark.parametrize("x, y, moving_left, moving_right, in_box, expected", [
    (400, 400, False, True, False, True),
    (200, 200, True, False, True, False),
    (100, 100, False, False, False, False),
])


def test_check_postion(x, y, moving_left, moving_right, in_box, expected):
    settings = GameSettings()
    screen = screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    var = {
        "settings": settings, 
        "x": x,
        "y": y,
        "map_matrix": Level_1(settings).map_matrix, 
        "screen": screen, 
        "speed": settings.ghosts_speed,
        "in_box": in_box,
        "turns": [False, False, False, False],
        "moving_up": False, 
        "moving_down": False, 
        "moving_left": moving_left, 
        "moving_right": moving_right
    }
    var = dotdict(var)

    ghostMovement = GhostMovement(ConcreteMovementOne())
    ghostMovement.check_position(var)

    assert var.in_box == expected


@pytest.mark.parametrize("algorithm, feed, expected", [
    (ConcreteMovementOne(), 700, -10 ), 
    (ConcreteMovementTwo(), -30, 700), 
    (ConcreteMovementThree(), 701, -10), 
    (ConcreteMovementFour(), -30, 700)])


def test_check_outer_map(algorithm, feed, expected):
    ghostMovement = GhostMovement(algorithm)

    settings = GameSettings()
    screen = screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    var = {"settings": settings,
        "x": feed,
        "y": 380,
        "map_matrix": Level_1(settings).map_matrix, 
        "screen": screen, 
        "speed": settings.ghosts_speed,
        "in_box": False,
        "turns": [False, False, False, False],
        "moving_up": False, 
        "moving_down": False, 
        "moving_left": False, 
        "moving_right": True,
        "ghost_targets": [450, 631]
    }
    var = dotdict(var)
    ghostMovement.do_movement(var)

    assert var.x == expected

def test_check_movement(for_movement_algorithm):
    ghostMovement = GhostMovement(ConcreteMovementOne())
    ghostMovement.do_movement(for_movement_algorithm)
    assert for_movement_algorithm.moving_up == True