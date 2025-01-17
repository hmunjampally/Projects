from itertools import groupby

chars = ["a","a","a","b","b","a","a"]

new_char = "".join(chars)
new_list = []

x = groupby(new_char)
count = 0

for key, value in x:
    chars[count] = key
    count += 1

    if len(list(value)) > 1:
        for num in str(len(list(value))):
            chars[count] = num
            count += 1

print(count)