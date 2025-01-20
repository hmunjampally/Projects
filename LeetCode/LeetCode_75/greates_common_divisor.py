str1 = "ABABABAB" 
str2 = "ABAB"

for i in range(1,len(str2)+1):
    if len(str2) % i == 0:
        new_str2 = str2[:i]
        if new_str2 * (len(str2) // i) == str2:
            break
if new_str2 * (len(str1) // len(new_str2)) == str1:
    print(new_str2)
else:
    print("")

