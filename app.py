#write a rock paper scissors game
# import random Module
import random

#write a main function to handle all the game logic
# user should be able to choose to conitnue playing until the user types 'exit'
# Repeat the game until the user types 'exit'
# if the minigame is terminated display the score
def main():
    #initialize the score
    score = 0
    #initialize the user choice
    user_choice = ''
    #initialize the computer choice
    computer_choice = ''
    #initialize the choices
    choices = ['rock', 'paper', 'scissors']
    #print the welcome message
    print("Welcome to the Rock, Paper, Scissors Game!")
    #print the instructions
    print("Choose rock, paper, or scissors. Type 'exit' to quit the game.")
    #repeat the game until the user types 'exit'
    while user_choice != 'exit':
        #get the user choice
        user_choice = input("Enter your choice: ")
        #if the user types 'exit' break out of the loop
        if user_choice == 'exit':
            break
        #if the user choice is not valid, continue to the next iteration
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        #get the computer choice
        computer_choice = random.choice(choices)
        #print the computer choice
        print("Computer choice: " + computer_choice)
        #if the user and computer choices are the same, it's a tie
        if user_choice == computer_choice:
            print("It's a tie!")
        #if the user choice is rock
        elif user_choice == 'rock':
            #if the computer choice is scissors, the user wins
            if computer_choice == 'scissors':
                print("You win!")
                score += 1
            #if the computer choice is paper, the computer wins
            else:
                print("Computer wins!")
        #if the user choice is paper
        elif user_choice == 'paper':
            #if the computer choice is rock, the user wins
            if computer_choice == 'rock':
                print("You win!")
                score += 1
            #if the computer choice is scissors, the computer wins
            else:
                print("Computer wins!")
        #if the user choice is scissors
        elif user_choice == 'scissors':
            #if the computer choice is paper, the user wins
            if computer_choice == 'paper':
                print("You win!")
                score += 1
            #if the computer choice is rock, the computer wins
            else:
                print("Computer wins!")
    #print the final score
    print("Final score: " + str(score))
    



#call the main function
if __name__ == "__main__":
    main()
    




