# Given list of strings
L = ["apple", "hi", "banana", "dog", "cat", "a"]

# (a) A list that consists of the strings of L with their first characters removed
first_char_removed = [s[1:] for s in L]
print("Strings with first characters removed:", first_char_removed)

# (b) A list of the lengths of the strings of L
lengths_of_strings = [len(s) for s in L]
print("Lengths of the strings:", lengths_of_strings)

# (c) A list that consists of only those strings of L that are at least three characters long
at_least_three = [s for s in L if len(s) >= 3]
print("Strings with at least three characters:", at_least_three)
