if __name__ == '__main__':
    a = "1010"
    b = "1011"

    x = max(len(a), len(b))

    for i in range(x):
        if a[i] + b[i]:
            print(1)