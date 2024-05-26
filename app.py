import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    while True:
        player_choice = input("Enter rock, paper, or scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose {computer_choice}")
        if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")
        print(f"Player: {player_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again == "no":
            break
    print("Thanks for playing!")

rock_paper_scissors()
