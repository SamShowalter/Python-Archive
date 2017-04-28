
#!/usr/bin/py
# Head ends here
from collections import Counter

n = int(input().strip())
alist = [int(num) for num in input().strip().split(' ')]

def lonelyinteger(b):
    x = Counter(b)
    for letter, count in list(x.most_common(100)):
        if count == 1:
            answer = letter
    return answer

print(lonelyinteger(alist))
