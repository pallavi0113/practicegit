# Prompt the user to enter a list containing numbers between 11 and 22
lst = list(map(int, input("Enter a list of numbers between 11 and 22, separated by spaces: ").split()))

# Replace all entries greater than 19 with 19
for i in range(len(lst)):
    if lst[i] > 19:
        lst[i] = 19  # Replace with 19 if the number is greater than 19

# Display the modified list
print("Modified list:", lst)
