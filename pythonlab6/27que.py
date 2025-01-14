# Initialize an empty dictionary to store product names and prices
product_dict = {}

# Loop to get product names and prices from the user
while True:
    product_name = input("Enter a product name (or type 'done' to stop): ")
    
    # Check if the user wants to stop entering products
    if product_name.lower() == 'done':
        break
    
    # Get the price for the product
    try:
        price = float(input(f"Enter the price for {product_name}: "))
        product_dict[product_name] = price  # Add product and price to the dictionary
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        continue

# Loop to allow the user to search for products by name
while True:
    search_name = input("Enter a product name to check its price (or type 'done' to stop): ")
    
    # Check if the user wants to stop searching
    if search_name.lower() == 'done':
        break
    
    # Check if the product is in the dictionary and print the price or an error message
    if search_name in product_dict:
        print(f"The price of {search_name} is ${product_dict[search_name]:.2f}.")
    else:
        print(f"Sorry, {search_name} is not in the dictionary.")
