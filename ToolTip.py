from tkinter import *

class ToolTip: 
        
    def show_tooltip(self, text, x, y):
        self.window = Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_geometry(f"+{x}+{y}")
        self.label = Label(self.window, borderwidth=1, relief = 'solid')
        self.label['text'] = text
        
        self.label.pack()
        
    def hide_tooltip(self):
        self.label.destroy()
        self.window.destroy()