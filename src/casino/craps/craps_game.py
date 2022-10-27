#!/usr/bin/env python3
"""A set of various casino games as classes"""
from random import randint

# Dice constant

# Imports random integer


# Main Program
def play():
  # Initial boolean variables for validation and program loop

  # Starting chip amount
  user_chips = 10000

  # Validation Loop
  # while keepGoing:
  # Validates chip wager amount
  wager = getValidWager(user_chips)

  # Bet type?
  user_chips = get_bet(user_chips, wager)

  # # Out of chips?
  # if user_chips == 0:
  #     print("You have lost all your chips. Better luck next time!")
  #     print("Thanks for playing.")
  #     keepGoing = False
  # # Leave table?
  # if keepGoing == True:
  #     print("Would you like to keep playing?")
  #     leaveGame = input(
  #         "(Enter 'q' to leave the table or anything else to continue): "
  #     )
  #     # Quit Game
  #     if leaveGame == "q" or leaveGame == "Q":
  #         print("You left with", (user_chips), "chips.")
  #         print("Thanks for playing. Have a nice day.")
  #         keepGoing = False


def getValidWager(user_chips):
  validate = False
  while not validate:
    wager = input("You have " + str(user_chips) +
                  " chips. How many chips would you like to wager?: ")
    try:
      wager = int(wager)
      if (wager >= 1) and (wager <= user_chips):
        validate = True
    # Validates input type
    except:
      print("Not a valid wager.")
  return wager


def get_bet(user_chips, wager):
  print("What type of bet would you like to place?")
  type_of_bet = ""
  while not (type_of_bet.lower() == "p" or type_of_bet.lower() == "dp"):
    type_of_bet = input(
      "(Enter 'p' to bet on Pass Line or 'dp' to bet on Dont Pass Line): ")
  user_chips = bet(type_of_bet, user_chips, wager)
  return user_chips


def bet(type_of_bet, user_chips, wager):
  if type_of_bet.lower() == "p":
    user_chips = pass_line_bet(user_chips, wager)
    print("You now have", (user_chips), "chips.")
    return user_chips
  # DONT PASS
  elif type_of_bet.lower() == "dp":
    user_chips = dont_pass_bet(user_chips, wager)
    print("You now have", (user_chips), "chips.")
    return user_chips


def increaseBetPass(user_chips, wager):
  if user_chips - wager > 1:
    print("Would you like to increase your Pass Line wager?")
    increasePass = input("(Enter 'y' for yes or any other key for no) ")
    # Validates PASS LINE bet increase
    if increasePass == "y" or increasePass == "Y":
      wager = doubleCheckPass(wager, user_chips)
  

def whilePass(first_rand_sum, continued_rolls, wager, user_chips):
  while (first_rand_sum != continued_rolls) and (continued_rolls != 7):
    print("The point is", (first_rand_sum))
    # Increase bet on PASS LINE during point roll?
    wager = increaseBetPass(user_chips, wager)
    # Roll again (point established)
    continued_rolls = input("(Press 'enter' to roll again) ")
    continued_roll_1 = random_roll()
    continued_roll_2 = random_roll()

    print("You rolled", continued_roll_1, "and", continued_roll_2)
    continued_rolls = continued_roll_1 + continued_roll_2
  return first_rand_sum, continued_rolls, wager, user_chips, continued_roll_1, continued_roll_2


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
def pass_line_bet(user_chips, wager):

  # Roll the dice
  print("Coming Out ...")
  rand_dice_1 = random_roll()
  rand_dice_2 = random_roll()
  # Craps lingo
  rand_sum = rand_dice_2 + rand_dice_1
  print("You rolled", rand_dice_1, "and", rand_dice_2)

  # Craps: loose PASS LINE bet
  if (rand_sum == 2) or (rand_sum == 3) or (rand_sum == 12):
    user_chips -= wager
    print(names(rand_dice_1, rand_dice_2))
    # Craps lingo
    print("Crap Out!")
    print("Your bet LOOSES")

  # Natural: win PASS LINE bet
  elif (rand_sum == 7) or (rand_sum == 11):
    user_chips += wager
    # Craps lingo
    print(names(rand_dice_1, rand_dice_2))
    print("Natural Winner")
    print("Your bet WINS")

  # Set up for point
  else:
    first_rand_sum = rand_sum
    continued_rolls = 0
    # Establish point
    first_rand_sum, continued_rolls, wager, user_chips, continued_roll_1, continued_roll_2 = whilePass(
      first_rand_sum, continued_rolls, wager, user_chips)
    # Seven out: PASS LINE looses (point established)
    user_chips = sevenOutPass(continued_rolls, user_chips, continued_roll_1,
                              continued_roll_2, wager, first_rand_sum)

  return user_chips


def sevenOutPass(continued_rolls, user_chips, continued_roll_1,
                 continued_roll_2, wager, first_rand_sum):
  if continued_rolls == 7:
    user_chips -= wager
    print(names(continued_roll_1, continued_roll_2))
    print("Seven Out")
    print("Your bet LOOSES")
    return user_chips
  # PASS LINE wins (point established)
  elif continued_rolls == first_rand_sum:
    user_chips += wager
    print(names(continued_roll_1, continued_roll_2))
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


