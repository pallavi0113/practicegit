def decimal_to_roman(num):
    # List of tuples with Roman numeral values
    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = ""
    
    # Loop through each Roman numeral value
    for value, symbol in roman_numerals:
        # While the number is larger than the current Roman numeral value, append the symbol
        while num >= value:
            result += symbol
            num -= value
    
    return result

# Ask the user for a decimal number
num = int(input("Enter a decimal number: "))

# Convert the decimal number to Roman numeral
roman = decimal_to_roman(num)

print(f"The Roman numeral for {num} is {roman}")
