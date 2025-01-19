def display_menu():
    print("\nMetric Conversion Tool 📐📏")
    print("""
1. length
2. Mass
3. Volume
4. Exit
""")

def get_units(category):
    if category == "length":
        return ["m", "cm", "km"]
    elif category == "mass":
        return ["g", "kg"]
    elif category == "volume":
        return ["L", "mL"]

def convert_length(value, from_unit, to_unit):
    if from_unit == "m":
        if to_unit == "cm":
            return value*100
        elif to_unit == "km":
            return value/1000
        else:
            return value
        
    elif from_unit == "cm":
        if to_unit == "m":
            return value/100
        elif to_unit == "km":
            return value/100000
        else:
            return value
        
    elif from_unit == "km":
        if to_unit == "m":
            return value*1000
        elif to_unit == "cm":
            return value*100000
        else:
            return value

def convert_mass(value, from_unit, to_unit):
    if from_unit == "g":
        if to_unit == "kg":
            return value/1000
        else:
            return value
        
    elif from_unit == "kg":
        if to_unit == "g":
            return value*1000
        else:
            return value
        
def convert_volume(value, from_unit, to_unit):
    if from_unit == "L":
        if to_unit == "mL":
            return value*1000
        else:
            return value
    
    elif from_unit == "mL":
        if to_unit == "L":
            return value/1000
        else:
            return value     
    else:
            print("❌ Invalid units. Please try again.")

def main():
    while True:
        display_menu()
        choice = input("Choose a category (1-4): ")
        if choice == "1":
            category = "length"
            units = get_units(category)
        elif choice == "2":
            category = "mass"
            units = get_units(category)
        elif choice == "3":
            category = "volume"
            units = get_units(category)
        
        elif choice == "4":
            print("Goodbye! 👋\n—hazellenuts")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"\nAvailable units for {category}: {', '.join(units)}")
        from_unit = input("Convert from: ").strip().lower()
        to_unit = input("Convert to: ").strip().lower()
        value = float(input("Enter the value: "))
        
        if from_unit or to_unit not in get_units(category):
            print("❌ Invalid units.")
            break

        if category == "length":
            result = convert_length(value, from_unit, to_unit)
        elif category == "mass":
            result = convert_mass(value, from_unit, to_unit)
        elif category == "volume":
            result = convert_volume(value, from_unit, to_unit)
        else:
            print("❌ Invalid units.")
            break

        print(f"\n✅ {value} {from_unit} = {result} {to_unit}")
        print("==================================================")

main()


