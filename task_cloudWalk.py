import re
from collections import defaultdict

class QuakeLogParser:
    def __init__(self, log_file):
        self.log_file = log_file
        self.games = defaultdict(dict)
        self.players = set()

    def parse_log(self):
        with open(self.log_file, 'r') as file:
            current_game = None
            for line in file:
                if 'InitGame' in line:
                    current_game = self._parse_init_game(line)
                elif 'Kill' in line:
                    self._parse_kill(line, current_game)
            self._generate_reports()

    def _parse_init_game(self, line):
        game_id = line.split(' ')[1]
        self.games[game_id] = {
            'total_kills': 0,
            'players': set(),
            'kills': defaultdict(int),
            'kills_by_means': defaultdict(int)
        }
        return game_id

    def _parse_kill(self, line, game_id):
        parts = line.split(':')
        player_killed = re.search(r'(?<=killed\s)(.*?)(?=\s)', parts[3]).group(0)
        if player_killed != '<world>':
            self.games[game_id]['kills'][player_killed] += 1
            self.games[game_id]['total_kills'] += 1
        else:
            player_killed = re.search(r'(?<=killed\s)(.*?)(?=\s)', parts[3]).group(0)
            self.games[game_id]['kills'][player_killed] -= 1

        self.players.add(player_killed)
        self.games[game_id]['players'].add(player_killed)

        means_of_death = re.search(r'(?<=by\s)(.*?$)', parts[3]).group(0)
        self.games[game_id]['kills_by_means'][means_of_death] += 1

    def _generate_reports(self):
        for game_id, game_data in self.games.items():
            print(f"Game: {game_id}")
            print("Total Kills:", game_data['total_kills'])
            print("Players:", ', '.join(game_data['players']))
            print("Kills:", dict(game_data['kills']))
            print("Kills by Means:", dict(game_data['kills_by_means']))
            print()

        print("Player Ranking:")
        sorted_players = sorted(self.players, key=lambda x: sum(game['kills'].get(x, 0) for game in self.games.values()), reverse=True)
        for player in sorted_players:
            total_kills = sum(game['kills'].get(player, 0) for game in self.games.values())
            print(f"{player}: {total_kills} kills")

if __name__ == "__main__":
    parser = QuakeLogParser("qgames.log")
    parser.parse_log()