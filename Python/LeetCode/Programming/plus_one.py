if __name__ == '__main__':
    digits = [9]
    new_str = ""
    for i in digits:
        new_str += str(i)
    new_num = int(new_str) + 1
    new_list = [int(i) for i in str(new_num)]
    print(new_list)


    """last = digits[-1]
    digits.pop()
    digits.append(last+1)
    print(digits)"""
        