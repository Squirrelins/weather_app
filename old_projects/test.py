# # Bubblesort algorythm

# import random

# def bubblesort(array):
#     for i in range(len(array)):
#         for j in range(len(array)-1):
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#     return array

# def main():
#     array = [random.randint(0,100) for i in range(10)]
#     print(array)
#     print(bubblesort(array))

# if __name__ == '__main__':
#     main()

# Bubblesort

l = [1, 4, 5, 3, 2, 0, -1]


def max(l):  # print the max value in the list
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max


print(max(l))

# def bubblesort(l):
#     for i in range(len(l)):
#         for j in range(len(l)-1):
#             if l[j] > l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]
#     return l

# print(bubblesort(l))
