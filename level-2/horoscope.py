import random

horoscopes = {
    "aries": [
        "Today is a great day to take charge and lead the way!",
        "Your energy is high, so use it to tackle challenges head-on.",
        "Be careful not to rush into decisions today. Take your time.",
        "A new opportunity is coming your way. Stay alert!"
    ],
    "taurus": [
        "Take some time to relax and enjoy the simple pleasures of life.",
        "Your persistence will pay off today. Keep pushing forward.",
        "A surprise encounter could brighten your day.",
        "Focus on your goals, but don’t forget to take breaks."
    ],
    "gemini": [
        "Your communication skills are on point today. Use them wisely.",
        "A busy day ahead, but you’ll handle it with ease.",
        "Stay open to new ideas and perspectives.",
        "You might feel torn between two choices. Trust your instincts."
    ],
    "cancer": [
        "Your intuition is strong today. Listen to your gut feelings.",
        "Spend some quality time with loved ones.",
        "A creative project could bring you joy today.",
        "Don’t let your emotions overwhelm you. Stay balanced."
    ],
    "leo": [
        "Your charisma is shining today. Use it to inspire others.",
        "A bold move could lead to great rewards.",
        "Take some time to pamper yourself. You deserve it!",
        "Be careful not to dominate conversations today."
    ],
    "virgo": [
        "Your attention to detail will help you succeed today.",
        "A small act of kindness could make a big difference.",
        "Stay organized, but don’t forget to go with the flow.",
        "You might feel the need to help others today. Don’t overdo it."
    ],
    "libra": [
        "Focus on finding balance in your life today.",
        "A social gathering could bring you joy and new connections.",
        "Your charm will help you navigate tricky situations.",
        "Don’t overthink decisions today. Trust your instincts."
    ],
    "scorpio": [
        "Your determination will help you overcome any obstacles today.",
        "A deep conversation could lead to a meaningful connection.",
        "Trust your instincts—they’re especially strong today.",
        "Be careful not to let jealousy or suspicion cloud your judgment."   
    ],
    "sagittarius": [
        "Adventure is calling! Embrace new experiences today.",
        "Your optimism will inspire those around you.",
        "A spontaneous decision could lead to something exciting.",
        "Be careful not to overcommit yourself today."
    ],
    "capricorn": [
        "Your hard work is paying off. Keep pushing forward!",
        "A practical approach will help you solve problems today.",
        "Take some time to reflect on your long-term goals.",
        "Don’t forget to reward yourself for your efforts."
    ],
    "aquarius": [
        "Your innovative ideas could lead to exciting opportunities today.",
        "A social cause might inspire you to take action.",
        "Stay open to unconventional solutions.",
        "Be careful not to isolate yourself. Connect with others."
    ],
    "pisces": [
        "Your creativity is flowing today. Use it to express yourself.",
        "A dream or intuition could provide valuable insight.",
        "Take some time to relax and recharge your energy.",
        "Be careful not to let your emotions overwhelm you."
    ]
}

def main():
    print("✨ Welcome to the Daily Horoscope Generator! ✨\n")
    while True:
        zodiac = input("Enter your zodiac sign: ").lower()
        if zodiac in horoscopes:
            horoscope = random.choice(horoscopes[zodiac])
            print(f"\nYour horoscope for today:\n{horoscope}")
        else:
            print("Invalid zodiac sign. Please try again.")

        again = input("\nWould you like to generate another horoscope? (y/n): ").lower()
        if again != "y":
            print("Remember, the stars may guide you, but your destiny is yours to create!🌌\n—hazellenuts")
            break

if __name__ == "__main__":
    main()