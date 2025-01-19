import random

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
    "A": 11
}


# Membuat ASCII art kartu
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

def calculate_total(hand):
    total = sum(cards[card] for card in hand)

    if total > 21 and "A" in hand:
        total -= 10
    return total

def display_cards(hand, title, hide_first_card = False):
    print(f"\n{title}:")

    if hide_first_card:
        card_lines = [card_art("?")] + [card_art(card) for card in hand[1:]]
    else:
        card_lines = [card_art(card) for card in hand]
    for line in zip(*card_lines):
        print("  ".join(line))

def calculate_wins(player_total, dealer_total):
    if player_total > 21:
        return "You BUST! Dealer wins."
    elif dealer_total > 21:
        return "Dealer BUSTS! You WIN!"
    elif player_total == dealer_total:
        return "It's a TIE!"
    elif player_total > dealer_total:
        return "You WIN!"
    else:
        return "Dealer wins."

def play_blackjack():
    deck = list(cards.keys())*4
    print(deck)
    random.shuffle(deck)

    print("Blackjack! ♠️♥️♣️♦️\n")

    while True:

        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)

        print("=======================================================")
        display_cards(player_hand, "Your cards")
        print(f"Total: {player_total}\n")

        display_cards(dealer_hand, "Dealer's cards", hide_first_card=True)
        print("Total: ?\n")

        while player_total < 21:
            action = input("do you want to (H)it or (S)tand? ").lower()

            if action == "h":
                player_hand.append(deck.pop())
                player_total = calculate_total(player_hand)
                print("=======================================================")
                display_cards(player_hand, "Your cards")
                print(f"Total: {player_total}\n")

                if player_total > 21:
                    print("You BUST!")
                    break
            elif action == "s":
                break
            else:
                print("Invalid input. Please enter 'H' to Hit or 'S' to Stand.")

        while dealer_total < 17 and player_total <= 21:
            dealer_hand.append(deck.pop())
            dealer_total = calculate_total(dealer_hand)

        display_cards(dealer_hand, "Dealer's cards")
        print(f"Total: {dealer_total}\n")

        res = calculate_wins(player_total, dealer_total)
        print(res)
        print("")

        pg = input("press Enter to play again or 'E' to end: ").lower()
        if pg == "e":
            print("\nThanks for playing Blackjack! ♠️♥️♣️♦️")
            print("Come back anytime for another round. —hazellenuts\n")
            break



play_blackjack()