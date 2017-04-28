
#!/bin/python3

import sys

t = int(input().strip())
    
def getHeight(n):
    beg = 1
    temp = 0
    if (n == 0): 
        return 1
    if (n % 2 == 0):
        while temp < n:
            beg = beg * 2
            beg += 1
            temp += 2
        return beg
    else:
        while temp < (n-1):
            beg = beg * 2
            beg += 1
            temp += 2
        return beg * 2

for a0 in range(t):
    n = int(input().strip())
    print(getHeight(n))

        
