import random

num = random.randint(1, 100)

attempts = 0
print("Welcome to Guess my Number!")
print("\nI'm thinking of a number between 1 and 100\n")
while True:
    try:
        user_guess = int(input("Guess the number! "))
        if user_guess == num:
            attempts += 1
            print(f"Correct! you guessed the number in {attempts} attempts.")
            print("the real win is having fun along the way. —hazzellenuts")
            break
        elif user_guess < num:
            print("Too low! try again.")
            attempts += 1
        elif user_guess > num:
            print("Too high! try again.")
            attempts += 1
    except ValueError:
        print("stop. that's not a number!")
        break
    