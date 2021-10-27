if __name__ == "__main__":
    num1 = int(input("Введите число: "))
    list_ = [int(i) for i in str(num1)]
    print(list_)
    print(sum(list_))
    list_even = [i for i in list_ if i % 2 == 0]
    print(sum(list_even))
    print(min(list_))
    print(max(list_))
    list_non_even_index = []
    print(list_[::2])
    print(list_[1::2])
    print(list_[1] - list_[-1])
    index_1 = list[1]
    min_index = []

        # num1 = 12345
        # print(list(str(num1)))
        #
        # # Конструкция для разбития числа на цифры
        # digits_list = [int(d) for d in str(num1)]
        # print(digits_list)
        #
        # join_num = "".join([str(d) for d in digits_list])
        # print(int(join_num))