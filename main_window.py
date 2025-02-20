import tkinter as tk
from PIL import Image, ImageTk
from flash_card import FlashCard, BGR_COLOR
from data import Data

# Window settings
W_TITLE = "Flashy"
W_PADX = 50
W_PADY = 50
W_WAIT_TIME = 3000

# Button images
B_BGR_CHECK = "images/right.png"
B_BGR_X = "images/wrong.png"

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(W_TITLE)
        self.window.config(padx=W_PADX, pady=W_PADY, bg=BGR_COLOR)

        self.flash_card = FlashCard()

        self.btn_check_bgr = ImageTk.PhotoImage(Image.open(B_BGR_CHECK))
        self.btn_check = tk.Button(image=self.btn_check_bgr, highlightthickness=0, command=self.btn_check_clicked)

        self.btn_x_bgr = ImageTk.PhotoImage(Image.open(B_BGR_X))
        self.btn_x = tk.Button(image=self.btn_x_bgr, highlightthickness=0, command=self.btn_x_clicked)

        self.flash_card.grid(row=0, column=0, columnspan=2)
        self.btn_x.grid(row=1, column=0)
        self.btn_check.grid(row=1, column=1)

        self.data = Data()
        self.current_pair = []
        self.timer_action = None

        self.get_new_card()

        self.window.mainloop()

    def get_new_card(self):
        if self.timer_action:
            self.window.after_cancel(self.timer_action)
        if self.data.has_words():
            self.current_pair = self.data.get_random_pair()
            self.flash_card.set_words_pair(self.current_pair)
            self.timer_action = self.window.after(W_WAIT_TIME, self.flash_card.flip_card)
        else:
            self.flash_card.set_endcard()
            self.btn_check.config(state="disabled")
            self.btn_x.config(state="disabled")

    def btn_x_clicked(self):
        self.get_new_card()

    def btn_check_clicked(self):
        self.data.remove_pair(self.current_pair)
        self.get_new_card()
