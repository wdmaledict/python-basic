# Task 1: Ask the user for a whole number.
# Print whether it is positive, negative, or zero.
#
# Example input: 5     Expected output: Positive
# Example input: -3    Expected output: Negative
# Example input: 0     Expected output: Zero

num = int(input("Enter whole number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")        

# Task 2: Ask the user for the temperature (a whole number) and print:
#   below 0      → Freezing
#   0 to 15      → Cold
#   16 to 25     → Nice
#   above 25     → Hot
#
# Example input: 18    Expected output: Nice
# Example input: -2    Expected output: Freezing

temp = int(input("Enter temperature: "))

if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Cold")
elif temp <= 25:
    print("Nice")
else:
    print("Hot") 


# Task 3: Ask the user which city they are in.
# If it is Novi Sad (ignoring uppercase letters and extra spaces), print "Welcome home!"
# Otherwise print "Welcome to <city>!" with each word capitalized.
#
# Example input: "  novi SAD "    Expected output: Welcome home!
# Example input: "sombor"         Expected output: Welcome to Sombor!

city = input("What city are you located in? ").strip()

if city.lower() == "novi sad":
    print("Welcome home!")
else:
    print(f"Welcome to {city.title()}!")    

# Task 4: Ask the user for two whole numbers and print which one is greater,
# or that they are equal.
#
# Example input: 7 and 3    Expected output: 7 is greater
# Example input: 2 and 9    Expected output: 9 is greater
# Example input: 4 and 4    Expected output: Equal

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater")
elif num2 > num1:
    print(f"{num2} is greater")    
else:
    print("Equal")    

# Task 5: The code below has a bug: for a score of 95 it prints more than one grade.
# Fix it so that it always prints exactly one grade,
# then write a comment explaining what the bug was.

score = int(input("Score? "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# The problem, or bug, was in the if statements. elif acts like a chain, 
# so when it encounters a true condition, it executes it and stops, 
# whereas using multiple separate if statements would execute every single true condition. 
# In this case, when we entered 95, all the conditions were true because 95 is greater than all the other numbers. 
# That is why we added elif.    