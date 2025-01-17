import random

options = ["rock", "paper", "scissors", "lizard", "spock"]

outcome = {
    "rock": {
        "scissors": "Rock crushes Scissors",
        "lizard": "Rock crushes Lizard"
    },
    "paper": {
        "rock": "Paper covers Rock",
        "spock": "Paper disproves Spock"
    },
    "scissors": {
        "paper": "Scissors cuts Paper",
        "lizard": "Scissors decapitates Lizard"
    },
    "lizard": {
        "spock": "Lizard poisons Spock",
        "paper": "Lizard eats Paper"
    },
    "spock": {
        "scissors": "Spock smashes Scissors",
        "rock": "Spock vaporizes Rock"
    }
}

while True:
    user = input("enter your choice (rock/paper/scissors/lizard/spock): ").lower()
    comp = random.choice(options)

    if user not in options:
        print("please choose rock/paper/scissors/lizard/spock.")
        continue
    elif user == comp:
        print("it's a tie!")
    elif comp in outcome[user]:
        print(f"You Win! {outcome[user][comp]}")
    else:
        print(f"You Lose. {outcome[comp][user]}")
    

    print("")
    pg = input("play again?(y/n) ").lower()
    if pg != "y":
        print("\n\nthat was fun! bye.\n—hazellenuts")
        break