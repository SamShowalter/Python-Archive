
#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while len(arr) > 0:
    tiny = min(arr)
    for i in range(len(arr)):
        arr[i] -= tiny
    newarr = []
    for i in range(len(arr)):
        if arr[i] > 0:
            newarr.append(arr[i])
    arr = newarr
    if len(arr) != 0:
        print(len(arr))
                 
