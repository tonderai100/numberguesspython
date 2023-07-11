import random


def play_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess == target_number:
            print("Congratulations! You guessed the correct number in", attempts, "attempts.")
            break
        elif guess < target_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")


def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == "yes":
            play_game()
        elif choice.lower() == "no":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

play_game()
play_again()
