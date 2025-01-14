import random

# Define the card deck with suits and values
card_deck = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Function to deal three cards with suits
def deal_cards():
    cards = random.sample(list(card_deck.keys()), 3)  # Randomly choose 3 card values
    suits_dealt = random.choices(suits, k=3)  # Randomly choose suits for the three cards
    dealt_cards = list(zip(cards, suits_dealt))  # Combine values and suits into card tuples
    return dealt_cards

# Function to check for flush, three-of-a-kind, pair, or straight
def check_hand(cards):
    values = [card_deck[card[0]] for card in cards]
    suits = [card[1] for card in cards]

    # Check for flush: all suits must be the same
    if len(set(suits)) == 1:
        return "Flush"
    
    # Check for three-of-a-kind: all values must be the same
    if len(set(values)) == 1:
        return "Three of a Kind"
    
    # Check for pair: two values must be the same, but not all three
    if len(set(values)) == 2:
        return "Pair"
    
    # Check for straight: the values must be in consecutive order
    values.sort()
    if values == list(range(values[0], values[0] + 3)):
        return "Straight"
    
    return "No special hand"

# Deal three cards to the player
dealt_cards = deal_cards()

# Print the dealt cards
print("Dealt cards:")
for card in dealt_cards:
    print(f"{card[0]} of {card[1]}")

# Check the hand
result = check_hand(dealt_cards)
print("\nResult:", result)
