def kolvo_mes(s, a, b):
    c = s + a
    n = 0
    while c > b:
        b = b * 1.05
        n += 1
        print (n, c, b)
    return


if __name__ == "__main__":
    kolvo_mes(100, 50, 100)
