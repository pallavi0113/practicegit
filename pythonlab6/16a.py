# Ask the user to enter a sentence
sentence = input("Enter a sentence: ").split()

# Check if the sentence has at least three words
if len(sentence) >= 3:
    print("The third word is:", sentence[2])
else:
    print("The sentence does not have a third word.")
