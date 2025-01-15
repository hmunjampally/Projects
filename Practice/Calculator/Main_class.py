from arithematic_calculations import *


def calculator():
    while True:
        operation = input("enter the character from +,-,/,*,pow2 for calculation and exit for exiting the calcuklator \n")
        if (operation == "exit"):
            print("calculator is closed")
            break
    
        if(operation not in ['+', '-', '*', '/', 'pow2']):
            print("Invalid operation please enter from +,-,/,*,pow2")
            continue

        number = input("enter numbers/integers separated by comma(,) or space \n")
        number = number.replace(",", " ")

        number = list(map(float, number.split()))
    
        if(len(number) < 2):
            print("minimum of two numbers are needed")
            continue

        if(operation == "+"):
            addition(number)
    
        if(operation =="-"):
            substraction(number)
        
        if(operation =="/"):
            division(number)
        
        if(operation =="*"):
            multiplication(number)

if __name__ == "__main__":
    calculator()

        # if(operation =="pow2"):
        #     if(len(number) > 2):
        #         print("sorry only single integer can perform power 2")
        #     pow2()
    

