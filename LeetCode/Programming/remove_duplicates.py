nums = [1,1,1,2,2,3,3,4]
count = 0
sort_nums = []

copy_nums = nums.copy()

for i in copy_nums:
    if i not in sort_nums:
        sort_nums.append(i)
        nums.remove(i)
        count += 1
        
for i in range(len(sort_nums)-1, -1,-1):
            nums.insert(0,sort_nums[i])

print(count)
print(nums)


