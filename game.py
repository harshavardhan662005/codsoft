import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower().strip()
computer_choice = random.choice(choices)

if user_choice not in choices:
    print("Invalid choice! Please run the game again and pick rock, paper, or scissors.")
else:
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! ")
    else:
        print("Computer wins! ")