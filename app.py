import random

user_input = input("Enter [rock [r], paper[p], scissors[s]]: ")
options = ['r', 'p', 's']
computer_choice = random.choice(options)
print(f"Computer choice: {computer_choice}")

# Check who wins
if user_input == computer_choice:
    print("It's a tie!")
elif (user_input == 'r' and computer_choice == 's') or (user_input == 's' and computer_choice == 'p') or (user_input == 'p' and computer_choice == 'r'):
    print("You win!")
else:
    print("Computer wins!")

# Run the app


