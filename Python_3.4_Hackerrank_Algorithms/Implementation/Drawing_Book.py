
import sys

#n is total pages, p is the page the teacher wants her to turn to.
n = int(input().strip())
p = int(input().strip())
# your code goes here

if n % 2 == 0:
    if (n - p) <= p:
        print((n-p)//2)
    else:
        print(p//2)
else:
    if (n - p) <= p:
        print((n-p)//2)
    else:
        print(p//2)
