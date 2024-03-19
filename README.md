# Quake Log Parser

This Python script is designed to parse Quake III Arena log files and generate reports on the games and player rankings based on kill data.

## Installation

Ensure you have Python installed on your system. This script is compatible with Python 3.x.

## Usage

1. Place your Quake III Arena log file (e.g., qgames.log) in the same directory as the task_cloudWalk.py script.

2. Run the script by executing the following command in your terminal:

```Bash
python task_cloudWalk.py
```

3. The script will parse the log file and generate reports for each game, including total kills, players involved, kills by each player, and kills by means. It will also display a player ranking based on total kills.

## Script Overview

- `QuakeLogParser` class: This class contains methods to parse the log file, extract game data, and generate reports.
- `parse_log()`: Reads the log file, extracts game data, and generates reports.
- `_parse_init_game()`: Parses the initialization of a game, extracting game ID and initializing game data.
- `_parse_kill()`: Parses kill events, extracting data on the player killed, updating kill counts, and recording means of death.
- `_generate_reports()`: Generates reports for each game, including total kills, players involved, kills by each player, and kills by means. It also displays a player ranking based on total kills.

## Example Output

Sample output for a game:

Game: game_1
Total Kills: 45
Players: Dono da bola, Isgalamido, Zeh
Kills: {'Dono da bola': 5, 'Isgalamido': 18, 'Zeh': 20}
Kills by Means: {'MOD_SHOTGUN': 10, 'MOD_RAILGUN': 2, 'MOD_GAUNTLET': 1, ...}

Player Ranking:
Isgalamido: 18 kills
Zeh: 20 kills
Dono da bola: 5 kills

## Notes

- This script assumes the format of the Quake III Arena log file specified in the task description.
- Make sure to replace `"qgames.log"` with the actual filename if it differs.
