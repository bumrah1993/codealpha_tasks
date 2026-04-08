# Task 1 — Hangman Game 🎯

A simple text-based Hangman game built in Python where the player guesses a hidden word one letter at a time.

---

## 📋 Objective

Guess the secret word before the hangman is fully drawn. You get **6 incorrect guesses** before the game ends.

---

## 🧠 Concepts Used

| Concept | Where Used |
|---|---|
| `random` | Picking a random word from the list |
| `while` loop | Main game loop |
| `if-else` | Checking correct / incorrect guess |
| Strings | Word display, input validation |
| Lists | Tracking guessed letters |
| Functions | Modular code structure |

---

## 📁 File Structure

```
task1_hangman.py      ← Main game file (single file, no dependencies)
```

---

## ▶️ How to Run

```bash
python task1_hangman.py
```

**Requirements:** Python 3.x — no external libraries needed.

---

## 🎮 How to Play

1. Run the script
2. A random word is chosen (hidden from the player)
3. Enter one letter at a time
4. ✔ Correct guess → letter is revealed in the word
5. ✘ Wrong guess → hangman drawing progresses
6. Win by guessing all letters before 6 wrong guesses
7. After each round, choose to play again or quit

---

## 🖥️ Sample Output

```
=============================================
       Welcome to H A N G M A N !
=============================================
  The word has 6 letters. Good luck!


   -----
   |   |
       |
       |
       |
       |
  =========

  Word  : _ _ _ _ _ _
  Wrong guesses (0/6): -

  Enter a letter: p
  ✔  'p' is in the word!


   -----
   |   |
       |
       |
       |
       |
  =========

  Word  : p _ _ _ _ _
  Wrong guesses (0/6): p

  Enter a letter: a
  ✘  'a' is NOT in the word. 5 guess(es) left.


   -----
   |   |
   O   |
       |
       |
       |
  =========

  Word  : p _ _ _ _ _
  Wrong guesses (1/6): a, p

  Enter a letter: y
  ✔  'y' is in the word!

  Word  : p y _ _ _ _
  Wrong guesses (1/6): a, p, y

  Enter a letter: t
  ✔  't' is in the word!

  Word  : p y t _ _ _
  Wrong guesses (1/6): a, p, t, y

  Enter a letter: h
  ✔  'h' is in the word!

  Word  : p y t h _ _
  Wrong guesses (1/6): a, h, p, t, y

  Enter a letter: o
  ✔  'o' is in the word!

  Word  : p y t h o _
  Wrong guesses (1/6): a, h, o, p, t, y

  Enter a letter: n
  ✔  'n' is in the word!

  Word  : p y t h o n
  Wrong guesses (1/6): a, h, n, o, p, t, y

  🎉  Congratulations! You guessed the word!

  Play again? (yes / no): yes


=============================================
       Welcome to H A N G M A N !
=============================================
  The word has 8 letters. Good luck!

  Enter a letter: z
  ✘  'z' is NOT in the word. 5 guess(es) left.

  Enter a letter: x
  ✘  'x' is NOT in the word. 4 guess(es) left.

  Enter a letter: q
  ✘  'q' is NOT in the word. 3 guess(es) left.

  Enter a letter: v
  ✘  'v' is NOT in the word. 2 guess(es) left.

  Enter a letter: j
  ✘  'j' is NOT in the word. 1 guess(es) left.

  Enter a letter: w
  ✘  'w' is NOT in the word. 0 guess(es) left.


   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
  =========

  Word  : _ _ _ _ _ _ _ _
  Wrong guesses (6/6): j, q, v, w, x, z

  💀  Game over! The word was: 'keyboard'

  Play again? (yes / no): no

  Thanks for playing Hangman! Goodbye.
```

---

## ⚙️ Input Validation

| Invalid Input | Response |
|---|---|
| More than one character | "Please enter exactly ONE letter." |
| Non-alphabetic input (e.g. `3`, `!`) | "Only alphabetic characters are allowed." |
| Already guessed letter | "You already guessed 'x'. Try a different letter." |

---

## 🔧 Word List

The game uses 5 predefined words:

```python
WORD_LIST = ["python", "keyboard", "monitor", "internet", "programming"]
```

To add more words, simply extend this list inside `task1_hangman.py`.

---

## 📌 Notes

- No external libraries required — uses only Python's built-in `random` module
- All logic is split into clearly named functions for readability
- The game supports unlimited replays in a single session
