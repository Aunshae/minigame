import random

print("Enter a Choice")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice < 1 or choice > 4:
    print("\nInvalid Choice")
elif choice == 1:
    print("\nYou chose Rock")
elif choice == 2:
    print("\nYou chose Paper")
elif choice == 3:
    print("\nYou chose Scissors")

print("\nComputer Turn")

compChoice = random.randint(1, 3)
if compChoice == 1:
    print("\nComputer chose Rock")
elif compChoice == 2:
    print("\nComputer chose Paper")
else:
    print("\nComputer chose Scissors")


if choice == compChoice:
    print("\nIt's a Tie")
elif choice == 1 and compChoice == 3:
    print("\nYou Win")
elif choice == 2 and compChoice == 1:
    print("\nYou Win")
elif choice == 3 and compChoice == 2:
    print("\nYou Win")
else:
    print("\nComputer Wins")
