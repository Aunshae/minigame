import random

def get_user_choice():
    """
    Solicita al usuario que elija entre Rock, Paper o Scissors.
    Devuelve la opción del usuario en minúsculas.
    """
    user_choice = input("Elige Rock, Paper o Scissors: ").strip().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Por favor, elige una opción válida (Rock, Paper o Scissors).")
        user_choice = input("Elige Rock, Paper o Scissors: ").strip().lower()
    return user_choice

def get_computer_choice():
    """
    Genera aleatoriamente la opción de la computadora entre Rock, Paper o Scissors.
    """
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """
    Determina el ganador del juego.
    Devuelve el resultado del juego.
    """
    if user_choice == computer_choice:
        return "Empate!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "¡Ganaste!"
    else:
        return "¡La computadora gana!"

def play_game():
    """
    Función principal para jugar el juego de Rock, Paper, Scissors.
    """
    print("Bienvenido al juego de Rock, Paper, Scissors contra la computadora.")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("La computadora elige:", computer_choice)
        print(determine_winner(user_choice, computer_choice))

        play_again = input("¿Quieres jugar de nuevo? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print("¡Gracias por jugar!")

# Iniciar el juego
play_game()
