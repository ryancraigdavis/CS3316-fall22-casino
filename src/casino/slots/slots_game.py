import random
import time
import os
"""A set of various casino games as classes"""





def clear():
    if os.name == 'nt':
        os.system('CLS')
    else:
        os.system('clear')
            

def leave(message):
    clear()
    print(message)
    time.sleep(2)
    clear()
    print("Returning to the casino center...")
    time.sleep(2)
    clear()


def runForIfContinueOrNot(ans, balance, stake):
    if ans =="y":
        done = True
        play(balance, stake)
    elif ans == "n":
        done = True
        leave("Thanks for playing!")
    else:
        print("Please enter a correct answer")
        time.sleep(0.8)
        clear()
    return done


def whichCherry(secondWheel):
    """Determines which jackpot the player gets from
    CHERRY being on the 1st wheel"""
    if secondWheel == "CHERRY":
        return 5
    else:
        return 2


def winCalc(firstWheel, secondWheel, thirdWheel):
    """
    Calculates the current score
    """
    clear()
    allSlots = firstWheel + " " + secondWheel + " " + thirdWheel
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
    if (win == 0) and (firstWheel == "CHERRY"):
        return whichCherry(secondWheel)
    return win


def printScore(firstWheel, secondWheel, thirdWheel, balance):
    """
    prints the current score and acts as a runner for winCalc
    """
    win = winCalc(firstWheel, secondWheel, thirdWheel)
    balance += win
    if win > 0:
        print(
            firstWheel
            + "\t"
            + secondWheel
            + "\t"
            + thirdWheel
            + " -- You win $"
            + str(win)
            + "!"
        )
    else:
        print(
            firstWheel
            + "\t"
            + secondWheel
            + "\t"
            + thirdWheel
            + " -- You lose!"
        )
    time.sleep(1)

    return balance


def spinWheel():
    """
    returns a random item from the wheel
    """
    items = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]
    rand = random.randint(0, 5)
    return  items[rand]


def play(balance, stake):
    balance -= stake
    clear()
    firstWheel = spinWheel()
    secondWheel = spinWheel()
    thirdWheel = spinWheel()
    balance = printScore(firstWheel, secondWheel, thirdWheel, balance)


def welcome():
    stake = 5
    balance = 500
    clear()
    print("Welcome to ")
    print(f"The cost is ${stake} per game.")


#uncomment next three lines to play slots (Will be implemented into
# the HelloCasino class once the relevant functions are added
# to select game)
welcome()
