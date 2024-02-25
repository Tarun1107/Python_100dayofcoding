#Password Generator
#Importing modules and packages
import random
import string
from  string import ascii_letters, digits, punctuation

#Giving variables for letters, digits and symbols
letters = ascii_letters
# for alph in letters:
#     print(alph)
numbers = digits
# for numb in digits:
#     print(numb)
symbols = punctuation
# for i in symbols:
#     print(i)

#Welcome message
print("Welcome to the PyPassword Generator!")

#Taking input from user as to long the password must be
password_length=int(input("Enter the length of your Password:\n"))
password = []

for _ in range(password_length):
    password.append(random.choice(letters + numbers + symbols))

print("Your password is: ", "".join(password))
    