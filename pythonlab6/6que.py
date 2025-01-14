# Prompt the user to enter a string
string = input("Enter a string: ")

# Iterate over each character in the string and display its ASCII value
for char in string:
    print(f"Character: '{char}', ASCII Value: {ord(char)}")
