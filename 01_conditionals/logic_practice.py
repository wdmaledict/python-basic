# Task 1: Ask the user for their age and whether they have a ticket ("yes" or "no").
# Print "You can enter" only if they are 18 or older AND have a ticket.
# Otherwise print "Access denied".
# The ticket answer should ignore uppercase letters and extra spaces.
#
# Example input: 25 and " YES "    Expected output: You can enter
# Example input: 16 and "yes"      Expected output: Access denied
# Example input: 30 and "no"       Expected output: Access denied

age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? (yes/no): ").strip().lower()


if age >=18 and has_ticket == "yes":
    print("You can enter")
else:
    print("Access denied")   

# Task 2: Ask the user for a day of the week.
# Print "Weekend" if it is Saturday or Sunday, otherwise print "Weekday".
# Ignore uppercase letters and extra spaces.
#
# Example input: "  SUNDAY"    Expected output: Weekend
# Example input: "monday"      Expected output: Weekday

day = input("What day is it today? ").strip().lower()

if day == "saturday" or day == "sunday":
    print("Weekend")
else:
    print("Weekday")    

# Task 3: Ask the user for a whole number.
# Print "In range" if it is between 1 and 100 (including 1 and 100),
# otherwise print "Out of range".
#
# Example input: 1      Expected output: In range
# Example input: 100    Expected output: In range
# Example input: 0      Expected output: Out of range
# Example input: 150    Expected output: Out of range

number = int(input("Enter number: "))

if 1 <= number <= 100:
    print("In range")
else:
    print("Out of range")    

# Task 4: Ask the user for a temperature (a whole number) and whether it is raining ("yes" or "no").
# Print "Stay home" if the temperature is below 5 OR it is raining.
# Otherwise print "Go outside".
#
# Example input: 20 and "yes"    Expected output: Stay home
# Example input: 2 and "no"      Expected output: Stay home
# Example input: 20 and "no"     Expected output: Go outside

temp = int(input("What is the temperature? "))
raining = input("Is it raining? (yes/no): ")

if temp < 5 or raining == "yes":
    print("Stay home")
else:
    print("Go outside")
    
# Task 5: Ask the user for a username.
# If the user typed nothing (or only spaces), print "Username cannot be empty".
# Otherwise print "Hello, <username>!" using the username without extra spaces.
# Use not in your solution.
#
# Example input: "   "        Expected output: Username cannot be empty
# Example input: " alex42 "   Expected output: Hello, alex42!

username = input("Please enter your username: ").strip()

if not username:
    print("Username cannot be empty")
else:
    print(f"Hello, {username}!")

# Task 6: The code below has a bug: for "green" it prints "Primary color".
# Fix it so it prints "Primary color" only for red, blue or yellow,
# and "Not a primary color" for anything else.
# Then write a comment explaining what the bug was.

color = input("Color? ").strip().lower()

if color == "red" or color == "blue" or color == "yellow":
    print("Primary color")
else:
    print("Not a primary color")

# The problem was that the condition used "blue" by itself instead of color == "blue". 
# In Python, or "blue" is always evaluated as true, so the condition always passed regardless of the input.