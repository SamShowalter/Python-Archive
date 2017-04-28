
#!/bin/python3

import sys

s = input().strip()
n = int(input().strip())
fullcount = 0
partcount = 0
length = len(s)

for i in s:
    if i == 'a':
        fullcount += 1
        
for i in range(n%length):
    if s[i] == 'a':
        partcount += 1
        
print((n//length)*fullcount + partcount)
               
               
