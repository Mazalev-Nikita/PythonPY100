if __name__ == "__main__":
    def list_new(n, m):
        return [i for i in range(n, m+1) if i > (sum(range(n, m+1))/len(range(n, m+1)))]
    print(list_new(1,10))
