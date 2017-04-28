
l = int(input())
r = int(input())

def maxXor(l, r):
    return max([(x ^ y) for y in range(l, r+1) for x in range(y, r+1)])

print(maxXor(l, r))
