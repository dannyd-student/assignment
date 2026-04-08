import random

def get_word():
    with open("data/words.txt", "r") as file:
        words = [line.strip() for line in file if line.strip()]
    return random.choice(words)