
#!/bin/python3

import sys

n = int(input().strip())

for a0 in range(n):
    fcount = 0
    s = input().strip()
    final = ""
    
    for i in s:
        if i not in final:
            fcount += 1
            final += i
    print(fcount)


