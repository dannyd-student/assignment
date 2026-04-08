def is_win(secret_word, guessed_letters):
    """
    Returns True if all letters in the secret word have been guessed.
    """
    return all(letter in guessed_letters for letter in secret_word)

def render_state(secret_word, guessed_letters):
    """
    Returns the current state of the word (e.g., _ a _ e).
    """
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

def update_slices(secret_word, guess, slices):
    """
    Decreases slices if guess is incorrect.
    """
    if guess not in secret_word:
        return slices - 1
    return slices
