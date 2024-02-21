#Rollercoster ticket counter
print("Welcome to rollercoster ride!")

#Collecting height and age inputs from user
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))

#Calculating the cost of the ticket based on height and age.
if height >= 120:
    print("You can ride the rollercoster")
    if age > 18:
        print("The ticket cost is $12")
    elif age > 12 and age < 18:
        print("The ticket cost is $7")
    elif age < 12:
        print("The ticket cost is $7")
else:
    print("You can not ride")