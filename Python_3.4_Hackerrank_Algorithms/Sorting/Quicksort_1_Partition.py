
# I actually wrote this. No lie.
n = int(input().strip())
sort = [int(num) for num in input().strip().split(' ')]

p = sort[0]
equal = [sort[0]]
left = []
right = []
for i in range(1,n):
    if sort[i] > p:
        right.append(sort[i])
    elif sort[i] < p:
        left.append(sort[i])
    else:
        equal.append(sort[i])
        
print(' '.join(str(num) for num in left) , ' '.join(str(num) for num in equal) , ' '.join(str(num) for num in right))
