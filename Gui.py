from tkinter import *
import Card
import Deck
import GameLogic
import ScoreBoard

GameLogic = GameLogic.GameLogic
Card = Card.Card
Deck = Deck.Deck
ScoreBoard = ScoreBoard.ScoreBoard

class Gui:
    def __init__(self):
        self.cards = []
        self.buttons = []
        self.num_rows = 3
        self.num_columns = 4
        self.num_cards = 12
        self.root = Tk()
        self.root.title("Best SET Game Ever By: The Truffle Oil Crew")
        self.scoreboard_frame = ScoreBoard(self.root)
        self.game_frame = Frame(self.root)
        self.game_frame.pack(side = TOP)
        self.control_frame = Frame(self.root)
        self.control_frame.pack(side = BOTTOM)
        self.game_logic = GameLogic()

    # Adds cards to play board.
    # Parameter: List of 12 or 15 cards.
    def place_cards_on_board(self, cards, num_rows, num_columns):
        
        num_cards = len(cards)
        if num_cards != 12 and num_cards != 15:
            raise Exception(f"Must place 12 or 15 cards. Placed {num_cards} cards.")
        self.define_board(num_cards, num_rows, num_columns)
        
        self.cards = cards
        self.create_buttons()
        
    def set_up_quit_button(self):
        quit_button = Button(self.control_frame, text = "Quit", command = lambda: self.root.destroy())
        quit_button.pack(side = LEFT)
        
    def set_up_new_game_button(self):
        new_game_button = Button(self.control_frame, text = "New Game", command = lambda: self.new_game())
        new_game_button.pack(side = RIGHT)

    # Performs GUI reaction to one of the cards being selected and fires method to inform game 
    # logic which item was chosen
    # TODO call method in game logic, should be able to identify with buttonId which matches the index of the card
    def selected(self, button_id):
        button_text = self.buttons[button_id]['text']
        self.buttons[button_id]['text'] = f"{button_text} selected"
        self.game_logic.selected.append(self.cards[button_id])
        for i in range(0, len(self.game_logic.selected)):
            print(self.game_logic.selected[i].color)
            
        if len(self.game_logic.selected) == 3:
                self.game_logic.check_selected_cards()
                self.scoreboard_frame.add_point()
                self.next_board()
        
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
        window = self.game_frame
        cards = self.cards
        images = []
        for i in range(0,self.num_cards):
            images.append(PhotoImage(file = f"CardImages/{cards[i].color} {cards[i].fill} {cards[i].shape}{cards[i].number}.gif"))
        self.buttons = [
            Button(window, image = images[0], command = lambda: self.selected(0)),
            Button(window, image = images[1], command = lambda: self.selected(1)),
            Button(window, image = images[2], command = lambda: self.selected(2)),
            Button(window, image = images[3], command = lambda: self.selected(3)),
            Button(window, image = images[4], command = lambda: self.selected(4)),
            Button(window, image = images[5], command = lambda: self.selected(5)),
            Button(window, image = images[6], command = lambda: self.selected(6)),
            Button(window, image = images[7], command = lambda: self.selected(7)),
            Button(window, image = images[8], command = lambda: self.selected(8)),
            Button(window, image = images[9], command = lambda: self.selected(9)),
            Button(window, image = images[10], command = lambda: self.selected(10)),
            Button(window, image = images[11], command = lambda: self.selected(11))
        ]
        if (self.num_cards == 15):
            self.buttons.append(Button(window, image = images[12], command = lambda: self.selected(12)))
            self.buttons.append(Button(window, image = images[13], command = lambda: self.selected(13)))
            self.buttons.append(Button(window, image = images[14], command = lambda: self.selected(14)))
        for i in range(0,self.num_cards):
            self.buttons[i].image = images[i]
            
    def next_board(self):
        self.wipe_board()
        self.place_cards_on_board(self.game_logic.cards_in_play, 3, 4)
        self.create_grid(self.buttons, self.cards)
        
    def new_game(self):
        self.wipe_board()
        self.game_logic = GameLogic()
        self.scoreboard_frame.reset_score()
        self.start_game()
        
    def wipe_board(self):
        for button in self.buttons:
            button.grid_forget()
        
    def start_game(self):
        
        #Configure window and label
        self.game_logic.start_game(12)
        self.place_cards_on_board(self.game_logic.cards_in_play, 3, 4)
        self.create_grid(self.buttons, self.cards)

        self.root.mainloop()
        
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
        
gui = Gui()
gui.set_up_quit_button()
gui.set_up_new_game_button()
gui.start_game()