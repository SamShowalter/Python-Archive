
#!/bin/python3

import sys

q = int(input().strip())

for a0 in range(q):
    s = input().strip()
    status = ''
    
    def landhead():
        i = len(s)//2
        status = ''
        head = ''
        while i >= 1:
            if int(s[:i]) == (int(s[i:i + i]) - 1) or int(s[:i]) == (int(s[i:min(i + i + 1,len(s))]) - 1):
                head = s[:i]
                i = -1
            else:
                i -= 1 
        if head != '':
            return head
        else:
            head = "NULL"
            return head
          
    head = landhead()
    
    if status != 'done' and head != "NULL":
        thead = int(head)
        t = head
        while len(t) < len(s):
            thead += 1
            t += str(thead)
        if t == s:
            print("YES " + head)
        else:
            print("NO")
    else:
        print("NO")
    
    
 
