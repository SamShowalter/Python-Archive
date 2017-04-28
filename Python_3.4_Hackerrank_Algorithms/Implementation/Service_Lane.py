
#!/bin/python3

import sys

n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]

for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]
    tempwidth = width[i: j+1]
    answer = min(tempwidth)
    
    print(answer)


    