def validatePass(wager, newWager, user_chips):
  validate = True
  while validate:
    if ((wager + newWager) < user_chips) and (newWager >= 1):
      wager = newWager + wager
      validate = False
      doubleCheck = False
    else:
      print("Not a valid wager.")
      newWager = int(
        input("Enter the amount you would like to increase your bet: "))
  return doubleCheck, wager


def doubleCheckPass(wager, user_chips):
  doubleCheck = True
  while doubleCheck:
    newWager = int(
      input("Enter the amount you would like to increase your bet: "))
    doubleCheck, wager = validatePass(wager, newWager, user_chips)
  return newWager


def yesDontPass(increaseDontPass, wager, user_chips):
  if increaseDontPass == "y" or increaseDontPass == "Y":
    ##fixing
    doubleCheckPass(wager, user_chips)


def whileDontPass(first_rand_sum, continued_rolls, wager, user_chips):
  while (first_rand_sum != continued_rolls) and (continued_rolls != 7):
    print("The Point is", (first_rand_sum))
    print("Would you like to increase your Dont Pass Line wager?")
    increaseDontPass = input("Enter 'y' for yes or any other key for no): ")
    yesDontPass(increaseDontPass, wager, user_chips)
    ###fixing
    continued_rolls = input("(Press 'enter' to roll again): ")
    continued_roll_1 = random_roll()
    continued_roll_2 = random_roll()
    print("You rolled", continued_roll_1, "and", continued_roll_2)
    continued_rolls = continued_roll_1 + continued_roll_2
  return first_rand_sum, continued_rolls, wager, user_chips, continued_roll_1, continued_roll_2


def dont_pass_bet(user_chips, wager):

  print("Coming Out ...")
  rand_dice_1 = random_roll()
  rand_dice_2 = random_roll()
  rand_sum = rand_dice_2 + rand_dice_1
  print("You rolled", rand_dice_1, "and", rand_dice_2)

  if (rand_sum == 2) or (rand_sum == 3):
    user_chips += wager
    print(names(rand_dice_1, rand_dice_2))
    print("Craps")
    print("Your bet WINS")

  elif rand_sum == 12:
    print(names(rand_dice_1, rand_dice_2))
    print("Push")
    print("Your bet is BARRED")

  elif (rand_sum == 7) or (rand_sum == 11):
    user_chips -= wager
    print(names(rand_dice_1, rand_dice_2))
    print("Natural")
    print("Your bet LOOSES")
  else:
    first_rand_sum = rand_sum
    continued_rolls = 0
    first_rand_sum, continued_rolls, wager, user_chips, continued_roll_1, continued_roll_2 = whileDontPass(
      first_rand_sum, continued_rolls, wager, user_chips)
    user_chips = sevenoutDontPass(continued_rolls, user_chips,
                                  continued_roll_1, continued_roll_2, wager,
                                  first_rand_sum)

  return user_chips


def sevenoutDontPass(continued_rolls, user_chips, continued_roll_1,
                     continued_roll_2, wager, first_rand_sum):
  if continued_rolls == 7:
    user_chips += wager
    print(names(continued_roll_1, continued_roll_2))
    print("Seven Out")
    print("Your bet WINS")
    return user_chips

  elif continued_rolls == first_rand_sum:
    user_chips -= wager
    print(names(continued_roll_1, continued_roll_2))
    print("Your bet LOOSES")
    return user_chips


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
def dice_roll(random_number):
  dice_roll_table = {
    6: " _______ \n| *   * |\n| *   * |\n| *   * |\n ------- \n",
    5: " _______ \n| *   * |\n|   *   |\n| *   * |\n ------- \n",
    4: " _______ \n| *   * |\n|       |\n| *   * |\n ------- \n",
    3: " _______ \n| *     |\n|   *   |\n|     * |\n ------- \n",
    2: " _______ \n| *     |\n|       |\n|     * |\n ------- \n",
    1: " _______ \n|       |\n|   *   |\n|       |\n ------- \n",
  }
  action = dice_roll_table.get(random_number)
  return (action)


##Description:
##  Simulates dice being thrown
##Calls:
##  dice_roll
##Parameters:
##  dice1
##  dice2
##Returns:
##  random_number
def random_roll():
  MIN = 1
  MAX = 6
  # Throw dice
  random_number = randint(MIN, MAX)
  print(random_number)
  print(dice_roll(random_number))

  return random_number


def names(dice1, dice2):
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
  if dice1 == dice2 or dice1 == 4 and dice2 == 5 or dice1 == 5 and dice2 == 4:
    specialRoll = (dice1 * 10) + dice2
    name = special_roll_name_table.get(specialRoll)
    return name

  else:
    diceSum = dice1 + dice2
    name = regular_roll_name_table.get(diceSum)
    return name


# class HelloCasino:
#     """Welcome to the casino"""

#     def __init__(self):
#         """Inits the players name"""
#         self.name = "Joe"

#     def welcome(self):
#         """Welcome shouter"""
#         print(f"Welcome to the Casino, {self.name}")
if __name__ == "__main__":
  play()
