
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
b = sorted(a)
mindif = max(b) + 1

for i in range(n-1):
    dif = abs(b[i] - b[i + 1])
    if dif < mindif:
         mindif = dif
            
print(mindif)       
        
        
        
        
    
