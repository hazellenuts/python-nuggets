import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"],
        "correct_answer": "B",
        "difficulty": "easy",
        "value": 1000
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "correct_answer": "B",
        "difficulty": "easy",
        "value": 1000
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "correct_answer": "C",
        "difficulty": "medium",
        "value": 5000
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "correct_answer": "D",
        "difficulty": "medium",
        "value": 5000
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Stephen Hawking", "D. Nikola Tesla"],
        "correct_answer": "B",
        "difficulty": "hard",
        "value": 10000
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Diamond", "C. Iron", "D. Quartz"],
        "correct_answer": "B",
        "difficulty": "hard",
        "value": 10000
    }
]

print("Welcome to Who Wants to be a Millionaire! 🤑💸")

money = 0
fifty_used = False

for i, question in enumerate(questions, start = 1):
    print(f"\nQuestion {i}:")
    print(question["question"])
    for option in question["options"]:
        print(option)

    user = input("your answer (a/b/c/d/50-50): ").upper()

    
    while user not in ["A", "B", "C", "D", "50-50"]:
        print("invalid input.")
        user = input("your answer (a/b/c/d/50-50): ").upper()

    if user == "50-50":
        if fifty_used:
            print("you already used 50-50 lifeline!")
            user = input("your answer (a/b/c/d): ").upper()
        else:
            correct_option = question["correct_answer"]
            options_copy = question["options"].copy()

            options_copy = [opt for opt in options_copy if not opt.startswith(correct_option)]
            removed_opt = random.sample(options_copy,2)

            remainings = [opt for opt in question["options"] if opt not in removed_opt]
            print("\nRemaining options after 50-50:")
            for opt in remainings:
                print(opt)
            user = input("your answer (a/b/c/d): ").upper()
            fifty_used = True

    if user == question["correct_answer"]:
        print("correct! 🎉")
        money+=question["value"]
    
    else:
        print(f"Wrong answer! The correct answer was {question['correct_answer']}.")
        break

if money == 32000:
    print(f"\nCongratulations! You answered all questions correctly and won the game! 🏆\n🤑 ${money}.")
    print("good game —hazellenuts")
else:
    print(f"\nGame over! Your final score is ${money}/$32000.")
    print("nice try —hazellenuts")