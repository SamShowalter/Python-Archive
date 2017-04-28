
n = int(input().strip())

for a0 in range(n):
    stone = int(input().strip())
    difa = int(input().strip())
    difb = int(input().strip())
    flist =[]
    start = 0
    count = stone
    
    for i in range(count):
        flist.append(difa*i + difb*(count - 1 - i))
        
    print(' '.join(str(num) for num in sorted(set(flist))))
            
    
