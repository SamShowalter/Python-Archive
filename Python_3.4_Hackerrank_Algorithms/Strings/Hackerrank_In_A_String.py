
#!/bin/python3

import sys

ref = "hackerrank"
length = len(ref)
q = int(input().strip())

for a0 in range(q):
    s = input().strip()
    # your code goes here
    index = [-1]
    new = ""
    
    for i in s:
        if i in ref:
            new += i
            
    for j in range(length):
        for i in range(j,len(new)):
            if new[i] == ref[j] and i not in index and i > max(index):
                index.append(i)
                break
                
    index.remove(index[0])
    if len(index) == length and index == sorted(index):
        print("YES")
    else:
        print("NO")
    
                
    
        
            
