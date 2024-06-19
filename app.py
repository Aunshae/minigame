"""# create a rock paper scissors game using python with GitHub Copilot

import random
from random import randint
from flask import jsonify, request

def play_game():
    # return a JSON response
    # 1. Parse the POST request to get the player's choice
    data = request.get_json() # type: ignore
    player_choice = data["choice"]
        
        # 2. Generate a random choice for the computer
    choices = ["rock", "paper", "scissors"]
    computer_choice = choices[randint(0, 2)]
        
        # 3. Determine the winner
    if player_choice == computer_choice:
        winner = "It's a draw!"
    elif player_choice == "rock":
        if computer_choice == "paper":
            winner = "Computer wins!"
        else:
            winner = "Player wins!"
    elif player_choice == "paper":
        if computer_choice == "scissors":
            winner = "Computer wins!"
        else:
            winner = "Player wins!"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            winner = "Computer wins!"
        else:
            winner = "Player wins!"
        
        # 4. Return the result as a JSON response
        result = {
            "player_choice": player_choice,
            "computer_choice": computer_choice,
            "winner": winner
        }
        return jsonify(result)

play_game()"""


# create a rock paper scissors game using python with GitHub Copilot

# import the random module
import random

# create a list of options
options = ["rock", "paper", "scissors"]

# create the score and round played variables
score = 0
rounds_played = 0

# create the loop to play the game

while True:

    # choose a random option of the list
    computer_choice = random.choice(options)

    # asking for the user input
    player_choice = input("Rock, paper or scissors?  ")

    # if player chose rock 
    if player_choice.lower() == "rock":
        if computer_choice == "rock":
            print("Computer chose rock. It's a tie!")
        elif computer_choice == "paper":
            print("Computer chose paper. You lose!")
        elif computer_choice == "scissors":
            print("Computer chose scissors. You win!")
            score += 1
        rounds_played += 1

    # if player chose paper
    elif player_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Computer chose rock. You win!")
            score += 1
        elif computer_choice == "paper":
            print("Computer chose paper. It's a tie!")
        elif computer_choice == "scissors":
            print("Computer chose scissors. You lose!")
        rounds_played += 1

    # if player chose scissors
    elif player_choice.lower() == "scissors":
        if computer_choice == "rock":
            print("Computer chose rock. You lose!")
        elif computer_choice == "paper":
            print("Computer chose paper. You win!")
            score += 1
        elif computer_choice == "scissors":
            print("Computer chose scissors. It's a tie!")
        rounds_played += 1

    # if player chose something else
    else:
        print("That's not a valid play. Check your spelling!")

    # ask the user if they want to play again and break the loop if they don't
    # if they break the loop, print the score
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        print(f"You played {rounds_played} rounds and got {score} points!")
        break