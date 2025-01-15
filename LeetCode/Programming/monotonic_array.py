if __name__ == '__main__':
    nums = [1, 3, 2]
    increasing = True
    decreasing = True
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
           increasing = False
        if nums[i] < nums[i-1]:
            decreasing = False
    print(increasing, decreasing)