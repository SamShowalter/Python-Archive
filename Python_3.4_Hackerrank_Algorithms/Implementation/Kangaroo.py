
import sys

#Another easy one. Just a lot of parameters to keep track of.
x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

k1 = x1
k2 = x2
def kangaroo(k1,k2,v1,v2):
    count = 0
    while count < 10000:
        if k1 == k2:
            print("YES")
            return
        k1 = k1 + v1
        k2 = k2 + v2
        count += 1
    print("NO")
    
kangaroo(k1,k2,v1,v2)
