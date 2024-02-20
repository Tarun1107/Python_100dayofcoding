#Tip Calculator
print("Welcome to the tip calculator.")

#Taking inputs such as total bill, percentage from user, number of people,
total_bill = float(input("What was the total total bill: \n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? \n"))
number_of_people = int(input("How many people to split the bill? \n"))

#Converting to percentage and getting the tip amount
tip_in_percentage = tip/100
tip_amount = total_bill * tip_in_percentage

#total amount with tip included
total_amount_with_tip = total_bill + tip_amount

#Amount each person needs to pay
bill_per_person = total_amount_with_tip/number_of_people
print("\nEach person should pay: $", round(bill_per_person, 2))