if __name__ == '__main__':
    nums = [1,2,2,10]
    nums.sort(reverse=True)
    
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] + nums[i+2]:
            print(nums[i] + nums[i+1] + nums[i+2])