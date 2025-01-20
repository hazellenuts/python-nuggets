import math

def circle_area(radius):
    return math.pi*radius*radius

def rectangle_area(length, width):
    return length*width

def triangle_area(base, height):
    return (base*height)/2

def square_area(side):
    return side*side

def main_menu():
    print("\nArea Calculator 📐🧮")
    print("""
1. Circle
2. Rectangle
3. Triangle
4. Square
""")
    
def main():
    while True:
        main_menu()
        choice = input("Select a shape (1-4): ")
        if choice == "1":
            radius = float(input("Enter the radius of the circle: "))
            area = circle_area(radius)
            print(f"the area of the circle is: {area:.2f} square units")
        elif choice == "2":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = rectangle_area(length, width)
            print(f"the area of the rectangle is: {area:.2f} square units")
        elif choice == "3":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = triangle_area(base, height)
            print(f"the area of the triangle is: {area:.2f} square units")
        elif choice == "4":
            side = float(input("Enter the side of the square: "))
            area = square_area(side)
            print(f"the area of the square is: {area:.2f} square units")
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

        print("")

        pg = input("Do you want to calculate another area? (y/n): ").lower()
        if pg != "y":
            print("bye! —hazellenuts")
            break
        print("===========================================================")
if __name__ == "__main__":
    main()