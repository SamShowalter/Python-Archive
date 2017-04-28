
#!/bin/python3

import sys

t = int(input().strip())

def getDigit(n,k):
    n = str(n)
    return int(n[k-1])

for a0 in range(t):
    n = str(input().strip())
    count = 0
    for i in range(len(n)):
        if (int(n[i]) == 0):
            count += 0
        elif int(n) % int(n[i]) == 0:
            count += 1
    print(count)
