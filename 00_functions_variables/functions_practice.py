# Task 1: Define a function say_hi that prints "Hi there!".
# Call it twice.
#
# Expected output:
# Hi there!
# Hi there!

def say_hi():
    print("Hi there!")

say_hi()
say_hi()

# Task 2: Define a function greet with one parameter (a name)
# that prints a greeting. Call it once with "Ana" and once with "Marko".
#
# Expected output:
# Hello, Ana!
# Hello, Marko!

def greet(name):
    print(f"Hello, {name}!")

greet("Ana")
greet("Marko")

# Task 3: Define a function welcome with one parameter (a city) that has
# a default value of "Novi Sad". Call it once without an argument, and once with "Sombor".
#
# Expected output:
# Welcome to Novi Sad!
# Welcome to Sombor!

def welcome(city="Novi Sad"):
    print(f"Welcome to {city}!")

welcome()
welcome("Sombor")    

# Task 4: Define a function double that RETURNS a number multiplied by 2.
# The function itself must not print anything.
# Outside the function, call it with 7, add 1 to the result, and print it.
#
# Expected output:
# 15

def double(number):
    return number * 2

result = double(7) + 1
print(result)

# Task 5: Define a function full_name with two parameters (first and last name)
# that RETURNS the full name, cleaned of extra spaces and with capital first letters.
# Ask the user for first and last name with input, call the function, and print the result.
#
# Example input:
#   "  matija "  and  " petrovic"
# Expected output:
# Your name is Matija Petrovic.

def full_name(first, last):
    return f"{first.strip().title()} {last.strip().title()}"

user_first = input("Enter first name: ")
user_last = input("Enter last name: ")

result = full_name(user_first, user_last)
print(f"Your name is {result}.")