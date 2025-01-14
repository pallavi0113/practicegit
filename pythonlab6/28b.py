# Define the dictionary with month names and the number of days
month_days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

# (a) Ask the user to enter a month name (first three letters) and get the number of days
month_input = input("Enter the first three letters of a month (e.g., Jan, Feb): ").capitalize()

# Find the month using the first three letters (case-insensitive)
found_month = None
for month in month_days:
    if month.startswith(month_input):
        found_month = month
        break

if found_month:
    print(f"{found_month} has {month_days[found_month]} days.")
else:
    print("Invalid month entered.")

# (b) Print all of the keys (months) in alphabetical order
print("\nMonths in alphabetical order:")
for month in sorted(month_days.keys()):
    print(month)

# (c) Print all months with 31 days
print("\nMonths with 31 days:")
for month, days in month_days.items():
    if days == 31:
        print(month)

# (d) Print the (key-value) pairs sorted by the number of days in each month
print("\nMonths sorted by number of days:")
sorted_months_by_days = sorted(month_days.items(), key=lambda x: x[1])
for month, days in sorted_months_by_days:
    print(f"{month}: {days} days")
