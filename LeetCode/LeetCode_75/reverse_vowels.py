s = "IceCreAm"
vowels = ['A','E','I','O','U','a','e','i','o','u']

vows = [i for i in s if i in vowels]
ind = [i for i, char in enumerate(s) if char in vowels]

new_s = list(s)
rev_vows = vows[::-1]

for i, char in zip(ind, rev_vows):
    new_s[i]=char

print(''.join(new_s))
