import random;
options = ["rock" , "paper", "scissors"];

score = 0; 
rounds = 0;

while  True: 
    computer_choice = random.choice(options);
    player_choice = input( "rock , paper or scissors ? ");

    if player_choice.lower() == "rock" :
        if computer_choice == "rock" :
            print("Match tie ...");
            rounds += 1;
        elif computer_choice == "paper":
            rounds += 1;
        elif computer_choice == "scissors":
            score += 1;
            rounds += 1;
    elif player_choice.lower() == "paper" :
        if computer_choice == "paper" :
            print("Match tie ...");
            rounds += 1;
        elif computer_choice == "scissors":
            rounds += 1;
        elif computer_choice == "rock":
            score += 1;
            rounds += 1;
    elif player_choice.lower() == "scissors" :
        if computer_choice == "scissors" :
            print("Match tie ...");
            rounds += 1;
        elif computer_choice == "rock":
            rounds += 1;
        elif computer_choice == "paper":
            score += 1;
            rounds += 1;
    else :
        print("Invalid input ! Please select the correct one...");

    play_again = input ("Do you want to play again ? (y/N) ");
    if play_again.lower() == "n":
        print(f"your total score is {score} and rounds played {rounds} ");
        break;