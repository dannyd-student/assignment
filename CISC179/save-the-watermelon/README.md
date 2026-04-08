# Save the Watermelon

## Description
Save the Watermelon is a terminal-based word guessing game built in Python. The player must guess letters to reveal a hidden word before running out of slices (lives). This project demonstrates basic Python concepts including functions, modules, input validation, and testing.

## How to Run

Make sure you are in the project root directory, then run:

```bash
python -m src.game
```
OR

```bash
python src/game.py
```

# How to Test

Run the unit tests with:
```bash
python -m unittest
```

## Features
- Random word selection from a file
- Letter guessing system
- Slice (life) system
- Win and lose conditions
- Input validation (single letters only)
- Prevents duplicate guesses

## Game Rules
- You guess one letter at a time 
- Correct guesses reveal letters in the word 
- Incorrect guesses reduce your slices 
- You win if you guess all letters before slices run out 
- You lose if slices reach zero

## Known Issues / Limitations
- Terminal-based only (no graphical interface)
- Limited word list 
- No difficulty settings 

## Project Structure

```text
save-the-watermelon/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ src/
│  ├─ game.py
│  ├─ logic.py
│  ├─ words.py
│  └─ __init__.py
├─ tests/
│  ├─ test_logic.py
│  └─ __init__.py
├─ docs/
│  ├─ design.md
│  ├─ pseudocode.md
│  └─ test-plan.md
└─ data/
   └─ words.txt
```
## Credits

**Created by Danny DeGraff for CISC179**