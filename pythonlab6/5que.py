# Prompt the user to enter a list of strings
strings = input("Enter a list of strings separated by spaces: ").split()

# Create a new list with the first character of each string removed
new_list = []
for string in strings:
    new_string = ""
    for i in range(1, len(string)):  # Start from the second character
        new_string += string[i]
    new_list += [new_string]

# Display the new list
print("New list with first characters removed:", new_list)
