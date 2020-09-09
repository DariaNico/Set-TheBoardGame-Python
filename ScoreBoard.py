from tkinter import *

class ScoreBoard:
    
    def __init__(self, root):
        self.scoreboard_frame = Frame(root)
        self.scoreboard_frame.pack(side =TOP)
        Label(self.scoreboard_frame, text = "Set Count:").pack(side = TOP)
        self.scoreboard = Label(self.scoreboard_frame)
        self.scoreboard.pack(side = TOP)
        
    def update_score(self, score):
        self.scoreboard['text'] = score