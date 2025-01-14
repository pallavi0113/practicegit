# Define a 4x4 list of integers
matrix = [
    [4, 8, 12, 16],
    [3, 7, 11, 15],
    [2, 6, 10, 14],
    [1, 5, 9, 13]
]

# Calculate the sum of all elements
total_sum = 0
total_elements = 0

for row in matrix:
    for value in row:
        total_sum += value
        total_elements += 1

# Calculate the average
average = total_sum / total_elements

# Display the result
print("Matrix:")
for row in matrix:
    print(row)

print(f"\nAverage of all entries: {average:.2f}")
