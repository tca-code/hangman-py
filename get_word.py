from random import choice

def get_word():
    words_raw = open("words.csv", "r")
    words = words_raw.read().split("\n")
    return choice(words)