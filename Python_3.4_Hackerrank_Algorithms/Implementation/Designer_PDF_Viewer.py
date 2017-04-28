
import sys

h = list(map(int, input().strip().split(' ')))
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dict = {}
word = input().strip()
maxH = 0

for i in word:
    temp = abc.index(i)
    tempH = h[temp]
    if tempH > maxH:
        maxH = tempH

print(len(word)*maxH)
