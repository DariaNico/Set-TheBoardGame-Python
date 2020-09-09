from tkinter import *

class ScoreBoard:
    
    def __init__(self, root):
        self.scoreboard_frame = Frame(root)
        self.scoreboard_frame.pack(side =TOP)
        Label(self.scoreboard_frame, text = "Set Count:").pack(side = TOP)
        self.scoreboard = Label(self.scoreboard_frame)
        self.scoreboard.pack(side = TOP)
        
    def update_score(self, score):
        if score == 23:
            self.scoreboard['text'] = f"{score} - one set needed to win. Careful, if you fail this round you lose!"
        else:
            self.scoreboard['text'] = score