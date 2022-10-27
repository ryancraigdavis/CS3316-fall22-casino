import pytest
import src.casino.craps.craps_game as craps
import random


@pytest.mark.parametrize("expected_result, test_input", [
  pytest.param(" _______ \n|       |\n|   *   |\n|       |\n ------- \n",
               1,
               id="Test case 1"),
  pytest.param(" _______ \n| *     |\n|       |\n|     * |\n ------- \n",
               2,
               id="Test case 2"),
  pytest.param(" _______ \n| *     |\n|   *   |\n|     * |\n ------- \n",
               3,
               id="Test case 3"),
  pytest.param(" _______ \n| *   * |\n|       |\n| *   * |\n ------- \n",
               4,
               id="Test case 4"),
  pytest.param(" _______ \n| *   * |\n|   *   |\n| *   * |\n ------- \n",
               5,
               id="Test case 5"),
  pytest.param(" _______ \n| *   * |\n| *   * |\n| *   * |\n ------- \n",
               6,
               id="Test case 6"),
])
def test_dice_roll(expected_result, test_input):
  """This tests the dice roll function"""
  actual_result = craps.dice_roll(test_input)
  assert actual_result == expected_result


@pytest.mark.parametrize(
  "expected_result, input_test_wager",
  [
    pytest.param(100, "100", id="getValidWager: test val 100"),
    pytest.param(50, "50", id="getValidWager: test val 50"),
    pytest.param(999, "999", id="getValidWager: test val 999"),
  ],
)
def test_getValidWager(expected_result, input_test_wager, monkeypatch):

  monkeypatch.setattr('builtins.input', lambda _: input_test_wager)
  wager = craps.getValidWager(10000)
  assert wager == expected_result


@pytest.mark.parametrize("dieOne, dieTwo, expected_result", [
  pytest.param(5, 4, "Jesse James!", id="Die 1 = 5, Die 2 = 4 , Jessie James"),
  pytest.param(5, 3, "Easy Eight!", id="Die 1 = 5, Die 2 = 3 , Easy Eight"),
  pytest.param(3, 3, "Hard Six!", id="Die 1 = 3, Die 2 = 3 , Hard Six"),
])
def test_names(dieOne, dieTwo, expected_result):
  actual_result = craps.names(dieOne, dieTwo)
  assert actual_result == expected_result


def test_random_roll(mocker):
  """Testing random_roll function"""
  mocker.patch.object(random, "randint").return_value = 1
  actual_result = craps.random_roll()
  assert actual_result == 1


@pytest.mark.parametrize(
  "expected_result, wager, input_test",
  [
    pytest.param(10000, 100, "p", id="get_bet: test val p"),
    pytest.param(10000, 100, "dp", id="get_bet: test val dp"),
  ],
)
def test_get_bet(expected_result, wager, input_test, mocker, monkeypatch):
  mocked_bet = mocker.patch.object(craps, "bet")
  mocked_bet.return_value = 10000
  monkeypatch.setattr('builtins.input', lambda _: input_test)
  result = craps.get_bet(10000, wager)
  assert expected_result == result


@pytest.mark.parametrize(
  "expected_result, type_of_bet, user_chips, wager",
  [
    pytest.param(10000, "dp", 10000, 100, id="get_bet: test val p"),
    pytest.param(10000, "p", 10000, 100, id="get_bet: test val dp"),
  ],
)
def test_bet(expected_result, type_of_bet, user_chips, wager, mocker,
             monkeypatch):
  mocked_bet = mocker.patch.object(craps, "pass_line_bet")
  mocked_bet.return_value = 10000
  mocked_bet = mocker.patch.object(craps, "dont_pass_bet")
  mocked_bet.return_value = 10000
  result = craps.bet(type_of_bet, user_chips, wager)
  assert expected_result == result


