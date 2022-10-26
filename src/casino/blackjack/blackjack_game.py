"""A set of various casino games as classes"""
import os
import random




def selectGame():
    while True:
        print(
            "Games:\nteam1Game:1\nteam2game:2\nteam3game:3\nBlackjack:4\nteam5game:5\nQuit:q"
        )
        selectedGame = input("What game would you like to play?")
        print(selectedGame)
        if selectedGame == "4":
            print("Blackjack selected")
            game()
        elif selectedGame.lower() == "q":
            break
        else:
            print("invalid selection")
    

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand
def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []

        game()
    else:
        print("Bye!")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            total += ace_card(total)
        else:
            total += card
    return total

def ace_card(total):
    if total >= 11:
        return 1
    else:
        return 11
def hit(hand,deck):
    card = deck.pop()
    hand.append(card)
    return hand
def clear():
    if os.name == "nt":
        os.system("CLS")
    if os.name == "posix":
        os.system("clear")
def print_results(dealer_hand, player_hand):
    clear()
    print(
        "The dealer has a "
        + str(dealer_hand)
        + " for a total of "
        + str(total(dealer_hand))
    )
    print(
        "You have a "
        + str(player_hand)
        + " for a total of "
        + str(total(player_hand))
    )
def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a \n")
        play_again()
def check_player_wins(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        play_again()
    else:
        pass
def check_dealer_wins(dealer_hand, player_hand):
    if total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got 21\n")
        play_again()
    else:
        pass
def check_player_loses(dealer_hand, player_hand):
    if total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry. You busted. You lose.\n")
        play_again()
    else:
        pass
def check_dealer_busts(dealer_hand, player_hand):
    if total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer busts. You win!\n")
        play_again()
    else:
        pass
def check_losing_score(dealer_hand, player_hand):
    if total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
        play_again()
    else:
        pass
def check_winning_score(dealer_hand, player_hand):
    if total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Congratulations. Your score is higher than the dealer. You win\n")
        play_again()
    else:
        pass

def check_tie(dealer_hand, player_hand):
    if total(player_hand) == total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Tie, nobody wins.\n")
        play_again()
    else:
        pass
def score(dealer_hand, player_hand):
    check_dealer_busts(dealer_hand, player_hand)
    check_player_loses(dealer_hand, player_hand)
    check_player_wins(dealer_hand, player_hand)
    check_dealer_wins(dealer_hand, player_hand)
    check_losing_score(dealer_hand, player_hand)
    check_winning_score(dealer_hand, player_hand)

def chose_h(player_hand, dealer_hand,deck):
    hit(player_hand, deck)
    while total(dealer_hand) < 17:
        hit(dealer_hand, deck)
    score(dealer_hand, player_hand)
    play_again()

def chose_s(player_hand, dealer_hand, deck):
    while total(dealer_hand) < 17:
        hit(dealer_hand, deck)
    score(dealer_hand, player_hand)
    play_again()

def chose_q():
    print("Bye!")
    exit()

def game():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4
    choice = 0
    clear()
    print("WELCOME TO BLACKJACK!\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != "q":
        print("The dealer is showing a " + str(dealer_hand[0]))
        print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        if choice == "h":
            chose_h(player_hand, dealer_hand, deck)
        elif choice == "s":
            chose_s(player_hand, dealer_hand, deck)
        elif choice == "q":
            chose_q()


# Run main here.
if __name__ == "__main__":
    selectGame()
