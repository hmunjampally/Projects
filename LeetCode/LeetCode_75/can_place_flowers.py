flowerbed = [0,0]
n = 1
times = 0

if len(flowerbed) == 1:
    if flowerbed[0] == 0 and n==1:
        print(True)
        exit()

    elif flowerbed[0] == 1 and n==1:
        print(False)
        exit()

    elif flowerbed[0] == 1 and n==0:
        print(True)
        exit()

if len(flowerbed)>1 and flowerbed[0] == 0 and flowerbed[1] == 0 and times<n:
    flowerbed[0] = 1
    times += 1

if len(flowerbed)>1 and flowerbed[-1] == 0 and flowerbed[-2] == 0 and times<n:
    flowerbed[-1] = 1
    times += 1

for i in range(1,len(flowerbed)-1):
    prev = flowerbed[i-1]
    curr = flowerbed[i]
    next = flowerbed[i+1]
    
    if prev == 0 and curr == 0 and next == 0 and times<n:
        flowerbed[i] = 1
        times += 1
    
if times >=n:
    print(True)
    print(flowerbed)
    exit()

else:
    if times<n:
        print(False)   
        print(flowerbed)     