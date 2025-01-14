# Ask the user to enter a list of integers
lst = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# (a) Print the total number of items in the list
print("Total number of items in the list:", len(lst))

# (b) Print the last item in the list
if len(lst) > 0:
    print("Last item in the list:", lst[-1])
else:
    print("The list is empty, no last item.")

# (c) Print the list in reverse order
print("List in reverse order:", lst[::-1])

# (d) Print Yes if the list contains a 5 and No otherwise
if 5 in lst:
    print("Yes")
else:
    print("No")

# (e) Print the number of fives in the list
count_fives = 0
for item in lst:
    if item == 5:
        count_fives += 1
print("Number of fives in the list:", count_fives)

# (f) Remove the first and last items, sort the remaining, and print the result
if len(lst) > 2:
    sublist = lst[1:-1]
    sublist.sort()
    print("List after removing first and last items and sorting:", sublist)
else:
    print("Not enough elements to remove first and last items.")

# (g) Print how many integers in the list are less than 5
count_less_than_5 = 0
for item in lst:
    if item < 5:
        count_less_than_5 += 1
print("Number of integers less than 5:", count_less_than_5)
