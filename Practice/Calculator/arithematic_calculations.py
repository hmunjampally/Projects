def addition(list):
    sum = 0
    for i in list:
        sum = sum + i
        #list.index(i) gives position of i
    print(sum)

def substraction(list):
    sub = 0
    for x in list:
        sub = x- sub 
    print(abs(sub))

def division(list):
    div = 1
    for x in list:
        if(x == 0):
            print("division is not possible with 0")
        div = x / div
    print(div)

def multiplication(list):
    multi = 1
    for x in list:
        multi = x * multi
    print(multi)

# def pow2(list):
#     print("**2")