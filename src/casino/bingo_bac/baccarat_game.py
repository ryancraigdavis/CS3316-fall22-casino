# This is a python file to show how the game works
import random


def compute_score(hand):
    VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
    CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    """Compute the score of a hand"""
    total_value = 0
    for card in hand:
        total_value += VALUE[CARDS.index(card)]
    return total_value % 10



# functions for play
def bankerVSplayer(pScore, bScore):
    OUTCOME = ['Player wins', 'Banker wins', 'Tie']
    if pScore != bScore:
        return OUTCOME[bScore > pScore]
    else:
        return OUTCOME[2]

def bankerDrawMaybe(bankerS, third, bHand):
    CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    irange = lambda start, end: range(start, end + 1)
    if (bankerS == 6 and third in [6, 7]) or \
       (bankerS == 5 and third in irange(4, 7)) or \
       (bankerS == 4 and third in irange(2, 7)) or \
       (bankerS == 3 and third != 8) or \
       (bankerS in [0, 1, 2]):
        bHand.append(random.choice(CARDS))
        print('Banker gets a third card:\t' + bHand[2])

def bankerDrawTrue(bScore, bHand):
    CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    irange = lambda start, end: range(start, end + 1)
    if bScore in irange(0, 5):
        bHand.append(random.choice(CARDS))
        print('Banker gets a third card:\t' + bHand[2])

def checkPlayerScore(pScore, pHand, pThird, bScore, bHand):
    CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    irange = lambda start, end: range(start, end + 1)
    if pScore in irange(0, 5):
        # Player get's a third card
        pHand.append(random.choice(CARDS))
        pThird = compute_score([pHand[2]])
        print('Player gets a third card:\t' + pHand[2])

        # Determine if banker needs a third card
        bankerDrawMaybe(bScore, pThird, bHand)

    elif pScore in [6, 7]:
        bankerDrawTrue(bScore, bHand)

def compareScores(pScore, bScore):
    OUTCOME = ['Player wins', 'Banker wins', 'Tie']
    if pScore != bScore:
        return OUTCOME[bScore > pScore]
    else:
        return OUTCOME[2]

def anyScoreHigh (pScore, bScore):
    if pScore in [8, 9] or bScore in [8, 9]:
        return bankerVSplayer(pScore, bScore)


def play():
    CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
    OUTCOME = ['Player wins', 'Banker wins', 'Tie']

    # Inclusive range function
    irange = lambda start, end: range(start, end + 1)

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
    anyScoreHigh(player_score, banker_score)
    # Player has low score
    player_third = int

    checkPlayerScore(player_score, player_hand, player_third, banker_score, banker_hand)

    # Compute the scores again and return the outcome
    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)

    print('Player has final score of\t' + str(player_score))
    print('Banker has final score of\t' + str(banker_score))

    compareScores(player_score, banker_score)


if __name__ == "__main__":
    print(play())
