# Ask the user for a list of elements
lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Rotate the list
if len(lst) > 0:  # Check if the list is not empty
    rotated_lst = [lst[-1]] + lst[:-1]  # Move the last element to the front
else:
    rotated_lst = []

# Display the rotated list
print("Rotated list:", rotated_lst)
