# Simple Rock, Paper, Scissors Game

'''
Game Rules:
- The computer randomly chooses rock, paper, or scissors each round.
- The player inputs their choice of rock, paper, or scissors in the console.
- An invalid option prompts a warning.
- After each round, the game announces if the player won, lost, or tied.
- The player can choose to play again after each round.
- The game displays the player's score at the end.
- The game handles user inputs, converting them to lowercase and validating the option.

Winning Conditions:
- Rock beats scissors.
- Scissors beat paper.
- Paper beats rock.
'''
# Import the random module
import random
# Define the game variables
options = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
game = True

# Define the game loop
while game:
    # Computer's move
    computer_move = random.choice(options)
    
    # Player's move
    player_move = input('Choose rock, paper, or scissors: ').lower()

    # Check if the player's move is valid
    if player_move not in options:
        print('Invalid option. Please choose rock, paper, or scissors.')
        continue

    # Game logic
    # Tie
    if player_move == computer_move:
        print(f'Computer choose {computer_move}. It is a tie!')
    # Player wins
    elif (player_move == 'rock' and computer_move == 'scissors') or (player_move == 'scissors' and computer_move == 'paper') or (player_move == 'paper' and computer_move == 'rock'):
        print(f'Computer choose {computer_move}. You win!')
        player_score += 1
    # Computer wins
    else:
        print(f'Computer choose {computer_move}. You lose!')
        computer_score += 1

    # Play again
    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        game = False

# Display the final scores
print(f'Player score: {player_score}')
print(f'Computer score: {computer_score}')



