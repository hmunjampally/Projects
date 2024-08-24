from collections import defaultdict

if __name__ == '__main__':

    n, m = map(int, input().split())
    A = []
    B = []
    
    finals = defaultdict(list)
    
    for i in range(n):
        A.append(input())
       
    for i in range(m):
        B.append(input())

    for indexOfA, valueOfA in enumerate(A):
        finals[valueOfA].append(indexOfA+1)

    for match in B:
        if match in finals.keys():
            print(' '.join(map(str, finals[match])))
        else:
            print('-1')

