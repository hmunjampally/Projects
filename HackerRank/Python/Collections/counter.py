

if __name__ == '__main__':
    X = int(input())
    shoes_sizes = list(map(int, input().split()))
    no_of_customers = int(input()) 
    
    total = []
    for i in range(no_of_customers):

        size, price = map(int, input().split())
        if size in shoes_sizes:
            total.append(price)
            shoes_sizes.remove(size)
    print(sum(total))



