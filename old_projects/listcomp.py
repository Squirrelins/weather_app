# list = [i for i in range(1000)]
# even_list = [x for x in list if x % 2 == 0]
# odd_list = [x for x in list if x % 2 == 1]
# print(even_list)
# print(odd_list)

# list = [i for i in range(1000)]
# even_or_odd = [(even, odd) for even in list if num % 2 == 0]

odd = []
even = []

nums = [i for i in range(1, 1001)]
even = [i for i in nums if i % 2 == 0 or odd.append(i)]
# Prime Numbers to 1000
prime = []
# for i in nums:
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             prime.append(i)
prime = [
    i for i in nums if i > 1 and all(i % j != 0 for j in range(2, int(i**0.5) + 1))
]


print(f"Number list : {nums}")
print(f"Even Numbers List : {even}")
print(f"Odd Numbers List : {odd}")
print(f"Prime Numbers List : {prime}")


even_count = len(even)
odd_count = len(odd)
prime_count = len(prime)
list_count = len(nums)

print(
    f"Even numbers : {even_count}, Odd numbers : {odd_count}, Prime numbers : {prime_count}, there was originally : {list_count} numbers."
)

# Print the even prime number in the list.
even_prime = [i for i in even if i in prime]
print(f"Even prime numbers : {even_prime}")