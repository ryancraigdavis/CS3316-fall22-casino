"""Tests for bingo_game"""
import pytest
import src.casino.bingo_bac.bingo_game as bingo
import pygame as pg

def test_demo():
    actual_result = 0
    expected_result = 0
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "expected_result, test_input",
    [
        pytest.param(1, 1, id="test1"),
        pytest.param(2, 2, id="test2"),
    ],
)
def test_parametrize_demo(expected_result, test_input):
    actual_result = test_input
    assert actual_result == expected_result


def test_mock_demo(mocker):
    mocker.patch.object(bingo, "playBingo").return_value = 1
    actual_result = bingo.playBingo()
    expected_result = 1
    assert actual_result == expected_result


## Tests ##
def test_new_num(mocker):
    mocker.patch.object(bingo.Number, "new_num").return_value = 1
    num = bingo.Number().new_num()
    assert num == 1


# def test_something(mocker):
#     mocker.patch.object(bingo, "Number").return_value = 1
#     mocker.patch.object(pg.event, "get").return_value = pg.QUIT
#     assert bingo.playBingo() == 0
