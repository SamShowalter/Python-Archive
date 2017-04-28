
#!/bin/python3

import sys

t = int(input().strip())

for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    #black gifts
    cost = 0
    if y + z < x:
        cost += b*(y+z)
    else:
        cost += b*x

    #white gifts
    if x + z < y:
        cost += (x + z)*w
    else:
        cost += y * w
    print(cost)
