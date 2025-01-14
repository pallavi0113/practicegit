# Input: List with repeated items
lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Initialize an empty list to store unique items
unique_lst = []

# Iterate through the original list
for item in lst:
    # Check if the item is not already in the unique list
    exists = False
    for unique_item in unique_lst:
        if item == unique_item:
            exists = True
            break
    if not exists:
        unique_lst += [item]  # Add the item to the unique list

# Display the list with duplicates removed
print("List with duplicates removed:", unique_lst)
