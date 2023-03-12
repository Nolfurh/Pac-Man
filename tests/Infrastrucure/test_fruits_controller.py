import pytest
import pygame
import src.Infrastructure.gameCore
import src.Infrastructure.gameMaps
import src.Core.Abstract.player
import src.Infrastructure.gameProcesses.fruits
from src.Infrastructure.fruitsController import FruitsController
import src.Core.Abstract.item
import src.Infrastructure.gameProcesses.fruits as fruits
from src.Infrastructure.gameProcesses.statistics import Statistics

@pytest.fixture()
def fruit_controller():
    time_to_fruit1 = 2
    time_to_fruit2 = 5
    settings = src.Infrastructure.gameCore.GameSettings()
    game_map = src.Infrastructure.gameMaps.Level_1(settings)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    player = src.Core.Abstract.player.Pacman(screen, settings, game_map)

    return FruitsController(time_to_fruit1, time_to_fruit2, game_map, player, settings)


def test_spawn_fruit(fruit_controller, monkeypatch):
    def mock_mixer(*args, **kwargs):
        pass

    monkeypatch.setattr("pygame.mixer.Sound", mock_mixer)

    fruit_controller.spawn_fruit()
    assert isinstance(fruit_controller.fruit, src.Core.Abstract.item.FruitEntity)


def test_fruit_controller_update_first_fruit_should_spawn(fruit_controller, monkeypatch):
    def mock_mixer_sound(*args, **kwargs):
        pass

    def mock_process_time(*args, **kwargs):
        return fruit_controller.time_to_fruit_appearing1

    monkeypatch.setattr("pygame.mixer.Sound", mock_mixer_sound)
    monkeypatch.setattr("time.process_time", mock_process_time)
    fruit_controller.start_time = 0

    fruit_controller.fruit_controller_update()
    assert isinstance(fruit_controller.fruit, src.Core.Abstract.item.FruitEntity)


def test_fruit_controller_update_second_fruit_should_spawn(fruit_controller, monkeypatch):
    def mock_mixer_sound(*args, **kwargs):
        pass

    def mock_process_time(*args, **kwargs):
        return fruit_controller.time_to_fruit_appearing2

    monkeypatch.setattr("pygame.mixer.Sound", mock_mixer_sound)
    monkeypatch.setattr("time.process_time", mock_process_time)
    fruit_controller.start_time = 0

    fruit_controller.fruit_controller_update()
    assert isinstance(fruit_controller.fruit, src.Core.Abstract.item.FruitEntity)


def test_fruit_controller_update_fruit_should_not_spawn(fruit_controller, monkeypatch):
    def mock_mixer_sound(*args, **kwargs):
        pass

    def mock_process_time(*args, **kwargs):
        return 144

    monkeypatch.setattr("pygame.mixer.Sound", mock_mixer_sound)
    monkeypatch.setattr("time.process_time", mock_process_time)
    fruit_controller.start_time = 0

    fruit_controller.fruit_controller_update()
    assert fruit_controller.fruit is None
