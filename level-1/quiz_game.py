import random

questions = [
    {
        "question": "Who is the captain of the USS Enterprise in 'Star Trek: The Original Series'?",
        "options": ["A. Jean-Luc Picard", "B. James T. Kirk", "C. Benjamin Sisko", "D. Kathryn Janeway"],
        "correct_answer": "B"
    },
    {
        "question": "What is the name of Spock's home planet?",
        "options": ["A. Vulcan", "B. Romulus", "C. Qo'noS", "D. Cardassia"],
        "correct_answer": "A"
    },
    {
        "question": "Which species is known for their strict adherence to logic and suppression of emotions?",
        "options": ["A. Klingons", "B. Vulcans", "C. Ferengi", "D. Borg"],
        "correct_answer": "B"
    },
    {
        "question": "What is the name of the Starfleet academy where officers are trained?",
        "options": ["A. Starfleet Command", "B. Starfleet Academy", "C. Starfleet Headquarters", "D. Starfleet Institute"],
        "correct_answer": "B"
    },
    {
        "question": "Which Star Trek series features the USS Voyager?",
        "options": ["A. Star Trek: The Next Generation", "B. Star Trek: Voyager", "C. Star Trek: Deep Space Nine", "D. Star Trek: Enterprise"],
        "correct_answer": "B"
    }
]

def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

def get_user_answer():
    user = input("your answer (A/B/C/D/50-50)? ").upper()
    if user in ["A", "B", "C", "D", "50-50"]:
        return user
    else:
        print("Invalid input.")

def fifty_fifty(question):
    correct_option = question["correct_answer"]
    options_copy = question["options"].copy()

    options_copy = [opt for opt in options_copy if not opt.startswith(correct_option)]

    removed_options = random.sample(options_copy, 2)
    remainings = [opt for opt in question["options"] if opt not in removed_options]
    print("\nRemaining options after 50-50:")
    for opt in remainings:
        print(opt)

def check_answer(question, user_answer):
    return user_answer == question["correct_answer"]

def run_quiz(questions):
    score = 0
    fifty_used = False

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        display_question(question)
        user_answer = get_user_answer()

        #handle 50-50 lifeline
        if user_answer == "50-50":
            if fifty_used:
                print("You have already used the 50-50 lifeline!")
            else:
                fifty_fifty(question)
                fifty_used = True
                user_answer = get_user_answer()
        
        if check_answer(question, user_answer):
            print("You got it right! 🎉")
            score += 1
        else:
            print(f"that's incorrect. the correct answer was {question['correct_answer']}.")
            break

    return score


#main program
print("Welcome to the Star Trek Quiz! 🌠")
final_score = run_quiz(questions)
print(f"your final score is: {final_score}/{len(questions)}.\n\nLive long and prosper 🖖\n—hazellenuts")