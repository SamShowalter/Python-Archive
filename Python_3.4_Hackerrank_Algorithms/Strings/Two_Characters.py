
#!/bin/python3

import sys
n = int(input().strip())
s = input().strip()
l = set(s)
ml = 0
z = list(l)
q = []

for i in range(0, len(z) - 1):
    for j in range(i + 1, len(z)): 
        q.append([z[i], z[j]])
        
for c in q:
    _s = s
    
    for x in l:
        if x not in c: 
            _s = _s.replace(x, '')
            
        if len(set(_s)) > 2: 
            continue
            
        valid = True
        
        for i in range(0, len(_s) - 1):
            if _s[i] == _s[i + 1]: valid = False
              
        if not valid: 
            continue
            
        if len(_s) > ml: 
            ml = len(_s)
            
print(ml)
