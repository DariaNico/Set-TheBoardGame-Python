from tkinter import *

class ToolTip: 
    
    def __init__(self):
        self.is_showing = False
        self.windows = []
        
    def show_tooltip(self, text, x, y):
        self.window = Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_geometry(f"+{x}+{y}")
        self.label = Label(self.window, borderwidth=1, relief = 'solid')
        self.label['text'] = text
        self.is_showing = True
        self.windows.append(self.window)
        
        self.label.pack()
        
    def hide_tooltip(self, index):
        self.is_showing = False
        self.windows[index].destroy()
        self.windows.pop(index)
    
    def wipe_all(self):
        if self.windows:
            for i in range(0, len(self.windows)-1):
                self.hide_tooltip(i)