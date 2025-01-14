import random

# Generate a list of 20 random numbers between 1 and 100
lst = [random.randint(1, 100) for _ in range(20)]

# (a) Print the list
print("Generated list of random numbers:", lst)

# (b) Print the average of the elements in the list
total = 0
for num in lst:
    total += num
average = total / len(lst)
print("Average of the elements in the list:", average)

# (c) Print the largest and smallest values in the list
largest = lst[0]
smallest = lst[0]
for num in lst:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest value in the list:", largest)
print("Smallest value in the list:", smallest)

# (d) Print the second largest and second smallest entries in the list
sorted_lst = sorted(lst)
second_smallest = sorted_lst[1]
second_largest = sorted_lst[-2]
print("Second smallest value in the list:", second_smallest)
print("Second largest value in the list:", second_largest)

# (e) Print how many even numbers are in the list
even_count = 0
for num in lst:
    if num % 2 == 0:
        even_count += 1
print("Number of even numbers in the list:", even_count)
