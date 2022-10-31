import random
import pytest
import mock
from unittest.mock import patch, call, Mock

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

def test_score(mocker):
    dealer = [1]
    player = [1]
    t = mocker.patch.object(blackjack,"check_dealer_busts")
    y = mocker.patch.object(blackjack, "check_player_loses")
    u = mocker.patch.object(blackjack, "blackjack")
    i = mocker.patch.object(blackjack, "check_losing_score")
    o = mocker.patch.object(blackjack, "check_winning_score")
    blackjack.score(dealer,player)
    t.assert_called_once()
    y.assert_called_once()
    u.assert_called_once()
    i.assert_called_once()
    o.assert_called_once()


@pytest.mark.parametrize("total, expected_result", [(11, 1), (15, 1), (20, 1), (1, 11), (4, 11), (10, 11)])
def test_ace_card(total, expected_result):
    assert expected_result == blackjack.ace_card(total)

@pytest.mark.parametrize("hand, expected_total", [(["J", 3], 13), ([10, "A"], 21), ([1, 2], 3),
 (["Q", "Q"], 20), (["K", "A"], 21)])
def test_total(hand, expected_total, mocker):
    mocker.patch("src.casino.blackjack.blackjack_game.ace_card", return_value=11)
    assert expected_total == blackjack.total(hand)


def test_deal(mocker):
    mocker.patch("random.shuffle")
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    expected_hand = ["A", "K"]
    assert expected_hand == blackjack.deal(deck)

@patch('builtins.print')
def test_print_results(mocked_print,mocker):
    t = mocker.patch.object(blackjack,"clear")
    blackjack.print_results([1],[1])
    t.assert_called_once()
    assert len(mocked_print.mock_calls) == 2

def test_clear():
    mock = Mock(blackjack.clear())
    mock()
    mock.assert_called_once()

def test_game_choice_h(mocker):
    t = mocker.patch.object(blackjack,"input_override")
    t.return_value = "h"
    b = mocker.patch.object(blackjack,"blackjack")
    c = mocker.patch.object(blackjack,"chose_h")
    d = mocker.patch.object(blackjack,"deal")
    d.return_value = [3,"A"]
    blackjack.game()
    c.assert_called_once()
    b.assert_called_once()

def test_game_choice_s(mocker):
    t = mocker.patch.object(blackjack,"input_override")
    t.return_value = "s"
    b = mocker.patch.object(blackjack,"blackjack")
    c = mocker.patch.object(blackjack,"chose_s")
    d = mocker.patch.object(blackjack,"deal")
    d.return_value = [3,"A"]
    blackjack.game()
    c.assert_called_once()
    b.assert_called_once()
def test_game_choice_q(mocker):
    t = mocker.patch.object(blackjack,"input_override")
    t.return_value = "q"
    b = mocker.patch.object(blackjack,"blackjack")
    c = mocker.patch.object(blackjack,"chose_q")
    d = mocker.patch.object(blackjack,"deal")
    d.return_value = [3,"A"]
    blackjack.game()
    c.assert_called_once()
    b.assert_called_once()
    t  = mocker.patch.object(blackjack,"play_again")

def test_selectGame_4(mocker):
    mocked_game = mocker.patch.object(blackjack,"game")
    t = mocker.patch.object(blackjack, "input_override")
    t.return_value = "4"
    blackjack.selectGame()
    mocked_game.assert_called()

def test_selectGame_q(mocker):
    mocked_game = mocker.patch.object(blackjack,"game")
    t = mocker.patch.object(blackjack, "input_override")
    t.return_value = "q"
    blackjack.selectGame()
    assert not mocked_game.called
@pytest.mark.parametrize("user_input", ["0", "1", "2", "3", "5", "a", "b", "#", "A", "B"])
def test_selectGame(mocker, user_input):
    mocked_game = mocker.patch.object(blackjack, "game")
    mocked_input = mocker.patch.object(blackjack, "input_override")
    mocked_input.return_value = user_input
    blackjack.selectGame()
    mocked_game.assert_not_called
def test_chose_s(mocker):
    mocked_chose_s = mocker.patch.object(blackjack, "chose_s")
    mocked_chose_s()
    mocked_chose_s.assert_called()

def test_play_agin(mocker):
    t = mocker.patch.object(blackjack,"input_override")
    t.return_value = "y"
    g = mocker.patch.object(blackjack,"game")
    blackjack.play_again()
    g.assert_called_once()

def test_hit():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    hand = []
    expected_hand = ["A"]
    assert blackjack.hit(hand, deck) == expected_hand