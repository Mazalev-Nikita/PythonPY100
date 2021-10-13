a = int(input("Введите число А: " ))
b = int(input("Введите число В: " ))
cond_1 = a % 2 != 0
cond_2 = b % 2 != 0
if cond_1 and cond_2:
    print("Числа нечетные")
elif cond_1 or cond_2:
    print("Одно число нечетное")
else:
    print("Оба числа четные")