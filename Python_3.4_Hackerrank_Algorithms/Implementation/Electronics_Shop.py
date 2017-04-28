
import sys

#Thise careful about where and why you are indenting. Contextualize what is happening.
money, nk, nusb = [int(num) for num in input().strip().split(' ')]
kc = [int(num) for num in input().strip().split(' ')]
kusb = [int(num) for num in input().strip().split(' ')]

def electronics():
    best = 0
    costdif = 0
    mindif = money
    cost = 0
    for i in range(nk):
        for j in range(nusb):
            cost = kc[i] + kusb[j]
            if cost <= money:
                costdif = money - cost
                if costdif < mindif:
                    mindif = costdif
                    best = cost
    if best == 0:
        return -1
    else:
        return best      
    
print(electronics())
