import re

# Function to generate the report of matches, player rankings, and death cause statistics
def generate_report(games):
    for game_id, game_data in games.items():
        # Print basic information about the game
        print(f"Timestamp: {game_data['timestamp']}")
        print(f"Game: {game_id}")
        print(f"Total Kills: {game_data['total_kills']}")
        print("Players:", ", ".join(game_data['players']))
        print("Kills:")

        # Print kills for each player
        for player, kills in game_data['kills'].items():
            print(f"{player}: {kills}")
        print()

        # Generate death cause report
        print("Kills by Means:")
        for means, count in game_data['kills_by_means'].items():
            print(f"{means}: {count}")

        # Generate player ranking
        player_kills = {}
        for player, kills in game_data['kills'].items():
            if player not in player_kills:
                player_kills[player] = 0
            player_kills[player] += kills

        sorted_players = sorted(player_kills.items(), key=lambda x: x[1], reverse=True)
        print("Player Ranking:")
        for player, kills in sorted_players:
            print(f"{player}: {kills} kills")

        print()

# Modify the parse_log_file() function to include counting deaths by cause
def parse_log_file(log_file):
    # Regular expression to extract death information
    death_pattern = re.compile(r'Kill:\s+(\d+)\s+(\d+)\s+(\d+):(\d+)\s+(.*)\skilled\s(.*)\sby\s(.*)')

    # Dictionary to store data for each match
    games = {}

    with open(log_file, 'r') as file:
        current_game = None
        for line in file:
            match = death_pattern.match(line)
            if match:
                # Extract information from the log line
                game_id, _, _, hour, minute, killer, killed, cause = match.groups()
                if game_id not in games:
                    # Initialize game data if it's a new game
                    games[game_id] = {'total_kills': 0, 'players': set(), 'kills': {}, 'kills_by_means': {}, 'timestamp': None}
                current_game = games[game_id]
                current_game['timestamp'] = f"{hour}:{minute}"

                # Update total kills count
                current_game['total_kills'] += 1
                # Add players involved in the kill to the set of players
                current_game['players'].add(killer)
                current_game['players'].add(killed)

                if killer != '<world>':
                    # Increment killer's kill count
                    current_game['kills'][killer] = current_game['kills'].get(killer, 0) + 1
                else:
                    # Decrement killed player's kill count if killed by <world>
                    current_game['kills'][killed] = current_game['kills'].get(killed, 0) - 1

                # Count deaths by cause
                current_game['kills_by_means'][cause] = current_game['kills_by_means'].get(cause, 0) + 1

    return games

# Example log file
log_file = "qgames.log"

# Parse the log file and generate the report
games = parse_log_file(log_file)
generate_report(games)