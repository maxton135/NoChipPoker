print("\n\n\nRUNNING POKER HELPER\n\n\n")

import eel
from tkinter import *
from backend.Card import Card
from backend.Deck import Deck
from backend.Table import Table

# Tkinter classes
class StartScreen():
    def __init__(self):
        self.root = Tk()
        self.play_button = Button(
            self.root,
            text="Play",
            font=("Arial"),
            width=50,
            height=10,
            bg="black",
            fg="white",
            command=self.play_button_click,
        )
        self.exit_button = Button(
            self.root,
            text="Quit",
            font=("Arial"),
            width=50,
            height=10,
            #padx=10, 
            #pady=10,
            bg="black",
            fg="grey",
            command=self.exit_button_click,
        )
        self.play_button.pack()
        self.exit_button.pack(side=TOP)
        self.root.mainloop()
    
    def play_button_click(self):
        self.root.destroy()

    def exit_button_click(self):
        quit()

class SetupScreen():
    def __init__(self):
        self.root = Tk()
        self.title = "Poker Game Setup"
        self.playername_entries = []
        self.playernum = 0
        self.playernames = []
        self.validNames = False
        self.validNum = False
        self.validSS = False

        self.setup_msg = Label(self.root, text="Set up the poker game")
        self.playernum_label = Label(self.root, text="How many players?")
        self.playernum_entry = Entry(self.root)
        self.playernum_button = Button(self.root, text="Enter", command=self.get_playernum)
        self.playername_button = Button(self.root, text="Enter", command=self.get_playernames)
        self.startingstack_label = Label(self.root, text="Starting stack size?")
        self.startingstack_entry = Entry(self.root)
        self.startingstack_button = Button(self.root, text="Enter", command=self.get_startingstack)
        self.startgame_button = Button(self.root, text="Start game", command=self.initiate_game)

        # Setup instruction message
        self.setup_msg.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.playernum_label.grid(row=1, column=0, padx=10, pady=10)
        self.playernum_entry.grid(row=1, column=1, padx=10, pady=10)
        self.playernum_button.grid(row=1, column=2, padx=10, pady=10)


        self.root.mainloop()

    def get_playernum(self):
        self.validNum = False
        pn = self.playernum_entry.get()
        if (pn.isdigit() and int(pn) > 0 and int(pn) < 5):
            self.playernum = int(pn)
            self.playernum_entry.config(bg='green')
            for player in range(self.playernum):
                entry = Entry(self.root)
                self.playername_entries.append(entry)
                entry.grid(row=2+player, column=1, padx=10, pady=10)
                #self.playername_entries[player].grid(row=2+player, column=1, padx=10, pady=10)
            self.playername_button.grid(row=self.playernum+1, column=2, padx=10, pady=10)
            self.validNum = True
        else:
            self.playernum_entry.config(bg='red')

    def get_playernames(self):
        #check if all entries are filled
        self.validNames = False
        valid_count = 0
        for p in range(self.playernum):
            entry = self.playername_entries[p].get()
            print(entry)
            if(entry != ""):
                self.playername_entries[p].config(bg='green')
                self.playernames.append(entry)
                valid_count += 1
            else:
                self.playername_entries[p].config(bg='red')
        if (valid_count == self.playernum):
            validNames = True
            self.startingstack_label.grid(row=self.playernum+2, column=0, padx=10, pady=10)
            self.startingstack_entry.grid(row=self.playernum+2, column=1, padx=10, pady=10)
            self.startingstack_button.grid(row=self.playernum+2, column=2, padx=10, pady=10)

    def get_startingstack(self):
        self.validSS = False
        entry = self.startingstack_entry.get()
        if (entry.isdigit() and int(entry) > 0):
            self.startingstack_entry.config(bg='green')
            self.validSS = True
            self.startgame_button.grid(row=self.playernum+3, column=0, columnspan=3, padx=10, pady=10)
        else:
            self.startingstack_entry.config(bg='red')

    def initiate_game(self):
        self.root.destroy()

