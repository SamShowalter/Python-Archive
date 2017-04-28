

from collections import Counter

s = input().strip()
c = Counter(s)
l = list(c.values())
odd = 0

for i in l:
    if i%2 != 0:
        odd += 1

if odd <= 1:
    print("YES")
else:
    print("NO")
        
