import tkinter as tk

# Canvas settings
C_WIDTH = 800
C_HEIGHT = 526

# Background image settings
BGR_COLOR = "#B1DDC6"
BGR_FRONT = "images/card_front.png"
BGR_BACK = "images/card_back.png"

class FlashCard(tk.Canvas):
    def __init__(self):
        super().__init__()

        self.bgr_image_back = tk.PhotoImage(file=BGR_FRONT)

        self.config(width=C_WIDTH, height=C_HEIGHT, bg=BGR_COLOR, highlightthickness=0)
        self.create_image(C_WIDTH / 2, C_HEIGHT / 2, image=self.bgr_image_back)
