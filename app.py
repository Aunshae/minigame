# write 'hello world' to the console
# create simple console game 'Rock, Paper, Scissors' with user input user can chose one of three options and computer will randomly chose one of three options and then compare them and print the result to the console
# rules: rock beats scissors, scissors beats paper, paper beats rock
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option. The computer should also randomly select one of the three options and the winner should be determined according to the rules of the game. The game should be repeated as long as the player wants to continue playing.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent. The player should also be informed of the opponent's choice in each round.
#By the end of each round, the player can choose whether to play again. If the player chooses to continue, the game should start again with the player being asked to enter their choice of rock, paper, or scissors. If the player chooses to stop playing, the game should end with a message thanking the player for playing the game.
#Display the player's score at the end of the game. The player's score should be incremented by 1 if they win a round and decremented by 1 if they lose a round. The player's score should remain the same if they tie with the opponent. The player's score should be displayed at the end of the game along with a message thanking the player for playing the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
import random

print('Hello World')

score = 0
options = ['rock', 'paper', 'scissors']

while True:
    player_choice = input('Enter your choice (rock, paper, or scissors): ').lower()
    if player_choice not in options:
        print('Invalid option. Please try again.')
        continue

    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        print(f'It\'s a tie! The computer also chose {computer_choice}.')
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        score += 1
        print(f'You win! The computer chose {computer_choice}.')
    else:
        score -= 1
        print(f'You lose! The computer chose {computer_choice}.')

    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        break

print(f'Thank you for playing. Your final score is {score}.')


   



# ask player what is his name
player_name = input('What is your name? ')
print(f'Hello, {player_name}! Welcome to the Rock, Paper, Scissors game.')

