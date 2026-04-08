Pseudocode
```python
FUNCTION main_game_loop
    secret_word ← select_secret_word()
    guessed_letters ← empty set
    slices ← MAX_SLICES
    WHILE slices > 0 AND NOT is_win(secret_word, guessed_letters)
        DISPLAY current word state
        guess ← prompt user for input
        IF guess is not a single letter OR not alphabet THEN
            DISPLAY "Invalid input"
            CONTINUE
        ENDIF
        IF guess already in guessed_letters THEN
            DISPLAY "Already guessed"
            CONTINUE
        ENDIF
        ADD guess TO guessed_letters
        IF guess IN secret_word THEN
            DISPLAY "Correct guess"
        ELSE
            slices ← slices - 1
            DISPLAY "Wrong guess. Remaining slices: " + slices
        ENDIF
    ENDWHILE
    IF is_win(secret_word, guessed_letters) THEN
        DISPLAY "You saved the watermelon!"
    ELSE
        DISPLAY "The watermelon was sliced!"
    ENDIF
    ASK player if they want to play again
END FUNCTION
```
