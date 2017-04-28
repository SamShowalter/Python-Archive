
import sys

year = int(input().strip())

def solve(year):
    days_total = 243
    if (1700 <= year <= 1917) and (year%4 == 0):
        days_total += 1
    if (year == 1918):
        days_total = 230    
    if 1919 <= year and (year % 400==0 or  (year % 4==0 and year % 100!=0)):
        days_total += 1
    dd = 256 - days_total
    return str(dd)+"."+"09"+"."+str(year)

result = solve(year)
print(result)
