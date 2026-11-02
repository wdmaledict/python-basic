# Task 1: First write pseudocode as comments (only comments, no code yet) for this program:
# The program asks the user for their city and their country,
# then prints them on one line separated by a comma and a space.
# Example: Novi Sad, Serbia
# After the pseudocode is done, write the code under each comment.

# Ask user for their city and country.
city = input("What is your city? ")
country = input("What is your country? ")

# Prints the values on a single line, separated by a comma and a space.
print(city, country, sep=", ")

# Task 2: Below is code with bad comments. Rewrite each comment so it says
# what the goal is, not what the code literally does.
name = input("Name? ")  # Get the name so the greeting can be personal
print("Welcome,", name)  # Greets the user by name


# Task 3: Write pseudocode as comments, then the code, for this program:
# The program asks the user for a favorite food and a favorite drink,
# then prints one sentence using both.
# Example: I like pizza with lemonade.

# Ask user for their favorite food and drink
food = input("What's your favorite food? ")
drink = input("What's your favorite drink? ")

# Formats and prints a single sentence from the two input variables.
print(f"I like {food}, and {drink}.")

