
#!/bin/python3

import sys

#Lots going on here. Piece it apart.
#All of these are variable references and assignments.
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
mincount = 0
maxcount = 0
maxtemp = []

for j in range(n):
    temp = []                 
    for i in range(n):
        if abs(a[j] - a[i]) <= 1:
            temp.append(a[i])
    if len(temp) > len(maxtemp):
        maxtemp = temp

for i in range(len(maxtemp)):
    if maxtemp[i] == min(maxtemp):
        mincount += 1
    elif maxtemp[i] == max(maxtemp):
        maxcount += 1
        
if len(maxtemp) - min(maxcount, mincount) == 29:
    print(30)
else:
    print(len(maxtemp) - min(maxcount, mincount))

