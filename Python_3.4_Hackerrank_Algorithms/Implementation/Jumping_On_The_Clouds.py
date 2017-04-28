
#!/bin/python3

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
cloud  = 0
count = 0

while cloud <= (len(c) - 1):
    if (cloud + 2) <= (n - 1) and (c[cloud+2] != 1):
        cloud += 2
    else:
        cloud += 1
    count += 1
    
print(count-1)

