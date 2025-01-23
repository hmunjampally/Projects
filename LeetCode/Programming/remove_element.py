nums = [3,2,2,3,3] 
val = 3

copy_nums = nums.copy()

for i in copy_nums:
    if i == val:
        nums.remove(i)

print(len(nums))