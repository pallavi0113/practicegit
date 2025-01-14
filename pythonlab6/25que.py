# Define the 4x4 matrix (magic square example)
matrix = [
    [16, 23, 17, 12],
    [23, 17, 12, 16],
    [17, 12, 16, 23],
    [12, 16, 23, 17]
]

# Function to check if the matrix is a magic square
def is_magic_square(matrix):
    # Calculate the sum of the first row to set the magic constant
    magic_sum = sum(matrix[0])

    # Check if the sum of each row is equal to magic_sum
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    # Check if the sum of each column is equal to magic_sum
    for col in range(4):
        col_sum = sum(matrix[row][col] for row in range(4))
        if col_sum != magic_sum:
            return False

    # Check the sum of the main diagonal
    diagonal1_sum = sum(matrix[i][i] for i in range(4))
    if diagonal1_sum != magic_sum:
        return False

    # Check the sum of the secondary diagonal
    diagonal2_sum = sum(matrix[i][3 - i] for i in range(4))
    if diagonal2_sum != magic_sum:
        return False

    # If all conditions are met, it's a magic square
    return True

# Check if the matrix is a magic square
if is_magic_square(matrix):
    print("The matrix is a magic square.")
else:
    print("The matrix is not a magic square.")
