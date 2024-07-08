greeting = "Welcome to the tip calculator!\n"
print(greeting)

bill = float(input("What is the bill amount? $"))
tip_percentage = int(
    input("\nHow much tip would you like to add, e.g 10, 15 or 20%? "))
people = int(input("\nHow many people are splitting the bill? "))

tip = (bill / 100) * tip_percentage
total_bill = bill + tip
amount_per_person = total_bill / people
final_amount = round(amount_per_person, 2)

print(f"\nThe total amount is ${
      total_bill} - Each person should pay: ${final_amount}")
