
import sys

#Could also import string to get the alphabet in upper case
s = input().strip()
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
for i in s:
    if i in abc:
        count += 1
print(count + 1)
