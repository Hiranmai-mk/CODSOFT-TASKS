def simple_calculator():

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the operation (+, -, *, /): ")

    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    else:
        return "Invalid operation. Please choose +, -, *, or /."

   
    return f"The result of {num1} {operation} {num2} is: {result}"


print(simple_calculator())
