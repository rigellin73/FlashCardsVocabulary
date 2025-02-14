import tkinter as tk

# Window settings
W_TITLE = "Flashy"
W_PADX = 50
W_PADY = 50

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(W_TITLE)
        self.window.config(padx=W_PADX, pady=W_PADY)
