
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game where players guess letters to reveal a hidden word before running out of attempts. You'll practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Implement Word Selection and Display

#### Description
Create a function that randomly selects a word from a predefined list and displays the current progress using underscores. The player should see the word with blanks for unguessed letters (e.g., `_ _ _ _ _`).

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Display the word in underscore format initially
- Update the display to show correctly guessed letters
- Show which letters have been guessed


### 🛠️ Handle Guess Logic and Game Flow

#### Description
Implement the core game loop that accepts player guesses, validates them, and tracks the number of incorrect guesses remaining. The game should end when the player wins (guesses the word) or loses (runs out of attempts).

#### Requirements
Completed program should:

- Accept single letter guesses from the player
- Validate guess input (prevent duplicate guesses)
- Track incorrect guesses and decrement attempts
- Display win message when word is completely guessed
- Display lose message when attempts are exhausted
- Show final word state at game end
