
import sys

#A little more complicated than Kangaroo and Apple & Orange. Keep track of edge cases
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

final = 0
for i in range(max(a), min(b) + 1):
    for j in a:
        if i%j != 0:
            break
    else:
        for x in b:
            if x % i != 0:
                break
        else:
            final += 1

print(final)
