# Prompt the user to enter an encrypted message
encrypted_message = input("Enter the encrypted message: ").lower()

# Prompt the user to enter the shifts used for encryption
shifts = list(map(int, input("Enter the random shifts separated by spaces: ").split()))

# Decrypt the message
decrypted_message = ""
for i in range(len(encrypted_message)):
    char = encrypted_message[i]
    if char.isalpha():  # Reverse the shift for alphabetic characters
        decrypted_char = chr((ord(char) - ord('a') - shifts[i]) % 26 + ord('a'))
    else:  # Leave spaces and punctuation unchanged
        decrypted_char = char
    decrypted_message += decrypted_char

# Display the decrypted message
print("Decrypted message:", decrypted_message)
