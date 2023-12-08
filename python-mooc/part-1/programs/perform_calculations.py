def perform_calculation(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        return operator, num1, num2
    except ValueError as ve:
        raise ValueError("Invalid input. Please enter valid numbers.") from ve

def main():
    try:
        while True:
            operator, num1, num2 = get_user_input()
            result = perform_calculation(operator, num1, num2)
            print(f"Result: {result}")

            another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another_calculation != 'yes':
                break
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

