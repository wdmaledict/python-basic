# Task 1: Create a variable city with the value "Novi Sad" and print it.

city = "Novi Sad"
print(city)

# Task 2: Create a variable count with the value 10. On the next line, increase it by 5
# using the variable itself (not by writing 15). Print it. Expected output: 15

count = 10
count = count + 5
print(count)

# Task 3: Ask the user for their name with input and store it in a variable.
# Then print: Hello, <name>!
# Example: Hello, Matija!

name = input("What's your name? ")
# print("Hello, ", name, "!", sep="")
print(f"Hello, {name}!")

# Task 4: Ask the user for their first name and last name (two separate inputs).
# Print them on one line, separated by a single space.
# Example: Matija Petrović

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
print(first_name, last_name)


# Task 5: Ask the user for their age with input (without converting it).
# Print the age twice in a row with no space between, using one print call.
# Example: if the user types 39, output: 3939
# Then explain in a comment why the output looks like that.

age = input("What's your age ? ")
print(age * 2)
#It doesn't add or "append another string" with a string and a number; 
# instead, it repeats the string that many times: 
# "39" * 2 → "3939", "ab" * 3 → "ababab". If age were a number, 39 * 2 would be 78.
# input never returns an int, even when we "tell" it to. It always returns a string, 
# and we convert it later using int(): int(input(...)).