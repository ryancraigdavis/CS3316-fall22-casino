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
        self.total_collected = 0
        self.total_paid_out = 0
        self.testingMode = False


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


    def playAgain(self):
        done = False
        if self.balance >= self.stake:
            print("You now have: $",self.balance," Dollars.")
            while (done != True):
                ans = input("""Would you like to play again?\n\nYes(y)\t\t\tNo(n)""")
                ans = ans.lower()
                if ans == "y":
                    done = True
                    self.play()
                elif ans =="n":
                    done = True
                    self.leave("Thanks for playing!")
                else: 
                    print("Please enter a correct answer")
                    time.sleep(0.8)
                    self.clear()
        else:
            time.sleep(0.5)
            self.leave("Can't afford to play another round!")


    def printScore(self):
        '''
        prints the current score
        '''
        Slots.clear
        if((Slots.firstWheel == "CHERRY") and (Slots.secondWheel != "CHERRY")):
            win = 2
        elif((Slots.firstWheel == "CHERRY") and (Slots.secondWheel == "CHERRY") and (Slots.thirdWheel != "CHERRY")):
            win = 5
        elif((Slots.firstWheel == "CHERRY") and (Slots.secondWheel == "CHERRY") and (Slots.thirdWheel == "CHERRY")):
            win = 7
        elif((Slots.firstWheel == "ORANGE") and (Slots.secondWheel == "ORANGE") and ((Slots.thirdWheel == "ORANGE") or (Slots.thirdWheel == "BAR"))):
            win = 10
        elif((Slots.firstWheel == "PLUM") and (Slots.secondWheel == "PLUM") and ((Slots.thirdWheel == "PLUM") or (Slots.thirdWheel == "BAR"))):
            win = 14
        elif((Slots.firstWheel == "BELL") and (Slots.secondWheel == "BELL") and ((Slots.thirdWheel == "BELL") or (Slots.thirdWheel == "BAR"))):
            win = 20
        elif((Slots.firstWheel == "BAR") and (Slots.secondWheel == "BAR") and (Slots.thirdWheel == "BAR")):
            win = 250
        else:
            win = 0

        self.balance += win
        self.total_paid_out += win
        if(win > 0):
            print(Slots.firstWheel + '\t' + Slots.secondWheel + '\t' + Slots.thirdWheel + ' -- You win $' + str(win) + "!")
        elif(win <= 0):
            print(Slots.firstWheel + '\t' + Slots.secondWheel + '\t' + Slots.thirdWheel + ' -- You lose!')
        time.sleep(1)


    def spinWheel(self):
        '''
        returns a random item from the wheel
        '''
        rand = random.randint(0, 5)
        return  self.items[rand]


    def play(self):
        self.balance -= self.stake
        self.total_collected += self.stake
        self.clear()
        Slots.firstWheel = self.spinWheel()
        Slots.secondWheel = self.spinWheel()
        Slots.thirdWheel = self.spinWheel()
        self.printScore()
        if self.testingMode == False:
            self.playAgain()


    def welcome(self):
        self.clear()
        done = False

        if self.balance >= self.stake:
            print("Welcome to Slots!\nYou currently have: $",self.balance , "Dollars.\n")
            while (done != True):
                print("The cost is $",self.stake,"per game. Would you like to play?")
                ans = input("\n\nYes(y)\t\t\tNo(n)")
                ans = ans.lower()
                if ans == "y":
                    done = True
                    self.play()
                elif ans =="n":
                    done = True
                    self.leave("See you next time!")
                else:
                    self.clear() 
                    print("Please enter a correct answer")
                    time.sleep(0.8)
                    self.clear()
        else:
            self.leave("Can't afford to play!")


#Balance will be integrated with the Casino class in the future. For now, this is for testing purposes only. 
balance = 500


#uncomment next two lines to play slots
#Play_Slots = Slots(balance)
#Play_Slots.welcome()


# uncomment next three lines for testing mode
#Iterations = 10000
#test_slots = Slots(balance)
#test_slots.testMode(10000)
