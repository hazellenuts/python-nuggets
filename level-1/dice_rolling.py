import random

dice_faces = {
    1: "---------\n|       |\n|   o   |\n|       |\n---------",
    2: "---------\n| o     |\n|       |\n|     o |\n---------",
    3: "---------\n| o     |\n|   o   |\n|     o |\n---------",
    4: "---------\n| o   o |\n|       |\n| o   o |\n---------",
    5: "---------\n| o   o |\n|   o   |\n| o   o |\n---------",
    6: "---------\n| o   o |\n| o   o |\n| o   o |\n---------"
}

print("Dice Rolling Simulator 🎲")

while True:
    user = input("Would you like to roll the dice?(yes/no) ")
    if user.lower() == "yes":
        dice = random.randint(1, 6)
        print(f"You rolled a {dice}!\n{dice_faces[dice]}")
    else:
        print("Thank you for using this dice rolling simulator. Goodbye!\n\n—hazellenuts")
        break