def leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

print("Leap Year Checker 🗓️")
while True:
    print("")
    year = int(input("Enter a year to check if it's a leap year: "))
    if leap_year(year):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year.")
    pg = input("\ncheck another year?(y/n):").lower()
    if pg == "n":
        print("\nA leap year means 24 extra hours to make a year memorable. Make every second count. —hazellenuts")
        break
    elif pg == "y":
        continue
    else:
        print("let's just continue :>")
        continue