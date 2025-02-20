import tkinter as tk

# Canvas settings
C_WIDTH = 800
C_HEIGHT = 526

# Background image settings
BGR_COLOR = "#B1DDC6"
BGR_FRONT = "images/card_front.png"
BGR_BACK = "images/card_back.png"

# Text settings
T_FILL_FRONT = "black"
T_FILL_BACK = "white"
T_LANG_POSX = C_WIDTH / 2
T_LANG_POSY = 150
T_LANG_FONT = ("Arial", 40, "italic")
T_LANG_ENDCARD = "Congratulations!"

T_WORD_POSX = C_WIDTH / 2
T_WORD_POSY = 263
T_WORD_WIDTH = C_WIDTH - 20
T_WORD_FONT = ("Arial", 60, "bold")
T_WORD_ENDCARD = "You've learned all words"
T_WORD_ENDCARD_FONT = ("Arial", 40, "bold")

class FlashCard(tk.Canvas):
    def __init__(self):
        super().__init__()

        self.bgr_image_front = tk.PhotoImage(file=BGR_FRONT)
        self.bgr_image_back = tk.PhotoImage(file=BGR_BACK)

        self.config(width=C_WIDTH, height=C_HEIGHT, bg=BGR_COLOR, highlightthickness=0)
        self.canvas_image = self.create_image(C_WIDTH / 2, C_HEIGHT / 2, image=self.bgr_image_front)

        self.lang_text = self.create_text(T_LANG_POSX, T_LANG_POSY, font=T_LANG_FONT)
        self.word_text = self.create_text(T_WORD_POSX, T_WORD_POSY, font=T_WORD_FONT, width=T_WORD_WIDTH)

        self.front_lang = "Source Language"
        self.front_word = "Source word"
        self.back_lang = "Target Language"
        self.back_word = "Target word"
        self.front_side = True
        self.setup_card()

    def set_words_pair(self, pair):
        for index, key in enumerate(pair):
            if index == 0:
                self.front_lang = key
                self.front_word = pair[key]
            else:
                self.back_lang = key
                self.back_word = pair[key]

        self.front_side = True
        self.setup_card()

    def flip_card(self):
        self.front_side = False
        self.setup_card()

    def setup_card(self):
        if self.front_side:
            self.itemconfig(self.lang_text, text=self.front_lang, fill=T_FILL_FRONT)
            self.itemconfig(self.word_text, text=self.front_word, fill=T_FILL_FRONT)
            self.itemconfig(self.canvas_image, image=self.bgr_image_front)
        else:
            self.itemconfig(self.lang_text, text=self.back_lang, fill=T_FILL_BACK)
            self.itemconfig(self.word_text, text=self.back_word, fill=T_FILL_BACK)
            self.itemconfig(self.canvas_image, image=self.bgr_image_back)

    def set_endcard(self):
        self.itemconfig(self.lang_text, text=T_LANG_ENDCARD, fill=T_FILL_FRONT)
        self.itemconfig(self.word_text, text=T_WORD_ENDCARD, fill=T_FILL_FRONT, font=T_WORD_ENDCARD_FONT)
        self.itemconfig(self.canvas_image, image=self.bgr_image_front)
