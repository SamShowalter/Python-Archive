
import sys

#Fairly straightforward.
q = int(input().strip())

for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if (abs(z - x) == abs(y - z)):
        print("Mouse C")
    elif (abs(z - x) > abs(y - z)):
        print("Cat B")
    else:
        print("Cat A")
