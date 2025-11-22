#Write a Python program to demonstrate handling multiple exceptions.


def multiple_exceptions_demo():
    try:
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter another integer: "))
        result = num1 / num2  # This may raise ZeroDivisionError
        print(f"Result of division: {result}")
        
        # This will raise IndexError if num1 is out of range for the list
        sample_list = [1, 2, 3]
        print(f"Accessing list element at index {num1}: {sample_list[num1]}")

    except ValueError:
        print("ValueError: Invalid input! Please enter an integer.")
    except ZeroDivisionError:
        print("ZeroDivisionError: Division by zero is not allowed.")
    except IndexError:
        print("IndexError: Index out of range for the list.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the demo
multiple_exceptions_demo()
