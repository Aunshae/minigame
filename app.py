import random

score = 0
valid_choices = {"r": "rock", "p": "paper", "s": "scissors"}

while True:
    print("1. Rock (r)\n2. Paper (p)\n3. Scissors (s)")
    player_choice = input("Choose your option (r, p, or s): ").lower()
    if player_choice not in valid_choices:
        print("Invalid choice. Please try again.")
        continue

    program_choice = random.choice(list(valid_choices.keys()))
    print(f"Program chose {valid_choices[program_choice]}")

    if player_choice == program_choice:
        print("It's a tie!")
    elif (player_choice == "r" and program_choice == "s") or \
         (player_choice == "p" and program_choice == "r") or \
         (player_choice == "s" and program_choice == "p"):
        print("You win!")
        score += 1
    else:
        print("You lose!")

    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        break

print(f"Your score: {score}")