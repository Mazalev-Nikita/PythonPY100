if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_new = [i - round(sum(list_)/len(list_)) for i in list_]
    print(list_new)