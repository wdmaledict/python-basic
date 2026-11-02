# Task 1: Ask the user for their name. The user may type extra spaces before or after it.
# Print a greeting using an f-string.
# Example input: "   Matija   "  → Output: Hello, Matija!
name = input("What's your name? ").strip()
print(f"Hello, {name}!")

# Task 2: Ask the user for their full name. The user may type it in lowercase and with extra spaces.
# Clean it in a single line (chain the methods) and print it using an f-string.
# Example input: "  matija petrovic "  → Output: Your name is Matija Petrovic.
name = input("What's your full name? ").strip().title()
print(f"Your name is {name}.")

# Task 3: Create a variable sentence with the value "   python IS fun   " (do not use input).
# Clean it so the output is exactly: Python is fun
sentence = "  python IS fun  "
cleaned_sentence = sentence.strip().capitalize()
print(cleaned_sentence)

# Task 4: Create a variable word with the value "ha".
# Using one f-string, print: He laughed: hahaha!
# Do not type "hahaha" yourself.
word = "ha"
print(f"He laughed: {word * 3}!")

# Task 5: Create a variable city with the value "novi sad".
# Call .title() on it WITHOUT assigning the result, then print city.
# Then call .title() again WITH assigning the result, then print city.
# Write a comment explaining why the two outputs are different.
city = "novi sad"
city.title()
print(city)  

# 2. Call .title() with assignment
city = city.title()
print(city)  

# Explanation:
# Immutability: Python strings cannot be changed after they are created. 
# Calling .title() generates a modified copy of the string, 
# but leaves the original string intact unless you explicitly save (assign) the result back to the variable.