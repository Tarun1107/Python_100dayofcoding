#Rock, Paper and Scissors game
# importing modules and packages
import random
print("Welcome to Rock Paper Scissors game!")

#Game images representing rock, paper and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

#Taking user input
player_choice = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice >=3 or player_choice < 0:
    print("You have entered an invalid number!")
else:
    print(game_images[player_choice])

    #Generates coumputer choice randomly
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {computer_choice}")
    print(game_images[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose!")
    elif player_choice > computer_choice:
        print("You win!")
    elif computer_choice >  player_choice:
        print("You lose!")
    elif computer_choice == player_choice:
        print("It's a draw!")