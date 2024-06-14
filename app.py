import random

def get_user_choice():
    user_input = input("Enter your choice (rock, scissors, paper): ").lower()
    while user_input not in ["rock", "scissors", "paper"]:
        print("Invalid choice. Please choose rock, scissors, or paper.")
        user_input = input("Enter your choice (rock, scissors, paper): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(["rock", "scissors", "paper"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    player_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. The computer chose {computer_choice}.")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            player_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"Score: Player {player_score}, Computer {computer_score}")
        
        while True:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again in ["y", "yes"]:
                break  # Breaks the inner loop and continues the game
            elif play_again in ["n", "no"]:
                print("Thanks for playing!")
                return  # Exits the play_game function, thus ending the game
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    play_game()