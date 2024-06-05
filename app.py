# import random then difine a funtion named jugar()
import random

def jugar():
    # Define a list of options
    opciones = ["piedra", "papel", "tijeras"]
    # Define a variable to store the user's choice
    eleccion = input("Elige piedra, papel o tijeras: ")
    # Define a variable to store the computer's choice
    computadora = random.choice(opciones)
    # Print the computer's choice
    print(f"La computadora eligió: {computadora}")
    # Print the user's choice
    print(f"Tu elegiste: {eleccion}")
    # Check if the user and the computer chose the same option
    if eleccion == computadora:
        print("Empate!")
    # Check if the user chose "piedra" and the computer chose "tijeras"
    elif eleccion == "piedra" and computadora == "tijeras":
        print("Ganaste!")
    # Check if the user chose "papel" and the computer chose "piedra"
    elif eleccion == "papel" and computadora == "piedra":
        print("Ganaste!")
    # Check if the user chose "tijeras" and the computer chose "papel"
    elif eleccion == "tijeras" and computadora == "papel":
        print("Ganaste!")
    # If none of the above conditions are met, the user loses
    else:
        print("Perdiste!")

# Call the jugar() function
jugar()