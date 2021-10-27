if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    def new_list(list_random):
        return [i ** 3 if i > 0 else 0 for i in list_random]

    print(new_list(list_))
