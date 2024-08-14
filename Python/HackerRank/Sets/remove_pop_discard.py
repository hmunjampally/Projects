n = int(input())
s = set(map(int, input().split()))
N = int(input())   # N commands

for i in range(N):
    command = input()
    if command == "pop":
        s.pop()
    elif "remove" in command:
        op, x = command.split()
        s.remove(int(x))
    elif "discard" in command:
        op, x = command.split()
        s.discard(int(x))

print((sum(s)))





"""
sample case

10        
0 1 2 3 4 5 6 7 8 9
19
remove 1
pop
pop
discard 1
discard 2
discard 3
discard 2
remove 6
pop
discard 6
discard 1
discard 8
discard 2
pop
discard 1
discard 8
discard 3
discard 1
discard 0


"""