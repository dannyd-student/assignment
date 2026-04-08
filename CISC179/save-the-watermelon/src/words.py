import random

def get_word():
    """
    Returns a random word from a predefined list.
    """
    words = [
        "apple",
        "melon",
        "grape",
        "peach",
        "banana",
        "orange",
        "cherry"
    ]
    return random.choice(words)
