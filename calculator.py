# Define functions


# Define Addition function
def addition(x, y):
    return x + y


# Define Subtraction function
def subtraction(x, y):
    return x - y


# Define Multiplication function
def multiplication(x, y):
    return x * y


# Define Division function
def division(x, y):
    return x / y


# Define Exponent function
def exponent(x, y):
    return x**y


# Define Square Root function
def square_root(x):
    return x**0.5


# Define Square function
def square(x):
    return x**2


# Call functions
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponent")
print("6.Square Root")
print("7.Square")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6/7): ")

if choice in ("1", "2", "3", "4", "5", "6", "7"):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(num1, "+", num2, "=", addition(num1, num2))

    elif choice == "2":
        print(num1, "-", num2, "=", subtraction(num1, num2))

    elif choice == "3":
        print(num1, "*", num2, "=", multiplication(num1, num2))

    elif choice == "4":
        print(num1, "/", num2, "=", division(num1, num2))

    elif choice == "5":
        print(num1, "**", num2, "=", exponent(num1, num2))

    elif choice == "6":
        print(num1, "** 0.5 =", square_root(num1))

    elif choice == "7":
        print(num1, "** 2 =", square(num1))

else:
    print("Invalid Input")

# End of program
