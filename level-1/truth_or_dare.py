import random

truths = [
    "What's the most embarrassing thing you've ever done?",
    "Have you ever lied to get out of trouble?",
    "What's a secret you've never told anyone?",
    "If you could switch lives with someone for a day, who would it be?",
    "What's the weirdest thing you've ever eaten?",
    "Have you ever had a crush on a friend's partner?",
    "What's the silliest thing you've ever cried over?",
    "What's your biggest fear?",
    "Have you ever cheated on a test?",
    "What's the most trouble you've ever been in?"
]

dares = [
    "Do a silly dance for 10 seconds.",
    "Sing your favorite song out loud.",
    "Text a random number and say 'I love you.'",
    "Eat a spoonful of a condiment (e.g., ketchup, mustard).",
    "Wear socks on your hands for the next 3 rounds.",
    "Speak in an accent for the next 10 minutes.",
    "Let someone draw on your face with a pen.",
    "Call a friend and sing 'Happy Birthday' to them.",
    "Do 20 push-ups right now.",
    "Try to lick your elbow."
]


print("Let's play Truth or Dare!")
while True:
    print("")
    user_input = input("Choose! truth or dare?\n>> ").lower()
    if "truth" in user_input:
        print(f"Truth: {random.choice(truths)}")
    elif "dare" in user_input:
        print(f"Dare: {random.choice(dares)}")
    else:
        print("please choose between truth or dare.")
    pg = input("\nplay again?(y/n)\n>> ").lower()
    if pg == "n":
        print("\nYou’re a Truth or Dare champion! Bye for now. —hazellenuts")
        break
    else:
        continue
