from tkinter import *
import GameLogic
import ScoreBoard
from playsound import playsound
import ToolTip
import ToolTipButton
from functools import partial

GameLogic = GameLogic.GameLogic
ScoreBoard = ScoreBoard.ScoreBoard
ToolTip = ToolTip.ToolTip
ToolTipButton = ToolTipButton.ToolTipButton

class Gui:
    def __init__(self):
        self.cards = []
        self.buttons = []
        self.num_columns = 4
        self.num_cards = 12
        self.root = Tk()
        self.root.title("Best SET Game Ever By: The Truffle Oil Crew")
        self.scoreboard_frame = ScoreBoard(self.root)
        self.game_frame = Frame(self.root)
        self.game_frame.pack(side = TOP)
        self.control_frame = Frame(self.root)
        self.control_frame.pack(side = BOTTOM)
        self.ttb = ToolTipButton(self.root)
        self.tooltip = ToolTip()
        self.game_logic = GameLogic()

    # Adds cards to play board.
    # Parameter: List of 12 or 15 cards.
    def place_cards_on_board(self, cards):
        self.cards = cards
        if len(cards) == 12:
            self.num_cards = 12
            self.num_columns = 4
        elif len(cards) == 15:
            self.num_cards = 15
            self.num_columns = 5
        self.create_buttons()
        
    def set_up_control_buttons(self):
        new_game_button = Button(self.control_frame, text = "New Game", command = lambda: self.new_game())
        new_game_button.pack(side = RIGHT)
        quit_button = Button(self.control_frame, text = "Quit", command = lambda: self.root.destroy())
        quit_button.pack(side = LEFT)
        self.ttb = ToolTipButton(self.control_frame)
        self.ttb.button.pack(side=LEFT)

    def selected(self, button_id):
        playsound('Sounds/CardSound.wav')
        button_text = self.buttons[button_id]['text']
        self.buttons[button_id]['text'] = f"{button_text} selected"
        if (self.game_logic.cards_in_play[button_id] in self.game_logic.selected):
            self.game_logic.selected.remove(self.game_logic.cards_in_play[button_id])
            self.buttons[button_id]['bg'] = 'SystemButtonFace'
        else: 
            self.game_logic.selected.append(self.cards[button_id])
            self.buttons[button_id]['bg'] = 'SkyBlue1'
        for i in range(0, len(self.game_logic.selected)):
            print(self.game_logic.selected[i].color)
            
        if len(self.game_logic.selected) == 3:
                self.game_logic.check_selected_cards()
                self.next_board()
        
    def create_buttons(self):
        # Adding the buttons in a loop in the way below results in all the lambda events to recieve the last index
        # for i in range(0,num_cards):
        #     buttonId = i
        #     button = tk.Button(window, text = f"test button {i}", command = lambda: thanks(i))
        #     buttons.append(button)

        # So I need to do it manually for now
        window = self.game_frame
        cards = self.cards
        self.buttons = []
        for i in range(0,self.num_cards):
            image = PhotoImage(file = f"CardImages/{cards[i].color} {cards[i].fill} {cards[i].shape}{cards[i].number}.gif")
            self.buttons.append(Button(window, image = image, command = lambda i=i: self.selected(i), highlightbackground='#3E4149'))
            self.buttons[i].image = image
            self.buttons[i].bind('<Enter>', lambda event, i=i : self.show_tooltip(i))
            self.buttons[i].bind('<Leave>', self.hide_tooltip)
            
    def show_tooltip(self, id):
        card = self.cards[id]
        print("in show tooltip")
        if self.ttb.is_on:
            self.tooltip.show_tooltip(f"{card.color}\n{card.fill}\n{card.shape}\n{card.number}", self.root.winfo_pointerx(), self.root.winfo_pointery())
            
    def hide_tooltip(self, event):
        print("in hide_tooltip")
        if self.ttb.is_on:
            self.tooltip.hide_tooltip()
            
    def next_board(self):
        self.wipe_board()
        self.scoreboard_frame.update_score(len(self.game_logic.successful_set_pile))
        self.place_cards_on_board(self.game_logic.cards_in_play)
        self.create_grid(self.buttons, self.cards)
        
    def new_game(self):
        playsound('Sounds/MenuSelect.wav')
        self.wipe_board()
        self.start_game()
        
    def wipe_board(self):
        for button in self.buttons:
            button.grid_forget()
        
    def start_game(self):
        #Configure window and label
        self.game_logic.new_game()
        self.scoreboard_frame.update_score(len(self.game_logic.successful_set_pile))
        self.place_cards_on_board(self.game_logic.cards_in_play)
        self.create_grid(self.buttons, self.cards)

        self.root.mainloop()
        
    def create_grid(self, buttons, cards):
        for i in range(0, self.num_cards):
            row = int(i / self.num_columns) + 1
            column = int(i % self.num_columns)
            self.buttons[i].grid(row = row, column = column)

gui = Gui()
gui.set_up_control_buttons()
gui.start_game()