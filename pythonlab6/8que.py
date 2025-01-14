# Given lists L and M
L = [3, 1, 4]
M = [1, 5, 9]

# Initialize an empty list N to store the sums
N = []

# Add corresponding elements of L and M to create N
for i in range(len(L)):
    N += [L[i] + M[i]]

# Display the result
print("List N (sum of corresponding elements):", N)
