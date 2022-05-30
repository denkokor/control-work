
class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []

    def count_used_words(self):

        return len(self.used_words)

    def add_word(self, word):

        self.used_words.append(word)

    def has_newer_seen(self, word):

        return word not in self.used_words

    def get_name(self):

        return self.name

    def __repr__(self):
        return f"{self.name}, {self.used_words}"





