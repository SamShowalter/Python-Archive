

n = int(input().strip())
alist = [ int(num) for num in input().strip().split(' ')]

#Understanding the recursion for this quicksort algorithm can be tricky
def quicksort(alist):
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        l , pivot , r = [num for num in alist if num < pivot], [num for num in alist if num == pivot], [num for num in alist if num > pivot]
        subarr = quicksort(l) + pivot + quicksort(r)
        print(' '.join(map(str,subarr)))
        return subarr
    
quicksort(alist)
