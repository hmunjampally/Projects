if __name__ == '__main__':
    
    n = int(input())  # students subscribed to english paper
    roll_no_eng = set(map(int, input().split()))
    b = int(input())  # students subscribed to french paper
    roll_no_french = set(map(int, input().split()))
    
    print(len(roll_no_eng.symmetric_difference(roll_no_french)))

    """
    sample inputs:
    9
    1 2 3 4 5 6 7 8 9
    9
    10 1 2 3 11 21 55 6 8
    
    output: 8
    
    """