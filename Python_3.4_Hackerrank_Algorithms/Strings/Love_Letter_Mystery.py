
n = int(input().strip())

for a0 in range(n):
    count = 0
    s = input().strip()
    leng = len(s)
    
    if leng % 2 == 0:
        left = s[:leng//2]
        right = s[leng//2:]
    else:
        left = s[:leng//2]
        right = s[leng//2 + 1:]
    
    #Reverse the order
    left = left[::-1]
    
    for i in range(len(left)):
        count += abs(ord(left[i]) - ord(right[i]))
    print(count)
