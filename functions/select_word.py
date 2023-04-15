from random import choice

def select_word():
    with open("data/mots_communs.txt", "r", encoding='utf-8') as f:
        words = f.readlines()
    return choice(words)