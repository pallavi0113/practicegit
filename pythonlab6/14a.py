import random

# Prompt the user to enter a message
message = input("Enter a message to encrypt: ").lower()

# Generate random shifts
shifts = [random.randint(1, 25) for _ in message]

# Encrypt the message
encrypted_message = ""
for i in range(len(message)):
    char = message[i]
    if char.isalpha():  # Shift alphabetic characters
        encrypted_char = chr((ord(char) - ord('a') + shifts[i]) % 26 + ord('a'))
    else:  # Leave spaces and punctuation unchanged
        encrypted_char = char
    encrypted_message += encrypted_char

# Display the encrypted message and shifts
print("Encrypted message:", encrypted_message)
print("Random shifts:", shifts)
