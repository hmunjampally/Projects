
nums = [5,4,3,2,1]
first = 1
second = 1

for i in nums:
    if i <= first:
        first = i
    elif i <= second:
        second = i
    else: 
        print(True)
        break
print(False)


"""
for i in range(1, len(nums)-1):
    prev_ind = i-1
    curr_ind = i
    next_ind = i+1
    prev = nums[i-1]
    curr = nums[i]
    next = nums[i+1]

    if  (prev_ind< curr_ind < next_ind) and (prev < curr < next):
        print(True)
        break
    
else:
    print(False)"""
    