
from itertools import groupby

if __name__ == '__main__':
    string = input()
    for key,value in groupby(string):
        x = (len(list(value)), int(key))
        print(x, end=" ")

