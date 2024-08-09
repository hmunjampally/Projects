if __name__ == '__main__':
    temp = [2,5,5,11]
    val = 10
    result = []
    for i in range(0, len(temp)-1):
        rem = val - temp[i]
        if rem in temp[i+1:]:
            result.append(i)
            result.append(temp.index(rem)+1)
    print(result)
    
