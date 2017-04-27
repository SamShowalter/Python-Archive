
import sys

#Python is the best for very big numbers
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

sum = 0
for i in range(n):
    sum += arr[i]
    
print(sum)
