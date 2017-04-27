
import sys

#Find the number of ways to break up the chocolate
def getWays(squares, d, m):
    count = 0
    if len(squares) < m:
        return 0
    if len(squares) == 1 and squares[0] == d and m == 1:
        return 1
    for i in range(n - m + 1):
        if sum(choc[i:i+m]) == d: 
            count += 1
    return count
                

n = int(input().strip())
choc = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(choc, d, m)
print(result)
