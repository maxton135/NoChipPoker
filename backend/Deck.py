from .Card import Card

combos = ["Highcard", "Pair", "Two Pair", "Trips", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
suits = ["spades", "hearts", "clubs", "diamonds"]

import random
from datetime import datetime
random.seed(datetime.now())

class Deck:
    
    def __init__(self):
        self.cards = []
        #suits = ["spades", "clubs", "hearts", "diamonds"]
        for x in range(4):
            for y in range(1, 14):
                self.cards.append(Card(suits[x], y))
    
    def shuffle(self):
        random.shuffle(self.cards)
 
    def print(self):
        for x in range(len(self.cards)):
            print(str(x) + ": " + str(self.cards[x].getNum()) + " of " + str(self.cards[x].getSuit()))
 
    def draw(self):
        pulled_card = self.cards[0]
        self.cards.pop(0)
        return pulled_card
 