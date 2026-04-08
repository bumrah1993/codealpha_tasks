"""
Task 1: Hangman Game
Author  : Ved Patel
Purpose : Text-based Hangman game — internship submission
Concepts: random, while loop, if-else, strings, lists
"""

import random


# ─── Constants ────────────────────────────────────────────────────────────────

WORD_LIST = ["python", "keyboard", "monitor", "internet", "programming"]
MAX_WRONG_GUESSES = 6

# ASCII art stages (0 = fresh gallows … 6 = full hangman)
HANGMAN_STAGES = [
    """
   -----
   |   |
       |
       |
       |
       |
  =========
    """,
    """
   -----
   |   |
   O   |
       |
       |
       |
  =========
    """,
    """
   -----
   |   |
   O   |
   |   |
       |
       |
  =========
    """,
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
  =========
    """,
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
  =========
    """,
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
  =========
    """,
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
  =========
    """,
]


# ─── Helper Functions ──────────────────────────────────────────────────────────

def display_status(wrong_count: int, guessed_letters: list, word: str) -> None:
    """Print the hangman drawing, current word state, and wrong guesses."""
    print(HANGMAN_STAGES[wrong_count])

    # Build the word display: show guessed letters, hide the rest with '_'
    word_display = " ".join(
        letter if letter in guessed_letters else "_" for letter in word
    )
    print(f"  Word  : {word_display}")
    print(f"  Wrong guesses ({wrong_count}/{MAX_WRONG_GUESSES}): {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
    print()


def get_player_guess(guessed_letters: list) -> str:
    """Prompt the player for a valid, previously-unused single letter."""
    while True:
        guess = input("  Enter a letter: ").strip().lower()

        if len(guess) != 1:
            print("  ⚠  Please enter exactly ONE letter.\n")
        elif not guess.isalpha():
            print("  ⚠  Only alphabetic characters are allowed.\n")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try a different letter.\n")
        else:
            return guess


def is_word_solved(word: str, guessed_letters: list) -> bool:
    """Return True when every letter in the word has been guessed."""
    return all(letter in guessed_letters for letter in word)


# ─── Main Game Logic ───────────────────────────────────────────────────────────

def play_hangman() -> None:
    """Run one full round of Hangman."""
    word            = random.choice(WORD_LIST)
    guessed_letters = []   # all letters the player has tried (right or wrong)
    wrong_count     = 0    # number of incorrect guesses so far

    print("\n" + "=" * 45)
    print("       Welcome to H A N G M A N !")
    print("=" * 45)
    print(f"  The word has {len(word)} letters. Good luck!\n")

    # ── Game Loop ──────────────────────────────────────────────────────────────
    while wrong_count < MAX_WRONG_GUESSES:
        display_status(wrong_count, guessed_letters, word)

        guess = get_player_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"  ✔  '{guess}' is in the word!\n")
        else:
            wrong_count += 1
            remaining = MAX_WRONG_GUESSES - wrong_count
            print(f"  ✘  '{guess}' is NOT in the word. {remaining} guess(es) left.\n")

        # Check win condition
        if is_word_solved(word, guessed_letters):
            display_status(wrong_count, guessed_letters, word)
            print("  🎉  Congratulations! You guessed the word!\n")
            return

    # ── Player lost ────────────────────────────────────────────────────────────
    display_status(wrong_count, guessed_letters, word)
    print(f"  💀  Game over! The word was: '{word}'\n")


def main() -> None:
    """Entry point — allows the player to replay without restarting the script."""
    while True:
        play_hangman()

        again = input("  Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thanks for playing Hangman! Goodbye.\n")
            break


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
