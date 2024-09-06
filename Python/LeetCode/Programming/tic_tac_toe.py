if __name__ == '__main__':
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
     
    moves_A = []
    moves_B = []

    winning = [ [[0,0], [0,1], [0,2]],
               [[1,0], [1,1], [1,2]],
               [[2,0], [2,1], [2,2]],
               [[0,0], [1,0], [2,0]],
               [[0,1], [1,1], [2,1]],
               [[0,2], [1,2], [2,2]],
               [[0,0], [1,1], [2,2]],
               [[0,2], [1,1], [2,0]]]


    for i in range(0, len(moves)):
        if i % 2 == 0:
            moves_A.append(moves[i])
        else:
            moves_B.append(moves[i])

    print(moves_A)
    print(moves_B)

    for combi in winning:
        if all(move in moves_A for move in combi):
            print("A Own")
            break
    else:
        for combi in winning:
            if all(move in moves_B for move in combi):
                print("B Own")
                break
        else:
            if len(moves) < 9:
                print("pending")
            else:
                print("draw")