# Fizz Buzz is a classic programming problem. Here is its slightly modified version from class.

for i in range(1, 51):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
