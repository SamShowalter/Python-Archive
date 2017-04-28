
n,k = input().strip().split(' ')
n, k = int(n), int(k)

alist = [int(num) for num in input().strip().split(' ') if int(num) < k]
alist = sorted(alist)

s = 0
i = 0
count = 0
newlist = []

while k - (s + alist[i]) > 0 and (i < len(alist)):
    s += alist[i]
    newlist.append(alist[i])
    count += 1
    i += 1
    if i == len(alist):
        break
    
print(count)
