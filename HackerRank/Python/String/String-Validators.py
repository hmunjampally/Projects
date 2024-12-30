"""
Python has built-in string validation methods for basic data. 
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
"""

if __name__ == '__main__':
    s = input("your string please: ")
    #below checks if any one iterartion is true it prints true
    print(any(y.isalnum() for y in s))
    print(any(y.isalpha() for y in s))
    print(any(y.isdigit() for y in s))
    print(any(y.islower() for y in s))
    print(any(y.isupper() for y in s))
    

    
    """if s.isalnum():
        print(True)
    print(False)
    
    if s.isalpha():
        print(True)
    print(False)
    
    if s.isdigit():
        print(True)
    print(False)
    
    if s.islower():
        print(True)
    print(False)
    
    if s.isupper():
        print(True)
    print(False)"""
