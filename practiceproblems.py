# def radian (degree):
#     return degree * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 / 180
# def degree (radian):
#     return radian * 180 / 3.141592653589793238462643383279502884197169399375105820974944592307816406286
# def main():
#     print("This program converts radians to degrees and vice versa.")
#     print("1. Convert radians to degrees")
#     print("2. Convert degrees to radians")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         rad = float(input("Enter the number of radians: "))
#         print("The number of degrees is", degree(rad))
#     elif choice == 2:
#         deg = float(input("Enter the number of degrees: "))
#         print("The number of radians is", radian(deg))
#     else:
#         print("Invalid choice.")

# main()

# Sort a list

# list1 = input("Enter a list of numbers separated by spaces: ").split()
# list1 = [int(num) for num in list1]
# descending = input("Sort in descending order? (y/n): ")
# if descending == 'y':
#     list1.sort(reverse=True)
# else:
#     list1.sort()
# print(list1)

# Calculate the discount of an item

item = float(input("Enter the price of the item: "))
discount = float(input("Enter the discount percentage: "))
print("The price of the item after the discount is", item * (1 - discount / 100))