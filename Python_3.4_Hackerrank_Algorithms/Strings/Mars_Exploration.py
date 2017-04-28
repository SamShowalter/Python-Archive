
#!/bin/python3

import sys

S = input().strip()
count = 0
temp = "SOS"*100

for i in range(len(S)):
    if S[i] != temp[i]:
        count += 1

print(count)
