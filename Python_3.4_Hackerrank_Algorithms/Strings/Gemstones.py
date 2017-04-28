
import string

n = int(input().strip())
gemlist = []
#Full alphabet, but lowercase    
abc = string.ascii_lowercase

for a0 in range(n):
    s = str(input().strip())
    gemlist.append(s)

for i in string.ascii_lowercase:
    for n in gemlist:
        if i not in  n:
            abc = abc.replace(i,'')
                  
print(len(abc))          

       
