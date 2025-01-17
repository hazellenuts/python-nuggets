import random

option = ["rock", "paper", "scissors"]
win_conditions = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

while True:

    user = input("rock/paper/scissors? ").lower()
    comp = random.choice(option)

    if user not in option:
        print("please choose rock/paper/scissors.")
    elif user==comp:
        print("tie")
    elif win_conditions[user] == comp:
        print(f"You Win! {user} beats {comp}")
    else:
        print(f"You Lose. {comp} beats {user}")

    print("")
    pg = input("play again?(y/n) ").lower()
    if pg == "y":
        continue
    else:
        print("\n\nGood Game. bye! \n—hazellenuts")
        break