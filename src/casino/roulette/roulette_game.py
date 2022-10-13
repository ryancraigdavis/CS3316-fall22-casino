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


class playRoulette:
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    green = [0]
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    front_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    back_nums = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    zero = [0]
    print(
        "Welcome to the roulette tables! Please enter some starting information to begin."
    )
    playerBalance = int(
        input("How much money would you like to start with? (only whole numbers) ")
    )
    keepPlaying = True
    betType = ""

    # picks a random number
    def spinTheWheel(self):
        spin = random.randint(0, 36)
        return spin

    # gets what type of bet the player wants to make (color, number, odd/even)
    def placeBet(self, balance):
        placeBet = True
        while placeBet:
            bet = int(input("Please enter how much you want to bet in dollars. "))
            if bet > balance:
                print(
                    "You do not have enough money to make that bet. Please enter a smaller number."
                )
            else:
                return bet

    # gets input from user on what they would like to bet on
    def chooseBet(self):
        startBet = True
        while startBet:
            betSelection = str(
                input(
                    "What number would you like to bet on?\n\t(N) Single Number\n\t(H) Front half or Back half\n\t(O) Odd or Even\n\t(R) Red or Black\n"
                )
            )
            if betSelection.upper() == "N":
                self.betType = "N"
                return self.betType
            elif betSelection.upper() == "H":
                self.betType = "H"
                return self.betType
            elif betSelection.upper() == "O":
                self.betType = "O"
                return self.betType
            elif betSelection.upper() == "R":
                self.betType = "R"
                return self.betType
            else:
                print("That is not a valid selection.")

    # actually plays the game and uses the variable set in chooseBet to compare to actual outcome
    def playGame(
        self,
    ):  # having an issue where bet types are overriding the check and making certain bets not calculate correctly
        keepPlaying = True
        while (
            keepPlaying
        ):  # sets game to be continuous until player says to stop playing
            if self.playerBalance > 0:  # checks player has any money to play with
                # Menu for player to decide what to do
                whatToDo = input(
                    "What would you like to do?\n\t(C) Check your current balance\n\t(P) Play roulette\n\t(Q) Quit the game\n"
                )
                if whatToDo.upper() == "C":
                    print(
                        "Your current balance is $" + str(self.playerBalance)
                    )  # displays current balance

                elif whatToDo.upper() == "P":  # starts playing the game
                    betAmount = self.placeBet(
                        self.playerBalance
                    )  # gets bets from player
                    bet = self.chooseBet()
                    if bet == "N":
                        self.singleNumberPlay(betAmount)
                    elif bet == "H":
                        self.isHalves(betAmount)
                    elif bet == "O":
                        self.oddOrEvenPlay(betAmount)
                    elif bet == "R":
                        self.redOrBlack(betAmount)

                elif whatToDo.upper() == "Q":  # exits game
                    keepPlaying = False
                else:
                    print("That is not a valid selection.")
            else:  # ends the game if player runs out of money
                print("Sorry you are out of money.")
                keepPlaying = False

    def singleNumberPlay(self, betAmount):
        userNumber = int(input("What number would you like to choose?"))
        spunNumber = self.spinTheWheel()
        if userNumber == spunNumber:
            self.winText(spunNumber)
            self.playerBalance = self.playerBalance + betAmount * 35
        else:
            self.loseText(spunNumber)
            self.playerBalance = self.playerBalance - betAmount

    def oddOrEvenPlay(self, betAmount):
        userSelection = input(
            "Would you like to play odd or even?\n\t(D) Odd\n\t(E) Even\n"
        )
        spunNumber = self.spinTheWheel()
        if userSelection.upper() == "D":
            for num in self.odd:
                if spunNumber == self.odd[num]:
                    self.winText(spunNumber)
                    self.playerBalance += betAmount * 2
                    break
                else:
                    self.loseText(spunNumber)
                    self.playerBalance -= betAmount
                    break

        if userSelection.upper() == "E":
            for num in self.even:
                if spunNumber == self.even[num]:
                    self.winText(spunNumber)
                    self.playerBalance += betAmount * 2
                    break
                else:
                    self.loseText(spunNumber)
                    self.playerBalance -= betAmount
                    break
        else:
            print("That is not a valid selection")

    def isHalves(self, betAmount):
        frontOrBack = input("Do you want to bet on the front or back half? (F/B) ")
        if frontOrBack.upper() == "F":
            whichHalf = "F"
        elif frontOrBack.upper() == "B":
            whichHalf = "B"
        ballNum = self.spinTheWheel()
        print("The ball landed in " + str(ballNum))
        print(whichHalf)
        if whichHalf == "F":
            if ballNum in self.front_nums:
                self.winText(ballNum)
                self.playerBalance += betAmount
            else:
                self.loseText(ballNum)
                self.playerBalance -= betAmount
        if whichHalf == "B":
            print("You chose the back half.")
            if ballNum in self.back_nums:
                self.winText(ballNum)
                self.playerBalance += betAmount
            else:
                self.loseText(ballNum)
                self.playerBalance += betAmount

    def redOrBlack(self, betAmount):
        userColor = input("What color would you like to choose? black or red (X/Y)")
        ballNum = self.spinTheWheel()

        if userColor.upper() == "Y":
            if ballNum in self.red:
                self.winText(ballNum)
                self.playerBalance += betAmount
            else:
                self.loseText(ballNum)
                self.playerBalance -= betAmount

        if userColor.upper() == "X":
            if ballNum in self.black:
                self.winText(ballNum)
                self.playerBalance += betAmount
            else:
                self.loseText(ballNum)
                self.playerBalance -= betAmount

    def winText(self, num):
        return print(
            "\tWinner winner chicken dinner! The number was " + str(num) + "!\n"
        )

    def loseText(self, num):
        return print("\tYou lose! The number was " + str(num) + "!\n")


# Driver code
# class_instance = playRoulette()
# class_instance.playGame()
