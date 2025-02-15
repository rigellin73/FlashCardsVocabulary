import tkinter as tk
from flash_card import FlashCard, BGR_COLOR
from flash_button import FlashButton
from data import Data

# Window settings
W_TITLE = "Flashy"
W_PADX = 50
W_PADY = 50

# Button images
B_BGR_RIGHT = "images/right.png"
B_BGR_WRONG = "images/wrong.png"

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(W_TITLE)
        self.window.config(padx=W_PADX, pady=W_PADY, bg=BGR_COLOR)

        self.flash_card = FlashCard()

        self.btn_right = FlashButton(B_BGR_RIGHT, command=self.get_new_card)
        self.btn_wrong = FlashButton(B_BGR_WRONG, command=self.get_new_card)

        self.flash_card.grid(row=0, column=0, columnspan=2)
        self.btn_wrong.grid(row=1, column=0)
        self.btn_right.grid(row=1, column=1)

        self.data = Data()

    def get_new_card(self):
        self.flash_card.set_words_pair(self.data.get_random_pair())
