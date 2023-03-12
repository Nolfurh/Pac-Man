import pytest
from src.Infrastructure.gameProcesses.statistics import Statistics

def test_check_win_without_winning():
    Statistics.allPacDots = 10
    Statistics.collectedPacDots = 0
    Statistics.check_win()
    assert Statistics.win is False

def test_check_win_all_pacdots_collected():
    Statistics.allPacDots = 10
    Statistics.collectedPacDots = 10
    Statistics.check_win()
    assert Statistics.win


def test_check_win_all_pacdots_collected_after_lose():
    Statistics.lose = True
    Statistics.allPacDots = 10
    Statistics.collectedPacDots = 10
    Statistics.check_win()
    assert Statistics.win
