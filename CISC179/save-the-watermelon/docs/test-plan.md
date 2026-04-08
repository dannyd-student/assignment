# Test Plan – Save the Watermelon

## Test Matrix

| Test Case | Input | Expected Result |
|----------|------|----------------|
| Valid guess | a | Letter added to guessed set |
| Invalid input (number) | 1 | Error message shown |
| Invalid input (multiple letters) | ab | Error message shown |
| Repeat guess | a twice | "Already guessed" message |
| Correct guess | letter in word | Reveals letter |
| Incorrect guess | letter not in word | Slice count decreases |
| Win condition | all letters guessed | Win message |
| Lose condition | slices = 0 | Lose message |

## Manual Testing

### Manual Test 1 – Normal Gameplay
- Started the game using `python -m src.game`
- Entered valid single-letter guesses
- Confirmed correct letters were revealed
- Confirmed incorrect guesses reduced slices

### Manual Test 2 – Invalid Inputs
- Entered a number (`1`)
- Entered multiple letters (`ab`)
- Entered a repeated guess
- Confirmed all invalid inputs showed helpful messages and did not crash the game

### Manual Test 3 – End Conditions
- Played until all letters were guessed
- Confirmed the win message appeared
- Played until slices reached 0
- Confirmed the lose message appeared

## Unit Test Results

Ran the tests using:

```bash
python -m unittest
