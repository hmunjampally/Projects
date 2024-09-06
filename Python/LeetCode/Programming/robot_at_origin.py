if __name__ == '__main__':
    moves = "UD"#"LLUURDRD"

    origin = [0, 0]

    for i in moves:
        if i == "L":
            origin[1] -= 1
        if i == "R":
            origin[1] += 1
        if i == "U":
            origin[0] -= 1
        if i == "D":
            origin[0] += 1
    print(origin)
        