if __name__ == '__main__':
    ops = ["5","-2","4","C","D","9","+","+"]
    result = []

    for i in range(len(ops)):
        try:
            result.append(int(ops[i]))
        except ValueError:
            if ops[i] == "+" and len(result) >= 2:
                x = result[-1] + result[-2]
                result.append(x)
            if ops[i] == "D":
                x = result[-1]*2
                result.append(x)
            if ops[i] == "C":
                result.pop()
    print(sum(result))