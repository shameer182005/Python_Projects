import random

lowest_number = 0
highest_number = 100
score = 0
is_correct = True
answer = random.randint(lowest_number,highest_number)

print("--------Number Guessing Game--------")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_correct:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess > highest_number or guess < lowest_number:
            print("Your guess is out of the range!")
            score += 1
        elif guess < answer:
            print("Your guess is too low!")
            score += 1
        elif guess > answer:
            print("Your guess is too high!")
            score += 1
        else:
            print("Your guess is correct!")
            score += 1
            print(f"Total score: {score}")
            is_correct = False
    else:
        print(f"Please enter a number between {lowest_number} and {highest_number}")