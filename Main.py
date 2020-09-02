import tkinter as tk
import Card
import Deck

Card = Card.Card
Deck = Deck.Deck

mCards = []
buttons = []

# Adds cards to play board.
# Parameter: List of 9 cards.
def place_cards_on_board(cards):
    global mCards 
    mCards = cards
    
    start_game()

# Performs GUI reaction to one of the cards being selected and fires method to inform game 
# logic which item was chosen
# TODO call method in game logic, should be able to identify with buttonId which matches the index of the card
def selected(buttonId):
    buttons[buttonId]['text'] = "selected"
    
def create_grid(buttons, cards):
    for i in range(0,9):
        buttons[i].grid(row = int(i/3)+1, column = int(i%3))
    
def start_game():
    global buttons
    
    #Configure window and label
    window = tk.Tk()
    window.title("GUI")
    label = tk.Label(window, text = "First window")
    label.grid(row=0, column=0)
    
    #Below is for manually entering cards for testing. #TODO remove when ready
    # deck = Deck()
    # deck.shuffle()
    # cards = []
    # for i in range(0,9):
    #     cards.append(deck.getCard(i))
    #     print(cards[i].getColor())
    # place_cards_on_board(cards)

    # Adding the buttons in a loop in the way below results in all the lambda events to recieve the last index
    # for i in range(0,9):
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
        tk.Button(window, text = mCards[8].color, command = lambda: selected(8))
    ]

    create_grid(buttons, mCards)

    window.mainloop()