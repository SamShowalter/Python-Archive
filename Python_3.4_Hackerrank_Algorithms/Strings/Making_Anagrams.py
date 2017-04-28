
from collections import Counter

a = [str(num) for num in input().strip()]
b = [str(num) for num in input().strip()]

la = len(a)
lb = len(b)
count = 0

for i in range(la):
    if a[i] in b:
        count += 1
        b.remove(a[i])
    
total = (la + lb - 2*count)

print(total)
       
