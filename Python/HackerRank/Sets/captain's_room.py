# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

k = int(input())
room_list = list(map(int, input().split()))
count = Counter(room_list)
for i in count:
    if count[i] == 1:
        captain = i
print(captain)


"""
Counter returns a dictionary keys being the list values 
 and its paired value being its occurence

"""