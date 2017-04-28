
#!/bin/python3

import sys


d1,m1,y1 = input().strip().split(' ')
Ad,Am,Ay = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
Ed,Em,Ey = [int(d2),int(m2),int(y2)]

if Ad < 10: sAd = "0" + str(Ad)
else: sAd = Ad
if Ed < 10: sEd = "0" + str(Ed)
else: sEd = Ed
if Am < 10: sAm = "0" + str(Am)
else: sAm = Am
if Em < 10: sEm = "0" + str(Em)
else: sEm = Em

aFullDate = int(str(Ay) + str(sAm) + str(sAd))
eFullDate = int(str(Ey) + str(sEm) + str(sEd))

if (aFullDate > eFullDate):
    if (Am == Em) and (Ay == Ey):
        print(15*(Ad-Ed))
    elif ((Am != Em) and (Ay == Ey)):
        print(500*(Am - Em))
    else:
        print(10000)
else:
    print(0)
        
 
