import tkinter as tk
from flash_card import FlashCard, BGR_COLOR
from flash_button import FlashButton
from data import Data

# Window settings
W_TITLE = "Flashy"
W_PADX = 50
W_PADY = 50
W_WAIT_TIME = 3000

# Button images
B_BGR_RIGHT = "images/right.png"
B_BGR_WRONG = "images/wrong.png"

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(W_TITLE)
        self.window.config(padx=W_PADX, pady=W_PADY, bg=BGR_COLOR)

        self.flash_card = FlashCard()

        self.btn_right = FlashButton(B_BGR_RIGHT, command=self.btn_clicked)
        self.btn_wrong = FlashButton(B_BGR_WRONG, command=self.btn_clicked)

        self.flash_card.grid(row=0, column=0, columnspan=2)
        self.btn_wrong.grid(row=1, column=0)
        self.btn_right.grid(row=1, column=1)

        self.data = Data()
        self.timer_action = None

    def get_new_card(self):
        self.flash_card.set_words_pair(self.data.get_random_pair())
        self.timer_action = self.window.after(W_WAIT_TIME, self.flash_card.flip_card)

    def btn_clicked(self):
        self.window.after_cancel(self.timer_action)
        self.get_new_card()
