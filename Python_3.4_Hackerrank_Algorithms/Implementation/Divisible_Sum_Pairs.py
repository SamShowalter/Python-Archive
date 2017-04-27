
import sys

#Use floor division to get the rounded-down whole number
n,k = input().strip().split(' ')
n,k = int(n),int(k)
list = [int(a_temp) for a_temp in input().strip().split(' ')]

count = 0
for i in range(n):
    for j in range(n):
        #Full disclosure, this has terrible runtime.
        if i != j and ((list[i] + list[j]) % k == 0):
            count += 1
            
print(count//2)
