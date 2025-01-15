if __name__ == '__main__':
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = 'XV'

    total = 0
    for i in range(len(s) - 1):
        cur = romans[s[i]]
        nex = romans[s[i+1]]
        if cur < nex:
            total -= cur
        else:
           total += cur
    total += romans[s[-1]] 
    print(total)   