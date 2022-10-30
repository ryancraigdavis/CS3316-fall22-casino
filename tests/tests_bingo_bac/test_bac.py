"""Tests for baccarat_game"""
import copy

import pytest
import src.casino.bingo_bac.baccarat_game as baccarat

# variables
empty_hand = []
one_card_hand = ['A']
low_hand = ['A', 'A']
normal_hand = ['4', '2']
high_hand = ['8', 'K']
baccarat_hand = ['10', '10']


# Basic test to make sure tests are working
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
    mocker.patch.object(baccarat, "play").return_value = 1
    actual_result = baccarat.play()
    expected_result = 1
    assert actual_result == expected_result


### Tests ###

@pytest.mark.parametrize(
    "input_hand, expected_value",
    [
        pytest.param(empty_hand, 0, id="test_empty_hand"),
        pytest.param(one_card_hand, 1, id="one_card_hand"),
        pytest.param(low_hand, 2, id="test_low_hand"),
        pytest.param(normal_hand, 6, id="test_normal_hand"),
        pytest.param(high_hand, 8, id="test_large_hand"),
        pytest.param(baccarat_hand, 0, id="baccarat_hand")
    ],
)
def test_compute_score(input_hand, expected_value):
    assert baccarat.compute_score(input_hand) == expected_value


# Test for banker vs player scores
@pytest.mark.parametrize("pScore, bScore, expected_winner", [
    pytest.param(5, 2, 'Player wins', id=("pScore = 5, bScore = 2, Player Win")),
    pytest.param(1, 4, 'Banker wins', id=("pScore = 1, bScore = 4, Banker Wins")),
    pytest.param(2, 2, "Tie", id=("pScore = 2, bScore = 2, Tie"))
])
def test_bankerVSplayer(pScore, bScore, expected_winner):
    actual_result = baccarat.bankerVSplayer(pScore, bScore)
    assert actual_result == expected_winner


# Test for Banker's third draw
@pytest.mark.parametrize("bankerS, third, bhand",[
    pytest.param(1,3, baccarat_hand, id=("baccarat hand, gets a third card")),
    pytest.param(3,8, low_hand, id=("low hand, should not get third card")),
    pytest.param(3,2, low_hand, id=("low hand, should get third card")),
    pytest.param(4,5, high_hand, id=("high hand, should get third card")),
    pytest.param(5, 5, normal_hand, id=("normal hand, should get third card"))
])

def test_bankerDrawMaybe(bankerS,third,bhand):
    old_bhand = copy.deepcopy(bhand)
    irange = lambda start, end: range(start, end + 1)
    if bankerS in irange(0,6) and third in irange(2,7):
        baccarat.bankerDrawMaybe(bankerS,third,bhand)
        assert old_bhand is not bhand
    else:
        baccarat.bankerDrawMaybe(bankerS,third,bhand)
        assert old_bhand == bhand


@pytest.mark.parametrize("input_hand, input_score", [
    pytest.param(low_hand, 2, id="test_low_hand"),
    pytest.param(normal_hand, 6, id="test_normal_hand"),
    pytest.param(high_hand, 8, id="test_large_hand"),
    pytest.param(baccarat_hand, 0, id="baccarat_hand")
]
)
def test_bankerDrawTrue(input_hand, input_score):
    irange = lambda start, end: range(start, end + 1)
    old_hand = copy.deepcopy(input_hand)
    if input_score in irange(0, 5):
        baccarat.bankerDrawTrue(input_score, input_hand)
        assert old_hand is not input_hand
    else:
        baccarat.bankerDrawTrue(input_score, input_hand)
        assert old_hand == input_hand


def test_checkPlayerScore():
    actual_result = 0
    expected_result = 0
    assert actual_result == expected_result


def test_compareScores():
    actual_result = 0
    expected_result = 0
    assert actual_result == expected_result


def test_anyScoreHigh():
    actual_result = 0
    expected_result = 0
    assert actual_result == expected_result


def test_play():
    actual_result = 0
    expected_result = 0
    assert actual_result == expected_result
