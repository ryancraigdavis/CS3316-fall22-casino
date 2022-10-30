"""Tests for baccarat_game"""
import pytest
import src.casino.bingo_bac.baccarat_game as baccarat

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
    mocker.patch.object(baccarat, "play").return_value = 1
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

# Test for banker vs player scores
@pytest.mark.parametrize("pScore, bScore, expected_winner",[
    pytest.param(5,2, 'Player wins', id=("pScore = 5, bScore = 2, Player Win")),
    pytest.param(1,4, 'Banker wins', id=("pScore = 1, bScore = 4, Banker Wins")),
    pytest.param(2,2, "Tie", id=("pScore = 2, bScore = 2, Tie"))
])

def test_bankerVSplayer(pScore, bScore, expected_winner):
    actual_result = baccarat.bankerVSplayer(pScore,bScore)
    assert actual_result == expected_winner

# # Test for Banker's third draw
# mocking_bhand = ['A']
# mocking_drawThird = ['2']
# @pytest.mark.parametrize("bankerS, third, bhand, expected_result",[
#     pytest.param(6,6,mocking_bhand, mocking_drawThird, id=("bankerS= 6, third= 6, hand= A"))
# ])
#
# def test_bankerDrawMaybe(bankerS,third,bhand,expected_result):
#     actual_result = baccarat.bankerDrawMaybe(bankerS,third,mocking_bhand)
#     assert actual_result == expected_result
