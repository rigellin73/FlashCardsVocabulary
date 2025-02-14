import tkinter as tk

# Canvas settings
C_WIDTH = 800
C_HEIGHT = 526

# Background image settings
BGR_COLOR = "#B1DDC6"
BGR_FRONT = "images/card_front.png"
BGR_BACK = "images/card_back.png"

# Text settings
T_LANG_POSX = C_WIDTH / 2
T_LANG_POSY = 150
T_LANG_TEXT_FRONT = "Svenska"
T_LANG_TEXT_BACK = "English"
T_LANG_FONT = ("Arial", 40, "italic")

T_WORD_POSX = C_WIDTH / 2
T_WORD_POSY = 263
T_WORD_TEXT_DEFAULT = "Ord"
T_WORD_FONT = ("Arial", 60, "bold")

class FlashCard(tk.Canvas):
    def __init__(self):
        super().__init__()

        self.bgr_image_back = tk.PhotoImage(file=BGR_FRONT)

        self.config(width=C_WIDTH, height=C_HEIGHT, bg=BGR_COLOR, highlightthickness=0)
        self.create_image(C_WIDTH / 2, C_HEIGHT / 2, image=self.bgr_image_back)

        self.lang_text = self.create_text(T_LANG_POSX, T_LANG_POSY, text=T_LANG_TEXT_FRONT, font=T_LANG_FONT)
        self.word_text = self.create_text(T_WORD_POSX, T_WORD_POSY, text=T_WORD_TEXT_DEFAULT, font=T_WORD_FONT)
