import random
from collections import Counter

# Create a 5x5 list of random numbers between 1 and 10
matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

# Print the 5x5 matrix
print("5x5 Matrix:")
for row in matrix:
    print(row)

# Flatten the matrix to create a list of all numbers
all_numbers = [num for row in matrix for num in row]

# Create a dictionary (Counter) to count occurrences of each number
number_counts = Counter(all_numbers)

# Print the three most common numbers
print("\nThree most common numbers:")
most_common = number_counts.most_common(3)
for num, count in most_common:
    print(f"Number: {num}, Count: {count}")
