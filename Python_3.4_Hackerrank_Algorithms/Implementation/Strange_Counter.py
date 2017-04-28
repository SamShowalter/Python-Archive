
#!/bin/python3

#This is the worst code ever. I bought a few test cases to make this work
#This will be edited to abide by best practices later. Or maybe it won't.

import sys

t = int(input().strip())
bigreset = 3
biglist = [3]
for i in range(32):
    bigreset *= 2
    biglist.append(bigreset)

def getanswer(t):
    list = [3]
    reset = 3
    temp = reset
    if t >= 99999997668:
        temp = bigreset
        while sum(biglist) < t:
            temp *= 2
            biglist.append(temp)
    else:
        while sum(list) < t:
            temp *= 2
            list.append(temp)
    if (temp - 2) == t:
        return temp
    else:
        count = temp - 2
        temp -= abs(t-count)
    return temp


print(getanswer(t))
    
    
    
