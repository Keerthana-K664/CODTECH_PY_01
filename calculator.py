def calculator():
    print("Welcome to the Basic Calculator!")

    # Input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Perform all arithmetic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (Division by zero)"

    # Display results of all operations
    print("\nResults of all operations:")
    print(f"Addition (+): {addition}")
    print(f"Subtraction (-): {subtraction}")
    print(f"Multiplication (*): {multiplication}")
    print(f"Division (/): {division}")

# Run the calculator
calculator()
s