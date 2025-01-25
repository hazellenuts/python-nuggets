import requests
import random

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_details(name):
    try:
        response = requests.get(f"{POKEAPI_URL}{name}")
        response.raise_for_status()
        data = response.json()
        print("===============================")
        print("\n🎉 Here's your Pokémon! 🎉\n")
        print(f"Name: {data['name'].capitalize()}")
        print(f"ID: {data['id']}")
        print("Type(s):", ", ".join(t['type']['name'].capitalize() for t in data['types']))
        print("Abilities:", ", ".join(a['ability']['name'].capitalize() for a in data['abilities']))
        print("Base Stats:")
        for stat in data['stats']:
            print(f" > {stat['stat']['name'].capitalize()}: {stat['base_stat']}")
        print("\n===============================")
    except requests.exceptions.HTTPError:
        print("⚠️ Oops, Pokémon not found! Check the name and try again.")
    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")

def get_random_pokemon():
    random_id = random.randint(1, 1010)
    get_pokemon_details(random_id)

def main():
    print("Welcome to the pokémon Finder!")
    while True:
        print("""
[1] Search Pokémon by name
[2] Generate a random Pokémon
[3] Exit
""")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter the name of the Pokémon: ").lower()
            get_pokemon_details(name)

        elif choice == "2":
            get_random_pokemon()

        elif choice == "3":
            print("\nThanks for playing, Catch you later! \n—hazellenuts\n")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()