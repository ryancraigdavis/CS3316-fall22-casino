"""Tests for bingo_game"""
import pytest
import src.casino.bingo_bac.bingo_game as bingo

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
