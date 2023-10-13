my_tuple = (1, "two", 3.0, [4, "four"], 5)

z, *y, x = my_tuple

print(z)

dict1 ={"1": "one", "2": "two", "3": "three"}
dict2 ={"4": "four", "5": "five", "6": "six"}

dict3 = {**dict1, **dict2}

print(dict3)

