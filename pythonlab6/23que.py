import random

# Create a 10x10 list of random integers between 1 and 100
matrix = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

# (a) Print the list
print("10x10 Matrix:")
for row in matrix:
    print(row)

# (b) Find the largest value in the third row
third_row = matrix[2]  # Index 2 corresponds to the third row
largest_in_third_row = max(third_row)
print(f"\nLargest value in the third row: {largest_in_third_row}")

# (c) Find the smallest value in the sixth column
sixth_column = [row[5] for row in matrix]  # Index 5 corresponds to the sixth column
smallest_in_sixth_column = min(sixth_column)
print(f"Smallest value in the sixth column: {smallest_in_sixth_column}")
