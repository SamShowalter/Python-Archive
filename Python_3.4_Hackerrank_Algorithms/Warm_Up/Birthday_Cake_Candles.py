
#Find the number of the tallest candles in the birthday cake with the built in count function
import sys
from collections import Counter

n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

print(height.count(max(height)))
