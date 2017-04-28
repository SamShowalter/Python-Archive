

count = int(input().strip())
klist = [int(num) for num in input().strip().split(' ')]
most = 0
num = 0
length = len(klist)
#Look up what the key=.count function does online.
most = max(set(klist), key=klist.count)

for i in range(length):
    if klist[i] == most:
        num += 1
        
print(length - num)
