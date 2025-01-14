# Conversion factors
conversion_factors = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]
conversion_units = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]

# Prompt the user to enter a length in feet
length_feet = float(input("Enter length in feet: "))

# Prompt the user to choose a conversion option
print("Conversion options:")
print("1. Inches")
print("2. Yards")
print("3. Miles")
print("4. Millimeters")
print("5. Centimeters")
print("6. Meters")
print("7. Kilometers")

choice = int(input("Enter the number corresponding to your choice: "))

# Perform the conversion and display the result
if 1 <= choice <= 7:
    converted_value = length_feet * conversion_factors[choice - 1]
    print(f"{length_feet} feet is equal to {converted_value} {conversion_units[choice - 1]}.")
else:
    print("Invalid choice.")
