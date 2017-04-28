
t1,t2,n = input().strip().split(' ')
t1,t2,n = [int(t1),int(t2),int(n)]

#Iteratively defining fibonnaci sequence may be a sin.
def nthFiboMod(t1,t2, n):
    count = 2
    while count < n:
        t3 = t1 + t2**2
        t1 = t2
        t2 = t3
        count += 1
    return t3

print(nthFiboMod(t1,t2,n))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
