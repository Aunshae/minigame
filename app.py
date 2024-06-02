# write 'hello world' to the console
print("hello world")
import random

def play_game():
    wins = 0
    rounds = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        possible_choices = ["rock", "paper", "scissors"]

        if user_choice not in possible_choices:
            print("Invalid option. Please try again.")
            continue

        computer_choice = random.choice(possible_choices)
        print(f"Computer chose {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You won!")
            wins += 1
        else:
            print("You lost!")

        rounds += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Game over. You won {wins} out of {rounds} rounds.")
            break

if __name__ == "__main__":
    play_game()