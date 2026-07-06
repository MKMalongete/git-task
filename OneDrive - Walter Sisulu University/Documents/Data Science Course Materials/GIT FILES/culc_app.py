# A simple calculator application that performs calculations

def format_number(number):
    """
    This function removes .0 from whole numbers.
    Example: 24.0 becomes 24
    """
    if number == int(number):
        return str(int(number))
    else:
        return str(number)


def get_number(message):
    """
    This function keeps asking the user for a number
    until they enter a valid one.
    """
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def perform_calculation():
    """
    This function performs a calculation and saves it to equations.txt.
    """
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    operation = input("Enter an operation (+, -, *, or /): ")

    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: You cannot divide by zero.")
            return
        answer = num1 / num2
    else:
        print("Invalid operation. Please use +, -, *, or /.")
        return

    equation = (
        format_number(num1) + " " + operation + " " +
        format_number(num2) + " = " + format_number(answer)
    )

    print("Answer:", equation)

    with open("equations.txt", "a", encoding="utf-8") as file:
        file.write(equation + "\n")

    print("The equation has been saved to equations.txt.")


def print_previous_calculations():
    """
    This function reads and displays previous calculations
    from equations.txt.
    """
    try:
        with open("equations.txt", "r", encoding="utf-8") as file:
            calculations = file.read()

            if calculations == "":
                print("There are no previous calculations yet.")
            else:
                print("\nPrevious calculations:")
                print(calculations)

    except FileNotFoundError:
        print("No previous calculations found. The equations.txt file does not exist yet.")


while True:
    print("\nSimple Calculator Application")
    print("1. Perform a calculation")
    print("2. Print previous calculations")
    print("3. Exit")

    choice = input("Choose an option 1, 2, or 3: ")

    if choice == "1":
        perform_calculation()
    elif choice == "2":
        print_previous_calculations()
    elif choice == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")