# writ 'Hello Wrld' to the console
import random


print('Hello World')
# Create a method to play the game
def play_game():
    # Create a list with three options rock, paper, or scissors 
    options = ['rock', 'paper', 'scissors']
    # Create a variable to store the user's choice
    user_choice = input('Enter rock, paper, or scissors: ')
    # Create a variable to store the computer's choice
    computer_choice = random.choice(options)
    # Print the user's choice
    print('User choice:', user_choice)
    # Print the computer's choice
    print('Computer choice:', computer_choice)
    # Compare the user's choice to the computer's choice
    if user_choice == computer_choice:
        print('Tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
    else:
        print('You lose!')

# Call the play_game method
play_game()
# ask to play again
play_again = input('Do you want to play again? (yes or no): ')
if play_again == 'yes' or play_again == 'y':
    play_game()
else:
    print('Thanks for playing!')

# print message to the console 
print('Goodbye!')