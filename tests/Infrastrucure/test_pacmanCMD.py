import argparse

import pytest
import src.Infrastructure.pacmanCMD as pacmd
import src.Infrastructure.gameCore as gmcore

@pytest.fixture()
def pacman_cmd_prepare():
    parse_string = "--command change-settings --item wall-color --parameter green"
    parser = argparse.ArgumentParser()

    parser.add_argument('--command', help='command name')
    parser.add_argument('--item')
    parser.add_argument('--parameter')
    parser.add_argument('-r', '--redColor')
    parser.add_argument('-g', '--greenColor')
    parser.add_argument('-b', '--blueColor')

    args = parser.parse_args(parse_string.split())

    return args


def test_parsecmd_with_null_settings(pacman_cmd_prepare, monkeypatch):
    def mock_parse_args(*args, **kwargs):
        return pacman_cmd_prepare

    monkeypatch.setattr("argparse.ArgumentParser.parse_args", mock_parse_args)

    pacman_cmd = pacmd.pacmd(None)

    with pytest.raises(AttributeError):
        pacman_cmd.parse_cmd()



def test_parsecmd_with_normal_settings(pacman_cmd_prepare, monkeypatch):

    def mock_parse_args(*args, **kwargs):
        return pacman_cmd_prepare

    monkeypatch.setattr("argparse.ArgumentParser.parse_args", mock_parse_args)

    settings = gmcore.GameSettings()
    pacman_cmd = pacmd.pacmd(settings)
    pacman_cmd.parse_cmd()

