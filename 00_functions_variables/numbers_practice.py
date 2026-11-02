# # Task 1: Ask the user for two whole numbers and print their sum.
# # Example input: 3 and 5  → Output: 8

num1 = int(input("Enter the first whole number: "))
num2 = int(input("Enter the second whole number: "))

total = num1 + num2

print(f"Total sum of {num1} and {num2} is {total}")


# # Task 2: Ask the user for their age and print how old they will be in 10 years.
# # Example input: 39  → Output: In 10 years you will be 49.

age = int(input("How old you are: "))
years = int(input("How many years into the future? "))
future_age = age + years

print(f"In {years} years you will be {future_age} years old.")

# # Task 3: Ask the user for two numbers (they may have decimals).
# # Print the result of dividing the first by the second, rounded to 2 decimals.
# # Example input: 10 and 3  → Output: 3.33

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 / num2

print(f"Output: {result:.2f}")

# Task 4: Ask the user for a number of minutes (a whole number).
# Print how many full hours and remaining minutes that is.
# Example input: 135  → Output: 2 h 15 min

total_minutes = int(input("Enter the number of minutes: "))
hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(f"Output: {hours} h {remaining_minutes} min")

# Task 5: Ask the user for a price (may have decimals) and a quantity (whole number).
# Print the total with a thousands separator and exactly 2 decimals.
# Example input: 1999.5 and 3  → Output: Total: 5,998.50

price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
total = price * quantity

print(f"Total: {total:,.2f}")

# Task 6: Run Task 1 again, but type "abc" instead of a number.
# Write a comment with the name of the error you get and why it happened.

# This error happens because int() expects digits (like "123"), 
# but we typed letters ("abc"). Python cannot convert text letters into a whole number, so it raises a ValueError.