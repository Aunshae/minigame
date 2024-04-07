# Challenge project - Build a minigame console app with GitHub Copilot

# Rock Paper Scissors Game

This Python script allows you to play the classic game of Rock Paper Scissors against the computer. The game continues until the user decides to stop playing.

## How to Play

1. Run the Python script.
2. Enter your choice (rock, paper, or scissors) when prompted.
3. The computer will randomly select its choice.
4. The winner of the round will be determined based on the choices.
5. You can choose to play again or exit the game.

## Implementation Details

- The script imports the `random` module to enable random selection of the computer's choice.
- It defines a list `options` containing the possible choices: "rock", "paper", and "scissors".
- Variables `score` and `rounds_played` are initialized to keep track of the player's score and the number of rounds played.
- The game is played in a `while` loop, which continues until the player decides to stop.
- After each round, the result is printed, and the score and rounds played are updated accordingly.
- If the player inputs an invalid choice, they are prompted to enter a valid one.
- After each round, the player is asked if they want to play again. If not, the game displays the final score and the number of rounds played.

## License

This script is open-source and available under the MIT License. Feel free to modify and distribute it according to your needs.
