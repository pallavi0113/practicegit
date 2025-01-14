# List comprehension to generate palindromic numbers between 100 and 1000
palindromic_numbers = [n for n in range(100, 1000) if str(n) == str(n)[::-1]]

# Display the result
print("Palindromic numbers between 100 and 1000:", palindromic_numbers)
