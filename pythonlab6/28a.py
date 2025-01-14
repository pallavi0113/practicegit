# Define a dictionary of product names and their prices
product_dict = {
    'Apple': 1.25,
    'Banana': 0.75,
    'Orange': 1.50,
    'Grapes': 2.00,
    'Mango': 1.80
}

# Ask the user to enter a dollar amount
amount = float(input("Enter a dollar amount: $"))

# Print products whose price is less than the entered amount
print(f"Products with a price less than ${amount}:")
for product, price in product_dict.items():
    if price < amount:
        print(f"{product}: ${price:.2f}")
