#Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
#input).


def simple_calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            print("Invalid operation selected.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values for numbers.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

# Run the calculator
simple_calculator()
