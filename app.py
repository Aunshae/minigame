import random

def is_valid_choice(choice, options):
    """Check if a choice is valid based on the available options."""
    return choice in options

def is_winning_choice(choice, opponent_choice):
    """Check if a choice beats another choice."""
    if (choice == "rock" and opponent_choice == "scissors") or \
       (choice == "paper" and opponent_choice == "rock") or \
       (choice == "scissors" and opponent_choice == "paper"):
        return True
    return False

def main():
    """Main game loop."""
    player_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]

    while True:
        # Get player's choice
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        # Validate player's choice
        if not is_valid_choice(player_choice, options):
            print("Invalid choice. Please try again.")
            continue

        # Get computer's choice
        computer_choice = random.choice(options)

        # Display choices
        print(f"Player chose {player_choice} and computer chose {computer_choice}.")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif is_winning_choice(player_choice, computer_choice):
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Display scores
        print(f"Player score: {player_score} | Computer score: {computer_score}")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no) ").lower()

        # Exit the game loop if the player doesn't want to play again
        if play_again != "yes":
            break

    # Display final scores
    print(f"Player score: {player_score} | Computer score: {computer_score}")

if __name__ == "__main__":
    main()