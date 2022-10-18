#!/usr/bin/env python3
"""A set of various casino games as classes"""
import os
import random
import pygame as pg




class HelloCasino:
    """Welcome to the casino"""

    def __init__(self):
        """Inits the players name"""
        self.name = "Joe"

    def welcome(self):
        """Welcome shouter"""
        print(f"Welcome to the Casino, {self.name}")

class BingoNumber:
    def __init__(self):
        self.timer = 0.0
        self.delay = 3000
        self.new_num()

    def new_num(self):
        num = random.randint(1, 100)
        self.image, self.rect = self.make_text(str(num), (255, 0, 0), screen_rect.center, 75, 'Ariel')

    def make_text(self, message, color, center, size, fonttype):
        font = pg.font.SysFont(fonttype, size)
        text = font.render(message, True, color)
        rect = text.get_rect(center=center)
        return text, rect

    def update(self):
        if pg.time.get_ticks() - self.timer > self.delay:
            self.timer = pg.time.get_ticks()
            self.new_num()

    def draw(self, surf):
        surf.blit(self.image, self.rect)

def compute_baccarot_score(hand):
    """Compute the score of a hand"""
    total_value = 0
    for card in hand:
        total_value += VALUE[CARDS.index(card)]
    return total_value % 10

def playBaccarot():
    """Returns the winner"""
    player_hand = [
        random.choice(CARDS),
        random.choice(CARDS)
    ]
    banker_hand = [
        random.choice(CARDS),
        random.choice(CARDS)
    ]

    player_score = compute_baccarot_score(player_hand)
    banker_score = compute_baccarot_score(banker_hand)

    print('Player has cards:\t' + player_hand[0] + '\t' + player_hand[1])
    print('Player has score of\t' + str(player_score))
    print('Banker has cards:\t' + banker_hand[0] + '\t' + banker_hand[1])
    print('Banker has score of\t' + str(banker_score))

    # Natural

    def bankerVSplayer():
        if player_score != banker_score:
            return OUTCOME[banker_score > player_score]
        else:
            return OUTCOME[2]

    if player_score in [8, 9] or banker_score in [8, 9]:
        return bankerVSplayer()

    # Player has low score

    def bankerDrawMaybe():
        if (banker_score == 6 and player_third in [6, 7]) or \
           (banker_score == 5 and player_third in irange(4, 7)) or \
           (banker_score == 4 and player_third in irange(2, 7)) or \
           (banker_score == 3 and player_third != 8) or \
           (banker_score in [0, 1, 2]):
            banker_hand.append(random.choice(CARDS))
            print('Banker gets a third card:\t' + banker_hand[2])

    def bankerDrawTrue():
        if banker_score in irange(0, 5):
            banker_hand.append(random.choice(CARDS))
            print('Banker gets a third card:\t' + banker_hand[2])

    if player_score in irange(0, 5):
        # Player get's a third card
        player_hand.append(random.choice(CARDS))
        player_third = compute_baccarot_score([player_hand[2]])
        print('Player gets a third card:\t' + player_hand[2])

        # Determine if banker needs a third card
        bankerDrawMaybe()

    elif player_score in [6, 7]:
        bankerDrawTrue()

    # Compute the scores again and return the outcome
    player_score = compute_baccarot_score(player_hand)
    banker_score = compute_baccarot_score(banker_hand)

    print('Player has final score of\t' + str(player_score))
    print('Banker has final score of\t' + str(banker_score))

    if player_score != banker_score:
        return OUTCOME[banker_score > player_score]
    else:
        return OUTCOME[2]



# Run main here.
if __name__ == "__main__":
    NewCasino = HelloCasino()
    NewCasino.welcome()

playBingo = False
if playBingo:
    pg.init()

    screen = pg.display.set_mode((800, 600))
    screen_rect = screen.get_rect()
    clock = pg.time.Clock()
    done = False

    num = BingoNumber()

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        screen.fill((0, 0, 0))
        num.update()
        num.draw(screen)
        pg.display.update()
        clock.tick(60)

playBac = True
if playBac:
    CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
    OUTCOME = ['Player wins', 'Banker wins', 'Tie']

    # Inclusive range function
    irange = lambda start, end: range(start, end + 1)

    print(playBaccarot())
