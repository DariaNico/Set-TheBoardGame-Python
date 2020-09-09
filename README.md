# Requirements to Run This Game
Python Version: 3.7.3
Pip Version: 20.2.2

IMPORTANT: To play this game:
- Install Python (we developed this on 3.7.3)
- Install pip (19.0.3 or newer)
- run `pip install -r requirements.txt` in the terminal to install the necessary packages
- Run the Gui.py file (navigate to folder containing Gui.py and run `python .\Gui.py` in terminal) to start the game.

Rules of the game are viewable at:
http://magliery.com/Set/SetRules.html#:~:text=Players%20do%20not%20take%20turns,the%20player%20loses%20one%20point.

Visual indication of selected cards only works on Windows, sorry Mac users. Also, there are sound effects, but if your playsound for python isn't installed correctly, it will make the game unplayable, so it is commented out by default. To enable sound, uncomment all lines in Gui.py that are marked with: #TODO Uncomment this if you want sound

Known bugs: 
- If you have tooltips turned on and select Card A and then Card B, and then deselect Card A, Card B's tooltip will disappear.
- If you win or lose the game, you can still select cards until you hit New Game, possibly causing odd visual effects or multiple win/lose screens to open.
- Visual selection indication doesn't work on Mac because Mac. :(

# SetAssignment
Things we will need to do:

--Develop a process for determining if 3 cards form a set
  
--Develop a process for displaying either 12 or 15 cards in a Grid
  
--We will need to be able to interact with the cards...to select 3
  
--For the game itself, we will need to be able to start a new game, let the user select 3 cards, check to see if the 3 cards form a set:  if so, remove the cards and insert new cards from the deck.  if not, clear the card selection and indicate that the selection did not form a set
  
--Once the deck is empty, and no sets are possible, end the game
  
--Track things like time, number of sets found, etc...

For Topics I students: the expectation is that a basic game can be played

For Topics II students: the expectation is that a basic game can be played, and statistics can be tracked and displayed.  Additional features are appreciated.

You should be able to explain your decisions regarding game mechanics.  What process did you use to display your cards? What process did you use to determine if the 3 cards form a set? 

We will play each other's games and provide feedback
=======
# Intro-to-Game-Dev-Set-in-Python
Coding up our take on the Set board game in Python

# Class Github Organization
https://github.com/UICS-Game-Dev

# Professor Szecei Github Account
https://github.com/szecsei