list_1 = [12, 3, 4, 10]
last_digit = list_1.pop(-1)
list_1.insert(0, last_digit)
print(list_1)

list_1 = [1]
last_digit = list_1.pop(-1)
list_1.insert(0, last_digit)
print(list_1)

list_1 = []
list_1 = list_1[-1:] + list_1[:-1]
print(list_1)