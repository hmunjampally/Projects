if __name__ == '__main__':
     s ='ababab'
     def repeatedSubstringPattern(s):
        return s in (s+s)[1:-1]
    