if __name__ == '__main__':
    size = 10
    arr = [161, 167, 170, 171, 174, 176, 182, 154]
    sums = sum(set(arr))
    total = len(set(arr))
    print(sums/total)