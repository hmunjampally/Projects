password = '#HackerRank'

char_need = 0
special = '!@#$%^&*()-+'

if not any(letter.islower() for letter in password):
    char_need += 1
if not any(letter.isupper() for letter in password):
    char_need += 1
if not any(letter.isdigit() for letter in password):
    char_need += 1
if not any(letter in special for letter in password):
    char_need += 1

if char_need + len(password) < 6:
    char_need += 6 - (char_need + len(password))

print(char_need)