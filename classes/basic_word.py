
class BasicWord:

    def __init__(self, value, sub_words):
        self.value = value
        self.sub_words = sub_words

    def get_word(self):
        return self.value

    def has_sub_word(self, word):
        return word in self.sub_words


    def number_of_sub_words(self):
        return len(self.sub_words)

    def __repr__(self):
        return(f" {self.value}, {self.sub_words}")

