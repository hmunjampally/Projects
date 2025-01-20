s = "3[a]2[bc]"

stack = []
current_num = 0
current_str = ""
    
for char in s:
    if char.isdigit():
            # Build the full number (to handle multi-digit numbers)
        current_num = current_num * 10 + int(char)
    elif char == '[':
            # Push the current number and string onto the stack
        stack.append((current_num, current_str))
        current_num = 0
        current_str = ""
    elif char == ']':
            # Pop from the stack, repeat the string, and append to the current string
        num, prev_str = stack.pop()
        current_str = prev_str + current_str * num
    else:
            # Build the current substring
        current_str += char
    
print(current_str)

"""stacking=[]
new_string = ""
multiplier = 0

for i in s:
    if i.isdigit():
        multiplier = multiplier*10 + int(i)
    elif i == '[':
        stacking.append((multiplier, new_string))
        new_string = ""
        multiplier = 0
    elif i == ']':
        multiplier, prev_string = stacking.pop()
        new_string = prev_string + new_string * multiplier
    else:
        new_string += i
print(new_string)
"""
