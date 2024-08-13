def print_rangoli(size):
    # your code goes here
    S, count, list = "", 0, []
    for i in range((96+size), 96, -1):
        if i == (96+size):
            S += f"{chr(i)}"
            list.append(S)
            pattern(S, (3*size)+size-3)
        elif i == (96+size-1):

            S += f"-{chr(i)}-{S[::-1]}"
            list.append(S)
            count += 2
            pattern(S, (3*size)+size-3)
        else:

            S = S[:-count]
            count += 2
            S += f"-{chr(i)}-{S[::-1]}"
            list.append(S)
            pattern(S, (3*size)+size-3)
    for j in range(len(list)-2, -1, -1):
        pattern(list[j], (3*size)+size-3)
def pattern(string, w):
    print(string.center(w, "-"))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)