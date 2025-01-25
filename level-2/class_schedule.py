schedules = [
    {"name": "Calculus", "day": "Monday", "start_time": "10:00", "end_time": "11:30"},
    {"name": "Algebra", "day": "Sunday", "start_time": "10:00", "end_time": "11:30"},
    {"name": "Data Mining", "day": "Friday", "start_time": "08:00", "end_time": "10:30"}
]

def calculate_max_widths(schedules):
    max_name = max(len(cls["name"]) for cls in schedules) if schedules else 0
    max_day = max(len(cls["day"]) for cls in schedules) if schedules else 0
    max_time = max(len(f"{cls['start_time']} - {cls['end_time']}") for cls in schedules) if schedules else 0
    return max_name, max_day, max_time

def display_table(schedules):
    if not schedules:
        print("No classes found.")
        return
    
    max_name, max_day, max_time = calculate_max_widths(schedules)
    
    header = f"| {'No.':<4} | {'Subject':<{max_name}} | {'Day':<{max_day}} | {'Time':<{max_time}} |"
    separator = "—" * len(header)
    
    print(separator)
    print(header)
    print(separator)
    
    for idx, cls in enumerate(schedules, start=1):
        row = f"| {idx:<4} | {cls['name']:<{max_name}} | {cls['day']:<{max_day}} | {cls['start_time']} - {cls['end_time']:<{max_time-7}}|"
        print(row)
    
    print(separator)

def add_class():
    name = input("Enter class name: ")
    day = input("Enter day: ")
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    
    schedules.append({"name": name, "day": day, "start_time": start_time, "end_time": end_time})
    display_table(schedules)
    print("Class added successfully!")

def filter_by_day():
    day = input("Enter day to filter: ")
    filtered = [cls for cls in schedules if cls["day"].lower() == day.lower()]
    
    if not filtered:
        print(f"No classes found on {day}.")
    else:
        print(f"\nClasses on {day}:")
        display_table(filtered)

def delete_class():
    display_table(schedules)
    if not schedules:
        return
    
    try:
        num = int(input("Enter the number of the class to delete: "))
        if 1 <= num <= len(schedules):
            deleted_class = schedules.pop(num - 1)
            print(f"Deleted class: {deleted_class['name']}")
            display_table(schedules)
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print("""
Class Schedule 🎒📔
""")
    display_table(schedules)

    while True:
        print("""
1. Add a class
2. Filter by day
3. Delete
4. Exit""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_class()
        elif choice == "2":
            filter_by_day()
        elif choice == "3":
            delete_class()
        elif choice == "4":
            print("\nAlright, that's a wrap! I'd give this project an A+ for effort (and maybe a gold star for cuteness 🌟) \n—hazellenuts.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()