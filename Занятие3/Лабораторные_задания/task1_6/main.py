def rashod(a, b):
    c = 0
    for n in range(0, 10):
        c = c + (b - a)
        b = int(b * 1.03)
        print (n, b, c)
    print(c)


if __name__ == "__main__":
    rashod(5000, 6000)
