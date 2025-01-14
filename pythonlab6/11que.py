# Initialize the list with the first 1
lst = [1]

# Create the list by adding increasing zeroes between ones
for i in range(1, 11):  # We want the separation to go up to 10 zeroes
    lst += [0] * i + [1]

# Display the resulting list
print("Generated list:", lst)
