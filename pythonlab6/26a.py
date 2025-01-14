# Define a 2D list (array) of any size
matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# Translate from row-column (left) to flattened index (right)
flattened = []
rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        flattened.append((i, j, matrix[i][j]))  # Store (row, col, value)

# Print the flattened index representation
print("Flattened index representation (row, col, value):")
for entry in flattened:
    print(f"({entry[0]},{entry[1]}) -> {entry[2]}")
