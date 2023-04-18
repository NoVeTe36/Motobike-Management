import tkinter as tk
import time

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.background = self['bg']
        self.bind("<Enter>", self.hover)
        self.bind("<Leave>", self.leave)

    def hover(self, e):
        self['bg'] = self['activebackground']
    def leave(self, e):
        self['bg'] = self.background

def clearFrame(contentFrame):
    for widget in contentFrame.winfo_children():
        widget.destroy()

def move_in(move_Frame):
    x = -50
    while x <= 60:
        move_Frame.place(x=x, y= 60)
        x += 1
        time.sleep(0.01)
        move_Frame.update()
    move_Frame.place(x=60, y=60)
