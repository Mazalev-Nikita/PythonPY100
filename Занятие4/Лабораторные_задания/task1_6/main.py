if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    a = list_[0]
    list_new = [i for i in list_ if i > a]
    print(list_new)