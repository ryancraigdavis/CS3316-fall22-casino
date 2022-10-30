"""Tests for baccarat_game"""
import pytest
import casino.bingo_bac.baccarat_game as baccarat
import mock

# variables
empty_hand = []
normal_hand = ['A', '2', '3']
large_hand = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
five_aces_hand = ['A', 'A', 'A', 'A', 'A']

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
    mocker.patch.object(baccarat, "playBingo").return_value = 1
    actual_result = baccarat.play()
    expected_result = 1
    assert actual_result == expected_result

@pytest.mark.parametrize(
    "input_hand, expected_value",
    [
        pytest.param(empty_hand, 0, id="test_empty_hand"),
        pytest.param(normal_hand, 6, id="test_normal_hand"),
        pytest.param(large_hand, 5, id="test_large_hand"),
        pytest.param(five_aces_hand, 5, id="test_five_aces_hand")
    ],
)
def test_compute_score(input_hand, expected_value):
    assert baccarat.compute_score(input_hand) == expected_value