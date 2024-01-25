print("Created by: Mohit Jalal\nRoll No.- 2100971520026\nProgram No.- 07")
print("Program name- WAP in Python for Hangman Game")

import random

words = ['cloud', 'bird', 'rabbit', 'cartoon', 'court', 'list', 'clothes', 'important', 'cluster', 'road']
word = random.choice(words)
name = input("Enter Player name: ")
print("Best of Luck!", name)
guessWord = ''
chances = 10

while chances > 0:
    failed = 0
    for char in word:
        if char in guessWord:
            print(char, end=" ")
        else:
            if failed == 0:
                print("_", end=" ")
            failed += 1

    print()

    if failed == 0:
        print("You Won!")
        print("The word is: ", word)
        break

    guess = input("Guess a letter: ")
    guessWord += guess

    if guess not in word:
        chances -= 1
        print("Wrong")
        print("You have", chances, 'more guesses')

    if chances == 0:
        print("Better Luck Next Time!")
