#!/usr/bin/env python3
"""A set of various casino games as classes"""
import os
import random
from random import randint
from random import randint

class Craps:

    # Dice constant
    MIN = 1
    MAX = 6

    # Imports random integer

    # Main Program
    def main(self):

        # Prints ascii title screen
        print("")
        print("")
        print("")
        print("     ▄████████    ▄████████    ▄████████  ▄█  ███▄▄▄▄    ▄██████▄ ")
        print("    ███    ███   ███    ███   ███    ███ ███  ███▀▀▀██▄ ███    ███")
        print("    ███    █▀    ███    ███   ███    █▀  ███▌ ███   ███ ███    ███")
        print("    ███          ███    ███   ███        ███▌ ███   ███ ███    ███")
        print("    ███        ▀███████████ ▀███████████ ███▌ ███   ███ ███    ███")
        print("    ███        ▀███████████ ▀███████████ ███▌ ███   ███ ███    ███")
        print("    ███    ███   ███    ███    ▄█    ███ ███  ███   ███ ███    ███")
        print("    ████████▀    ███    █▀   ▄████████▀  █▀    ▀█   █▀   ▀██████▀ ")
        print("")
        print("")
        print("   ▄████████    ▄████████    ▄████████    ▄███████▄    ▄████████")
        print("   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███")
        print("   ███    █▀    ███    ███   ███    ███   ███    ███   ███    █▀ ")
        print("   ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███   ███       ")
        print("   ███        ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀███████████")
        print("   ███    █▄  ▀███████████   ███    ███   ███                 ███")
        print("   ███    ███   ███    ███   ███    ███   ███           ▄█    ███")
        print("   ████████▀    ███    ███   ███    █▀   ▄████▀       ▄████████▀ ")
        print("                ███    ███                                       ")
        print("")
        print("")
        print("")

        # Initial boolean variables for validation and program loop
        keepGoing = True

        # Starting chip amount
        user_chips = 10000

        # Validation Loop
        while keepGoing:
            # Validates chip wager amount
            wager = self.getValidWager(user_chips)
            
            # Bet type?
            user_chips = self.bet(user_chips, wager)

            
            # Out of chips?
            if user_chips == 0:
                print("You have lost all your chips. Better luck next time!")
                print("Thanks for playing.")
                keepGoing = False
            # Leave table?
            if keepGoing == True:
                print("Would you like to keep playing?")
                leaveGame = input(
                    "(Enter 'q' to leave the table or anything else to continue): "
                )
                # Quit Game
                if leaveGame == "q" or leaveGame == "Q":
                    print("You left with", (user_chips), "chips.")
                    print("Thanks for playing. Have a nice day.")
                    keepGoing = False
            
    def getValidWager(self, user_chips):
        validate = False
        while not validate:
            wager = input(
                "You have "
                + str(user_chips)
                + " chips. How many chips would you like to wager?: "
            )
            try:
                wager = int(wager)
                if (wager >= 1) and (wager <= user_chips):
                    validate = True
            # Validates input type
            except:
                print("Not a valid wager.")
        return wager

    def bet(self, user_chips, wager):
        print("What type of bet would you like to place?")
        type_of_bet = input(
            "(Enter 'p' to bet on Pass Line or 'dp' to bet on Dont Pass Line): "
        )
        # PASS
        if type_of_bet.lower() == "p":
            user_chips = self.pass_line_bet(user_chips, wager)
            print("You now have", (user_chips), "chips.")
            return user_chips
        # DONT PASS
        elif type_of_bet.lower() == "dp":
            user_chips = self.dont_pass_bet(user_chips, wager)
            print("You now have", (user_chips), "chips.")
            return user_chips

            
    def whilePass(self, first_rand_sum, continued_rolls, wager, user_chips):
        while (first_rand_sum != continued_rolls) and (continued_rolls != 7):
            print("The point is", (first_rand_sum))
            # Increase bet on PASS LINE during point roll?
            if user_chips - wager > 1:
                print("Would you like to increase your Pass Line wager?")
                increasePass = input("(Enter 'y' for yes or any other key for no) ")
                # Validates PASS LINE bet increase
                if increasePass == "y" or increasePass == "Y":
                    self.doubleCheckPass(wager, user_chips)
            # Roll again (point established)
            continued_rolls = input("(Press 'enter' to roll again) ")
            continued_roll_1 = self.random_roll()
            continued_roll_2 = self.random_roll()

            print("You rolled", continued_roll_1, "and", continued_roll_2)
            continued_rolls = continued_roll_1 + continued_roll_2
            
    # Function:
    ##  pass_line_bet
    ##Description:
    ##  Simulates a PASS LINE bet senario
    ##Calls:
    ##  names()
    ##  random_roll()
    ##Parameters:
    ##  user_chips
    ##  wager
    ##Returns:
    ##  user_chips
    def pass_line_bet(self, user_chips, wager):

        # Initial boolean variables for validation loops
        validate = True
        doubleCheck = True

        # Roll the dice
        print("Coming Out ...")
        rand_dice_1 = self.self.random_roll()
        rand_dice_2 = self.self.random_roll()
        # Craps lingo
        rand_sum = rand_dice_2 + rand_dice_1
        print("You rolled", rand_dice_1, "and", rand_dice_2)

        # Craps: loose PASS LINE bet
        if (rand_sum == 2) or (rand_sum == 3) or (rand_sum == 12):
            user_chips -= wager
            print(self.names(rand_dice_1, rand_dice_2))
            # Craps lingo
            print("Crap Out!")
            print("Your bet LOOSES")

        # Natural: win PASS LINE bet
        elif (rand_sum == 7) or (rand_sum == 11):
            user_chips += wager
            # Craps lingo
            print(self.names(rand_dice_1, rand_dice_2))
            print("Natural Winner")
            print("Your bet WINS")

        # Set up for point
        else:
            first_rand_sum = rand_sum
            continued_rolls = 0
            # Establish point
            self.whilePass(first_rand_sum, continued_rolls, wager, user_chips)
            # Seven out: PASS LINE looses (point established)
            if continued_rolls == 7:
                user_chips -= wager
                print(self.names(continued_roll_1, continued_roll_2))
                print("Seven Out")
                print("Your bet LOOSES")
            # PASS LINE wins (point established)
            elif continued_rolls == first_rand_sum:
                user_chips += wager
                print(self.names(continued_roll_1, continued_roll_2))
                print("Your bet WINS")

        return user_chips

    # Function:
    ##  dont_pass_bet
    ##Description:
    ##  Simulates a DONT PASS LINE bet senario
    ##Calls:
    ##  names()
    ##  random_roll()
    ##Parameters:
    ##  user_chips
    ##  wager
    ##Returns:
    ##  user_chips
    
    def validatePass(self, wager, newWager, user_chips):
        validate = 'true'
        while validate:
            if ((wager + newWager) < user_chips) and (newWager >= 1):
                    wager = newWager + wager
                    validate = False
                    doubleCheck = False
            else:
                print("Not a valid wager.")
                newWager = int(
                    input(
                        "Enter the amount you would like to increase your bet: "
                    )
                )
        return doubleCheck

    def doubleCheckPass(self, wager, user_chips):
        doubleCheck = 'true'
        while doubleCheck:
            newWager = int(
                input(
                    "Enter the amount you would like to increase your bet: "
                )
            )
            doubleCheck = self.validatePass(wager, newWager, user_chips)    
        return newWager
   
    def whileDontPass(self, first_rand_sum, continued_rolls, wager, user_chips):
        while (first_rand_sum != continued_rolls) and (continued_rolls != 7):
            print("The Point is", (first_rand_sum))
            print("Would you like to increase your Dont Pass Line wager?")
            increaseDontPass = input("Enter 'y' for yes or any other key for no): ")
            if increaseDontPass == "y" or increaseDontPass == "Y":
                ##fixing
                self.doubleCheckPass(wager, user_chips)
            ###fixing
            continued_rolls = input("(Press 'enter' to roll again): ")
            continued_roll_1 = self.random_roll()
            continued_roll_2 = self.random_roll()
            print("You rolled", continued_roll_1, "and", continued_roll_2)
            continued_rolls = continued_roll_1 + continued_roll_2

    def dont_pass_bet(self, user_chips, wager):

        validate = True
        doubleCheck = True

        print("Coming Out ...")
        rand_dice_1 = self.random_roll()
        rand_dice_2 = self.random_roll()
        rand_sum = rand_dice_2 + rand_dice_1
        print("You rolled", rand_dice_1, "and", rand_dice_2)

        if (rand_sum == 2) or (rand_sum == 3):
            user_chips += wager
            print(self.names(rand_dice_1, rand_dice_2))
            print("Craps")
            print("Your bet WINS")

        elif rand_sum == 12:
            print(self.names(rand_dice_1, rand_dice_2))
            print("Push")
            print("Your bet is BARRED")

        elif (rand_sum == 7) or (rand_sum == 11):
            user_chips -= wager
            print(self.names(rand_dice_1, rand_dice_2))
            print("Natural")
            print("Your bet LOOSES")

        else:
            first_rand_sum = rand_sum
            continued_rolls = 0
            self.whileDontPass(first_rand_sum, continued_rolls, wager, user_chips)           
            if continued_rolls == 7:
                user_chips += wager
                print(self.names(continued_roll_1, continued_roll_2))
                print("Seven Out")
                print("Your bet WINS")

            elif continued_rolls == first_rand_sum:
                user_chips -= wager
                print(self.names(continued_roll_1, continued_roll_2))
                print("Your bet LOOSES")

        return user_chips

    dice_roll_table = {
      6: " _______ \n| *   * |\n| *   * |\n| *   * |\n ------- \n",
      
      5: " _______ \n| *   * |\n|   *   |\n| *   * |\n ------- \n",
      
      4: " _______ \n| *   * |\n|       |\n| *   * |\n ------- \n",
      
      3: " _______ \n| *     |\n|   *   |\n|     * |\n ------- \n",
      
      2: " _______ \n| *     |\n|       |\n|     * |\n ------- \n",
      
      1: " _______ \n|       |\n|   *   |\n|       |\n ------- \n",

   		}
    # Function:
    ##  dice_roll
    ##Description:
    ##  prints ascii dice graphic
    ##Calls:
    ##  none
    ##Parameters:
    ##  random_number
    ##Returns:
    ##  none
    def dice_roll(self, random_number):
      action = self.dice_roll_table.get(random_number)
      print(action)

    ##Description:
    ##  Simulates dice being thrown
    ##Calls:
    ##  dice_roll
    ##Parameters:
    ##  dice1
    ##  dice2
    ##Returns:
    ##  random_number
    def random_roll(self):

        # Throw dice
        random_number = random.randint(self.MIN, self.MAX)
        print(random_number)
        self.dice_roll(random_number)

        return random_number

    def names(self, dice1, dice2):
        if dice1 == dice2 or dice1 == 4 and dice2 == 5 or dice1 == 5 and dice2 ==5:
            specialRoll = (dice1 * 10) + dice2
            name = self.special_roll_name_table.get(specialRoll)
            return name
          
        else:
            diceSum = dice1 + dice2
            name = self.regular_roll_name_table.get(diceSum)
            return name
      
      
    special_roll_name_table = {
      
      11: "Snake Eyes!",
      
      22: "Little Joe from Kokomo, Hard Four!",
      
      33: "Hard Six!",
      
      44: "Square Pair, Hard Eight!",
      
      45: "Jesse James!",
      
      54: "Jesse James!",
      
      55: "General Patton, Hard Ten!",
    }

    regular_roll_name_table = {
      
       3: "Ace Deuce!",
      
       4: "Easy Four!",
      
       5: "Fever Five!",
      
       6: "Jimmy Hicks from the Sticks, Easy Six!",
      
       7: "Big Red!",
      
       8: "Easy Eight!",
      
       9: "Nina from Pasadena!",
      
      10: "Easy Ten!",
      
      11: "Yo!",
      
      12: "BoxCars!",
    }


# class HelloCasino:
#     """Welcome to the casino"""

#     def __init__(self):
#         """Inits the players name"""
#         self.name = "Joe"

#     def welcome(self):
#         """Welcome shouter"""
#         print(f"Welcome to the Casino, {self.name}")



craps = Craps()
craps.main()