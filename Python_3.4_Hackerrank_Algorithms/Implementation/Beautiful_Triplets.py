
n,d = input().split(' ')
n,d = int(n),int(d)
nums = [int(i) for i in input().strip().split(' ')]

k = [i for i in nums if (i+d) in nums and (i-d) in nums]

print(len(k))
