# Task 2 — Basic Chatbot 🤖

A simple rule-based chatbot built in Python that responds to common conversational inputs using keyword matching.

---

## 📋 Objective

Build a chatbot that reads user input, matches it against predefined rules, and prints appropriate replies — no AI or internet required.

---

## 🧠 Concepts Used

| Concept | Where Used |
|---|---|
| `if-elif` | Inside keyword matching logic |
| Functions | `get_response()`, `print_banner()`, `main()` |
| `while` loop | Keeps chat session running |
| `input()` / `print()` | User interaction |
| Lists & Tuples | Storing keyword-reply rule pairs |
| `datetime` | Fetching current time dynamically |

---

## 📁 File Structure

```
task2_chatbot.py      ← Main chatbot file (single file, no dependencies)
```

---

## ▶️ How to Run

```bash
python task2_chatbot.py
```

**Requirements:** Python 3.x — no external libraries needed.

---

## 💬 Supported Inputs

| What You Type | Bot Replies With |
|---|---|
| `hello` / `hi` / `hey` | Greeting message |
| `how are you` / `you good` | Status reply |
| `your name` / `who are you` | Bot introduction |
| `help` / `what can you do` | List of commands |
| `tell me a joke` / `funny` | Programmer joke |
| `what time is it` / `time` | Current system time |
| `thank you` / `thanks` | Acknowledgement |
| `sad` / `frustrated` / `bored` | Empathy response |
| `bye` / `exit` / `quit` | Ends the chat |

---

## 🖥️ Sample Output

```
==================================================
       Welcome to ChatBot 🤖
==================================================
  I'm a simple rule-based Python chatbot.
  Type 'help' to see what I can do.
  Type 'bye' or 'exit' to quit.
==================================================

  You   : hello
  Bot   : Hi there! 👋 How can I help you today?

  You   : how are you
  Bot   : I'm doing great, thanks for asking! 😊 How about you?

  You   : what is your name
  Bot   : I'm ChatBot 🤖 — a simple rule-based assistant built in Python!

  You   : help
  Bot   : You can ask me:
            • hello / hi          → greeting
            • how are you         → my status
            • your name / who     → about me
            • tell me a joke      → a bad joke 😄
            • what time is it     → current time
            • bye / exit / quit   → end chat

  You   : tell me a joke
  Bot   : Why do programmers prefer dark mode? 🌑
          Because light attracts bugs! 🐛

  You   : what time is it
  Bot   : The current time is 03:22 PM ⏰

  You   : I am feeling sad today
  Bot   : I'm sorry to hear that. 😔 Hope things get better soon!

  You   : thanks
  Bot   : You're welcome! 😄 Happy to help.

  You   : hahaha you are awesome
  Bot   : You're welcome! 😄 Happy to help.

  You   : what is quantum physics
  Bot   : Hmm, I didn't quite understand that. 🤔
          Type 'help' to see what I can do!

  You   : bye
  Bot   : Goodbye! It was nice chatting with you. 👋
```

---

## ⚙️ How the Matching Works

The chatbot uses a `RULES` list where each entry is a tuple of:

```python
(list_of_keywords,  reply_string)
```

When the user types something, the bot checks if **any keyword** from a rule appears in the input (case-insensitive). The **first matching rule** wins.

```python
# Example rule
(["hello", "hi", "hey"], "Hi there! 👋 How can I help you today?")
```

This makes it easy to extend — just add a new tuple to the `RULES` list.

---

## ➕ Adding New Rules

Open `task2_chatbot.py` and add a new entry inside the `RULES` list:

```python
(["weather", "rain", "sunny"],
 "I can't check the weather, but I hope it's nice outside! ☀️"),
```

No other changes needed.

---

## 📌 Notes

- No external libraries required — uses only Python's built-in `datetime` module
- Handles empty input and `Ctrl+C` (keyboard interrupt) gracefully
- Multi-line bot replies are auto-indented for clean formatting
- Case-insensitive matching — `Hello`, `HELLO`, and `hello` all work the same
