class Card:
 
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
 
    def getNum(self):
        return self.num
 
    def getSuit(self):
        return self.suit
 
    def printCard(self):
        print("[" + str(self.num) + " Of " + str(self.suit) + "]")
 