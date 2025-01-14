# Define the flattened index representation
flattened = [
    (0, 0, 0), (0, 1, 1), (0, 2, 2),
    (1, 0, 3), (1, 1, 4), (1, 2, 5),
    (2, 0, 6), (2, 1, 7), (2, 2, 8)
]

# Find the size of the matrix (rows and columns)
rows = max(entry[0] for entry in flattened) + 1  # Rows are determined by max row index
cols = max(entry[1] for entry in flattened) + 1  # Columns are determined by max column index

# Initialize an empty matrix with the determined dimensions
matrix = [[None for _ in range(cols)] for _ in range(rows)]

# Fill the matrix based on the flattened list
for entry in flattened:
    row, col, value = entry
    matrix[row][col] = value

# Print the restored matrix (row-column format)
print("Restored matrix (row-column representation):")
for row in matrix:
    print(row)
