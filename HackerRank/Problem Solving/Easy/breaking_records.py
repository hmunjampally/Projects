n = 9
scores = [10,5,20,20,4,5,2,25,1]

maxi_count = 0
mini_count = 0
    
curr_max = scores[0]
curr_mini = scores[0]
    
for i in range(1, len(scores)):
    current = scores[i]

    if current > curr_max:
        maxi_count += 1
        curr_max = current

    if current < curr_mini:
        mini_count += 1
        curr_mini = current
            
print(maxi_count, mini_count)