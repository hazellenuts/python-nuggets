roman = {
    "M": 1000, 
    "CM": 900,
    "D": 500, 
    "CD": 400, 
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4, 
    "I": 1
}

def int_to_roman(num):
    roman_numeral = ""
    for symbol, val in roman.items():
        while num >= val:
            roman_numeral += symbol
            num -= val
    return roman_numeral

def main():
    print("Roman Numeral Converter 🌹🏛️")
    try:
        num = int(input("Enter a number (1 to 3999): "))
        if 1 <= num <= 3999:
            roman = int_to_roman(num)
            print(f"Roman Numeral: {roman}")
            print("\nRome was not built in a day.\n—hazellenuts")
        else:
            print("please enter number between 1 and 3999.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()