# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    M = int(input()) #numbers of values in set a
    a = set(map(int, input().split()))
    N = int(input()) #numbers of values in set b
    b = set(map(int, input().split()))
   
    for i in sorted(a.symmetric_difference(b)):
        print(i)


    """
    x = a.difference(b)
    y = b.difference(a)

    for i in sorted(x):
        print(i)
    
    for i in sorted(y):
        print(i)
    
    """
