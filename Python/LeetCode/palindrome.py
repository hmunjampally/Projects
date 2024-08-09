if __name__ == '__main__':
    original = 121
    palin = original
    temp = 0
    while palin > 0:
        div = palin % 10
        temp = temp*10 + div
        palin = palin // 10

    if temp == original:
        print(True)
    else:
        print(False)