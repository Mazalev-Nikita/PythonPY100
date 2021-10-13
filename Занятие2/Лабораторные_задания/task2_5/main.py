list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3]

count_even = 0  # количество четных чисел
count_odd = 0  # количество нечетных чисел

for i in range(len(list_)):
    current_value = list_[i]
    if current_value % 2 == 0:


if count_even > count_odd:
    print('Четных чисел больше')
else:
    print('Нечетных чисел больше')
