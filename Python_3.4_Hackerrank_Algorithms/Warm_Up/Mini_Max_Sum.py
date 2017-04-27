
import sys

#Just remove the largest or smallest item from the set
a,b,c,d,e = input().strip().split(' ')
listmin = [int(a),int(b),int(c),int(d),int(e)]
listmax = [int(a),int(b),int(c),int(d),int(e)]

def minlist(list):
    return sum(list) - max(list)

def maxlist(list):
    return sum(list) - min(list)

print(str(minlist(listmin)) + " " + str(maxlist(listmax)))
