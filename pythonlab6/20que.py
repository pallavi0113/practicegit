# Create the list using a list comprehension
result = [1 if (n == 0) else 0 for i in range(11) for n in ([1] + [0] * i)]

# Display the result
print("Resulting list:", result)
