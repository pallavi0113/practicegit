import random

# List of questions and their corresponding answers
questions = [
    "What is the capital of France?", "What is 2 + 2?", 
    "What is the color of the sky?", "Who wrote 'Hamlet'?",
    "What is the square root of 16?", "Which planet is known as the Red Planet?",
    "What is the largest ocean on Earth?", "Who painted the Mona Lisa?",
    "What is the boiling point of water in Celsius?", "How many continents are there?"
]

answers = [
    "paris", "4", 
    "blue", "shakespeare", 
    "4", "mars", 
    "pacific", "da vinci", 
    "100", "7"
]

# Select 4 random questions
indices = random.sample(range(10), 4)

# Initialize score
score = 0

# Ask the questions one-by-one
for i in indices:
    user_answer = input(f"Question: {questions[i]} ").strip().lower()
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is '{answers[i]}'.")
    print()

# Display the total score
print(f"You got {score} out of 4 questions right.")
