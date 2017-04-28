
#!/bin/python3

import sys

t = int(input().strip())

for a0 in range(t):
    n,c,m = input().strip().split(' ')
    money,cost,wraptrade = [int(n),int(c),int(m)]
    initial = (money // cost)
    total = initial
    wrapcount = initial
    
    while wrapcount >= wraptrade:
        temp = (wrapcount // wraptrade)
        total += temp
        wrapcount -= (temp * wraptrade)
        wrapcount += temp
        
    print(total)
    
    
    
