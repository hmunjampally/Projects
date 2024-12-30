"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NxM. (N is an odd natural number, M and 3 is N times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
"""

if __name__ == "__main__":
    N, M = input().split() #N odd natural number; M = 3N
    x = ".|."
    reverse_list = []
    rows = (int(N)//2) + 1
    cols = (int(M)//2) + 1
    
    for i in range(1, int(N)+1):
        if 1 <= i < rows:
            reverse_list.append((2*i-1))
            print(((2*i-1)*x).center(int(M), '-'))
        
        if i == rows:
            print("WELCOME".center(int(M), '-'))
            
        if rows < i <= int(N):
            y = reverse_list[int(N)-i]
            print((y*x).center(int(M), '-'))