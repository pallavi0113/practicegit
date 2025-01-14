# Create an 8x8 checkerboard pattern list
checkerboard = [[1 if (i + j) % 2 == 0 else 2 for j in range(8)] for i in range(8)]

# Print the checkerboard pattern
print("8x8 Checkerboard Pattern:")
for row in checkerboard:
    print(row)
