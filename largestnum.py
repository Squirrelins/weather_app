def largestnum(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(largestnum(a,b,c))

