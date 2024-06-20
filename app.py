# write 'hello world' to the console
print('hello world')
# A multiplayer game where one player is the computer and the other player is a human
#This game's name is "Rock Paper Scissors"
# The winner of the game is determined by the following rules:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
# If both players choose the same item, the game is a tie
# The computer will randomly choose an item
# The human player will be prompted to choose an item through the console
# By the end of the round, the player can choose to play again or quit the game
# Display the player's score and the computer's score after each round
# The game will end when the player chooses to quit
# it must handle user inputs, putting them in lowercase and informing if the input is invalid
# execute the above commandlines in code in app.py file
import random
import sys

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_human_choice():
    
    
