
import sys
from collections import Counter

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here

#Applies counter properties to the list types
#See more about Counter at https://docs.python.org/3/library/collections.html
newtype = Counter(types)

mcount = max((newtype.values()))
newtype = dict(newtype)

finalist = []
for i in newtype:
    if newtype[i] == mcount:
        finalist.append(i)
        
print(min(finalist))
