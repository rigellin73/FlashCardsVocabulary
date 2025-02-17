import pandas
from random import choice

DATA_FILE = "dictionaries/sv_en.csv"
TO_LEARN_FILE = "dictionaries/words_to_learn.csv"
SOURCE_LANG_COLUMN_ID = 0
TARGET_LANG_COLUMN_ID = 1
NUMBER_OF_WORDS = 10

class Data:
    def __init__(self):
        try:
            self.raw_data = pandas.read_csv(TO_LEARN_FILE)
        except FileNotFoundError:
            self.raw_data = pandas.read_csv(DATA_FILE).head(NUMBER_OF_WORDS)
        languages = list(self.raw_data.columns)
        self.source_language = languages[SOURCE_LANG_COLUMN_ID]
        self.target_language = languages[TARGET_LANG_COLUMN_ID]
        self.dictionary = self.raw_data.to_dict(orient="records")
        print(self.dictionary)

    def get_random_pair(self):
        return choice(self.dictionary)
