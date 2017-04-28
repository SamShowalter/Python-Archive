
v = int(input().strip())
n = int(input().strip())

ar = [int(num) for num in input().strip().split(' ')]

for i in range(n):
    if ar[i] == v:
        print(i)

