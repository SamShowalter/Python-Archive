
import sys

#Another easy one. If you use custom input you can get this one on the first try.
n = int(input().strip())
score = list(map(int, input().strip().split(' ')))
# your code goes here

mini = score[0]
maxi = score[0]
mincount = 0
maxcount = 0
for i in range (1,n):
    if score[i] > maxi:
        maxcount += 1
        maxi = score[i]
    elif score[i] < mini:
        mincount += 1
        mini = score[i]
 
print(str(maxcount) + ' ' + str(mincount))
