#BMI Calculator
#This program helps a user to calculate their BMI by giving few inputs.
print("Welcome to Body Mass Index Calculator(BMI)")

#Getting weight in kgs and height in meters from the user
height = float(input("Enter your height in meters(m): \n"))
weight = int(input("Enter your weight in Kgs: \n"))

#BMI calculation
BMI = int(weight/(height**2))
print(BMI)