#!/usr/bin/env python3
"""A set of various casino games as classes"""
import os
import random


class HelloCasino:
    """Welcome to the casino"""

    def __init__(self):
        """Inits the players name"""
        self.name = "Joe"

    def welcome(self):
        """Welcome shouter"""
        print(f"Welcome to the Casino, {self.name}")


# Run main here.
if __name__ == "__main__":
    NewCasino = HelloCasino()
    NewCasino.welcome()

print("Welcome to the roulette tables! Please enter some starting information to begin.")
playerBalance = int(input("How much money would you like to start with? (only whole numbers) "))


# picks a random number
def spinTheWheel():
    spin = random.randint(0, 36)
    return spin


# gets what type of bet the player wants to make (color, number, odd/even)
def placeBet(balance):
    placeBet = True
    while placeBet:
        bet = int(input("Please enter how much you want to bet in dollars. "))
        if bet > balance:
            print(
                "You do not have enough money to make that bet. Please enter a smaller number."
            )
        else:
            return bet

#
# # gets input from user on what they would like to bet on
def chooseBet():
    startBet = True
    while startBet:
        betSelection = int(input(
            "What number would you like to bet on?\n\t(1) Single Number\n\t(2) Front half\n\t(3) Back half\n\t(4) Odd\n\t(5) Even\n\t(6) Red\n\t(7) Black\n"

        )
        )
        if 8 > betSelection > 0:
            return betSelection
        else:
            print("That is not a valid selection.")

#
# # actually plays the game and uses the variable set in chooseBet to compare to actual outcome
def playGame():  # having an issue where bet types are overriding the check and making certain bets not calculate correctly
    keepPlaying = True
    hasFunds = checkPlayerBalance()
    while keepPlaying == True and hasFunds == True:  # sets game to be continuous until player says to stop playing
        # Menu for player to decide what to do
        whatToDo =  input(
            "What would you like to do?\n\t(C) Check your current balance\n\t(P) Play roulette\n\t(Q) Quit the game\n"
        )
        if whatToDo.upper() == "C":
            print(
                "Your current balance is $" + str(playerBalance)
            )  # displays current balance

        elif whatToDo.upper() == "P":  # starts playing the game
            betType = chooseBet() - 1  # gets the bet type
            betAmount = placeBet(playerBalance)
            betList[betType](
                betAmount)  # will check the index of a list of the function and use the bet amount given
        elif whatToDo.upper() == "Q":  # exits game
            exit()
           # keepPlaying = False
        else:
            print("That is not a valid selection.")
        hasFunds = checkPlayerBalance()
#     # ends the game if player runs out of money
#
#
def checkPlayerBalance():
    global playerBalance
    if playerBalance > 0:
        return True
    else:
        print("Sorry, you are out of money.")
        return False
#
#
def singleNumberPlay(betAmount):
    global playerBalance
    userNumber = int(input("What number would you like to choose?"))
    spunNumber = spinTheWheel()
    if userNumber == spunNumber:
        winText(spunNumber)
        playerBalance = playerBalance + betAmount * 35
    else:
        loseText(spunNumber)
        playerBalance -= betAmount


def oddPlay(betAmount):
    global playerBalance
    redOrOdd = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    ballNum = spinTheWheel()
    if ballNum in redOrOdd:
        winText(ballNum)
        playerBalance += betAmount
    else:
        loseText(ballNum)
        playerBalance -= betAmount


def evenPlay(betAmount):
    global playerBalance
    blackOrEven = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    ballNum = spinTheWheel()
    if ballNum in blackOrEven:
        winText(ballNum)
        playerBalance += betAmount
    else:
        loseText(ballNum)
        playerBalance -= betAmount


def frontHalf(betAmount):
    global playerBalance
    front_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    ballNum = spinTheWheel()
    if ballNum in front_nums:
        winText(ballNum)
        playerBalance += betAmount
    else:
        loseText(ballNum)
        playerBalance -= betAmount


def backHalf(betAmount):
    global playerBalance
    back_nums = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    ballNum = spinTheWheel()
    if ballNum in back_nums:
        winText(ballNum)
        playerBalance += betAmount
    else:
        loseText(ballNum)
        playerBalance -= betAmount


def redPlay(betAmount):
    global playerBalance
    redOrOdd = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    ballNum = spinTheWheel()
    if ballNum in redOrOdd:
        winText(ballNum)
        playerBalance += betAmount
    else:
        loseText(ballNum)
        playerBalance -= betAmount


def blackPlay(betAmount):
    global playerBalance
    blackOrEven = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    ballNum = spinTheWheel()
    if ballNum in blackOrEven:
        winText(ballNum)
        playerBalance += betAmount
    else:
        loseText(ballNum)
        playerBalance -= betAmount


def winText(num):
    return print(
        "\tWinner winner chicken dinner! The number was " + str(num) + "!\n"
    )


def loseText(num):
    return print("\tYou lose! The number was " + str(num) + "!\n")

#
# # this is a list of functions so that they can be called by index
# # THIS HAS TO BE AFTER ALL FUNCTIONS ARE MADE
betList = [singleNumberPlay, frontHalf, backHalf, oddPlay, evenPlay, redPlay, blackPlay]
# # Driver code
#
# playGame()
