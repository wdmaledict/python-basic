# Task 1: Write a function is_positive(n) that returns True if n is greater than 0,
# otherwise False. In main, ask the user for a whole number and use the function
# to print "Positive" or "Not positive".
#
# Example input: 7     Expected output: Positive
# Example input: 0     Expected output: Not positive
# Example input: -4    Expected output: Not positive

def is_positive(n):
    return n > 0

def main():
    n = int(input("Enter number: "))
    if is_positive(n):
        print("Positive")
    else:
        print("Not positive")

main()        

# Task 2: Write a function is_weekend(day) that returns True for Saturday or Sunday.
# The function must work regardless of uppercase letters and extra spaces in day.
# In main, ask the user for a day and print "Weekend" or "Weekday".
#
# Example input: "  SATURDAY "    Expected output: Weekend
# Example input: "friday"         Expected output: Weekday

def is_weekend(day):
    day = day.strip().lower()
    return day == "saturday" or day == "sunday"

def main():
    day = input("What day is it today: ")
    if is_weekend(day):
        print("Weekend")
    else:
        print("Weekday")            

main()        

# Task 3: Write a function is_valid_age(age) that returns True if age is
# between 0 and 120 (including both). Do NOT use if inside the function.
# In main, ask the user for an age and print "Valid age" or "Invalid age".
#
# Example input: 0      Expected output: Valid age
# Example input: 120    Expected output: Valid age
# Example input: 121    Expected output: Invalid age
# Example input: -1     Expected output: Invalid age

def is_valid_age(age):
    return 0 <= age <= 120

def main():
    age = int(input("How old are you? "))
    if is_valid_age(age):
        print("Valid age")
    else:
        print("Invalid age")    
    
main()

# Task 4: Write a function can_drive(age, has_license) that returns True only if
# age is 18 or more AND has_license is True.
# In main, ask the user for their age and whether they have a license ("yes" or "no"),
# convert the answer to True or False, and print "Can drive" or "Cannot drive".
#
# Example input: 25 and "yes"    Expected output: Can drive
# Example input: 25 and "no"     Expected output: Cannot drive
# Example input: 16 and "yes"    Expected output: Cannot drive

def can_drive(age, has_license):
    return age >= 18

def main():
    age = int(input("How old are you? "))
    answer = input("Driving license? (yes/no): ")
    has_license = (answer == "yes")
    if can_drive(age, has_license): 
        print("Can drive")
    else:
        print("Cannot drive")

main()

# Task 5: Rewrite the function below so its body is a single line, without if.
# It must work exactly the same.

def is_odd(n):
    return n % 2 == 1