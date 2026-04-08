"""
Task 2: Basic Chatbot
Author  : Ved Patel
Purpose : Rule-based chatbot — internship submission
Concepts: if-elif, functions, loops, input/output
"""


# ─── Response Rules ────────────────────────────────────────────────────────────
#
# Each rule is a tuple:  (list_of_keywords,  reply_string)
# The chatbot checks user input for ANY keyword in the list (case-insensitive).
# Rules are evaluated in order — the FIRST match wins.
#
RULES = [
    # Greetings
    (["hello", "hi", "hey", "howdy", "greetings"],
     "Hi there! 👋 How can I help you today?"),

    # How-are-you variants
    (["how are you", "how r u", "how do you do", "you good", "doing well"],
     "I'm doing great, thanks for asking! 😊 How about you?"),

    # Name questions
    (["your name", "who are you", "what are you", "call you"],
     "I'm ChatBot 🤖 — a simple rule-based assistant built in Python!"),

    # Help / capabilities
    (["help", "what can you do", "commands", "features"],
     "You can ask me:\n"
     "  • hello / hi          → greeting\n"
     "  • how are you         → my status\n"
     "  • your name / who     → about me\n"
     "  • tell me a joke      → a bad joke 😄\n"
     "  • what time is it     → current time\n"
     "  • bye / exit / quit   → end chat"),

    # Jokes
    (["joke", "funny", "laugh", "humor"],
     "Why do programmers prefer dark mode? 🌑\n"
     "Because light attracts bugs! 🐛"),

    # Current time (uses Python's datetime)
    (["time", "what time", "current time"],
     "__TIME__"),   # special token — handled in get_response()

    # Compliments / thanks
    (["thank", "thanks", "great", "awesome", "good bot", "nice"],
     "You're welcome! 😄 Happy to help."),

    # Sadness / frustration
    (["sad", "upset", "angry", "frustrated", "bored"],
     "I'm sorry to hear that. 😔 Hope things get better soon!"),

    # Farewell — keep this LAST so 'bye' doesn't swallow other rules
    (["bye", "goodbye", "exit", "quit", "see you", "cya"],
     "__BYE__"),    # special token — handled in main loop
]

UNKNOWN_REPLY = (
    "Hmm, I didn't quite understand that. 🤔\n"
    "Type 'help' to see what I can do!"
)


# ─── Core Functions ────────────────────────────────────────────────────────────

def get_response(user_input: str) -> str:
    """
    Match the user's message against RULES and return the appropriate reply.
    Returns the matched reply string, or UNKNOWN_REPLY if nothing matches.
    """
    text = user_input.lower().strip()

    for keywords, reply in RULES:
        if any(kw in text for kw in keywords):

            # Handle the special __TIME__ token
            if reply == "__TIME__":
                from datetime import datetime
                now = datetime.now().strftime("%I:%M %p")   # e.g. 03:45 PM
                return f"The current time is {now} ⏰"

            return reply

    return UNKNOWN_REPLY


def print_banner() -> None:
    """Display a welcome banner when the chatbot starts."""
    print("\n" + "=" * 50)
    print("       Welcome to ChatBot 🤖")
    print("=" * 50)
    print("  I'm a simple rule-based Python chatbot.")
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 50 + "\n")


# ─── Main Chat Loop ────────────────────────────────────────────────────────────

def main() -> None:
    """Run the chatbot — reads user input in a loop until a farewell is detected."""
    print_banner()

    while True:
        # ── Get user input ─────────────────────────────────────────────────────
        try:
            user_input = input("  You   : ").strip()
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+C or piped input gracefully
            print("\n\n  Bot   : Goodbye! 👋\n")
            break

        # Skip empty input
        if not user_input:
            continue

        # ── Generate response ──────────────────────────────────────────────────
        response = get_response(user_input)

        # ── Handle farewell ────────────────────────────────────────────────────
        if response == "__BYE__":
            print("  Bot   : Goodbye! It was nice chatting with you. 👋\n")
            break

        # ── Print response (multi-line support) ────────────────────────────────
        first_line, *rest_lines = response.split("\n")
        print(f"  Bot   : {first_line}")
        for line in rest_lines:
            print(f"          {line}")   # indent continuation lines neatly
        print()


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
