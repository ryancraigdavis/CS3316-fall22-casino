import pytest
import random
import os
import time
from src.casino.slots.slots_game import clear as clear
from src.casino.slots.slots_game import leave as leave
from src.casino.slots.slots_game import runForIfContinueOrNot as continuePrompt
from src.casino.slots.slots_game import whichCherry as whichCherry
from src.casino.slots.slots_game import winCalc as winCalc
from src.casino.slots.slots_game import printScore as printScore
from src.casino.slots.slots_game import spinWheel as spinWheel
from src.casino.slots.slots_game import play as play
from src.casino.slots.slots_game import welcome as welcome

#def test_clear():

#def test_leave():

#def test_runForIfContinueOrNot():

@pytest.mark.parametrize("testInput, expectedResult",
                         [
                             pytest.param("CHERRY", 5, id="Cherry test"),
                             pytest.param("BAR", 2, id="Bar test"),
                             pytest.param("ORANGE", 2, id="Orange test"),
                             pytest.param("BELL", 2, id="Bell test"),
                             pytest.param("PLUM", 2, id="Plum test"),
                         ])
def test_whichCherry(expectedResult, testInput):
    actualResult = whichCherry(testInput)
    assert actualResult == expectedResult

@pytest.mark.parametrize("testInput1, testInput2, testInput3, expectedResult",
                         [
                             pytest.param("CHERRY", "CHERRY", "CHERRY", 7, id="Cherry win"),
                             pytest.param("ORANGE", "ORANGE", "ORANGE", 10, id="Orange win"),
                             pytest.param("PLUM", "PLUM", "PLUM", 14, id="Plum win"),
                             pytest.param("BELL", "BELL", "BELL", 20, id="Bell win"),
                             pytest.param("BAR", "BAR", "BAR", 250, id="Bar win"),
                             pytest.param("ORANGE", "ORANGE", "BAR", 10, id="Orange Bar"),
                             pytest.param("PLUM", "PLUM", "BAR", 14, id="Plum Bar"),
                             pytest.param("BELL", "BELL", "BAR", 20, id="Bell Bar"),
                             pytest.param("CHERRY", "CHERRY", "Bell", 5, id="First 2 Cherry"),
                             pytest.param("CHERRY", "BAR", "CHERRY", 2, id="First Wheel Cherry"),
                         ])
def test_winCalc(testInput1, testInput2, testInput3, expectedResult):
    actualResult = winCalc(testInput1, testInput2, testInput3)
    assert expectedResult == actualResult

#def test_printScore():

#def test_spinWheel():

#def test_play():

#def test_welcome():
