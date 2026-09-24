number_1 = float(input("Введіть перше число: "))
operation = input("Введіть дію над числами: ")
number_2 = float(input("Введіть друге число: "))

if operation == '+':
    print("Результат: ", number_1 + number_2)
elif operation == '-':
    print("Результат: ", number_1 - number_2)
elif operation == '*':
    print("Результат: ", number_1 * number_2)
elif operation == '/':
    if number_2 != 0:
        print("Результат: ", number_1 / number_2)
    else:
        print("Ділити на 0 не можна!")
else:
    print("Введіть дію +, -, *, /")

