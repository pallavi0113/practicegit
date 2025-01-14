# Ask the user to enter a sentence
sentence = input("Enter a sentence: ").split()

# Print every third word
print("Every third word:", " ".join(sentence[2::3]))
