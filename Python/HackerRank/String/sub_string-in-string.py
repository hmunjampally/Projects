def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        sub = len(sub_string)
        if sub_string == string[i:i+sub]:
            count += 1
    return count

if __name__ == '__main__':
    string = input("Enter the main string ").strip()
    sub_string = input("what is your substring? ").strip()
    
    count = count_substring(string, sub_string)
    print(count)