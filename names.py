from name_funct import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease enter your first name: ")
    if first == "q":
        break
    last = input("Please enter your last name: ")
    if last == "q":
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\nHello, {formatted_name}!")