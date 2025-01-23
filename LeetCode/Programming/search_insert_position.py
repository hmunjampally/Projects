nums = [1,3,5,6] 
target = 5

for i in nums:
    if i == target:
        print(nums.index(i))
        break
    
    else:
        nums.append(target)
        nums.sort()