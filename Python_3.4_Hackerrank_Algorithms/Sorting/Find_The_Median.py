
import statistics

n = int(input().strip())

alist = [int(s) for s in input().strip().split(' ')]

print(statistics.median(alist))
