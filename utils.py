import random
import requests as requests

from classes.basic_word import BasicWord

def load_words_from_jsonkeeper(path):

    response = requests.get(path)
    list_of_words = response.json()
    return list_of_words

def load_random_word(path):
    list_of_words = load_words_from_jsonkeeper(path)
    random_word = random.choice(list_of_words)

    word = random_word["word"]
    sub_words = random_word["subwords"]

    basic_word = BasicWord(word, sub_words)

    return basic_word

