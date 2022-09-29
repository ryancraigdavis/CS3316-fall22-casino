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
    def selectGame(self):
        while(True):
            print("Games:\nteam1Game:1\nteam2game:2\nteam3game:3\nBlackjack:4\nteam5game:5\nQuit:q")
            selectedGame = input("What game would you like to play?")
            print(selectedGame)
            if(selectedGame == "4"):
                print("Blackjack selected")
            elif(selectedGame.lower() == "q"):
                break
            else:
                print("invalid selection")

# Run main here.
if __name__ == "__main__":
    NewCasino = HelloCasino()
    NewCasino.welcome()
    NewCasino.selectGame()
