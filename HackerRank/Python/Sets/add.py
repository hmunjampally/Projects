# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    N = int(input()) # the total number of country stamps
    
    names= set()
    
    for i in range(N):
        countryNames = input()
        names.add(countryNames)
    print(len(names))