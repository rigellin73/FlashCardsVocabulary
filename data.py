import pandas
from random import choice
import config as cfg

class Data:
    def __init__(self):
        try:
            self.raw_data = pandas.read_csv(cfg.TO_LEARN_FILE)
        except FileNotFoundError:
            self.raw_data = pandas.read_csv(cfg.DATA_FILE).head(cfg.NUMBER_OF_WORDS)
        languages = list(self.raw_data.columns)
        self.source_language = languages[cfg.SOURCE_LANG_COLUMN_ID]
        self.target_language = languages[cfg.TARGET_LANG_COLUMN_ID]
        self.dictionary = self.raw_data.to_dict(orient="records")

    def get_random_pair(self):
        return choice(self.dictionary)

    def remove_pair(self, pair):
        i = self.raw_data[(self.raw_data[self.source_language] == pair[self.source_language])].index
        self.raw_data.drop(i, inplace=True)
        self.dictionary.remove(pair)
        self.raw_data.to_csv(cfg.TO_LEARN_FILE, index=False)

    def has_words(self):
        return len(self.dictionary) > 0
