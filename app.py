import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Enter again (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose

def main():
    score = {'win': 0, 'lose': 0, 'tie': 0}
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        if result == "win":
            print("You win!")
            score['win'] += 1
        elif result == "lose":
            print("You lose!")
            score['lose'] += 1
        else:
            print("It's a tie!")
            score['tie'] += 1
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print(f"Final score - Wins: {score['win']}, Losses: {score['lose']}, Ties: {score['tie']}")

if __name__ == "__main__":
    main()