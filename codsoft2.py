# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to calculate exponentiation
def exponentiate(x, y):
    return x ** y

# Function to calculate modulus
def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero."
    else:
        return x % y

# Main function to run the calculator
def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")

    # Get user input for operation choice
    choice = input("Enter operation number (1/2/3/4/5/6): ")

    # Get user input for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform operation based on user choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", exponentiate(num1, num2))
    elif choice == '6':
        print("Result:", modulus(num1, num2))
    else:
        print("Invalid operation choice")

if __name__ == "__main__":
    main()
