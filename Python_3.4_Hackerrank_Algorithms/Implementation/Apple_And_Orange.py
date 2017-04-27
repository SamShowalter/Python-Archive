import sys

#This one is easy, you just have to keep track of everything
s,t = input().strip().split(' ')
hStart,hEnd = int(s),int(t)
a,b = input().strip().split(' ')
appleT,orangeT = int(a),int(b)
m,n = input().strip().split(' ')
numA,numO = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

aCount = 0
oCount = 0
for i in apple:
    if (i + appleT >= hStart) and (i + appleT <= hEnd):
        aCount += 1

for j in orange:
    if (j + orangeT >= hStart) and (j + orangeT <= hEnd):
        oCount += 1
        
print(aCount)
print(oCount)
