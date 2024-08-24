
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

if __name__ == '__main__':
    N = int(input())
    
    item_list = OrderedDict()
    for i in range(N):
        *item, price = input().rsplit(' ', 1)
        item = (''.join(item))
        price = int(price)
        if item in item_list:
            item_list[item] += price
        else:
            item_list[item] = price


for item, price in item_list.items():
    print(f"{item} {price}")