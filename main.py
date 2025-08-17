# Guess the number game
import random

def guess_the_number():  
   # the computer randomly selects a number between 1 and 100
    secret_number = random.randint(1, 100)


    print("Welcome to the Guess the Number !")
    print("I have selected a number between 1 and 100.")

    guess = None  
    attempts = 0 

    while True:
        
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1 
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break

guess_the_number()



#word scramble game

import random

words = ["python", "javascript", "java", "automation", "pytest", 'guvi',"selenium"]

def word_scramble():
     word_letters = list(word)
     random.shuffle(word_letters)
     return ''.join(word_letters)

print("Welcome to the Word Scramble Game!")
play_again = 'yes'
while play_again.lower() == 'yes':
    word = random.choice(words)
    scrambled_word = word_scramble()
    print(f"\nUnScrambled word: {scrambled_word}")
    attempts = 3
    while attempts > 0:
        guess = input("Guess the word: ")
        if guess.lower() == word:
            print("Congratulations! You've guessed the word correctly.")
            break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")
    play_again = input("Do you want to play again? (yes/no): ")

print("Thank you for playing the Word Scramble Game!")
