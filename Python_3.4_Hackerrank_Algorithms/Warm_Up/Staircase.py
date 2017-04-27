import sys

n = int(input().strip())

def stairs(n):
    for i in range(1, n + 1):
        print(" "*(n - i) + "#"*i)
        
#This can also be done easily with recursion
stairs(n)
