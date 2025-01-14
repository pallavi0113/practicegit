import random

# Generate a list of 100 random integers (either 0 or 1)
lst = [random.choice([0, 1]) for _ in range(100)]

# Find the longest run of zeros
longest_run = 0
current_run = 0

# Iterate through the list to count consecutive zeros
for num in lst:
    if num == 0:
        current_run += 1  # Increase current run of zeros
        longest_run = max(longest_run, current_run)  # Update longest run
    else:
        current_run = 0  # Reset the current run when a 1 is encountered

# Display the generated list and the longest run of zeros
print("Generated list:", lst)
print("Longest run of zeros:", longest_run)
