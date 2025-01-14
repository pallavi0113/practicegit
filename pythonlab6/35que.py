# Sample dictionary
d = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]

# (a) Print users whose phone number ends in an 8
print("Users whose phone number ends in an 8:")
for user in d:
    if user['phone'].endswith('8'):
        print(user['name'], "-", user['phone'])

# (b) Print users that don't have an email address listed
print("\nUsers without an email address:")
for user in d:
    if not user['email']:
        print(user['name'], "-", "No email address")
