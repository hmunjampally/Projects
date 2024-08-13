import textwrap


if __name__  == '__main__':
    new = "AAABABCDD"
    news = textwrap.wrap(new, 3)
    empty = []

    for i in news:
        if len(i) == 3:
            if i[0] == i[1] == i[2]:
                empty.append(i[0])
            elif i[0] == i[1] and i[1] != i[2]:
                x = i[0]+i[2]
                empty.append(x)
                
            elif i[0] != i[1] and i[1] == i[2]:
                x = i[0]+i[1]
                empty.append(x)
               
            elif i[0] == i[2] and i[1] != i[2]:
                x = i[0]+i[1]
                empty.append(x)
                
            else:
                x = i[0]+i[1]+i[2]
                empty.append(x)
    print(empty)

    """
    if no clue of length of substring to make


    
    def merge_the_tools(string, k):
    
    substring = textwrap.wrap(string, k)

    result = []
    
    
    for sub in substring:
        seen = set()  
        unique_substring = ""  
        
        
        for char in sub:
            if char not in seen:  
                seen.add(char) 
                unique_substring += char  
        
        result.append(unique_substring)  
    
    
    for res in result:
        print(res)
    
    
    
    """