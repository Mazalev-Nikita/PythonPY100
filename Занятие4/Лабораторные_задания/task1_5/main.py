if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_even = [i for i in list_ if i % 2 == 0]
    list_not_even = [i for i in list_ if i % 2 != 0]
    if len(list_even) > len(list_not_even):
        print("Больше четных")
    elif len(list_even) == len(list_not_even):
        print("Одинаково")
    else:
        print("Больше нечетных")
