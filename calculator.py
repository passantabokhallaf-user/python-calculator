
import math

def display_menu():
    print("\nCalculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")

while True:
    display_menu()

    choice = input("Choose an option: ")

    if choice == "7":
        print("Calculator closed.")
        break

    if choice == "6":
        num = float(input("Enter a number: "))
        if num < 0:
            print("Cannot calculate square root of a negative number.")
        else:
            print("Result:", math.sqrt(num))
        continue

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            if num2 == 0:
                print("Division by zero is not allowed.")
                continue
            result = num1 / num2
        elif choice == "5":
            result = num1 ** num2

        print("Result:", result)
    else:
        print("Invalid option. Try again.")

