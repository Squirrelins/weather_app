# # Define Even or Odd from user inputed integer.


# # Even
# def even(x):
#     if x % 2 == 0:
#         return print("This is an even number")
#     else:
#         return print("This is an odd number")


# x = int(input("Enter a integer (Ex: 1, 2, 3, 4 (Think whole number)): "))

# even(x)


# def temp(x):
#     if x >= 65:
#         return True
#     else:
#         return False


# x = int(input("Enter a temperature(in F): "))

# print(temp(x))

# if temp(x) == True:
#     print("You don't need a jacket")

# else:
#     print("You need a jacket")

# Offer a loan if someone has been employeed for more than 2 years and makes a salary of at least 30000. Else, deny the loan.


# def loan(x, y):
#     if x >= 2 and y >= 30000:
#         return True
#     else:
#         return False

# x = int(input("How many years have you been employed?: "))
# y = int(input("Please enter your annual salary: "))
# print(loan(x, y))

# if loan(x, y) == True:
#     print("You qualify for a loan!")
# else:
#     print("You do not qualify for a loan.")


x = float(input("Enter the grade you got on your test (1-100): "))

if x >= 90:
    print("Your grade is an A!")
elif x >= 80:
    print("Your grade is a B!")
elif x >= 70:
    print("Your grade is a C!")
elif x >= 60:
    print("Your grade is a D!")
else:
    print("Your grade is a F! Whoops! ...Should've studied harder!")
