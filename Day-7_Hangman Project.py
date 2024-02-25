#Hangman Project
#importing modules and packages.
import random

#Hangman stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#List of words to be  used in the game
end_game = False
words = ["python", "java", "c++","javascript","php"]
chosen_word = random.choice(words)
word_length = len(chosen_word)

#variable with number of lives
lives = 6

display = []
for letter in range(word_length) :
    display += "_"
# for letter in chosen_word:
#     display += "_"

while not end_game:
    #Taking inputs from user to guess a letter and assign answer to guess variable.
    guess = input("Guess a letter: ").lower()


    #Check if letter from the guess variable is one of the letter in chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose")
    
#Joining all elements in the list and turing it into a string
    print(f"{' '.join(display)}")

#Checking if user has got all the letters.
    if "_" not in display:
        end_game = True
        print("You Win!")

    print(stages[lives])