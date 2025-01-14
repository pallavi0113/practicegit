# Dictionary to store team names and their wins and losses
team_stats = {}

# Repeatedly ask for game scores
while True:
    game_input = input("Enter the game result in format 'team1 score1 - team2 score2' (or type 'done' to stop): ")
    
    if game_input.lower() == 'done':
        break

    # Parse the input to extract team names and scores
    try:
        team1, score1, _, team2, score2 = game_input.split()
        score1, score2 = int(score1), int(score2)
        
        # Initialize team stats if not already present
        if team1 not in team_stats:
            team_stats[team1] = [0, 0]  # [wins, losses]
        if team2 not in team_stats:
            team_stats[team2] = [0, 0]  # [wins, losses]

        # Update the wins and losses based on the scores
        if score1 > score2:
            team_stats[team1][0] += 1  # team1 wins
            team_stats[team2][1] += 1  # team2 loses
        elif score2 > score1:
            team_stats[team2][0] += 1  # team2 wins
            team_stats[team1][1] += 1  # team1 loses
        else:
            # In case of a draw, no wins or losses are updated
            pass

    except ValueError:
        print("Invalid input format. Please use the format 'team1 score1 - team2 score2'.")
        continue

# Display the final stats
print("\nFinal Team Statistics:")
for team, (wins, losses) in team_stats.items():
    print(f"{team}: {wins} wins, {losses} losses")
