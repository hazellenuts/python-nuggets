import json


GROCERY_FILE = "python-nuggets/level-2/grocery.json"

def load_grocery():
    try:
        with open(GROCERY_FILE, "r") as file:
            grocery_list = json.load(file)
    except FileNotFoundError:
        grocery_list = []
        print("Grocery list file not found.")
    return grocery_list

def display_grocery_list(grocery_list):
    if not grocery_list:
        print("No items found")
    else:
        print("\nCurrent Grocery List:")
        max_name_length = max(len(item["name"]) for item in grocery_list)
        max_qty_length = max(len(item["qty"]) for item in grocery_list)

        for i, item in enumerate(grocery_list, start = 1):
            status = "✅" if item["status"] == "purchased" else "⬜"
            print(f"{status} {i}. {item['name'].ljust(max_name_length)} | {item['qty'].rjust(max_qty_length)} |")

def save_grocery(grocery_list):
    with open(GROCERY_FILE, "w") as file:
        json.dump(grocery_list, file, indent = 4)

def add_item(grocery_list):
    name = input("Enter the item name: ")
    if not name:
        print("Item name cannot be empty.")
        return
    try:
        quantity = input("Enter the quantity: ")
    except ValueError:
        print("Invalid input")
        return
    
    new_item = {
        "name": name, 
        "qty": quantity,
        "status": "pending"
    }
    grocery_list.append(new_item)
    save_grocery(grocery_list)
    print("Item added successfuly!")

def mark_purchased(grocery_list):
    try:
        item_num = int(input("Enter the item number to mark as purchased: "))
        if 1 <= item_num <= len(grocery_list):
            grocery_list[item_num - 1]["status"] = "purchased"
            save_grocery(grocery_list)
            print(f"Item {item_num} marked as purchased!")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input.")

def delete_item(grocery_list):
    try:
        item_num = int(input("Enter the item number to delete: "))
        if 1 <= item_num <= len(grocery_list):
            deleted_item = grocery_list.pop(item_num - 1)
            save_grocery(grocery_list)
            print(f"Item '{deleted_item['name']}' deleted successfully!")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input.")

def main():
    print("Let's go shopping!")
    grocery_list = load_grocery()

    while True:
        display_grocery_list(grocery_list)
        print("""
1. Add an item
2. Mark an item as purchased
3. Delete an item
4. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item(grocery_list)
        elif choice == "2":
            mark_purchased(grocery_list)
        elif choice == "3":
            delete_item(grocery_list)
        elif choice == "4":
            save_grocery(grocery_list)
            print("Saving grocery list to file...")
            print("happy shopping! —hazellenuts")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5")

if __name__ == "__main__":
    main()