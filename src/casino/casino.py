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
                BlackJack.game()
            elif(selectedGame.lower() == "q"):
                break
            else:
                print("invalid selection")

class BlackJack:

    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

    def __init__(self):
        BlackJack.game()

    def deal(deck):
        hand = []
        for i in range(2):
            random.shuffle(deck)
            card = deck.pop()
            if card == 11: card = "J"
            if card == 12: card = "Q"
            if card == 13: card = "K"
            if card == 14: card = "A"
            hand.append(card)
        return hand


    def play_again():
        again = input("Do you want to play again? (Y/N) : ").lower()
        if again == "y":
            dealer_hand = []
            player_hand = []
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
            BlackJack.game()
        else:
            print("Bye!")
            exit()


    def total(hand):
        total = 0
        for card in hand:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A":
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += card
        return total


    def hit(hand):
        card = BlackJack.deck.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
        return hand


    def clear():
        if os.name == 'nt':
            os.system('CLS')
        if os.name == 'posix':
            os.system('clear')


    def print_results(dealer_hand, player_hand):
        BlackJack.clear()
        print("The dealer has a " + str(dealer_hand) + " for a total of " + str(BlackJack.total(dealer_hand)))
        print("You have a " + str(player_hand) + " for a total of " + str(BlackJack.total(player_hand)))


    def blackjack(dealer_hand, player_hand):
        if BlackJack.total(player_hand) == 21:
            BlackJack.print_results(dealer_hand, player_hand)
            print("Congratulations! You got a Blackjack!\n")
            BlackJack.play_again()
        elif BlackJack.total(dealer_hand) == 21:
            BlackJack.print_results(dealer_hand, player_hand)
            print("Sorry, you lose. The dealer got a blackjack.\n")
            BlackJack.play_again()


    def score(dealer_hand, player_hand):
        if BlackJack.total(player_hand) == 21:
            BlackJack.print_results(dealer_hand, player_hand)
            print("Congratulations! You got a Blackjack!\n")
        elif BlackJack.total(dealer_hand) == 21:
            BlackJack.print_results(dealer_hand, player_hand)
            print("Sorry, you lose. The dealer got a blackjack.\n")
        elif BlackJack.total(player_hand) > 21:
            BlackJack.print_results(dealer_hand, player_hand)
            print("Sorry. You busted. You lose.\n")
        elif BlackJack.total(dealer_hand) > 21:
            BlackJack.print_results(dealer_hand, player_hand)
            print("Dealer busts. You win!\n")
        elif BlackJack.total(player_hand) < BlackJack.total(dealer_hand):
            BlackJack.print_results(dealer_hand, player_hand)
        # print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
        elif BlackJack.total(player_hand) > BlackJack.total(dealer_hand):
            BlackJack.print_results(dealer_hand, player_hand)
            print("Congratulations. Your score is higher than the dealer. You win\n")


    def game():
        choice = 0
        BlackJack.clear()
        print("WELCOME TO BLACKJACK!\n")
        dealer_hand = BlackJack.deal(BlackJack.deck)
        player_hand = BlackJack.deal(BlackJack.deck)
        while choice != "q":
            print("The dealer is showing a " + str(dealer_hand[0]))
            print("You have a " + str(player_hand) + " for a total of " + str(BlackJack.total(player_hand)))
            BlackJack.blackjack(dealer_hand, player_hand)
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
            BlackJack.clear()
            if choice == "h":
                BlackJack.hit(player_hand)
                while BlackJack.total(dealer_hand) < 17:
                    BlackJack.hit(dealer_hand)
                BlackJack.score(dealer_hand, player_hand)
                BlackJack.play_again()
            elif choice == "s":
                while BlackJack.total(dealer_hand) < 17:
                    BlackJack.hit(dealer_hand)
                BlackJack.score(dealer_hand, player_hand)
                BlackJack.play_again()
            elif choice == "q":
                print("Bye!")
                exit()

# Run main here.
if __name__ == "__main__":
    NewCasino = HelloCasino()
    NewCasino.welcome()
    NewCasino.selectGame()
