# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

if __name__ == '__main__':
    N = int(input())
    column_names = input().split()
    
    student = namedtuple('student', column_names)
    listOfStudents = []
    
    for i in range(N):
        student_data = input().split()
        listOfStudents.append(student(*student_data))
        
    total = 0
    count = 0
    
    for s in listOfStudents:
        total += int(s.MARKS)
        count += 1
    
    print(round(total/count, 2))