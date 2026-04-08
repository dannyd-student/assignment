from src.words import get_word
from src.logic import is_win, render_state, update_slices
MAX_SLICES = 5

def play_game():
    print("Welcome to Save the Watermelon!")
    secret_word = get_word()
    guessed_letters = set()
    slices = MAX_SLICES
    while slices > 0 and not is_win(secret_word, guessed_letters):
        print("\nWord:", render_state(secret_word, guessed_letters))
        print("Slices remaining:", slices)
        guess = input("Guess a letter: ").lower()
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
    if is_win(secret_word, guessed_letters):
        print("\nYou saved the watermelon!")
        print("The word was:", secret_word)
    else:
        print("\nThe watermelon was sliced!")
        print("The word was:", secret_word)
def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()