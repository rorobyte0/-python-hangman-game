import random
HANGMAN_STAGES = [
r”””
+—+
|   |
|
|
|
|
=========”””,
r”””
+—+
|   |
O   |
|
|
|
=========”””,
r”””
+—+
|   |
O   |
|   |
|
|
=========”””,
r”””
+—+
|   |
O   |
/|   |
|
|
=========”””,
r”””
+—+
|   |
O   |
/|\  |
|
|
=========”””,
r”””
+—+
|   |
O   |
/|\  |
/    |
|
=========”””,
r”””
+—+
|   |
O   |
/|\  |
/ \  |
|
=========”””
]
WORDS = [“bad”, “ugly”, “good”, “cute”]
MAX_ATTEMPTS = len(HANGMAN_STAGES) - 1
def display_word(word_progress):
“”“Display the current state of the hidden word.”””
print(” “.join(word_progress))
def play_hangman():
“”“Run a complete Hangman game.”””
secret_word = random.choice(WORDS)
word_progress = [”_”] * len(secret_word)
guessed_letters = set()
remaining_attempts = MAX_ATTEMPTS
print("Welcome to Hangman!")
print("Guess the hidden word one letter at a time.")
print(HANGMAN_STAGES[0])
display_word(word_progress)

while "_" in word_progress and remaining_attempts > 0:
    print(f"\nRemaining attempts: {remaining_attempts}")
    print("Guessed letters:", ", ".join(sorted(guessed_letters))
          if guessed_letters else "None")

    guess = input("Enter a letter: ").strip().lower()

    # Validate the user's input.
    if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
        print("Invalid input. Please enter one English letter.")
        continue

    # Prevent the same letter from being guessed twice.
    if guess in guessed_letters:
        print("You have already guessed that letter. Try again.")
        continue

    guessed_letters.add(guess)

    # Reveal matching letters or reduce the remaining attempts.
    if guess in secret_word:
        for position, letter in enumerate(secret_word):
            if letter == guess:
                word_progress[position] = guess

        print("Correct guess!")
    else:
        remaining_attempts -= 1
        print("Incorrect guess!")
        print(HANGMAN_STAGES[MAX_ATTEMPTS - remaining_attempts])

    display_word(word_progress)

# Display the final game result.
if "_" not in word_progress:
    print(f"\nCongratulations! You guessed the word: {secret_word}")
else:
    print(HANGMAN_STAGES[-1])
    print(f"\nGame over! The correct word was: {secret_word}")
if name == “main”:
play_hangman()
