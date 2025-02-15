from main_window import MainWindow
from data import Data

main_window = MainWindow()
flash_card = main_window.flash_card

data = Data()

words_pair = data.get_random_pair()
flash_card.set_words_pair(words_pair)

main_window.window.mainloop()
