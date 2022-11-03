import unittest
from unittest import mock
from mock import patch
import pytest
import random

import roulette
import roulette as r
from roulette import playerBalance, betList


def test_spinTheWheel():
    """Test to see wheel gives valid num"""
    actual_result = r.spinTheWheel()
    assert 0 <= actual_result <= 36


def test_placeBet():
    """Test that placebet is taking correct value"""
    expected_result = 100
    actual_result = r.placeBet(100)
    assert actual_result == expected_result

@pytest.mark.parametrize(
    "expected_result",
    [
        pytest.param(1, id='test single number'),
        pytest.param(2, id='test front half'),
        pytest.param(3, id='test back half'),
        pytest.param(4, id='test odd'),
        pytest.param(5, id='test even'),
        pytest.param(6, id='test red'),
        pytest.param(7, id='test black'),


    ]
)
def test_chooseBet(expected_result):
    """Checking correct """
    actual_result = r.chooseBet()
    assert actual_result == expected_result
@pytest.mark.parametrize(
    "actual_result, expected_result, whatToDo",
    [
        pytest.param("Your current balance is $" + str(roulette.playerBalance),"Your current balance is $" + str(roulette.playerBalance), 'C', id='test C'),
        pytest.param("Your current balance is $" + str(roulette.playerBalance),"Your current balance is $" + str(roulette.playerBalance), 'c', id='test c'),
        pytest.param(r.betList[1], r.betList, 'P', id='test P'),
        pytest.param(r.betList[1], r.betList, 'p', id='test p'),
        pytest.param("quit", "quit", 'Q', id='test Q'),
        pytest.param("quit", "quit", 'q', id='test q'),

    ],
)
def test_playGame(actual_result, expected_result,whatToDo):
    if whatToDo == "P" or "p":
        assert actual_result in expected_result
    elif whatToDo == "C" or whatToDo == "c":
        assert actual_result == expected_result
    elif whatToDo == "Q" or "q":
        assert actual_result == expected_result


def test_checkPlayerBalance():
    expected_result = True
    actual_result = r.checkPlayerBalance()
    assert actual_result == expected_result

    # the following are all checking the same thing so i figure they should all have
    #identical tests. I want to know if the function is correctly checking
    # if the number given from a spin is within a list of numbers
@pytest.mark.parametrize(
    "expected_result, number_spun,number_guessed",
    [
        pytest.param(True, 1, [1,2,3], id='test right number'),
        pytest.param(False, 4, [1,2,3], id='test wrong number' )
    ],
)

def test_singleNumberPlay(expected_result,number_spun,number_guessed):
    actual_result = (number_spun in number_guessed)
    assert actual_result == expected_result

@pytest.mark.parametrize(
    "expected_result, number_spun, number_guessed",
    [
        pytest.param(True, 1, [1,2,3], id='test right number'),
        pytest.param(False, 4, [1,2,3], id='test wrong number' )
    ],
)
def test_oddPlay(expected_result,number_spun,number_guessed):
    actual_result = (number_spun in number_guessed)
    assert actual_result == expected_result

@pytest.mark.parametrize(
    "expected_result, number_spun, number_guessed",
    [
        pytest.param(True, 2, [1,2,3], id='test right number'),
        pytest.param(False, 4, [1,2,3], id='test wrong number' )
    ],
)
def test_evenPlay(expected_result,number_spun, number_guessed):
    actual_result = (number_spun in number_guessed)
    assert actual_result == expected_result

@pytest.mark.parametrize(
    "expected_result, number_spun, number_guessed",
    [
        pytest.param(True, 1, [1,2,3], id='test right number'),
        pytest.param(False, 4, [1,2,3], id='test wrong number' )
    ],
)
def test_frontHalf(expected_result,number_spun,number_guessed):
    actual_result = (number_spun in number_guessed)
    assert actual_result == expected_result

@pytest.mark.parametrize(
    "expected_result, number_spun, number_guessed",
    [
        pytest.param(True, 1, [1,2,3], id='test right number'),
        pytest.param(False, 4, [1,2,3], id='test wrong number' )
    ],
)
def test_backHalf(expected_result,number_spun,number_guessed):
    actual_result = (number_spun in number_guessed)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "expected_result, number_spun, number_guessed",
    [
        pytest.param(True, 1, [1,2,3], id='test right number'),
        pytest.param(False, 4, [1,2,3], id='test wrong number')
    ],
)
def test_redPlay(expected_result,number_spun,number_guessed):
    actual_result = (number_spun in number_guessed)
    assert actual_result == expected_result

@pytest.mark.parametrize(
    "expected_result, number_spun, number_guessed",
    [
        pytest.param(True, 2, [1,2,3], id='test right number'),
        pytest.param(False, 4, [1,2,3], id='test wrong number' )
    ],
)
def test_blackPlay(expected_result,number_spun,number_guessed):
    actual_result = (number_spun in number_guessed)
    assert actual_result == expected_result
