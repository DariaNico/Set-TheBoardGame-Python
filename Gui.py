import tkinter as tk
import Card
import Deck

Card = Card.Card
Deck = Deck.Deck

mCards = []
buttons = []
mNum_rows = 3
mNum_columns = 4
mNum_cards = 12
window = tk.Tk()

# Adds cards to play board.
# Parameter: List of 12 or 15 cards.
def place_cards_on_board(cards):
    if(len(cards)!= 12 and len(cards)!= 15):
        raise Exception(f"Must place 12 or 15 cards. Placed {len(cards)} cards.")
    
    global mCards 
    mCards = cards
    create_buttons()
    start_game()

# Performs GUI reaction to one of the cards being selected and fires method to inform game 
# logic which item was chosen
# TODO call method in game logic, should be able to identify with buttonId which matches the index of the card
def selected(button_id):
    buttons[button_id]['text'] = "selected"
    
# Configure number of cards, rows, and columns the board will contain.
def define_board(num_cards, num_rows, num_columns):
    global mNum_cards
    global mNum_rows
    global mNum_columns
    mNum_cards = num_cards
    mNum_rows = num_rows
    mNum_columns = num_columns
    
def create_buttons():
    global buttons
    # Adding the buttons in a loop in the way below results in all the lambda events to recieve the last index
    # for i in range(0,mNum_cards):
    #     buttonId = i
    #     button = tk.Button(window, text = f"test button {i}", command = lambda: thanks(i))
    #     buttons.append(button)

    # So I need to do it manually for now
    buttons = [
        tk.Button(window, text = mCards[0].color, command = lambda: selected(0)),
        tk.Button(window, text = mCards[1].color, command = lambda: selected(1)),
        tk.Button(window, text = mCards[2].color, command = lambda: selected(2)),
        tk.Button(window, text = mCards[3].color, command = lambda: selected(3)),
        tk.Button(window, text = mCards[4].color, command = lambda: selected(4)),
        tk.Button(window, text = mCards[5].color, command = lambda: selected(5)),
        tk.Button(window, text = mCards[6].color, command = lambda: selected(6)),
        tk.Button(window, text = mCards[7].color, command = lambda: selected(7)),
        tk.Button(window, text = mCards[8].color, command = lambda: selected(8)),
        tk.Button(window, text = mCards[9].color, command = lambda: selected(9)),
        tk.Button(window, text = mCards[10].color, command = lambda: selected(10)),
        tk.Button(window, text = mCards[11].color, command = lambda: selected(11))
    ]
    if (mNum_cards == 15):
        buttons.append(tk.Button(window, text = mCards[12].color, command = lambda: selected(12)))
        buttons.append(tk.Button(window, text = mCards[13].color, command = lambda: selected(13)))
        buttons.append(tk.Button(window, text = mCards[14].color, command = lambda: selected(14)))
    
    
def create_grid(buttons, cards):
    for i in range(0,mNum_cards):
        row = int(i/mNum_columns)+1
        column = int(i%mNum_columns)
        buttons[i].grid(row = row, column = column)
        
def start_game():
    global buttons
    
    #Configure window and label
    window.title("GUI")
    label = tk.Label(window, text = "First window")
    label.grid(row=0, column=0)
    create_grid(buttons, mCards)

    window.mainloop()

# For testing during development 
#TODO remove or make a separate test file when ready
def self_test(num_cards, num_rows, num_columns):
    define_board(num_cards, num_rows, num_columns)
    deck = Deck()
    deck.shuffle()
    cards = []
    for i in range(0,mNum_cards):
        cards.append(deck.getCard(i))
        print(f"{i}: {cards[i].getColor()}")
    place_cards_on_board(cards)