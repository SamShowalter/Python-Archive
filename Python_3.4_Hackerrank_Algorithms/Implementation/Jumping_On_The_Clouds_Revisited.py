
import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
cloud = 0
E = 100

while cloud % n != 0 or E == 100:
    cloud += k
    E -= 1
    if c[(cloud % n)] == 1:
        E -= 2
        
print(E)

