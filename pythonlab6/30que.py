# Dictionary to store team names and their wins and losses
team_stats = {}

# Repeatedly ask for team names and stats
while True:
    team_name = input("Enter the team name (or type 'done' to stop): ")
    
    if team_name.lower() == 'done':
        break
    
    # Get the number of wins and losses
    wins = int(input(f"Enter the number of games won by {team_name}: "))
    losses = int(input(f"Enter the number of games lost by {team_name}: "))
    
    # Store the information in the dictionary
    team_stats[team_name] = [wins, losses]

# Function to calculate and print the winning percentage of a team
def get_winning_percentage(team_name):
    if team_name in team_stats:
        wins, losses = team_stats[team_name]
        total_games = wins + losses
        if total_games > 0:
            winning_percentage = (wins / total_games) * 100
            print(f"{team_name}'s winning percentage: {winning_percentage:.2f}%")
        else:
            print(f"{team_name} has no games played yet.")
    else:
        print(f"Team {team_name} not found.")

# Ask for the team name and print the winning percentage
team_to_check = input("\nEnter a team name to check its winning percentage: ")
get_winning_percentage(team_to_check)

# Create a list of the number of wins of each team
wins_list = [team_stats[team][0] for team in team_stats]
print("\nList of number of wins of each team:")
print(wins_list)

# Create a list of teams with a winning record (more wins than losses)
winning_teams = [team for team, stats in team_stats.items() if stats[0] > stats[1]]
print("\nTeams with winning records:")
print(winning_teams)
