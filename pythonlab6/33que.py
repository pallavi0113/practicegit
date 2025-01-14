import random

# Define the card deck as a dictionary
card_deck = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

# Function to deal three cards to a player
def deal_cards():
    return random.sample(list(card_deck.keys()), 3)

# Function to compare two hands
def compare_hands(player1_cards, player2_cards):
    # Sort both players' cards by value in descending order
    player1_sorted = sorted(player1_cards, key=lambda x: card_deck[x], reverse=True)
    player2_sorted = sorted(player2_cards, key=lambda x: card_deck[x], reverse=True)

    # Compare cards from highest to lowest
    for p1, p2 in zip(player1_sorted, player2_sorted):
        if card_deck[p1] > card_deck[p2]:
            return "Player 1 wins!"
        elif card_deck[p1] < card_deck[p2]:
            return "Player 2 wins!"

    # If all three cards are the same, it's a draw
    return "It's a draw!"

# Deal cards to both players
player1_cards = deal_cards()
player2_cards = deal_cards()

# Print the dealt cards for both players
print(f"Player 1's cards: {player1_cards}")
print(f"Player 2's cards: {player2_cards}")

# Compare the hands and determine the winner
result = compare_hands(player1_cards, player2_cards)
print(result)
