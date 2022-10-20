#!/usr/bin/env python3
"""A set of various casino games as classes"""
import os
import random
import time


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


class Slots:

    def __init__(self, balance):
        self.balance = balance
        self.stake = 5
        self.items = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]


    def clear(self):
        if os.name == 'nt':
            os.system('CLS')
        else:
            os.system('clear')
            

    def leave(self, message):
        self.clear()
        print(message)
        time.sleep(2)
        self.clear()
        print("Returning to the casino center...")
        time.sleep(2)
        self.clear()


    def runForIfContinueOrNot(self, ans):
        if ans =="y":
            done = True
            self.play()
        elif ans == "n":
            done = True
            self.leave("Thanks for playing!")
        else:
            print("Please enter a correct answer")
            time.sleep(0.8)
            self.clear()
        return done


    def canPlayAgain(self, addedStr):
        done = False
        print(f"You have ${self.balance} Dollars.")
        while (done != True):
            ans = input(f"""Would you like to play {addedStr}?
            \n\nYes(y)\t\t\tNo(n)""")
            done = self.runForIfContinueOrNot(ans.lower()) 


    def playAgain(self, addedStr):
        if self.balance >= self.stake:
            self.canPlayAgain(addedStr)
        else:
            time.sleep(0.5)
            self.leave("Can't afford to play!")


    def whichCherry(self):
        """Determines which jackpot the player gets from
        CHERRY being on the 1st wheel"""
        if Slots.secondWheel == "CHERRY":
            return 5
        else:
            return 2


    def winCalc(self):
        """
        Calculates the current score
        """
        Slots.clear
        allSlots = Slots.firstWheel + " " + Slots.secondWheel + " " + Slots.thirdWheel
        winDict = {
                "CHERRY CHERRY CHERRY": 7,
                "ORANGE ORANGE ORANGE": 10,
                "PLUM PLUM PLUM": 14,
                "BELL BELL BELL": 20,
                "BAR BAR BAR": 250,
                "ORANGE ORANGE BAR": 10,
                "PLUM PLUM BAR": 14,
                "BELL BELL BAR": 20,
                }
        win = winDict.get(allSlots, 0)
        if (win == 0) and (Slots.firstWheel == "CHERRY"):
            return self.whichCherry()
        return win


    def printScore(self):
        """
        prints the current score and acts as a runner for winCalc
        """
        win = self.winCalc()
        self.balance += win
        if win > 0:
            print(
                Slots.firstWheel
                + "\t"
                + Slots.secondWheel
                + "\t"
                + Slots.thirdWheel
                + " -- You win $"
                + str(win)
                + "!"
            )
        else:
            print(
                Slots.firstWheel
                + "\t"
                + Slots.secondWheel
                + "\t"
                + Slots.thirdWheel
                + " -- You lose!"
            )
        time.sleep(1)


    def spinWheel(self):
        """
        returns a random item from the wheel
        """
        rand = random.randint(0, 5)
        return  self.items[rand]


    def play(self):
        self.balance -= self.stake
        self.clear()
        Slots.firstWheel = self.spinWheel()
        Slots.secondWheel = self.spinWheel()
        Slots.thirdWheel = self.spinWheel()
        self.printScore()
        self.playAgain("again")


    def welcome(self):
        self.clear()
        print("Welcome to Slots!")
        print(f"The cost is ${self.stake} per game.")
        self.playAgain('')


#uncomment next three lines to play slots (Will be implemented into
# the HelloCasino class once the relevant functions are added
# to select game)
#balance = 500
#Play_Slots = Slots(balance)
#Play_Slots.welcome()
