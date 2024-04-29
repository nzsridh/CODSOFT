import math

# Function to perform basic arithmetic operations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    elif operator == '^':
        return num1 ** num2
    elif operator == 'sqrt':
        if num1 >= 0:
            return math.sqrt(num1)
        else:
            return "Error: Cannot calculate square root of a negative number!"
    else:
        return "Error: Invalid operator!"

# Function to check if the input is a valid number
def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

# Function to check if the input is a valid operator
def is_operator(input_str):
    operators = ['+', '-', '*', '/', '^', 'sqrt']
    return input_str in operators

def main():
    result = None

    while True:
        if result is not None:
            print(f"\nPrevious result: {result}")

        num1 = input("\nEnter the first number (or press Enter to use previous result): ")
        if num1 == '':
            if result is None:
                print("No previous result available.")
                continue
            num1 = result
        elif not is_number(num1):
            print("Invalid input. Please enter a valid number.")
            continue
        else:
            num1 = float(num1)

        num2 = input("Enter the second number: ")
        if not is_number(num2):
            print("Invalid input. Please enter a valid number.")
            continue
        else:
            num2 = float(num2)

        operator = input("Enter the operator (+, -, *, /, ^ for power, sqrt for square root): ")
        if not is_operator(operator):
            print("Invalid operator. Please enter a valid operator.")
            continue

        result = calculate(num1, num2, operator)
        print(f"\nResult: {result}")

        choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
