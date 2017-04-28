
#!/bin/python3

import sys

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calbest = sorted(calories, reverse = True)
milecount = 0

for i in range(n):
    milecount += (2**i)*calbest[i]
    
print(milecount)
    
