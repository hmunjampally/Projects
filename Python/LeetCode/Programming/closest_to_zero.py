if __name__ == '__main__':
    nums = [-10, -10]
    close = nums[0]
    for i in nums:
        if abs(i) < abs(close):
            close = i

    if close < 0 and abs(close) in nums:
        print(abs(close))
    print(close)