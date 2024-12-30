# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

if __name__ == '__main__':
    
    N = int(input())
    temp = deque()
     
    for i in range(N):
        data = input().split()
        op = data[0]
        if len(data) > 1:
            val = int(data[1])  
        
        if op == 'append':
            temp.append(val)
        if op == 'pop':
            temp.pop()
        if op == 'popleft':
            temp.popleft()
        if op == 'appendleft':
            temp.appendleft(val)
            
    for i in range(len(temp)):
        print(temp[i], end=" ")
            
            
             
             
             