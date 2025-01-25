import json

RECIPES_FILES = "python-nuggets/level-2/recipes.json"

def load_recipes():
    try:
        with open(RECIPES_FILES, "r") as file:
            recipes = json.load(file)
            return recipes
    except FileNotFoundError:
        print("No saved recipes found.")

def view_recipes(recipes):
    if not recipes:
        print("No recipes found.")
        return
    else:
        print("==========================")
        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}. {recipe['name']}")
        print("==========================")

def detail_recipe(recipes):
    if not recipes:
        print("No recipes found.")
        return
    choice = int(input("Enter the number of the recipe to view: "))-1
    if 0 <= choice < len(recipes):
        recipe = recipes[choice]
        print("===========================")
        print(f"\n{recipe['name']}\n")
        print("---------------------------")
        print("Ingredients:")
        for ingredient in recipe["ingredients"]:
            print(f"- {ingredient}")
        print("---------------------------")
        print("Instructions:")
        for i, step in enumerate(recipe["instructions"], start=1):
            print(f"{i}. {step}")
        print("===========================")
        back = input("\npress Enter")
    else:
        print("Invalid choice.")

def search_recipe(recipes):
    query = input("Enter recipe name or ingredient to search: ")
    results = [recipe for recipe in recipes if query.lower() in recipe["name"].lower() or any(query.lower() in ingredient.lower() for ingredient in recipe["ingredients"])]
    if results:
        view_recipes(results)
        detail_recipe(results)
    else:
        print("No recipes found")

def main():
    recipes = load_recipes()
    print("Recipe Book")

    while True:
        view_recipes(recipes)
        print("""
[1] View detailed recipe
[2] Search for a recipe
[3] Exit
""")
        choice = input("Choose an option: ")
        if choice == "1":
            detail_recipe(recipes)
        elif choice == "2":
            search_recipe(recipes)
        elif choice == "3":
            print("\nUntil next time, keep whisking up happiness!🥣✨\n—hazellenuts\n")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()