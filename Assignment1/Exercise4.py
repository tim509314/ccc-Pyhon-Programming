import random

min_range = 1
max_range = 20

secret_number = random.randint(min_range, max_range)
user_input = 0
attempts = 0

def get_user_guess():
    while True:
        try:
            guess = int(input(f"Please type a number between {min_range} and {max_range}: "))
            if min_range <= guess <= max_range:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while user_input != secret_number:
    user_input = get_user_guess()
    if user_input < secret_number:
        print("The number is smaller than the answer.")
    elif user_input > secret_number:
        print("The number is larger than the answer.")
    attempts += 1

print(f"Good job! You guessed my number in {attempts} guesses!")
