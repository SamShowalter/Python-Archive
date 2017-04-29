

n = int(input().strip())

sort = [int(num) for num in input().strip().split(' ')]

count = []
for i in range(100):
    count.append(0)
    
for i in range(n):
    count[sort[i]] += 1
   
print(' '.join(str(num) for num in count))