class PokerScreen():
    def __init__(self, pnum, pnames):
        self.root = Tk()
        self.title = "Poker Game"
        self.playernum = pnum
        self.playernames = pnames
        self.table_frame = Frame(self.root, bg="black")
        self.table_cards = []
        self.table_pot = Label(self.root, text="Pot: ")
        self.player_whole_frame = Frame(self.root)
        self.player_frames = []

        self.table_frame.grid(row=0, column=0, columnspan=5, padx=30, pady=30)
        
        #display card placements
        self.table_cards.append(Label(self.table_frame, text="Card1"))
        self.table_cards.append(Label(self.table_frame, text="Card2"))
        self.table_cards.append(Label(self.table_frame, text="Card3"))
        self.table_cards.append(Label(self.table_frame, text="Card4"))
        self.table_cards.append(Label(self.table_frame, text="Card5"))
        self.table_cards[0].grid(row=1, column=0, padx=5, pady=5)
        self.table_cards[1].grid(row=1, column=1, padx=5, pady=5)
        self.table_cards[2].grid(row=1, column=2, padx=5, pady=5)
        self.table_cards[3].grid(row=1, column=3, padx=5, pady=5)
        self.table_cards[4].grid(row=1, column=4, padx=5, pady=5)
        
        #display pot
        self.table_pot.grid(row=2, column=2, padx=10, pady=10)

        self.player_whole_frame.grid(row=0, column=0, columnspan=self.playernum, padx=30, pady=30)
        # Create frame for every player
        for name in self.playernames:
            self.player_frames.append(Frame(self.root, bg="black"))
        for x in range(self.playernum):
            self.player_frames[x].grid(row=1, column=x, padx=5, pady=5)


        # Frame + 2 Labels (Cards) + Button to show hand
        
        # Create Table
        # Automatically creates a deck
        table = Table(self.playernum)
        table.playerNames = self.playernames
        print("There are ", table.numPlayers, " playing. Their names are ", table.playerNames)
        # shuffle deck
        table.shuffleDeck()
        table.createDictionary()
        table.deal()
        table.printPlayerCards()
        
        """
        img1 = PhotoImage(file="PNG-cards-1.3/2_of_diamonds.png").subsample(3,3)
        Label(self.table_frame, image=img1).grid(row=1, column=0, padx=5, pady=5)
        img2 = PhotoImage(file="PNG-cards-1.3/3_of_diamonds.png").subsample(3,3)
        Label(self.table_frame, image=img2).grid(row=1, column=1, padx=5, pady=5)
        img3 = PhotoImage(file="PNG-cards-1.3/4_of_diamonds.png").subsample(3,3)
        Label(self.table_frame, image=img3).grid(row=1, column=2, padx=5, pady=5)
        #card_photo = PhotoImage(Image.open("/PNG-cards-1.3/2_of_diamonds.png"))
        #cpimage = card_photo.subsample(1, 2)
        #card = Label(self.table_frame, image=card_photo)
        #self.table_cards.append(card)
        #card.grid(row=1, column=0, padx=5, pady=5)
        """

        self.root.mainloop()


#start=StartScreen()
#setup=SetupScreen()
#playernames = setup.playernames
#playernum = setup.playernum
#game=PokerScreen(playernum, playernames)

#table = Table(3)

# Display Page
eel.init('web')

@eel.expose
def print_yolo():
    return 'yolo'

eel.start('index.html')



# Create Table, ask for names, shuffle the deck
table = Table(2)
table.askPlayerNames()
table.createDictionary()
table.shuffleDeck()

# Deal two cards to each player, evaluate hands
table.deal()
table.printPlayerCards()
table.findCombos()

# User press ENTER when done betting
table.askReady()

# Execute the FLOP, print all cards, evaluate
table.executeFlop()
table.printPlayerCards()
table.printCommunityCards()
table.findCombos()

# User press ENTER when done betting
table.askReady()

# Execute the TURN, print all cards, evaluate
table.executeTurn()
table.printPlayerCards()
table.printCommunityCards()
table.findCombos()

# User press ENTER when done betting
table.askReady()

# Execute the RIVER, print all cards, evaluate
table.executeRiver()
table.printPlayerCards()
table.printCommunityCards()
table.findCombos()

# Print winner and their combo value
table.printWinner()

input("Press ENTER to EXIT PROGRAM")