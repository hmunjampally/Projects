from itertools import permutations

if __name__ == '__main__':
    A, B = input().split()
    
    x = [*permutations(sorted(A), int(B))]
    print(A)
    print(B)
    for i in x:
       print(''.join(i))
        