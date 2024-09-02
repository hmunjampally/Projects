"""if __name__ == '__main__':
    word1 = "abc"
    word2 = 'pqrs'

    first = [i for i in word1]
    second = [j for j in word2]
    

    result = ''

    i = 0
    j = 0 

    while (i<len(first) or j < len(second)):
        if i<len(first):
            result += first[i]
            i += 1
        if j<len(second):
            result += second[j]
            j += 1
    
    print(result)
"""



from itertools import zip_longest

if __name__ == '__main__':
    word1 = "abcd"
    word2 = 'pq'

    # Use zip_longest to combine characters from both words
    result = ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

    print(result)