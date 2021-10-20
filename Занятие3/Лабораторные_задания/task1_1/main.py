def task_1_1():
    sum_sq = 0
    a = 1
    n = 0
    max_sum_sq = 500
    while True:
        sum_sq += a ** 2
        if sum_sq > max_sum_sq:
            break
        else:
            a += 1
            n += 1
    return print(n, sum_sq)


if __name__ == "__main__":
    print(task_1_1())


