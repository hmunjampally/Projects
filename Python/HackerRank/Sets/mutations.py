a = int(input()) # number of elements in set A
A = set(map(int, input().split()))
N = int(input())  # number of other sets


for i in range(N):
    op, x = input().split()
    values = set(map(int, input().split()))
    if op == "intersection_update":
        A.intersection_update(values)
    if op == "update":
        A.update(values)
    if op == "symmetric_difference_update":
        A.symmetric_difference_update(values)
    if op == "difference_update":
        A.difference_update(values)
    
print(sum(A))