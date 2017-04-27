
import sys
from collections import Counter

#Inputs
n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

#Setting up necessary variables and properties
temp = Counter(c)
final = 0

for i in temp:
    if temp[i] % 2 == 0:
        final += (temp[i]//2)
    else:
        final += (temp[i] - 1)//2

print(final)
