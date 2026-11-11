# Task 1: Ask the user for a traffic light color and print:
#   red    → Stop
#   yellow → Slow down
#   green  → Go
#   anything else → Invalid color
# Ignore uppercase letters and extra spaces. Use match.
#
# Example input: " RED "     Expected output: Stop
# Example input: "blue"      Expected output: Invalid color

traffic_light = input("What color is the traffic light? ").strip().lower()

match traffic_light:
    case "red":
        print("Stop")
    case "yellow":
        print("Slow down")
    case "green":
        print("Go")
    case _:
        print("Invalid color")            


# Task 2: Ask the user for a day of the week and print:
#   Saturday or Sunday              → Weekend
#   Monday, Tuesday, ..., Friday    → Weekday
#   anything else                   → Not a valid day
# Ignore uppercase letters and extra spaces. Use match.
#
# Example input: "sunday"      Expected output: Weekend
# Example input: "WEDNESDAY"   Expected output: Weekday
# Example input: "someday"     Expected output: Not a valid day

day = input("What day is it today? ").strip().lower()

match day:
    case "sunday" | "saturday":
        print("Weekend")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case _:
        print("Not a valid day")        

# Task 3: Simple calculator. Ask the user for two numbers (they may have decimals)
# and an operator (+, -, * or /). Print the result.
# For any other operator, print "Unknown operator".
# You may assume the second number is never 0 when dividing. Use match.
#
# Example input: 6, 3 and "/"    Expected output: 2.0
# Example input: 2.5, 4 and "*"  Expected output: 10.0
# Example input: 1, 2 and "%"    Expected output: Unknown operator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2) 
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0:
            print("Error: Division by zero!")
        else:    
            print(num1 / num2)
    case _:
        print("Unknown operator")        
                  

# Task 4: Rewrite the code below using match instead of if/elif/else.
# It must work exactly the same.

choice = input("Choose 1, 2 or 3: ").strip()

match choice:
    case "1":
        print("New game")
    case "2":
        print("Load game")
    case "3":
        print("Quit")
    case _:
        print("Invalid choice")


# Task 5: For each problem below, write in a comment whether you would use
# match or if/elif, and why:
#   a) Print a grade (A, B, C, F) based on a score from 0 to 100.
#   b) Print "Confirmed" for "yes" or "y", "Cancelled" for "no" or "n",
#      and "Please answer yes or no" for anything else.
# Then write the code for b).

# a) Use if/elif because it involves range comparisons (e.g., score >= 90).
#    match statement is designed for exact value matching, not numeric ranges.

# b) Use match because it is checking exact strings ("yes", "y", "no", "n").
#    It keeps the code clean, especially using the | (OR) pattern.

choice = input("Are you sure? ").strip().lower()

match choice:
    case "yes" | "y":
        print("Confirmed")
    case "no" | "n":
        print("Cancelled")
    case _:
        print("Please answer yes or no")        