import textwrap

if __name__ == '__main__':
    special = "(){}[]"

    sub = textwrap.wrap(special, 2)
    
    for i in sub:
        if i[0] == i[1]:
            print(i)