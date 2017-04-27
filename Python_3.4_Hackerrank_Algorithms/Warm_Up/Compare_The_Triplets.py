import sys

a0,a1,a2 = input().strip().split(' ')
a = [int(a0),int(a1),int(a2)] 
b0,b1,b2 = input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]

#Make a and b their own lists

A = B = 0
for i in range(3):
    if a[i] > b[i]:   #Point for alice
        A += 1
    elif a[i] < b[i]: #Point for bob
        B += 1
print(str(A) + ' ' + str(B))
