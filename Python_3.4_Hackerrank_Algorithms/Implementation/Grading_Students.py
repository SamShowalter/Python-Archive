
import sys

#Partition the grades based on the parameters of the problem.
n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    if (grade < 38):
        print(grade)
    elif ((grade - 1) % 5 == 0 or (grade - 2) % 5 == 0) or (grade%5 == 0):
        print(grade)
    else:
        if(grade + 1) % 5 == 0 and (grade >= 38):
            print(grade + 1)
        else:
            print(grade + 2)
