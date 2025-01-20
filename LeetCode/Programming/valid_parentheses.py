s = "([])"

stack = []

new_s = []

for i in s:
    if i == '(' or i == '{' or i == '[':
        stack.append(i)
    else:
        new_s.append(i)
        
"""print(new_s)
print(stack)
print(ord(stack[1]))
print(ord(new_s[1]))"""

for i in range(len(new_s)-1, -1, -1): 
    if (ord(new_s[i]) == 93 and ord(stack.pop()) == 91) or (ord(new_s[i]) == 125 and ord(stack.pop()) == 123) or (ord(new_s[i]) == 41 and ord(stack.pop()) == 40):
        print(True)
    else:
        print(False)
        break
    
    
    
"""if (i == '}' and stack[-1] == '{') or (i == ']' and stack[-1] == '[') or (i == ')' and stack[-1] == '('):
        stack.pop()
        print(True)
    else:
        print(False)
        break"""
        