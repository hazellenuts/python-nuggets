expenses = [
    {
        "category": "Food",
        "amount": 15.50,
        "date": "2025-01-10"
    },
    {
        "category": "Transport",
        "amount": 5.00,
        "date": "2025-01-10"
    },
    {
        "category": "Groceries",
        "amount": 30.00,
        "date": "2025-01-16"
    },
    {
        "category": "Food",
        "amount": 10.00,
        "date": "2025-02-10"
    },
    {
        "category": "Entertainment",
        "amount": 20.50,
        "date": "2025-02-20"
    }
]

def calculate_max_widths(expenses):
    max_category = max(len(cls["category"]) for cls in expenses) if expenses else 0
    max_amount = max(len(f"{cls['amount']:.2f}") for cls in expenses) if expenses else 0
    max_date = max(len(cls["date"]) for cls in expenses) if expenses else 0
    return max_category, max_amount, max_date

def display_expense(expenses, max_category, max_amount, max_date):
    if not expenses:
        print("No expenses found.")
        return
    
    print("\nExpenses:")
    
    header = f"| {'No.':<3} | {'Category':<{max_category}} | {'Amount':<{max_amount}} | {'Date':<{max_date}} |"
    separator = "—" * len(header)

    print(separator)
    print(header)
    print(separator)

    for idx, expense in enumerate(expenses, start=1):
        print(f"| {idx:<3} | {expense['category']:<{max_category}} | ${expense['amount']:<{max_amount}.2f} | {expense['date']:<{max_date}} |")
    
    print(separator)

def add_expense():
    category = input("Enter category (e.g., Food, Transport): ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    
    expenses.append({"category": category, "amount": amount, "date": date})
    print("Expense added successfully!")

def filter_by_category(max_category, max_amount, max_date):
    category = input("Enter category to filter: ")
    filtered = [expense for expense in expenses if expense["category"].lower() == category.lower()]
    
    if not filtered:
        print(f"No expenses found for category: {category}.")
    else:
        print(f"\nExpenses for {category}:")
        display_expense(filtered, max_category, max_amount, max_date)

def main():
    print("EXPENSES TRACKER")
    max_category, max_amount, max_date = calculate_max_widths(expenses)
    display_expense(expenses, max_category, max_amount, max_date)
    
    while True:
        print("""
1. Add an expense
2. Filter by Category
3. Exit
""")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
            
            max_category, max_amount, max_date = calculate_max_widths(expenses)
        elif choice == "2":
            filter_by_category(max_category, max_amount, max_date)
        elif choice == "3":
            print("Goodbye! —hazellenuts")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()