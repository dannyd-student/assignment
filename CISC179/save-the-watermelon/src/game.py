from src.words import get_word
from src.logic import is_win, render_state, update_slices
MAX_SLICES = 5
def main():
    print("Welcome to Save the Watermelon!")
    secret_word = get_word()
    guessed_letters = set()
    slices = MAX_SLICES
    while slices > 0 and not is_win(secret_word, guessed_letters):
        print("\nWord:", render_state(secret_word, guessed_letters))
        print("Slices remaining:", slices)
        guess = input("Guess a letter: ").lower()
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in secret_word:
            print("Nice! Correct guess.")
        else:
            slices = update_slices(secret_word, guess, slices)
            print("Wrong guess!")
    # End game result
    if is_win(secret_word, guessed_letters):
        print("\n You saved the watermelon!")
        print("The word was:", secret_word)
    else:
        print("\n The watermelon was sliced!")
        print("The word was:", secret_word)
if __name__ == "__main__":
    main()
