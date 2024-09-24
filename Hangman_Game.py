import random

def select_random_word():
    words = ["python", "hangman", "challenge", "programming", "computer", "science"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("Current word: " + " ".join(display_word))

def play_hangman():
    word = select_random_word()
    guessed_letters = set()
    attempts = 6  # Set the number of allowed incorrect guesses

    print("Welcome to Hangman!")
    print(f"You have {attempts} attempts to guess the word.")
    
    while attempts > 0:
        display_current_state(word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try a different one.")
        elif guess in word:
            print(f"Good job! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.add(guess)
            attempts -= 1
            print(f"You have {attempts} attempts left.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word '{word}' correctly.")
            break
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
