
if __name__ == '__main__':
    first = 'x'
    second = 'xx'

    sec = [i for i in second]
    fir = [i for i in first]

    for i in sec:
        if i in fir:
            fir.remove(i)
        else:
            print(i)
