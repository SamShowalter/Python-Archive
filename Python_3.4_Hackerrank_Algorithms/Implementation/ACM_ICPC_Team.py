
#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
maxcount = 0
tally = 0
countlist = []

for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)

for i in range(n):
    temp1 = topic[i]
    for j in range(i + 1, n):
        count = m
        temp2 = topic[j]
        for k in range(m):
            if (temp1[k] != "1") and (temp2[k]) != "1":
                count -= 1
        countlist.append(count)
        if maxcount < count:
            maxcount = count
            
for i in countlist:
    if i == maxcount:
        tally += 1
            
print(maxcount)
print(tally)
