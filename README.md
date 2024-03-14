# Quake Log Parser

## Description
This project implements a parser for Quake 3 Arena log files. The log file contains extensive information about each match, including player kills and death causes.

## Functionality
The project includes the following functionalities:

**Log Parsing**: Reads the Quake log file and extracts game data for each match.
**Data Grouping**: Groups game data for each match, including total kills, player list, kills by player, and kills by means.
**Report Generation**: Generates a report for each match, including basic information, player kills, kills by means, and player ranking.

## Usage
To use the project, follow these steps:

Clone the repository to your local machine.
Ensure you have Python installed.
Run the `task-cloudWalk.py` script with the Quake log file as an argument.

Example:

  ```bash
      python task-cloudWalk.py qgames.log
  ```
## Log File Format

The log file should follow the format of a Quake 3 Arena server log, with each line containing information about kills and events in the game.

Example Line:

  ```bash
    21:42 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
  ```
## Additional Notes
- When <world> kills a player, that player loses -1 kill score.
- <world> should not appear in the list of players or in the dictionary of kills.
- The counter total_kills includes player and world deaths.

## Dependencies
This project has no external dependencies beyond Python standard libraries.

## Contributing
Feel free to contribute to this project by submitting pull requests or raising issues.
