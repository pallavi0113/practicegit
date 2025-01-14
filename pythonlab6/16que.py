# Ask the user to enter five numbers as strings
numbers = []
for i in range(5):
    num = input(f"Enter number {i+1}: ")
    numbers.append(num)

# Create a string with numbers separated by plus signs
result = "+".join(numbers)

# Display the result
print("Resulting string:", result)
