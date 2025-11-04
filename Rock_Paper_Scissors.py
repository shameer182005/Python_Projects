import random

computer_score = 0
human_score = 0
inputs = ["rock", "paper", "scissor"]
is_close = True

print("--------Rock Paper Scissors---------")
print("---------------Game-----------------")
print()

while is_close:
    user_input = input("Rock, Paper, or Scissor: ").lower()
    computer_choice = random.choice(inputs)

    print(f"Computer choice : {computer_choice}")
    print(f"Your choice :     {user_input}")
    print()

    if computer_choice == "rock" and user_input == "rock":
        print("Draw")
        print(f"Computer score : {computer_score}")
        print(f"Your score : {human_score}")
        print()

    elif computer_choice == "rock" and user_input == "paper":
        human_score += 1
        print("You win!")
        print(f"Computer score : {computer_score}")
        print(f"Your score : {human_score}")
        print()

    elif computer_choice == "rock" and user_input == "scissor":
        computer_score += 1
        print("You Lost")
        print(f"Computer score : {computer_score}")
        print(f"Your score : {human_score}")
        print()

    elif computer_choice == "paper" and user_input == "rock":
        computer_score += 1
        print("You Lost")
        print(f"Computer score : {computer_score}")
        print(f"Your score : {human_score}")
        print()

    elif computer_choice == "paper" and user_input == "paper":
        print("Draw")
        print(f"Computer score : {computer_score}")
        print(f"Your score : {human_score}")
        print()

    elif computer_choice == "paper" and user_input == "scissor":
        human_score += 1
        print("You win!")
        print(f"Computer score : {computer_score}")
        print(f"Your score : {human_score}")
        print()

    elif computer_choice == "scissor" and user_input == "rock":
        human_score += 1
        print("You Win!")
        print(f"Computer score : {computer_score}")
        print(f"Your score : {human_score}")
        print()

    elif computer_choice == "scissor" and user_input == "paper":
        computer_score += 1
        print("You Lost")
        print(f"Computer score : {computer_score}")
        print(f"Your score : {human_score}")
        print()

    elif computer_choice == "scissor" and user_input == "scissor":
        print("Draw")
        print(f"Computer score : {computer_score}")
        print(f"Your score : {human_score}")
        print()

    else:
        print(f"Please enter either rock or paper, or scissor.")

    if input("Do you want to play again? (y/n) ").lower() != "y":
        is_close = False

print(f"Computer Score : {computer_score}")
print(f"Your Score : {human_score}")


