
n = int(input().strip())

for a0 in range(n):
    temp = input().strip()
    count = 0
    
    for i in range(len(temp) - 1):
        if temp[i] == temp[i+ 1]:
            count += 1
    print(count)
    
    
