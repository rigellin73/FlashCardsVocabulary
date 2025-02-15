import pandas
from random import choice

DATA_FILE = "dictionaries/sv_en.csv"
SOURCE_LANGUAGE_COLUMN = 0
TARGET_LANGUAGE_COLUMN = 1

class Data():
    def __init__(self):
        self.raw_data = pandas.read_csv(DATA_FILE)
        languages = list(self.raw_data.columns)
        self.source_language = languages[SOURCE_LANGUAGE_COLUMN]
        self.target_language = languages[TARGET_LANGUAGE_COLUMN]
        self.dictionary = self.raw_data.to_dict(orient="records")

    def get_random_pair(self):
        return choice(self.dictionary)
