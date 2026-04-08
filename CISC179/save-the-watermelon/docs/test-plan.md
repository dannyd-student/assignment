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

- Ran game multiple times
- Tested valid and invalid inputs
- Verified slices decrease correctly
- Verified win and lose conditions trigger properly

## Results

All core features work as expected.
No crashes during normal gameplay.

## Known Issues

- No graphical interface (terminal only)
- Limited word list
