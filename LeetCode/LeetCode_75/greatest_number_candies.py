candies = [2,3,5,1,3] 
extraCandies = 3

max_candies = max(candies)
newCandies = []

for i in candies:
    new_max = i + extraCandies

    if new_max >= max_candies:
        newCandies.append(True)
    else:
        newCandies.append(False)
print(newCandies)
