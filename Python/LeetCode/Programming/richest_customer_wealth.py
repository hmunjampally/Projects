if __name__ == '__main__':
    accounts = [[1,2,3],[3,2,1]]
    max_ac = []

    for i in accounts:
        max_ac.append(sum(i))

    print(max(max_ac))