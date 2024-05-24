# write 'hello world' to the console
#print("hello world")

#Rock beats scissors.
#Scissors beat paper.
#Paper beats rock.

# the computer randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. 
# Your interaction in the game will be through the console (Terminal).
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

# Create Simple Rock, Paper, Scissors Game

import random

def rock_paper_scissors():

    # Define the game options
    options = ['rock', 'paper', 'scissors']
    
    # Define the player and computer scores
    player_score = 0
    computer_score = 0
    
    # Define the game status
    game = True

    while game:
        # Player's move
        player_move = input('Enter your move: ')
        player_move = player_move.lower()
        if player_move not in options:
            print('Invalid option. Please try again.')
            continue

        # Computer's move
        computer_move = random.choice(options)
        print(f'Computer chose {computer_move}')
        
        # Game logic
        if player_move == computer_move:
            print('It is a tie!')
        elif player_move == 'rock' and computer_move == 'scissors':
            print('You win!')
            player_score += 1
        elif player_move == 'scissors' and computer_move == 'paper':
            print('You win!')
            player_score += 1
        elif player_move == 'paper' and computer_move == 'rock':
            print('You win!')
            player_score += 1
        else:
            print('You lose!')
            computer_score += 1

        # Play again
        play_again = input('Do you want to play again? (yes/no): ')
        play_again = play_again.lower()
        if play_again != 'yes':
            game = False

    # Display the final scores
    print(f'Player score: {player_score}')
    print(f'Computer score: {computer_score}')

rock_paper_scissors()


