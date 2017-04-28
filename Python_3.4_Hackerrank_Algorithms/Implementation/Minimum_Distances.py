
#!/bin/python3

import sys
from collections import Counter

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

mincount = n
for i in range(n):
    count = 0
    if A.count(A[i]) > 1:
        for j in range(i+ 1, n):
            if A[i] == A[j]:
                count = j - i
                if count < mincount:
                    mincount = count
if mincount == n:
    print(-1)
else:
    print(mincount)
