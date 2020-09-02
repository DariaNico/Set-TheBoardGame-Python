import tkinter as tk
import Card
import Deck

Card = Card.Card
Deck = Deck.Deck

class Gui:
    def __init__(self):
        self.cards = []
        self.buttons = []
        self.num_rows = 3
        self.num_columns = 4
        self.num_cards = 12
        self.window = tk.Tk()

    # Adds cards to play board.
    # Parameter: List of 12 or 15 cards.
    def place_cards_on_board(self, cards, num_rows, num_columns):
        
        num_cards = len(cards)
        if(num_cards != 12 and num_cards != 15):
            raise Exception(f"Must place 12 or 15 cards. Placed {num_cards} cards.")
        
        self.define_board(num_cards, num_rows, num_columns)
        
        self.cards = cards
        self.create_buttons()
        self.start_game()

    # Performs GUI reaction to one of the cards being selected and fires method to inform game 
    # logic which item was chosen
    # TODO call method in game logic, should be able to identify with buttonId which matches the index of the card
    def selected(self, button_id):
        self.buttons[button_id]['text'] = "selected"
        
    # Configure number of cards, rows, and columns the board will contain.
    def define_board(self, num_cards, num_rows, num_columns):
        self.num_cards = num_cards
        self.num_rows = num_rows
        self.num_columns = num_columns
        
    def create_buttons(self):
        # Adding the buttons in a loop in the way below results in all the lambda events to recieve the last index
        # for i in range(0,num_cards):
        #     buttonId = i
        #     button = tk.Button(window, text = f"test button {i}", command = lambda: thanks(i))
        #     buttons.append(button)

        # So I need to do it manually for now
        window = self.window
        cards = self.cards
        self.buttons = [
            tk.Button(window, text = cards[0].color, command = lambda: self.selected(0)),
            tk.Button(window, text = cards[1].color, command = lambda: self.selected(1)),
            tk.Button(window, text = cards[2].color, command = lambda: self.selected(2)),
            tk.Button(window, text = cards[3].color, command = lambda: self.selected(3)),
            tk.Button(window, text = cards[4].color, command = lambda: self.selected(4)),
            tk.Button(window, text = cards[5].color, command = lambda: self.selected(5)),
            tk.Button(window, text = cards[6].color, command = lambda: self.selected(6)),
            tk.Button(window, text = cards[7].color, command = lambda: self.selected(7)),
            tk.Button(window, text = cards[8].color, command = lambda: self.selected(8)),
            tk.Button(window, text = cards[9].color, command = lambda: self.selected(9)),
            tk.Button(window, text = cards[10].color, command = lambda: self.selected(10)),
            tk.Button(window, text = cards[11].color, command = lambda: self.selected(11))
        ]
        if (self.num_cards == 15):
            self.buttons.append(tk.Button(window, text = cards[12].color, command = lambda: self.selected(12)))
            self.buttons.append(tk.Button(window, text = cards[13].color, command = lambda: self.selected(13)))
            self.buttons.append(tk.Button(window, text = cards[14].color, command = lambda: self.selected(14)))
        
    def start_game(self):
        
        #Configure window and label
        self.window.title("GUI")
        label = tk.Label(self.window, text = "First window")
        label.grid(row=0, column=0)
        self.create_grid(self.buttons, self.cards)

        self.window.mainloop()
        
    def create_grid(self,buttons, cards):
        for i in range(0,self.num_cards):
            row = int(i/self.num_columns)+1
            column = int(i%self.num_columns)
            self.buttons[i].grid(row = row, column = column)

    # For testing during development 
    #TODO remove or make a separate test file when ready
    def self_test(self, num_cards, num_rows, num_columns):
        deck = Deck()
        deck.shuffle()
        cards = []
        for i in range(0,num_cards):
            cards.append(deck.getCard(i))
            print(f"{i}: {cards[i].getColor()}")
        self.place_cards_on_board(cards, num_rows, num_columns)