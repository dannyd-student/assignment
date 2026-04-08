# Design – Save the Watermelon

## Problem Statement
This project is a terminal-based word guessing game where the player must guess letters to reveal a hidden word before running out of slices. The game is designed for beginner Python users and focuses on logic, input handling, and game flow.

## Game Rules
- A random word is selected.
- The word is hidden using underscores.
- The player guesses one letter at a time.
- Correct guesses reveal letters.
- Incorrect guesses reduce slices (lives).
- The player wins if all letters are revealed.
- The player loses if slices reach 0.

## Core Features
- Random word selection
- Letter guessing system
- Slice/life system
- Win/lose conditions
- Input validation

## Stretch Goals
- ASCII art watermelon stages
- Difficulty levels
- Word categories
- Score tracking

## Game Flow
Start → Select word → Loop:
- Display word state
- Get user input
- Check guess
- Update slices or reveal letters
→ End (Win or Lose)

## Data Design
- secret_word: string
- guessed_letters: set
- slices: integer

## Modules
- game.py: main loop and user interaction
- logic.py: core game logic functions
- words.py: word selection
