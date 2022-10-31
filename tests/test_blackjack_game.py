import random
import pytest
import mock
import coverage

#from unittest.mock import Mock
import src.casino.blackjack.blackjack_game as blackjack


# @pytest.mark.parametrize(
#     "player, dealer",
#     [
#         pytest.param([2,2,2,2,2,2,2,2,2,2,2],[3,2,4],id="manyNums"),
#         pytest.param([9,10],[1,9,10],id="simpleHighNums")
#     ]
# )
def test_check_player_loses(mocker):
    player = [1]
    dealer = [1]
    y = mocker.patch.object(blackjack,"total",return_value = 22)
    t = mocker.patch.object(blackjack,"play_again")
    blackjack.check_player_loses(dealer,player)
    t.assert_called()
    y.assert_called()
def test_check_player_loses_neg(mocker):
    player = [1]
    dealer = [1]
    y = mocker.patch.object(blackjack,"total",return_value = 20)
    t = mocker.patch.object(blackjack,"play_again")
    blackjack.check_player_loses(dealer,player)
    assert not t.called
    y.assert_called()
def test_check_dealer_busts(mocker):
    player = [1]
    dealer = [1]
    y = mocker.patch.object(blackjack, "total", return_value=22)
    t = mocker.patch.object(blackjack, "play_again")
    blackjack.check_dealer_busts(dealer, player)
    t.assert_called()
    y.assert_called()

def test_check_dealer_busts_neg(mocker):
    player = [1]
    dealer = [1]
    y = mocker.patch.object(blackjack, "total", return_value=20)
    t = mocker.patch.object(blackjack, "play_again")
    blackjack.check_dealer_busts(dealer, player)
    assert not t.called
    y.assert_called()
def test_check_losing_score(mocker):
    player = [1,1]
    dealer = [1,3]
    t = mocker.patch.object(blackjack, "play_again")
    blackjack.check_losing_score(dealer, player)
    t.assert_called()
def test_check_losing_score_neg(mocker):
    player = [1,5]
    dealer = [1,3]
    t = mocker.patch.object(blackjack, "play_again")
    blackjack.check_losing_score(dealer, player)
    assert not t.called
def test_check_tie(mocker):
    player = [1,2]
    dealer = [1,2]
    t = mocker.patch.object(blackjack, "play_again")
    blackjack.check_tie(dealer, player)
    t.assert_called()

def test_check_tie_neg(mocker):
    player = [1, 2]
    dealer = [1, 1]
    t = mocker.patch.object(blackjack, "play_again")
    blackjack.check_tie(dealer, player)
    assert not t.called
@pytest.mark.parametrize(
    "player, dealer",
    [
        pytest.param([2,2,2,2,2,2,2,2,2,2,1],[3,2,4],id="playerBlackjack"),
        pytest.param([9,10],[2,9,10],id="dealerBlackjack")
    ]
)
def test_blackjack(player,dealer,mocker):
    t = mocker.patch.object(blackjack,"play_again")
    blackjack.blackjack(dealer,player)
    t.assert_called_once()
def test_blackjack_neither(mocker):
    dealer = [1]
    player = [1]
    t = mocker.patch.object(blackjack, "play_again")
    blackjack.blackjack(dealer, player)
    assert not t.called




