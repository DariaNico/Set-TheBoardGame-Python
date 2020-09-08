from tkinter import Button

class ToolTipButton:
    
    def __init__(self, root):
        self.button = Button(root, text="Turn on tooltips", command = lambda: self.on_off())
        self.is_on = False
    
    def on_off(self):
        if self.is_on:
            self.button['text'] = "Turn on tooltips"
            self.is_on = False
        else:
            self.button['text'] = "Turn off tooltips"
            self.is_on = True