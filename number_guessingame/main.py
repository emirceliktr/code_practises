
import random
import art
def game():
    number_of_attempts = 0
    my_number = random.randint(1,100)
    print(art.logo)
    print("\n")
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    level.lower()

    if level == "easy":
        number_of_attempts = 10
    else:
        number_of_attempts = 5

    while number_of_attempts >0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        guess = input("Make a guess:")
        guess = int(guess)
        if guess == my_number:
            print(f"You got it! The answer was {my_number} and your guess was {guess}")
            number_of_attempts =0
        elif guess < my_number:
            print("Too low")
            print("Guess again")
            number_of_attempts -= 1
            if number_of_attempts == 0:
                print("You've run out of guesses, you lose.")
        else:
            print("Too high")
            print("Guess again")
            number_of_attempts -= 1
            if number_of_attempts == 0:
                print("You've run out of guesses, you lose.")


game()


