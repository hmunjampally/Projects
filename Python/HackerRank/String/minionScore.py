def minion_game(string):
    # your code goes here
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_count = 0
    consonants_count = 0

    lower_string = string.lower()

    for i in range(len(string)):
        if lower_string[i] in vowels:
            vowels_count = vowels_count + 1 + (len(string)-1-i)
        else:
            consonants_count = consonants_count + 1 + (len(string)-1-i)
            
    if vowels_count > consonants_count:
        print("Kevin", vowels_count)
    elif consonants_count > vowels_count:
        print("Stuart", consonants_count)
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)