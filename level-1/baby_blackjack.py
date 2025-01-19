import random

# Nilai kartu
cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 1 
}

# membuat ASCII art kartu
def card_art(value):
    return [
        "┌─────────┐",
        f"│ {value.ljust(2)}      │",
        "│         │",
        "│         │",
        "│         │",
        f"│      {value.rjust(2)} │",
        "└─────────┘"
    ]

# menampilkan kartu
def display_cards(hand, title):
    print(f"\n{title}:")
    card_lines = [card_art(card) for card in hand]
    for line in zip(*card_lines):
        print("  ".join(line))

def calculate_wins(player_total, dealer_total):
    # Bandingkan total nilai
    if player_total == dealer_total:
        return "It's a TIE!"
    elif player_total > dealer_total:
        return "You WIN!"
    else:
        return "Dealer wins."

deck = list(cards.keys())

print("Baby BlackJack ♣️\n")
while True:
    print("==========================================")
    # Bagikan 2 kartu untuk pemain dan dealer
    player_hand = random.sample(deck, 2)
    player_total = sum(cards[card] for card in player_hand)

    dealer_hand = random.sample(deck, 2)
    dealer_total = sum(cards[card] for card in dealer_hand)

    # Tampilkan kartu pemain dan dealer
    display_cards(player_hand, "Your cards")
    print(f"Total: {player_total}\n")

    display_cards(dealer_hand, "Dealer's cards")
    print(f"Total: {dealer_total}\n")

    # Hitung hasil permainan
    res = calculate_wins(player_total, dealer_total)
    print(res)
    print("")
    
    # Tanya pemain apakah ingin bermain lagi
    pg = input("Press Enter to play again or 's' to stop: ").lower()
    if pg == "s":
        print("\nThanks for playing Baby Blackjack! ♣️")
        print("Come back anytime for another round. —hazellenuts\n")
        break