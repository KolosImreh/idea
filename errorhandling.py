def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Please provide valid numbers for division.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division successful!")

# Example usage:
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    divide_numbers(num1, num2)
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
