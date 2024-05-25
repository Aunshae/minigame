import random

def game():
    choices = ["rock", "paper", "scissors"]
    scores = {"player": 0, "computer": 0}
    rounds = 0

    while True:
        rounds += 1
        print(f"Round {rounds}")

        player = input("Enter your choice (rock/paper/scissors): ").lower()
        if player not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a draw!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "scissors" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            scores["player"] += 1
            print("You win!")
        else:
            scores["computer"] += 1
            print("You lose!")

        def show_result(scores, rounds):
            print("Final Result:")
            print(f"Player: {scores['player']} wins")
            print(f"Computer: {scores['computer']} wins")
            print(f"Number of rounds played: {rounds}")

        print(f"Scores: Player - {scores['player']}, Computer - {scores['computer']}")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            show_result(scores, rounds)
            break

game()