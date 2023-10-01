# Select the second largest of three numbers from user input.

def secondlargest(a,b,c):
    if a > b and a > c:
        if b > c:
            print(b)
        else:
            print(c)
    elif b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        if a > b:
            print(a)
        else:
            print(b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(secondlargest(a,b,c))

