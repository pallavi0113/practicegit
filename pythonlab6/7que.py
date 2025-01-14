# (a) A list consisting of the integers 0 through 59
list_a = []
for i in range(60):  # 0 to 59
    list_a += [i]

# (b) A list containing the squares of the integers 1 through 49
list_b = []
for i in range(1, 50):  # 1 to 49
    list_b += [i * i]

# (c) A list [’a’,’bb’,’ccc’,’dddd’, ...] ending with 26 copies of 'z'
list_c = []
for i in range(1, 27):  # 1 to 26
    list_c += [chr(96 + i) * i]  # Generate letters 'a' to 'z' repeated i times

# Print the results
print("(a) List of integers from 0 to 59:", list_a)
print("(b) List of squares from 1 to 49:", list_b)
print("(c) List ['a', 'bb', 'ccc', ..., 'zzzzzzzzzzzzzzzzzzzzzzzzzz']:", list_c)
