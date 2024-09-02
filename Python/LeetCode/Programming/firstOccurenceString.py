if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"

    for i in range(len(haystack)):
        if needle == haystack[i:i+len(needle)]:            
            print(i)
            break
    else:       
        print(-1)
            