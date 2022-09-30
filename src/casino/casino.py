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
# start of roulette class
# this still needs to be able to make changes to said balance from bets
# I didn't put in the check for odd or even yet 
class playRoulette:

    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    green = [0]
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

    print("Welcome to the roulette tables! Please enter some starting information to begin.")
    playerBalance = int(input("How much money would you like to start with? (only whole numbers) "))
    keepPlaying = True
    betType = ""

# picks a random number
    def spinTheWheel():
        spin = random.randint(0, 36)
        return spin

# gets what type of bet the player wants to make (color, number, odd/even)
    def placeBet(balance):
        startBet = True
        numberCheck = True
        placeBet = True
        while placeBet:
            bet = int(input("Please enter how much you want to bet in dollars. "))
            if bet > balance:
                print("You do not have enough money to make that bet. Please enter a smaller number.")
            else:
                while startBet:
                    typeBet = input("Would you like to bet on a number or a color? (N/C) ")
                    if typeBet.upper() == "C":
                        colorBet = input("What color would you like to bet on? (R/B) ")
                        if colorBet.upper() == "R":
                            startBet = False
                            return  colorBet
                        elif colorBet.upper() == "B":
                            startBet = False
                            return colorBet
                    elif typeBet.upper() == "N":
                        numTypeBet = input("Do you want to bet on a specific number or choose between odd and even? (S/C) ")
                        while numberCheck:
                            if numTypeBet.upper() == "S":
                                numberBet = int(input("What number would you like to bet on? (0-36)"))
                                if numberBet < 0 or numberBet > 36:
                                    print("That is not a valid number.")
                                else:
                                    numberCheck = False
                                    startBet = False
                                    return numberBet
                            elif numTypeBet.upper() == "C":
                                oddOrEven = input("Do you want to bet on odd or even? (O/E)")
                                numberCheck = False
                                startBet = False
                                return oddOrEven
                            else:
                                print("That is not a valid selection. ")
                    else:
                        print("That is not a valid selection.")

    # needs code to reward/take away money from bets
    # def changeBalance(currentBalance):


# start of main
    while keepPlaying: # sets game to be continuous until player says to stop playing
        if playerBalance > 0: # checks player has any money to play with
            # Menu for player to decide what to do
            whatToDo = input("What would you like to do?\n(C) Check your current balance\n(P) Play roulette\n(Q) Quit the game\n")
            if whatToDo.upper() == "C":
                print("Your current balance is $" + str(playerBalance)) # displays current balance
            elif whatToDo.upper() == "P": # starts playing the game
                bet = placeBet(playerBalance) # gets bets from player
                currentNumber = spinTheWheel() # starts the game
                if currentNumber in red: # displays red number
                    print("The number was red " + str(currentNumber) + "!")  # works
                elif currentNumber in black: # displays black number
                    print("The number was black " + str(currentNumber) + "!")  # works
                else: # displays green 0
                    print("The number was green 0!") # works
            elif whatToDo.upper() == "Q": # exits game
                keepPlaying = False
            else:
                print("That is not a valid selection.")
        else: # ends the game if player runs out of money
            print("Sorry you are out of money.")
            keepPlaying = False
