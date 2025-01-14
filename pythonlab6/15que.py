# Ask the user to enter some text
text = input("Enter some text: ").lower()

# Split the text into words
words = text.split()

# Initialize a counter for articles
article_count = 0

# List of articles
articles = ['a', 'an', 'the']

# Count the articles in the text
for word in words:
    if word in articles:
        article_count += 1

# Display the result
print("Number of articles in the text:", article_count)
