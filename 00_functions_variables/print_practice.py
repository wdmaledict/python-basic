# Task 1: Using one print call with three arguments ("Novi", "Sad", "Srbija"), print: Novi Sad Srbija
print("Novi", "Sad", "Srbija")

# Task 2: Using one print call with the same three words, print: Novi-Sad-Srbija
print("Novi", "Sad", "Srbija", sep="-")

# Task 3: Using two print calls, print on a single line: Hello, world!
# (the first print outputs "Hello,", the second outputs "world!")
print("Hello, ", end="")
print("world!")

# Task 4: Using one print call, with day, month and year as separate number arguments, print: 29.10.2026.
print(29, 10, 2026, sep=".", end=".\n")

# Task 5: Using one print call, print each word on its own line: Novi / Sad / Srbija
print("Novi", "Sad", "Srbija", sep="\n")

# Task 6: Using one print call with the numbers 1, 2, 3 (as numbers, not strings), print: 1, 2, 3
print(1, 2, 3, sep=", ")

# Task 7: Using three print calls, each printing one letter (a, b, c), print on a single line: a | b | c
print("a", end=" | ")
print("b", end=" | ")
print("c")

# Task 8: Using two print calls for the text, print "First line" and "Third line" with an empty line between them
# (you may add one more print if needed, but try without it first)
print("First line", end="\n\n")
print("Third line")