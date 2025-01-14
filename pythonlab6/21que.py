# Given list
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Calculate the gaps between consecutive entries
gaps = [L[i+1] - L[i] for i in range(len(L) - 1)]

# Find the maximum gap size
max_gap = max(gaps)

# Calculate the percentage of gaps that have size 2
gaps_of_2 = gaps.count(2)
percentage_of_2 = (gaps_of_2 / len(gaps)) * 100

# Display the results
print("Gaps between consecutive entries:", gaps)
print("Maximum gap size:", max_gap)
print(f"Percentage of gaps with size 2: {percentage_of_2:.2f}%")
