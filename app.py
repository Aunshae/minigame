import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Win"
    else:
        return "Lose"

def print_result(result):
    if result == "Win":
        print("Congratulations! You won!")
    elif result == "Lose":
        print("Sorry! You lost.")
    else:
        print("It's a tie!")

def main():
    player_score = 0
    rounds_played = 0
    
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid option! Please choose from rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer chose:", computer_choice)
        
        result = determine_winner(player_choice, computer_choice)
        print_result(result)
        
        if result == "Win":
            player_score += 1
        elif result == "Lose":
            player_score -= 1
        
        rounds_played += 1
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("Game over!")
    print("Your final score:", player_score)
    print("Total rounds played:", rounds_played)

if __name__ == "__main__":
    main()
