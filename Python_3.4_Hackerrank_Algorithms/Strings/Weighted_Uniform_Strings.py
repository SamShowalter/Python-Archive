
#!/bin/python3

import sys

s = input().strip()
n = int(input().strip())
all_val = get_set(s)

def get_set(s):
    # Get the first count, used for adding weights
    weight = ord(s[0]) - 96
    
    # The set of each value
    weights = set()
    weights.add(weight)
    
    for i in range(1, len(s)):
        # Duplicate, add the count
        if s[i] == s[i - 1]:
            weight += ord(s[i]) - 96
        else:
            weight = ord(s[i]) - 96
        weights.add(weight)
    return weights


for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    print('Yes' if x in all_val else 'No')
