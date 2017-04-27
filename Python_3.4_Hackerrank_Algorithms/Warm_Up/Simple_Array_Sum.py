
import sys

n = int(input().strip())
arr = [int(s) for s in input().strip().split(' ')]

#Sums up all values in array
def arraySum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
        
print(arraySum(arr))