@pytest.mark.parametrize(
  "expected_result, user_chips, wager, dice_1, dice_2",
  [
    pytest.param(9800, 10000, 200, 1, 1, id="pass_line_bet: test dice 1,1"),
    pytest.param(9800, 10000, 200, 1, 2, id="pass_line_bet: test dice 1,2"),
    pytest.param(9800, 10000, 200, 6, 6, id="pass_line_bet: test dice 6,6"),
    pytest.param(10200, 10000, 200, 6, 1, id="pass_line_bet: test dice 6,1"),
    pytest.param(10200, 10000, 200, 6, 5, id="pass_line_bet: test dice 6,5"),
    pytest.param(10200, 10000, 200, 5, 5, id="pass_line_bet: test dice 5,5"),
  ],
)
def test_pass_line_bet(expected_result, user_chips, wager, dice_1, dice_2,
                       mocker):
  mocked_roll = mocker.patch.object(craps, "random_roll")
  mocked_roll.side_effect = [dice_1, dice_2]

  mocked_whilePass = mocker.patch.object(craps, "whilePass")
  mocked_whilePass.return_value = dice_1 + dice_2, dice_1 + dice_2, 200, 10000, dice_1, dice_2

  result = craps.pass_line_bet(user_chips, wager)
  assert result == expected_result


def test_pass_line_bet_7_case(mocker):
  mocked_roll = mocker.patch.object(craps, "random_roll")
  mocked_roll.side_effect = [5, 5]

  mocked_whilePass = mocker.patch.object(craps, "whilePass")
  mocked_whilePass.return_value = 5 + 5, 7, 200, 10000, 5, 5

  result = craps.pass_line_bet(10000, 200)
  assert result == 9800


@pytest.mark.parametrize("wager, user_chips, input_test", [
  pytest.param(1, 1, 2, id="doubleCheckPass: test_wager = 1, test_chips = 1"),
])
def test_doubleCheckPass(wager, user_chips, input_test, mocker, monkeypatch):
  monkeypatch.setattr('builtins.input', lambda _: input_test)
  mocked_validatePass = mocker.patch.object(craps, "validatePass")
  mocked_validatePass.return_value = False, 3

  assert craps.doubleCheckPass(wager, user_chips) == 2


@pytest.mark.parametrize(
  "expected_result, user_chips, wager, dice_1, dice_2",
  [
    pytest.param(10200, 10000, 200, 1, 1, id="pass_line_bet: test dice 1,1"),
    pytest.param(10200, 10000, 200, 1, 2, id="pass_line_bet: test dice 1,2"),
    pytest.param(10000, 10000, 200, 6, 6, id="pass_line_bet: test dice 6,6"),
    pytest.param(9800, 10000, 200, 6, 1, id="pass_line_bet: test dice 6,1"),
    pytest.param(9800, 10000, 200, 6, 5, id="pass_line_bet: test dice 6,5"),
    pytest.param(9800, 10000, 200, 5, 5, id="pass_line_bet: test dice 5,5"),
  ],
)
def test_dont_pass_bet(expected_result, user_chips, wager, dice_1, dice_2,
                       mocker):
  mocked_roll = mocker.patch.object(craps, "random_roll")
  mocked_roll.side_effect = [dice_1, dice_2]

  mocked_whilePass = mocker.patch.object(craps, "whileDontPass")
  mocked_whilePass.return_value = dice_1 + dice_2, dice_1 + dice_2, 200, 10000, dice_1, dice_2

  result = craps.dont_pass_bet(user_chips, wager)
  assert result == expected_result


def test_dont_pass_line_bet_7_case(mocker):
  mocked_roll = mocker.patch.object(craps, "random_roll")
  mocked_roll.side_effect = [5, 5]

  mocked_whilePass = mocker.patch.object(craps, "whileDontPass")
  mocked_whilePass.return_value = 5 + 5, 7, 200, 10000, 5, 5

  result = craps.dont_pass_bet(10000, 200)
  assert result == 10200


@pytest.mark.parametrize("wager, newWager, user_chips,input_test", [
  pytest.param(1, 2, 16, 2),
  pytest.param(1, -1, 16, 2)
])
def test_validatePass(wager, newWager, user_chips, input_test, monkeypatch):
  monkeypatch.setattr('builtins.input', lambda _: input_test)
  result = craps.validatePass(wager, newWager, user_chips)
  assert result == (False, 3)
