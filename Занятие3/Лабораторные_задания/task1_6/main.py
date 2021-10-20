def rashod(a, b):
    c = 0
    for n in range(1, 11):
        c = c + (b - a)
        b = b * 1.03
        print (n, b, c)
    print(c)


if __name__ == "__main__":
    rashod(80, 100)
