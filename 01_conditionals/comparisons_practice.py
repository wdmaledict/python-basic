# Task 1: Ask the user for two whole numbers.
# Print whether the first number is greater than the second.
#
# Example input: 7 and 3
# Expected output:
# True

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 > num2)

# Task 2: Ask the user for their age. Store in a variable called is_adult
# whether the age is 18 or more, then print is_adult.
#
# Example input: 39
# Expected output:
# True

age = int(input("Enter your age: "))
is_adult = age >= 18

print(is_adult)

# Task 3: Ask the user for a password. Print whether it is exactly "python123".
#
# Example input: python123
# Expected output:
# True
#
# Example input: Python123
# Expected output:
# False

password = input("Enter your password: ")
print(password == "python123")

# Task 4: Ask the user to answer a question with "yes".
# Print whether the answer is "yes", ignoring uppercase letters and extra spaces.
#
# Example input: "   YeS  "
# Expected output:
# True

answer = input("Please answer with yes! ")
print(answer.strip().lower() == "yes")

# Task 5: BEFORE running, write in a comment next to each line what you think it prints.
# Then run and check your guesses.

print(5 != 5) #False
print("abc" == "ABC") #False
print(3 == 3.0) #True
print("5" == 5) #False

