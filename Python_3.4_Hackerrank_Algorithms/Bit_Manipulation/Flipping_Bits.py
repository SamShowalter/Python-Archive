
n = int(input().strip())

for a0 in range(n):
    t = input().strip()
    temp = bin(int(t))
    temp = temp[2:]
    x = '11111111111111111111111111111111'
    
    final = str(int(x) - int(temp))
    print(str(int(final,2)))
