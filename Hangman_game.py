#Hangman Game:
#A word-guessing game where the player tries to guess a word by suggesting letters.
#Incorrect guesses result in the creation of a stick figure that is slowly "hanged."
#The player wins if they successfully guess the word before the stick figure is completed.

import random

# List of words to choose from
word_list = ["python", "java", "kotlin", "javascript", "ruby"]

def display_word(word, guesses):
    """Displays the word with unguessed letters replaced by '_'"""
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display

def play_game():
    """Main game logic"""
    word = random.choice(word_list)
    guesses = []
    remaining_guesses = 6
    print("Welcome to Hangman!")
    while remaining_guesses > 0:
        print(f"You have {remaining_guesses} guesses left.")
        print(display_word(word, guesses))
        guess = input("Enter a letter: ").lower()
        if guess in word:
            print("Correct!")
            guesses.append(guess)
            if set(word) == set(guesses):
                print("You win! The word was", word)
                break
        else:
            print("Incorrect.")
            remaining_guesses -= 1
    else:
        print("You lose! The word was", word)

play_game()
