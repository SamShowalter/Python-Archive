
import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
bevs = 0
maxh = max(height)

if maxh > k:
    bevs = (maxh - k)

print(int(bevs))
