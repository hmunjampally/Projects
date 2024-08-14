A = set(map(int, input().split()))
n = int(input())

superset = "True"

for i in range(n):
    x = set(map(int, input().split()))
    if A.issuperset(x) != True:
        superset = "False"
print(superset)
