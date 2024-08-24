from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    x = input().split()
    K =int(input())

    comb = list(combinations(x, K))
    a_count = []
    for char in comb:
        if 'a' in char:
            a_count.append(char)
    
    prob = len(a_count)/ len(comb)
    print(round(prob,3))