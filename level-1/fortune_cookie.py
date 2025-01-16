import random

fortunes = ["Adventure is worthwhile in itself. – Amelia Earhart", "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb", "You are capable of more than you know. Choose a goal that seems right for you and strive to be the best.", "Happiness is not something ready-made. It comes from your own actions. – Dalai Lama", "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt", "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill", "Your imagination is your preview of life's coming attractions. – Albert Einstein", "The journey of a thousand miles begins with one step. – Lao Tzu", "You will soon receive a pleasant surprise. Stay open to new opportunities!", "Good things come to those who wait, but better things come to those who work for it."]

while True:
    print("Fortune Cookies 🥠🔮")
    user = input("Would you like to open a fortune cookie?(yes/no) ")

    if user.lower() == "yes":
        fortune = random.choice(fortunes)
        print("\nYour fortune: " + fortune + "\n")
    elif user.lower() == "no":
        print("Thank you for using the Fortune Cookie Program. Goodbye!")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'")