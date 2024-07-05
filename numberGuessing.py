import random

# Develop a game where the computer randomly selects a number within a specified range, and the user has to guess the number.
# Provide hints if the guessed number is too high or too low.

def number_guessing_game():
    lower_bound = 1
    upper_bound = 100

    number_to_guess = random.randint(lower_bound, upper_bound)
    print(f"Welcome to the Number Guessing Game!")
    print(f"Try guessing number between {lower_bound} and {upper_bound}.")
    print("Try to guess the number!")
    
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Increment the attempt counter
        attempts += 1

        # Check if the guess is correct
        if user_guess < number_to_guess:
            print("Your Guess is Too low! Please Try again.\n")
        elif user_guess > number_to_guess:
            print("Your Guess is Too high! Please Try again.\n")
        else:
            print(f"The random number was {number_to_guess}.")
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

number_guessing_game()
