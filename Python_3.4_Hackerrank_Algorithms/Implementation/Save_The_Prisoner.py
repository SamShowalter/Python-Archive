
count = int(input().strip())

for t in range(count):
    [n, m, s] = map(int, input().split(' '))
    res = (s - 1 + m) % n
    if res != 0:
        print(res)
    else:
        print(n)
