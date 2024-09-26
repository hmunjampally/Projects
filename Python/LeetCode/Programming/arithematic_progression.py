if __name__ == '__main__':
    arr = [1,2,4]
    progression = True
    arr.sort()
    common_difference = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != common_difference:
            print(False)
    print(True)