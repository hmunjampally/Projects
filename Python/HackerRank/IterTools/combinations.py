# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == '__main__':
    string, x = input().split()
    
    comb = [*combinations_with_replacement(sorted(string), int(x))]
    for i in comb:
        print(''.join(i))