# Ask the user for an integer
num = int(input("Enter an integer: "))

# Initialize an empty list to store factors
factors = []

# Find the factors of the integer
for i in range(1, num + 1):
    if num % i == 0:  # Check if i is a factor of num
        factors.append(i)

# Display the list of factors
print("Factors of", num, ":", factors)
