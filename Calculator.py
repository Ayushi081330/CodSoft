def Addition(a, b):
    return a + b

def Subtraction(a, b):
    return a - b

def Multplication(a, b):
    return a * b

def Division(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice your choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", Addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Subtraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Multplication(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Division(num1, num2))
        break
    else:
        print("Invalid Input")
