
import sys

n = int(input().strip())
a = []

#Generate a list of the rows (list of lists)
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    
#Primary Diagonal sum
def pdsum(a):
    pdsum = 0
    n = len(a)
    for i in range(n):
        #take the first item from the first list, the second item from the second...
        pdsum += a[i][i]
    return pdsum

#Secondary diagonal sum
def sdsum(a):
    sdsum = 0
    n = len(a)
    nindex = n - 1 
    for i in range(n):
        #take the last item from the first list, the second-last item from the second...
        sdsum += a[i][nindex - i]
    return sdsum

print(abs(pdsum(a) - sdsum(a)))
