# This is a python file to show how the game works
import random

CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
OUTCOME = ['Player wins', 'Banker wins', 'Tie']

# Inclusive range function
irange = lambda start, end: range(start, end + 1)

def compute_score(hand):
    """Compute the score of a hand"""
    total_value = 0
    for card in hand:
        total_value += VALUE[CARDS.index(card)]
    return total_value % 10



# functions for play
def bankerVSplayer(pScore, bScore):
    if pScore != bScore:
        return OUTCOME[bScore > pScore]
    else:
        return OUTCOME[2]
def bankerDrawMaybe(bankerS, third, bHand):
    if (bankerS == 6 and third in [6, 7]) or \
       (bankerS == 5 and third in irange(4, 7)) or \
       (bankerS == 4 and third in irange(2, 7)) or \
       (bankerS == 3 and third != 8) or \
       (bankerS in [0, 1, 2]):
        bHand.append(random.choice(CARDS))
        print('Banker gets a third card:\t' + bHand[2])

def bankerDrawTrue(bScore, bHand):
    if bScore in irange(0, 5):
        bHand.append(random.choice(CARDS))
        print('Banker gets a third card:\t' + bHand[2])

def play():

    player_hand = [
        random.choice(CARDS),
        random.choice(CARDS)
    ]
    banker_hand = [
        random.choice(CARDS),
        random.choice(CARDS)
    ]

    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)

    print('Player has cards:\t' + player_hand[0] + '\t' + player_hand[1])
    print('Player has score of\t' + str(player_score))
    print('Banker has cards:\t' + banker_hand[0] + '\t' + banker_hand[1])
    print('Banker has score of\t' + str(banker_score))

    # Natural
    if player_score in [8, 9] or banker_score in [8, 9]:
        return bankerVSplayer(player_score, banker_score)

    # Player has low score
    def checkPlayerScore(pScore, pHand, pThird):
        if pScore in irange(0, 5):
            # Player get's a third card
            pHand.append(random.choice(CARDS))
            pThird = compute_score([pHand[2]])
            print('Player gets a third card:\t' + pHand[2])

            # Determine if banker needs a third card
            bankerDrawMaybe(banker_score, player_third, banker_hand)

        elif player_score in [6, 7]:
            bankerDrawTrue(banker_score, banker_hand)

    player_third

    checkPlayerScore(player_score, player_hand, player_third)

    # Compute the scores again and return the outcome
    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)

    print('Player has final score of\t' + str(player_score))
    print('Banker has final score of\t' + str(banker_score))

    if player_score != banker_score:
        return OUTCOME[banker_score > player_score]
    else:
        return OUTCOME[2]


if __name__ == "__main__":
    print(play())
