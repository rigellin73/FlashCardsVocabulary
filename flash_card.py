import tkinter as tk
import config as cfg

class FlashCard(tk.Canvas):
    def __init__(self):
        super().__init__()

        self.bgr_image_front = tk.PhotoImage(file=cfg.C_BGR_FRONT)
        self.bgr_image_back = tk.PhotoImage(file=cfg.C_BGR_BACK)

        self.config(width=cfg.C_WIDTH, height=cfg.C_HEIGHT, bg=cfg.BGR_COLOR, highlightthickness=0)
        self.canvas_image = self.create_image(cfg.C_WIDTH / 2, cfg.C_HEIGHT / 2, image=self.bgr_image_front)

        self.lang_text = self.create_text(cfg.T_LANG_POSX, cfg.T_LANG_POSY, font=cfg.T_LANG_FONT)
        self.word_text = self.create_text(cfg.T_WORD_POSX, cfg.T_WORD_POSY, font=cfg.T_WORD_FONT, width=cfg.T_WORD_WIDTH)

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
            self.itemconfig(self.lang_text, text=self.front_lang, fill=cfg.T_FILL_FRONT)
            self.itemconfig(self.word_text, text=self.front_word, fill=cfg.T_FILL_FRONT)
            self.itemconfig(self.canvas_image, image=self.bgr_image_front)
        else:
            self.itemconfig(self.lang_text, text=self.back_lang, fill=cfg.T_FILL_BACK)
            self.itemconfig(self.word_text, text=self.back_word, fill=cfg.T_FILL_BACK)
            self.itemconfig(self.canvas_image, image=self.bgr_image_back)

    def set_endcard(self):
        self.itemconfig(self.lang_text, text=cfg.T_LANG_ENDCARD, fill=cfg.T_FILL_FRONT)
        self.itemconfig(self.word_text, text=cfg.T_WORD_ENDCARD, fill=cfg.T_FILL_FRONT, font=cfg.T_WORD_ENDCARD_FONT)
        self.itemconfig(self.canvas_image, image=self.bgr_image_front)
