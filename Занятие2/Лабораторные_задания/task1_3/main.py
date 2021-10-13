a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
summa_kv = a ** 2 + b ** 2
kv_summi = (a + b) ** 2
if summa_kv > kv_summi:
    print("Сумма квадратов больше квадрата суммы")
elif summa_kv == kv_summi:
    print("Сумма квадратов равна квадрата суммы")
else:
    print("Сумма квадратов меньше квадрата суммы")
