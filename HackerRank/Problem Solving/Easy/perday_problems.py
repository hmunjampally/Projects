from difference_dates import *

if __name__ == '__main__':
    start = input("enter start date as mm-dd-yyyy:\n")
    end = input("enter end date as mm-dd-yyyy:\n")

    days = calc_days(start, end)

    number_problems = int(input("enter number of problems per day:\n"))

    print("total problems you solve are:", days*number_problems)