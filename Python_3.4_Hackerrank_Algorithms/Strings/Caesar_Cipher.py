
#!/bin/python3

import sys
import string

labc = string.ascii_lowercase
uabc = string.ascii_uppercase
n = int(input().strip())
string = str(input().strip())
rotate  = int(input().strip())
newstring = ""

for i in string:
  if (i in labc):
      newstring += chr((ord(i) - 97 + rotate)%26 + 97)
  elif (i in uabc):
      newstring += chr((ord(i) - 65 + rotate)%26 + 65)
  else:
    newstring += i

print(newstring)
