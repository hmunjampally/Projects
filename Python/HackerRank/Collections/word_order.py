from collections import  Counter

if __name__ == '__main__':
    
    N = int(input())
    words = []
    
    for i in range(N):
        words.append(input())
        
    x = Counter(words)
    print(len(x))
    print(*x.values())