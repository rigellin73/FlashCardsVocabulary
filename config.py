# Data settings
DATA_FILE = "dictionaries/sv_en.csv"
TO_LEARN_FILE = "dictionaries/words_to_learn.csv"
SOURCE_LANG_COLUMN_ID = 0
TARGET_LANG_COLUMN_ID = 1
NUMBER_OF_WORDS = 10

# Window settings
W_TITLE = "Flashy"
W_PADX = 50
W_PADY = 50
W_WAIT_TIME = 3000
BGR_COLOR = "#B1DDC6"

# Button images
B_BGR_CHECK = "images/right.png"
B_BGR_X = "images/wrong.png"

# Canvas settings
C_WIDTH = 800
C_HEIGHT = 526

# Background image settings
C_BGR_FRONT = "images/card_front.png"
C_BGR_BACK = "images/card_back.png"

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
