
import sys

n = int(input().strip())
# n = total number of items in the array
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos = 0
neg = 0
zeros = 0

for i in range(n):
    if arr[i] == 0:
        zeros += 1
    elif arr[i] < 0:
        neg += 1
    else:
        pos += 1

        
print(float(pos/n))
print(float(neg/n))
print(float(zeros/n))
