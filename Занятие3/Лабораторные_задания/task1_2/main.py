def factorial(n):
    a = 0
    fact = 1
    for i in range(n):
        a += 1
        fact = fact * a
    return print(fact)



if __name__ == "__main__":
    factorial(5)
