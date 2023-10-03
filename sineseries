# Write a basic python function to find the Sine Series of a given number upto n terms. The function with the given value of X: 2 with the max limit of 7 = 0.9079365079365079
 

sign = 1
for i in range(1, 8):
    print(f"Sign = {sign}")
    sign = sign * -1

x = int(input("Enter the value of x: "))
n = int(input("Enter the number of times to repeat: "))

result = 0
sign = 1
list = []
for i in range(1, n+1):
    result = result + sign * (x**i)
    list.append(result)
    sign = sign * -1

print(f"The result is {result}")
print(list)

