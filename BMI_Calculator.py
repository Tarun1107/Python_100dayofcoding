#BMI Calculator
#This program helps a user to calculate their BMI by giving few inputs.
print("Welcome to Body Mass Index Calculator(BMI)")

#Getting weight in kgs and height in meters from the user
height = float(input("Enter your height in meters(m): \n"))
weight = int(input("Enter your weight in Kgs: \n"))

#BMI calculation
BMI = weight/(height**2)
print(BMI)

#Generates output as per the BMI
if BMI < 18.5:
    print(f"You are Underweight as your BMI is {BMI}")
elif BMI  >= 18.5 and BMI <= 24.9:
    print(f"Your weight is healthy as your BMI is {BMI}")
elif BMI > 25.0 and BMI <= 29.9:
    print(f"You are Overweight as you BMI is {BMI}")
else:
    print(f"You are Obese as your BMI is {BMI}")
