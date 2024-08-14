test_cases = int(input())  # number of test cases
for i in range(test_cases):
    no_of_A = int(input())  # number of elements in A
    A = set(map(int, input().split()))
    no_of_B = int(input())  # number of elements in B
    B = set(map(int, input().split()))
    
    print(A.issubset(B))