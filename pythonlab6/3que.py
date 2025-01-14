# Starting list
lst = [7, 9, 11]

# (a) Set the second entry (index 1) to 17
lst[1] = 17

# (b) Add 7, 5, and 9 to the end of the list
lst += [7, 5, 9]  # Appending manually by list concatenation

# (c) Remove the first entry from the list
new_lst = []
for i in range(1, len(lst)):  # Skip the first element (index 0)
    new_lst += [lst[i]]
lst = new_lst

# (d) Sort the list
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:  # Swap if the current element is greater
            lst[i], lst[j] = lst[j], lst[i]

# (e) Double the list
lst = lst + lst  # Manually doubling by concatenation

# (f) Insert 25 at index 3
new_lst = []
for i in range(len(lst) + 1):
    if i < 3:
        new_lst += [lst[i]]
    elif i == 3:
        new_lst += [25]  # Insert 25 at index 3
    else:
        new_lst += [lst[i - 1]]
lst = new_lst

# (g) Show the final list
print("Final list:", lst)
