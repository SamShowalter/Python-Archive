
n = int(input().strip())

for a0 in range(n):
    count = 0
    a = str(input().strip())
    b = str(input().strip())
    
    for i in a:
        if i in b:
            count += 1
    if count > 1:
        print("YES")
    else:
        print("NO")
    
