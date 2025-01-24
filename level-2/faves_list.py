import json
import os

FAVES_FILES = "python-nuggets/level-2/faves_list.json"

def load_faves():
    try:
        with open(FAVES_FILES, "r") as file:
            faves_list = json.load(file)
    except FileNotFoundError:
        faves_list = []
        print("File not found.")
    return faves_list

def display_faves(faves):
    if not faves:
        print("No faves found.")
    else:
        for fave in faves:
            print(f"\n🥨 {fave['category']} 🥨")
            for i, item in enumerate(fave['items'], start = 1):
                print(f"{i}. {item}")

def save_faves(faves_list):
    with open(FAVES_FILES, "w") as file:
        json.dump(faves_list, file, indent=4)

def add_faves(faves_list):
    category = input("Enter the category: ").capitalize()
    item = input("Enter the item: ")

    for fave in faves_list:
        if fave['category'] == category:
            fave['items'].append(item)
            break
    else:
        faves_list.append({"category": category, "items": [item]})
    save_faves(faves_list)
    print(f"Added '{item}' to '{category}'.")
        
def update_fave(faves_list):
    display_faves(faves_list)
    category = input("Enter the category to update: ").capitalize()
    item_index = int(input("Enter the item number to update: "))-1
    new_item = input("Enter the new item: ")

    for fave in faves_list:
        if fave['category'] == category:
            if 0 <= item_index < len(fave['items']):
                fave['items'][item_index] = new_item
                save_faves(faves_list)
                print(f"Updated item in '{category}'.")
                return
            else:
                print("Invalid item number.")
                return
    print("Category not found.")

def delete_fave(faves_list):
    display_faves(faves_list)
    category = input("Enter the category to delete from: ").capitalize()
    item_index = int(input("Enter the item number to delete: "))-1

    for fave in faves_list:
        if fave['category'] == category:
            if 0 <= item_index < len(fave['items']):
                deleted_item = fave['items'].pop(item_index)

                if not fave['items']:
                    faves_list.remove(fave)
                save_faves(faves_list)
                print(f"Deleted '{deleted_item}' from '{category}'.")
                return
            else:
                print("Invalid item number.")
                return
    print("Category not found.")

def main():
    print("My Favourites")
    faves_list = load_faves()

    while True:
        display_faves(faves_list)
        print("""
==================
|  [1] Add new   |
|  [2] Update    |
|  [3] Delete    |
|  [4] Exit      |
==================
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_faves(faves_list)
        if choice == "2":
            update_fave(faves_list)
        if choice == "3":
            delete_fave(faves_list)
        if choice == "4":
            print("thank you! —hazellenuts")
            break


if __name__ == "__main__":
    main()