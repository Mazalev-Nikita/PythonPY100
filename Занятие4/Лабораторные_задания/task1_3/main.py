if __name__ == "__main__":
    def list_sq(n, m):
        return [i for i in range(n, m) if i % 2 == 0]

    print(len(list_sq(2, 4)))
