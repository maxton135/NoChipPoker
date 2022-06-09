from .Card import Card
from .Deck import Deck

combos = ["Highcard", "Pair", "Two Pair", "Trips", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
suits = ["spades", "hearts", "clubs", "diamonds"]

class Table:
    
    def __init__(self, n):
 
        self.deck = Deck()
        self.communityCards = []
        self.numPlayers = n
        self.playerNames = []
        self.combos = {}
        self.cards = {}
 
    def askPlayerNames(self):
        for x in range(self.numPlayers):
            name = input("What is the name of a player?")
            self.playerNames.append(name)
 
    def shuffleDeck(self):
        self.deck.shuffle()
 
    def createDictionary(self):
        #self.dict["community"] = []
        self.cards["community"] = []
        for name in self.playerNames:
            #self.dict[name] = []
            self.combos[name] = -1
            self.cards[name] = []
 
    def giveCard(self, name):
        card = self.deck.draw()
        #self.dict[name].append(card)
        self.cards[name].append([card.getNum(), card.getSuit()])
    
    def deal(self):
        for name in self.playerNames:
            self.giveCard(name)
            self.giveCard(name)
    
    def printPlayerCards(self):
        print(self.cards)
        for name in self.playerNames:
            #print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(name + "'s Cards:")
            #input("Press ENTER to see " + name +"'s cards")
            for card in self.cards[name]:
                print(card)
    
    def printCommunityCards(self):
        print("Community Cards:")
        for card in self.cards["community"]:
                print(card)
    
    def executeFlop(self):
        for x in range(3):
            self.giveCard("community")
 
    def executeTurn(self):
        self.giveCard("community")
 
    def executeRiver(self):
        self.giveCard("community")

    def findCombos(self):
        for name in self.playerNames:
            #print(self.dict[name])
            #print(self.communityCards)
            #allcards = self.dict[name] + self.dict["community"]
            allcards = self.cards[name] + self.cards["community"]
            if self.checkRoyalFlush(name, allcards): continue
            if self.checkStraightFlush(name, allcards): continue
            if self.checkQuads(name, allcards): continue
            if self.checkFullHouse(name, allcards): continue
            if self.checkFlush(name, allcards): continue
            if self.checkStraight(name, allcards): continue
            if self.checkTrips(name, allcards): continue
            if self.checkTwoPair(name, allcards): continue
            if self.checkPair(name, allcards): continue
            if self.checkHighCard(name, allcards): continue

    def checkHighCard(self, name, cards):
        if self.combos[name] == 0:
            return True
        highest = 0
        for card in cards:
            if card[0] > highest:
                highest = card[0]
        self.combos[name] = 0.01*highest
        return True

    def checkPair(self, name, cards):
        if self.combos[name] == 1:
            return True
        highest = 0
        for i in range(len(cards)):
            num = cards[i][0]
            count = 1
            for j in range(len(cards)):
                if i != j:
                    if cards[j][0] == num:
                        count += 1
            if count == 2:
                if num > highest:
                    highest = num
        if highest != 0:
            self.combos[name] = 1 + 0.01*highest
            return True
        return False

    def checkTwoPair(self, name, cards):
        if self.combos[name] == 2:
            return True
        highest = 0
        pairCount = 0
        for i in range(len(cards)):
            num = cards[i][0]
            count = 1
            for j in range(len(cards)):
                if i != j:
                    if cards[j][0] == num:
                        count += 1
            if count == 2:
                pairCount += 1
                if num > highest:
                    highest = num
        if highest != 0 and pairCount >= 4:
            self.combos[name] = 2 + 0.01*highest
            return True
        return False

    def checkTrips(self, name, cards):
        if self.combos[name] == 3:
            return True
        highest = 0
        for i in range(len(cards)):
            num = cards[i][0]
            count = 1
            for j in range(len(cards)):
                if i != j:
                    if cards[j][0] == num:
                        count += 1
            if count == 3:
                if num > highest:
                    highest = num
        if highest != 0:
            self.combos[name] = 3 + 0.01*highest
            return True
        return False
                
    def checkStraight(self, name, cards):
        if self.combos[name] == 4:
            return True
        highest = 0
        for card in cards:
            count = 1
            num = card[0]
            for i in range(1, 5):
                if ([num+i, suits[0]] in cards) or ([num+i, suits[1]] in cards) or ([num+i, suits[2]] in cards) or ([num+i, suits[3]] in cards):
                    count += 1
            if count == 5:
                if num+4 > highest:
                    highest = num+4
        if highest != 0:
            self.combos[name] = (4 + 0.01*highest)
            return True
        return False

    def checkFlush(self, name, cards):
        if self.combos[name] == 5:
            return True
        heartsHighest = 0
        spadesHighest = 0
        diamondsHighest = 0
        clubsHighest = 0
        hearts = 0
        spades = 0
        diamonds = 0
        clubs = 0
        for card in cards:
            num = card[0]
            suit = card[1]
            if suit == "hearts":
                hearts += 1
                if num > heartsHighest:
                    heartsHighest = num
            elif suit == "spades":
                spades += 1
                if num > spadesHighest:
                    spadesHighest = num
            elif suit == "diamonds":
                diamonds += 1
                if num > diamondsHighest:
                    diamondsHighest = num
            else:
                clubs += 1
                if num > clubsHighest:
                    clubsHighest = num
        if hearts >= 5:
            self.combos[name] = 5 + 0.01*heartsHighest
            return True
        elif spades >= 5:
            self.combos[name] = 5 + 0.01*spadesHighest
            return True
        elif diamonds >= 5:
            self.combos[name] = 5 + 0.01*diamondsHighest
            return True
        elif clubs >= 5:
            self.combos[name] = 5 + 0.01*clubsHighest
            return True
        return False
        
    def checkFullHouse(self, name, cards):
        if self.combos[name] == 6:
            return True
        highest = 0
        tripsCount = 0
        pairCount = 0
        for i in range(len(cards)):
            num = cards[i][0]
            count = 1
            for j in range(len(cards)):
                if i != j:
                    if cards[j][0] == num:
                        count += 1
            if count == 3:
                tripsCount += 1
                if num > highest:
                    highest = num
        for i in range(len(cards)):
            num = cards[i][0]
            count = 1
            for j in range(len(cards)):
                if i != j:
                    if cards[j][0] == num:
                        count += 1
            if count == 2:
                pairCount += 1
        if highest != 0 and tripsCount > 0 and pairCount > 0:
            self.combos[name] = 6 + 0.01*highest
            return True
        return False     

    def checkQuads(self, name, cards):
        if self.combos[name] == 7:
            return True
        highest = 0
        for card in cards:
            num = card[0]
            if ([num, suits[0]] in cards) and ([num, suits[1]] in cards) and ([num, suits[2]] in cards) and ([num, suits[3]] in cards):
                if num > highest:
                    highest = num
                break
        if highest != 0:
            self.combos[name] = 7 + 0.01*highest

    def checkStraightFlush(self, name, cards):
        if self.combos[name] == 8:
            return True
        highest = 0
        for card in cards:
            count = 1
            num = card[0]
            suit = card[1]
            for i in range(1, 5):
                if [num+i, suit] in cards:
                    count += 1
            if count == 5:
                if num+4 > highest:
                    highest = num+4
        if highest != 0:
            self.combos[name] = (8 + 0.01*highest)
            return True
        return False

    def checkRoyalFlush(self, name, cards):
        if self.combos[name] == 9:
            return True
        for s in suits:
            if ([1, s] in cards) and ([10, s] in cards) and ([11, s] in cards) and ([12, s] in cards) and ([13, s] in cards):
                if self.combos[name] < 9:
                    self.combos[name] = 9
                return True
        return False

    def giveRF(self, name):
        #self.cards[name].append([13, "hearts"])
        #self.cards[name].append([13, "clubs"])
        #self.cards[name].append([13, "diamonds"])
        #self.cards[name].append([2, "clubs"])
        #self.cards[name].append([5, "clubs"])
        self.cards[name].append([5, "spades"])
    
    def printCombos(self):
        for name in self.playerNames:
            print(name + "'s combo value: ", self.combos[name])

    def printCardtest(self):
        for name in self.playerNames:
            print(name + "'s cards are:", self.cards[name])
    
    def askReady(self):
        input("Press ENTER when ready")
    
    def printWinner(self):
        highest = 0
        for name in self.playerNames:
            if self.combos[name] > highest:
                highest = self.combos[name]
                winner = name
        print("WINNER:", winner, "with a combo value of", highest)
