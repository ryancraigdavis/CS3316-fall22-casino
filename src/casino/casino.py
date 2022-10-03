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

    def cant_afford(self):
        print("You do not have enough money to play this game!")
        time.sleep(2)
        self.clear()
        self.fancyProgression("Returning to the casino center")
        self.clear()

    def broke(self):
        print("You are totally out of money!")
        time.sleep(2)
        self.clear()
        self.fancyProgression("Being booted out of the casino")
        exit()

    def fancyProgression(self, message):
        for i in range(4):
            print(message)
            time.sleep(1)
            message +=(" .")
            self.clear()
            

    def leave(self):
        self.clear()
        print("Thanks for playing!")
        time.sleep(2)
        self.clear()
        self.fancyProgression("Returning to the casino center")
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
                    self.leave()
                else: 
                    print("Please enter a correct answer")
                    time.sleep(0.8)
                    self.clear()

        elif self.stake > 0:
            self.cant_afford()
        else:
            self.broke()




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
            print(Slots.firstWheel + '\t' + Slots.secondWheel + '\t' + Slots.thirdWheel + ' -- You win $' + str(win))
        else:
            print(Slots.firstWheel + '\t' + Slots.secondWheel + '\t' + Slots.thirdWheel + ' -- You lose')





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
                    self.leave()
                else:
                    self.clear() 
                    print("Please enter a correct answer")
                    time.sleep(0.8)
                    self.clear()
        elif self.balance > 0:
            self.cant_afford()
        else:
            self.broke()


    def testMode(self, iterations):
        self.testingMode = True
        for i in range(iterations):
            self.play()
            self.balance = self.stake
            print("TESTING MODE\n\n")
            print("Total collected: $",self.total_collected)
            print("Total paid out: $",self.total_paid_out)
        self.clear()
        print("Iterations:",iterations)
        total_profit = self.total_collected - self.total_paid_out
        house_edge = ((total_profit / iterations) / self.stake * 100)
        print("Total collected: $",self.total_collected)
        print("Total paid out: $",self.total_paid_out)
        print("Total profit: $",total_profit)
        print("House Edge:",house_edge,"%")
        input("\n\n\nPress ENTER to exit program")
        exit()





#Balance will be integrated with the Casino class in the future. For now, this is for testing purposes only. 
balance = 500


#uncomment next two lines to play slots
#Play_Slots = Slots(balance)
#Play_Slots.welcome()


# uncomment next three lines for testing mode
#Iterations = 10000
#test_slots = Slots(balance)
#test_slots.testMode(10000)

