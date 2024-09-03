
if __name__ == '__main__':
    digits = [-1,-2,-3,-4,3,2,1]
    x = 1
    for i in digits:
        x *= i
    if x > 0:
        print(1)
    if x < 0:
        print(-1)
    if x == 0 :
        print(0)