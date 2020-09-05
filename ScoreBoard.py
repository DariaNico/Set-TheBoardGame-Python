from tkinter import *

class ScoreBoard:
    
    def __init__(self, root):
        self.score = 0
        self.scoreboard_frame = Frame(root)
        self.scoreboard_frame.pack(side =TOP)
        self.scoreboard = Label(self.scoreboard_frame, text = self.score)
        self.scoreboard.pack(side = TOP)
        
    def add_point(self):
        self.score = self.score + 1
        self.scoreboard['text'] = self.score
        
    def reset_score(self):
        self.score = 0
        self.scoreboard['text'] = self.score