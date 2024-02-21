# printing ASCII Art
print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
******************************************************************************* ''')

# Welcome message to the treasure island
print("Welcome to Treasure Hunt.")
print("Your mission is to find the treasure.")

# Taking input choices from user to find the treasure
choice1 = input('You are at a junction. Where do you want to go? Type "left" or "right":\n').lower()
if choice1 == "left":
    choice2 = input('You have reached a lake. There is an Island in the middle. Type "Boat" if you want to wait for a boat. Else Type "Swim" to swim to the island:\n').lower()
    if choice2 == "boat":
        choice3 = input('There is a house with three doors "Red","Green", and "Yellow" which one do you want to enter?\n').lower()
        if choice3 == "red":
            print("GAME OVER! the room is full of venomous snakes.")
        elif choice3 == "green":
            print("Congratulations! You found the Treasure!")
        elif choice3 == "yellow":
            print("GAME OVER! You have entered a room with fire.")
        else:
            print("Invalid colour")
    else:
        print("GAME OVER! You got eaten by a crocodile.")
else:
    print("GAME OVER! You reached a dead end.")

