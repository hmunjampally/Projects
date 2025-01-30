l1 = [2,4,3]
l2 = [5,6,4]
x = 0
y = 0

for i in range(len(l1)-1,-1,-1):
    x = x*10 + l1[i]
for i in range(len(l2)-1,-1,-1):
    y = y*10 + l2[i]

sum_l = x+y
new_l = [int(i) for i in str(sum_l)]
print(new_l[::-1])