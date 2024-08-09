if __name__ == '__main__':
    new_list = ["Flowers","Flow","Flight"]
    result =""
    sorted_new = sorted(new_list, key=len)
    small = len(sorted_new[0])

    for i in new_list:

        while not i.startswith(sorted_new[0][:small]):
            small = small - 1
            if small == 0:
                result = ""
                break
    result = sorted_new[0][:small].lower()
    print(result)