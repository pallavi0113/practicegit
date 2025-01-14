# Dictionary with usernames and corresponding passwords
user_credentials = {
    'john_doe': 'password123',
    'alice_smith': 'alice2023',
    'bob_jones': 'bobsecure',
    'charlie_brown': 'chocolate',
    'danielle_williams': 'daniellepass',
    'emma_white': 'emmasecure',
    'george_black': 'george2023',
    'hannah_green': 'greenpass',
    'ian_gray': 'ianguard',
    'jack_blue': 'jack2023'
}

# Ask the user to enter their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username exists in the dictionary
if username not in user_credentials:
    print("You are not a valid user of the system.")
else:
    # Check if the password is correct
    if user_credentials[username] == password:
        print("You are now logged in to the system.")
    else:
        print("Invalid password.")
