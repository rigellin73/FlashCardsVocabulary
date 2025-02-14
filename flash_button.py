import tkinter as tk
from PIL import Image, ImageTk
from flash_card import BGR_COLOR

class FlashButton(tk.Button):
    def __init__(self, bgr_image_path):
        super().__init__()

        self.bgr_image = ImageTk.PhotoImage(Image.open(bgr_image_path))

        self.config(image=self.bgr_image, highlightthickness=0, command=self.btn_clicked)
        self.image = self.bgr_image

    def btn_clicked(self):
        print("Button clicked")
