# import random module 
import random

#create a list  of options 
options = ["rock", "paper","scissors"]

#create the score and round played variables
score = 0
rounds_played = 0


#create the loop of the game
while true:

  # choose a random option of the list
  computer_choice = random.choice(options)

#asking for user input
player_choice = input("Rock,paper or scissors? ")
#if player chose rock
if player_choice.lower() == "rock":
  if computer_choice == "rock":
    print("Computer chose rock. Its a tie!")
  elif computer_choice == "paper":
    print("Computer chose paper. You lose!")
  elif computer_choice == "scissors":
    print("Computer chose scissors. You win!")
    score +=1

#if player chose paper
elif player_choice.lower() == "paper":
  if computer_choice == "rock":
    print("Computer chose rock. You win!")
    score +=1
elif computer_choice == "paper":
  print("Computer chose paper. Its a tie")
elif computer_choice == "scissors":
  print("Computer chose scissors. You lose!"):

#if player chose scissors
  elif player_choice.lower() == "scissors":
    if computer_choice == "rock":
      print("Computer chose rock. You lose!"):
      elif computer_choice == "paper":
        print("Computer chose paper. You win!"):
        elif computer_choice == "scissors"
         print("Computer chose scissors. Its a tie!"):

#if player chose sth else
else:
  print("Thats not a valid play. Check your spelling")

#ask if they would like to play again
      play_again = input("Do you want to play again? "(y/n) )
     if play_again.lower() != "y":
        print(f"You played {rounds_played} rounds and got {score} points!")
        break
    



