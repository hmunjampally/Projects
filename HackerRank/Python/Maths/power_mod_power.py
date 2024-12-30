# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    
    a = int(input())
    b = int(input())
    m = int(input())
    
    
    print(pow(a, b)) # this is a**b
    print(pow(a, b, m))  # this in simple means pow(a, b) % m
    